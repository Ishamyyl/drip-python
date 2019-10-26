from typing import TYPE_CHECKING

from drip.utils import json_object

if TYPE_CHECKING:
    from requests import Session


class Users:

    session: 'Session'
    api_domain: str
    api_version: str

    @json_object('users')
    def fetch_user(self, marshall=True):
        """
        fetch_user(marshall=True)

        Get the authenticated User.

        Returns:
            Response -- API Response, or the marshalled User object
        """
        return self.session.get(f'{self.api_domain}/{self.api_version}/user')
