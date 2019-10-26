from typing import TYPE_CHECKING

from drip.utils import json_list, json_object

if TYPE_CHECKING:
    from requests import Session


class Forms:

    session: 'Session'

    @json_list('forms')
    def forms(self, marshall=True, **options):
        """
        forms(marshall=True)

        List all forms.

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Form objects
        """
        return self.session.get('forms')

    @json_object('forms')
    def form(self, form_id, marshall=True, **options):
        """
        form(form_id, marshall=True)

        Get a form.

        Returns:
            Response -- API Response, or the marshalled Form object
        """
        return self.session.get(f'forms/{form_id}')
