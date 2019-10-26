from typing import TYPE_CHECKING

from drip.utils import json_list, raise_response

if TYPE_CHECKING:
    from requests import Session


class Events:

    session: 'Session'

    @raise_response()
    def track_event(self, email, action, **options):
        """
        track_event(email, action, prospect=True, properties=None, occurred_at=None, marshall=True)

        Apply an Event to the subsriber.

        Arguments:
            email {str} -- Subscriber email
            action {str} -- Event name

        Call Options:
            prospect {bool} -- Person is a Prospect (default: {True})
            properties {Mapping[str, str]} -- Number of objects to get on each page (default: {100})
            occurred_at {str} -- Date + time the Event happened, Eg. "2016-01-01T00:00:00Z" (default: {None})

        Returns:
            Response -- API Response
        """
        payload = {
            'email': email,
            'action': action,
        }
        if options:
            payload.update(options)
        return self.session.post('events', json={'events': [payload, ]})

    @json_list('event_actions')
    def event_actions(self, marshall=True, **params):
        """
        event_actions(page=0, per_page=100, marshall=True)

        List all Events performed.

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})

        Returns:
            Response -- API Response, or the marshalled List of Event objects
        """
        return self.session.get('event_actions', params=params)
