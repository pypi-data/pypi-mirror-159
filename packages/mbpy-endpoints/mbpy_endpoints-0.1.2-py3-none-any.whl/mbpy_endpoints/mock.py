from .endpoints import Endpoint
import re
from rich.text import Text
from rich.console import Console
console = Console()

class MockEndpoint(Endpoint):
    """
    Overrides writable endpoints 
    so that we don't actually do them, instead is output
    If body is passed as keyword argument, returns the body, 
    else {}
    """

    def __getattribute__(self, name):
        """
        Ensure that non-GET methods do not actually go to the wire
        """
        ret = object.__getattribute__(self, name)
        if hasattr(ret, '_request_definition'):
            method = ret._request_definition._method
            uri = ret._request_definition._uri
            if not method == 'GET':
                def print_and_return(*args, **kwargs):
                    try:
                        resolved = uri.format(**kwargs)
                    except KeyError:
                        # change {keyword} to {}
                        new_uri = re.sub('({).*?(})', r'\1\2', uri)
                        resolved = new_uri.format(*args)
                    text = Text.assemble(
                        (method, f'bold magenta yellow'),
                        ' ',
                        resolved,
                        (' => ', 'bold'),
                        ('200', 'bold green'),
                        ': ',
                        ('(MOCKED)', f'bold black')
                    )
                    console.print(text)
                    if body := kwargs.get('body'):
                        return body
                    return {}
                return lambda *args, **kwargs: print_and_return(*args, **kwargs)
        return ret
