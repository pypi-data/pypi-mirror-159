"""
Convenience wrapper around the raw mb_api that allows us to more easily orchestrate
simply. Its main job is — for endpoints that support it — it to page through the items for us. 
It uses rate limiting to ensure 429 error is not reached, but if so, is handled with back-off

TODO: An even better version will use asyncio to asyncronously fetch pages after #1. However:

1. The code would be less accessible
2. It would pound servers in a very short amount of time
"""

from .endpoints import Endpoint, output_console
from .mock import MockEndpoint
from collections.abc import Iterator
import datetime
import json


def build_generator(auth_token: str, tld: str = 'com', verbosity: int = 0, subdomain: str = 'api', mock=False, **kwargs):
    return Generator(
        auth_token=auth_token,
        tld=tld,
        subdomain=subdomain,
        verbosity=verbosity,
        Endpoint_class= MockEndpoint if mock else Endpoint,
        **kwargs
    )


class Terms:
    """
    Start with `start_term_id` and increments, taking into account academic year
    """

    def __init__(self, klass: dict, academic_info: dict):
        self.klass = klass
        self.academic_info = academic_info

    def __iter__(self) -> Iterator[int]:
        """
        yield every term_id from start_term_id to end_term_id
        works by collapsing the academic_years object
        """
        program = self.academic_info.get(self.klass.get("program_code"))

        # check to ensure there are term_ids to work with
        # with old MB classes, it's possible not to have start_term_ids, and thus no way to cycle through them
        if start_term_id := self.klass.get("start_term_id"):
            if end_term_id := self.klass.get("end_term_id"):
                assert start_term_id <= end_term_id, "Start term can't be after end term"
                for academic_year in program.get("academic_years"):
                    for academic_term in academic_year.get("academic_terms"):
                        academic_term_id = academic_term.get("id")
                        if start_term_id <= academic_term_id <= end_term_id:
                            yield academic_term_id


