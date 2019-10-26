from typing import TYPE_CHECKING

from drip.utils import json_list, json_object


if TYPE_CHECKING:
    from requests import Session


class Accounts:

    session: 'Session'
    api_domain: str
    api_version: str

    @json_list('accounts')
    def accounts(self, *, marshall=True, **kwargs):
        """
        accounts(marshall=True)

        List accounts associated with the authenticated user.

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Accounts objects
        """
        return self.session.get(f'{self.api_domain}/{self.api_version}/accounts/')

    @json_object('accounts')
    def account(self, account_id, *, marshall=True, **kwargs):
        """
        account(account_id, marshall=True)

        Get a specific account.

        Arguments:
            account_id {int} -- The account to get

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Account objects
        """
        return self.session.get(f'{self.api_domain}/{self.api_version}/accounts/{account_id}/')
