from typing import TYPE_CHECKING

from drip.utils import json_list, json_object

if TYPE_CHECKING:
    from requests import Session


class Broadcasts:

    session: 'Session'

    @json_list('broadcasts')
    def broadcasts(self, marshall=True, **params):
        """
        broadcasts(page=0, per_page=100, status='all', sort='created_at', direction='asc', marshall=True)

        List all broadcasts. Supports pagination and filtering.

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})
            status {str} -- Filter by status: all, draft, scheduled, sent (default: {'all'})
            sort {str} -- Attribute to sort by: created_at, send_at, name (default: {'created_at'})
            direction {str} -- Directon to sort by: asc, desc (default: {'asc'})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Broadcast objects
        """
        return self.session.get('broadcasts', params=params)

    @json_object('broadcasts')
    def broadcast(self, broadcast_id, marshall=True):
        """
        broadcast(broadcast_id, marshall=True)

        List a broadcast.

        Arguments:
            broadcast_id {int} -- Broadcast ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Broadcast object
        """
        return self.session.get(f'broadcasts/{broadcast_id}')