class Generator:
    """
    Provides high-level functionality to loop over items in an endpoint, and exposes `endpoints` with direct uplink class
    """
    # FIXME: Making two of these objects results in double calls
    def __init__(
        self, auth_token: str, tld: str = "com", subdomain: str = "api", verbosity=0, Endpoint_class=Endpoint
    ):
        self.auth_token: str = auth_token
        self.subdomain = subdomain
        self.tld = tld
        self.verbosity = verbosity
        self._instances = {}
        self._Endpoint_class = Endpoint_class
        # ensure that if a different class is passed, we got a new instance
        self.endpoint_class_name = self._Endpoint_class.__qualname__
        self.augment()

    def verbose(self):
        self.verbosity += 1
        self.augment()

    @property
    def hashed(self):
        return json.dumps({key: value for key, value in self.__dict__.items() if not key.startswith('_')}, sort_keys=True)

    def augment(self):
        if self.verbosity > 0:
            decorator = output_console
        else:
            decorator = lambda x: x  # no decorator

        # let mocking by passing in subclass to Endpoint class
        # the decorator enables different Uplink response handlers
        instance = decorator(self._Endpoint_class)(
            auth_token=self.auth_token, tld=self.tld, subdomain=self.subdomain
        )
        self.endpoints = instance

    def generate_classes_by(
        self, page: int, archived: bool, modified_since: str = None
    ):
        classes_respo = self.endpoints.get_classes(
            page=page, archived=int(archived), modified_since=modified_since
        )
        for clss in classes_respo.get("classes", []):
            yield clss

    def generate_students_by(self, page: int, archived: bool, modified_since: str):
        response = self.endpoints.get_students(
            page=page, archived=archived, modified_since=modified_since
        )
        for student in response.get("students", []):
            yield student

    def generate_teachers_by(self, page: int, modified_since: str = None):
        response = self.endpoints.get_teachers(page=page, modified_since=modified_since)
        for teacher in response.get("teachers", []):
            yield teacher

    def generate_parents_by(self, page: int, modified_since: str = None):
        response = self.endpoints.get_parents(page=page, modified_since=modified_since)
        for parent in response.get("parents", []):
            yield parent

    def generate_memberships_by(self, page: int, modified_since: str = None, **kwargs):
        response = self.endpoints.get_memberships(
            page=page, modified_since=modified_since, **kwargs
        )
        for membership in response.get("memberships", []):
            yield membership

    @classmethod
    def augment_class(cls, clss: dict, archived: bool):
        clss["archived"] = archived
        return clss

    def generate_classes(self, archived=False, modified_since=None, starting_page=1):
        """

        Adds "archived" property
        FIXME: Guard against repeat IDs...
        """
        ids = []
        classes_resp = self.endpoints.get_classes(
            page=starting_page, archived=int(archived), modified_since=modified_since
        )
        for clss in classes_resp.get("classes", []):
            id = clss.get("id")
            ids.append(id)
            yield self.augment_class(clss, archived)
        pages = range(
            starting_page + 1,
            classes_resp.get("meta", {"total_pages": 1}).get("total_pages") + 1,
        )
        for page in pages:
            for clss in self.generate_classes_by(
                page=page, archived=archived, modified_since=modified_since
            ):
                id_ = clss.get("id")
                if not id_ in ids:
                    yield self.augment_class(clss, archived)
                    ids.append(id_)

    def generate_students(self, modified_since=None, archived=None, starting_page=1):
        archived_value = None if archived is None else int(archived)
        response = self.endpoints.get_students(
            page=starting_page, modified_since=modified_since, archived=archived_value
        )
        for student in response.get("students"):
            yield student

        pages = range(
            starting_page + 1,
            response.get("meta", {"total_pages": 1}).get("total_pages") + 1,
        )

        for page in pages:
            yield from self.generate_students_by(
                page=page, archived=archived_value, modified_since=modified_since
            )

    def generate_teachers(self, modified_since=None, starting_page=1):
        page_one_response = self.endpoints.get_teachers(
            page=starting_page, modified_since=modified_since
        )
        for teacher in page_one_response.get("teachers", []):
            yield teacher

        pages = range(
            starting_page + 1, page_one_response.get("meta").get("total_pages") + 1
        )

        for page in pages:
            yield from self.generate_teachers_by(
                page=page, modified_since=modified_since
            )

    def generate_parents(self, modified_since: str = None, starting_page=1):
        response = self.endpoints.get_parents(
            page=starting_page, modified_since=modified_since
        )
        for parent in response.get("parents", []):
            yield parent

        pages = range(starting_page + 1, response.get("meta").get("total_pages") + 1)

        for page in pages:
            yield from self.generate_parents_by(
                page=page, modified_since=modified_since
            )

    def generate_memberships(self, modified_since=None, starting_page=1, **kwargs):
        page_one_response = self.endpoints.get_memberships(
            page=starting_page, modified_since=modified_since, **kwargs
        )

        for membership in page_one_response.get("memberships", []):
            yield membership

        pages = range(
            starting_page + 1, page_one_response.get("meta").get("total_pages") + 1
        )

        for page in pages:
            yield from self.generate_memberships_by(
                page=page, modified_since=modified_since, **kwargs
            )

    def generate_academic_years(self):
        academic_years = self.endpoints.get_academic_years()
        convert = datetime.datetime.fromisoformat
        for program_code, ay in academic_years.items():
            ays = ay.get('academic_years', [])
            ays.sort(key=lambda a: datetime.datetime.fromisoformat(a['starts_on']))
            if len(ays) > 0:
                first_ay = ays[0]
                year_start = convert(first_ay['starts_on']).year
                for entity in ays:
                    entity["program_code"] = program_code
                    entity['ordinal'] = convert(entity['starts_on']).year - year_start + 1
                    yield entity

    def generate_school_subjects(self):
        school_subjects = self.endpoints.get_school_subjects()
        for program_code, subjects in school_subjects.items():
            for subject in subjects:
                yield dict(program_code=program_code, **subject)

    def generate_term_grades(self, classes=None, include_archived=True):
        if classes is None:
            classes = list(self.generate_classes(archived=False))
            if include_archived:
                classes.extend(list(self.generate_classes(archived=True)))
        yield from self.generate_termgrades_from_classes(classes)

    def generate_termgrades_from_classes_by_termid(self, classes, term_id):
        for clss in classes:
            class_id = clss.get("id")
            program_code = clss.get("program_code")
            page: int = 1
            while page is not None:
                response_json = self.endpoints.get_term_grades(
                    class_id, term_id, page=page
                )
                term_grades = response_json.get("students")
                for term_grade in term_grades:
                    term_grade["class_id"] = class_id
                    term_grade["student_id"] = term_grade["id"]
                    del term_grade["id"]
                    term_grade["term_id"] = term_id
                    term_grade["program_code"] = program_code
                    yield term_grade
                # increment:
                page = response_json.get("meta", {}).get("next_page", None)

    def generate_termgrades_from_classes(self, classes: list):
        # need academic years endpoint to pass to Terms object: FIXME refactor to just use db?
        academic_year_response = self.endpoints.get_academic_years()
        for clss in classes:
            class_id = clss.get("id")
            program_code = clss.get("program_code")
            terms = Terms(
                clss, academic_year_response
            )  # auto-incrementor, taking into account academic years
            for term in terms:
                # term will be the ID in sequential order by academic year!
                page: int = 1
                while True:
                    response_json = self.endpoints.get_term_grades(
                        class_id, term, page=page
                    )
                    term_grades = response_json.get("students")
                    if len(term_grades) == 0:
                        # just respond with one key, class_id
                        # special handling will ensure it's process to count but no further
                        yield dict(class_id=class_id)
                    for term_grade in term_grades:
                        term_grade["class_id"] = class_id
                        term_grade["student_id"] = term_grade["id"]
                        del term_grade["id"]  # renamed to student_id
                        term_grade["term_id"] = term
                        term_grade["program_code"] = program_code
                        yield term_grade
                    meta = response_json.get("meta")
                    total_pages = meta.get("total_pages")
                    page = meta.get("current_page", total_pages) + 1
                    if page > total_pages:
                        break

    def generate_classes_with(
        self, program_code: str, grade_number: int, archived: bool = True
    ):
        classes = list(self.generate_classes(archived=archived))
        yield from (
            clss
            for clss in classes
            if clss.get("program_code") == program_code
            and clss.get("grade_number") == grade_number
        )

    def generate_homeroom_attendance(self, year_group_id: int, term_id: int):
        students = self.endpoints.get_homeroom_attendance(year_group_id, term_id).get(
            "students"
        )
        if students is None:
            return
        for student in students:
            attendance = student.get("attendance")
            yield dict(
                student_id=student["id"],
                present=attendance.get("Present", 0),
                late=attendance.get("Late", 0),
                absent=attendance.get("Absent", 0),
                term_id=term_id,
                attendance=attendance,
            )

    def generate_class_attendance(self, class_id: int, term_id: int):
        response = self.endpoints.get_class_attendance(class_id, term_id)
        if response is None:
            return
        for student in response.get("students", []):
            attendance = student.get("attendance")
            yield dict(
                student_id=student["id"],
                term_id=term_id,
                class_id=class_id,
                present=attendance.get("Present", 0),
                late=attendance.get("Late", 0),
                absent=attendance.get("Absent", 0),
                attendance=attendance,
            )

    def generate_parentchild_relationships(self, parent_id, starting_page=1):
        page_one_response = self.endpoints.get_parentchild_relationships(
            parent_id, page=starting_page
        )

        for item in page_one_response.get("children", []):
            yield item

        pages = range(
            starting_page + 1, page_one_response.get("meta").get("total_pages") + 1
        )
        for page in pages:
            response = self.endpoints.get_parentchild_relationships(parent_id, page=page)
            for item in response.get("children", []):
                yield item

    def generate_terms_from_class_id(self, clss):
        response = self.endpoints.get_academic_years()
        terms = Terms(clss, response)
        for term in terms:
            yield term

    def generate_timetable_from_class_id(self, class_id, **kwargs):
        response = self.endpoints.get_class_timetable(class_id, **kwargs)
        academic_years = response.get("academic_years", [])
        for academic_year in academic_years:
            for slot in academic_year.get("slots", []):
                yield dict(
                    class_id=class_id,
                    academic_year_id=academic_year.get("id"),
                    day=slot.get("day"),
                    period=slot.get("period"),
                    start_date=academic_year.get("start_date", ""),
                    end_date=academic_year.get("end_date", ""),
                    name=academic_year.get("name", ""),
                    enabled=slot.get("enabled"),
                )

    def generate_class_timetable(self, archived=False, **kwargs):
        class_ids = []
        classes = self.generate_classes(archived=archived)
        for class_ in classes:
            class_ids.append(class_.get('id'))
        for class_id in class_ids:
            yield from self.generate_timetable_from_class_id(class_id, **kwargs)