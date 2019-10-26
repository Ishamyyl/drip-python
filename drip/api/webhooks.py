from typing import TYPE_CHECKING

from drip.utils import json_list, json_object, raise_response

if TYPE_CHECKING:
    from requests import Session


class Webhooks:

    session: 'Session'

    @json_list('webhooks')
    def webhooks(self, marshall=True, **options):
        """
        webhooks(marshall=True)

        List all webhooks.

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Webhook objects
        """
        return self.session.get('webhooks')

    @json_object('webhooks')
    def webhook(self, webhook_id, marshall=True):
        """
        webhook(webhook_id, marshall=True)

        Get a specific webhook.

        Arguments:
            webhook_id {int} -- Webhook ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Webhook object
        """
        return self.session.get(f'webhooks/{webhook_id}')

    @json_object('webhooks')
    def create_webhook(self, post_url, marshall=True, **options):
        """
        create_webhook(post_url, include_received_email=False, events=None, marshall=True)

        Arguments:
            post_url {str} -- URL to send data from the webhook to

        Keyword Arguments:
            include_received_email {bool} -- Also active the Received Email webhook (default: {False})
            events {Iterable[str]} -- List of webhook names to activate (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Webhook object
        """

        payload = {
            'post_url': post_url,
        }
        payload.update(options)
        return self.session.post('webhooks', json={'webhooks': [payload, ]})

    @raise_response()
    def delete_webhook(self, webhook_id):
        """
        delete_webhook(webhook_id)

        Delete a specific webhook.

        Arguments:
            webhook_id {int} -- Webhook ID

        Returns:
            Response -- API Response
        """
        return self.session.delete(f'webhooks/{webhook_id}')
