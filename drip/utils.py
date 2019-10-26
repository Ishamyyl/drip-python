from functools import partial, wraps
from typing import TYPE_CHECKING

from requests import HTTPError, codes

if TYPE_CHECKING:
    from typing import Callable, Union, Any, List, Mapping
    from requests import Response
    from drip.typeshed import JsonListType, JsonMappingType
    from drip.client import Client

accepted_codes = {codes.ok, codes.created, codes.accepted, codes.no_content}  # pylint: disable=no-member


class DripApiError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__()

    def __str__(self):
        j = 'Drip REST API returned the following error(s):', *(f"\t{e['code']}: {e['message']}" for e in self.errors)
        return '\n'.join(j)


class raise_response:

    def __call__(self, api_call):
        @wraps(api_call)
        def wrapped(client, *args, **kwargs):
            response = api_call(client, *args, **kwargs)
            if 'errors' in response:
                raise DripApiError(response['errors'])
            try:
                response.raise_for_status()
            except HTTPError as exptn:
                raise type(exptn)(*exptn.args).with_traceback(exptn.__traceback__)
            return response.status_code in accepted_codes
        return wrapped


class json_list:
    """
    Convenience decorator that gets all pages.

    If a valid 'page' is passed to the function, then this will fetch that page only (or the single un-marshalled Response).

    Otherwise-- that is, if page is 0 (default) or negative-- then this will fetch the JSON objects for all pages and return
    the full list. This will ignore the 'per_page' argument and use 1000 for maximum efficiency.

    Currently, we won't support getting all pages of 1 object per page for example, since we don't see a valid use-case for this.
    This means essentially that 'per_page' only makes sense when asking for a specific 'page'.
    This also means that you can only marshal a specific page (this may change in the future).
    """

    def __init__(self, section):
        self.section = section

    def __call__(self, api_call):
        @wraps(api_call)
        def wrapped(client: 'Client', *args, **kwargs) -> 'Union[JsonListType, Response]':
            page = kwargs.pop('page', 0)
            per_page = kwargs.pop('per_page', 100)
            wants_to_marshall = kwargs.pop('marshall', True)

            frozen_api_call: 'Callable[..., Response]' = partial(api_call, client, *args, **kwargs)

            # Do they want a specific page?
            if page > 0:
                response_one_page = frozen_api_call(page=page, per_page=per_page)
                if 'errors' in response_one_page.json():
                    raise DripApiError(response_one_page.json()['errors'])  # stop yelling at me!
                if wants_to_marshall:
                    return response_one_page.json()[self.section]
                else:
                    return response_one_page
            else:
                # Get the 1st page
                response_all_pages = frozen_api_call(page=1, per_page=1000).json()
                if 'errors' in response_all_pages:
                    raise DripApiError(response_all_pages['errors'])
                result = response_all_pages[self.section]

                meta = response_all_pages.get('meta', False)
                if meta:
                    total_pages = meta.get('total_pages', 0)
                    if total_pages > 1:
                        # Loop through any remaining pages
                        for next_page in range(2, total_pages+1):
                            r = frozen_api_call(page=next_page, per_page=1000).json()
                            if 'errors' in r:
                                raise DripApiError(r['errors'])
                            result.extend(r[self.section])
                return result
        return wrapped


class json_object:

    def __init__(self, section):
        self.section = section

    def __call__(self, api_call):
        @wraps(api_call)
        def wrapped(client: 'Client', *args, **kwargs) -> 'Union[JsonMappingType, Response]':
            should_marshall = kwargs.pop('marshall', True)
            result = api_call(client, *args, **kwargs)
            if 'errors' in result:
                raise DripApiError(result['errors'])
            if should_marshall:
                return result.json()[self.section][0]
            return result
        return wrapped
