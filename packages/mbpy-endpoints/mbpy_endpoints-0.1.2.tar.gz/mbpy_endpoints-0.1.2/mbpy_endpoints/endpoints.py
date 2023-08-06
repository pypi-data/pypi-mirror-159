"""
Interface with the mb api implemented with uplink
"""
from datetime import datetime

from rich.text import Text
from rich.console import Console


from uplink import (
    Consumer,
    RequestsClient,
    Path,
    Body,
    Query,
    json,
    retry,
    get,
    post,
    patch,
    put,
    delete,
    ratelimit,
    returns,
    headers,
    response_handler,
)
from uplink.retry import RetryBackoff

console = Console()
from .errors import NotFound, NoPermissions


@response_handler
def output_console(response):
    """
    Display the requests and cooresponding responses as they come back from the server
    """
    request = response.request
    response_json = response.json()
    message = (
        ', '.join(
            [
                f'{key} ({len(response_json[key])})'
                if type(response_json[key]) == list
                else key
                for key in response_json.keys()
            ]
        )
        if response.ok
        else response_json.get('error')
    )
    text = Text.assemble(
        (request.method,
         f'bold {"magenta" if request.method == "GET" else "yellow"}'),
        ' ',
        request.url,
        (' => ', 'bold'),
        (str(response.status_code), 'bold green' if response.ok else 'bold red'),
        ': ',
        message,
    )
    console.print(text)
    return response


class FourTwentyNine(RetryBackoff):
    def get_timeout_after_response(self, request, response):
        seconds = None  # default
        if bland_style := response.header.get('Retry-After'):
            # seconds
            seconds = bland_style
        elif github_style := response.headers.get('X-RateLimit-Reset'):
            # gives us a timestamp
            now = datetime.now()
            future_date = datetime.strptime(github_style, '%Y-%m-%d %H:%M:%S UTC')
            seconds = abs((future_date - now).second)
        elif twitter_style := response.headers.get('X-Rate-Limit-Reset'):
            # gives us the seconds hurray
            seconds = twitter_style
        if not seconds is None:
            method, url, _ = request
            text = Text.assemble(
                (method, 'bold magenta'),
                ' ',
                url,
                (' => ', 'bold'),
                ('429', 'bold yellow'),
                ': ',
                (f'Sleeping for {seconds} second(s)', 'bold')
            )
            console.print(text)
        return seconds


class FourZeroFour(RetryBackoff):
    def get_timeout_after_response(self, request, response):
        prefix = f"Encountered 404: "
        method, url, _ = request
        raise NotFound(
            f"{prefix}{method} {url} -> {response.status_code} {response.json().get('error', response.text)}"
        )

class FourZeroOneFourZeroThree(RetryBackoff):
    def get_timeout_after_response(self, request, response):
        prefix = f"Invalid API key, or no permission for this endpoint: "
        method, url, _ = request
        raise NoPermissions(
            f"{prefix}{response.status_code} {response.json().get('error', response.text)} when trying {url}"
        )


@ratelimit(calls=100, period=60)  # Be polite and limit it to average a bit more than one call per second
@retry(
    # Handle 5xxs with extreme politeness
    when=retry.when.status_5xx(),
    stop=retry.stop.after_attempt(2),
    backoff=retry.backoff.jittered(multiplier=2),
)
@retry(
    # Raises custom error
    when=retry.when.status(429),
    stop=retry.stop.after_attempt(1),
    backoff=FourTwentyNine()
)
@retry(
    # Raises custom error
    when=retry.when.status(401) | retry.when.status(403),
    stop=retry.stop.after_attempt(1),
    backoff=FourZeroOneFourZeroThree()
)
@retry(
    # Raises custom error
    when=retry.when.status(404),
    stop=retry.stop.after_attempt(1),
    backoff=FourZeroFour()
)
@headers({'User-Agent': 'ctt/mbpy'})
#                        ^-- enables usage statitics to be tracked please and thank you
class Endpoint(Consumer):
    def __init__(self, auth_token, tld='com', subdomain='api', client=RequestsClient):
        # FIXME It only sends the host not the v2 part??
        base_url = f'https://{subdomain}.managebac.{tld}/'
        super(Endpoint, self).__init__(base_url=base_url, client=client)
        self.session.headers['auth-token'] = auth_token

    #
    # School
    #

    @returns.json(key='school')
    @get('v2/school')
    def get_school_details(self): pass

    @returns.json(key='year_groups')
    @get('v2/year-groups')
    def get_year_groups(self): pass

    @returns.json(key='academic_years')
    @get('v2/school/academic-years')
    def get_academic_years(self): pass

    @returns.json(key='subjects')
    @get('v2/school/subjects')
    def get_school_subjects(self): pass

    #
    # Classes
    #

    @returns.json
    @post('v2/classes/{class_id}/add_students')
    def add_student_to_class(self, class_id: Path, **body: Body): pass

    @returns.json
    @post('v2/classes/{class_id}/remove_students')
    def remove_students_from_class(self, class_id: Path, **body: Body): pass

    @returns.json
    @get('v2/classes')
    def get_classes(
        self,
        page: Query = 1,
        per_page: Query = 50,
        archived: Query = 0,
        modified_since: Query = None,
    ): pass

    @returns.json
    @get('v2/classes/{class_id}')
    def get_class(self, class_id: Path): pass

    @returns.json
    @get("v2/classes/{class_id}/assessments/term/{term_id}/term-grades")
    def get_term_grades(
        self,
        class_id: Path,
        term_id: Path,
        page: Query = 1,
        per_page: Query = 50,
        include_archived_students: Query = 1,
    ): pass

    #
    # Teachers
    #

    @returns.json
    @get("v2/teachers")
    def get_teachers(self, page: Query = 1, modified_since: Query = None): pass

    @returns.json
    @post('v2/teachers')
    def create_teacher(self, body: Body): pass

    #
    # Parents
    #

    @returns.json
    @get('v2/parents')
    def get_parents(self, page: Query = 1, modified_since: Query = None): pass

    @returns.json
    @post('v2/parents')
    def create_parent(self, body: Body): pass

    @returns.json
    @get('v2/parents/{parent_id}/children')
    def get_children(self, parent_id: Path): pass

    @returns.json
    @post('v2/parents/{parent_id}/children/{child_id}')
    def add_child_association(self, parent_id: Path, child_id: Path, body: Body): pass

    @returns.json
    @post('v2/parents/{parent_id}/children')
    def define_children(self, parent_id: Path, body: Body): pass

    @returns.json
    @patch('v2/parents/{parent_id}/children/{child_id}')
    def update_child(self, parent_id, child_id, body: Body): pass

    @returns.json
    @put('v2/parents/{parent_id}/children')
    def bulk_update_children(self, parent_id: Path, body: Body): pass

    @delete('/v2/parents/{parent_id}/children/{child_id}')
    def remove_child_association(
        self, parent_id: Path, child_id: Path, body: Body): pass

    #
    # Attendance
    #

    @returns.json
    @get('v2/year-groups/{year_group_id}/homeroom/attendance/term/{term_id}')
    def get_homeroom_attendance(self, year_group_id: Path, term_id: Path): pass

    @returns.json
    @get('v2/classes/{class_id}/attendance/term/{term_id}')
    def get_class_attendance(self, class_id: Path, term_id: Path): pass

    @returns.json(key='timetable')
    @get('v2/classes/{class_id}/timetable')
    def get_class_timetable(self, class_id: Path, class_happens_on: Query = None): pass

    #
    # Students
    #

    @returns.json
    @get('v2/students')
    def get_students(
        self,
        page: Query = 1,
        per_page: Query = 50,
        archived: Query = None,
        status: Query = None,
        modified_since: Query = None,
        deleted_since: Query = None,
        q: Query = None,
    ): pass

    @returns.json(key='student')
    @get('v2/students/{id}')
    def get_a_student(self, id: Path): pass

    @returns.json
    @post('v2/students')
    def create_new_student(self, **body: Body): pass

    @returns.json
    @patch('v2/students/{id}')
    def update_a_student(self, id: Path, **body: Body): pass

    @returns.json
    @put('v2/students/{id}/archive')
    def archive_a_student(
        self, id: Path, withdrawn_on: Query = None, graduated_on: Query = None
    ): pass

    @returns.json
    @put('v2/students/{id}/unarchive')
    def unarchive_a_student(self, id: Path): pass

    #
    # Teachers
    #

    @returns.json(key='teacher')
    @get('v2/teachers/{id}')
    def get_a_teacher(self, id: Path): pass

    #
    # Parents
    #

    @returns.json(key='parent')
    @get('v2/parents/{id}')
    def get_a_parent(self, id: Path): pass

    @returns.json
    @get('v2/parents/{parent_id}/children')
    def get_parentchild_relationships(
        self, parent_id: Path, page: Query = 1, per_page: Query = 50
    ): pass

    #
    # Memberships
    #

    @returns.json
    @get('v2/memberships')
    def get_memberships(
        self,
        modified_since: Query = None,
        deleted_since: Query = None,
        class_happens_on: Query = None,
        classes: Query = None,
        user_ids: Query = None,
        users: Query = None,
        page: Query = 1,
        per_page: Query = 50,
    ): pass
