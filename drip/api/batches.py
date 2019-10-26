from typing import TYPE_CHECKING

from drip.utils import raise_response

if TYPE_CHECKING:
    from requests import Session


class Batches:

    session: 'Session'
    api_domain: str
    account_id: int

    @raise_response()
    def create_or_update_subscribers(self, subscribers):
        """
        create_or_update_subscribers(subscribers)

        Update a batch of subscribers or create them if they don't exist.

        Arguments:
            subscribers {Iterable[SubscriberJsonType]} -- A list of Subscriber objects

        Returns:
            Response -- API Response
        """
        return self.session.post('subscribers/batches', json={'batches': [{'subscribers': subscribers}, ]})

    @raise_response()
    def unsubscribe_subscribers(self, subscribers):
        """
        unsubscribe_subscribers(subscribers)

        Unsubscribe a batch of subscribers.

        Arguments:
            subscribers {Iterable[EmailJsonType]} -- A list of subscriber emails

        Returns:
            Response -- API Response
        """
        return self.session.post('unsubscribes/batches', json={'batches': [{'subscribers': subscribers}, ]})

    @raise_response()
    def track_events(self, events):
        """
        track_events(events)

        Apply an Events to the related subscriber in a batch.

        Arguments:
            events {Iterable[EventJsonType]} -- A list of event objects

        Returns:
            Response -- API Response
        """
        return self.session.post('events/batches', json={'batches': [{'events': events}, ]})

    @raise_response()
    def orders(self, orders):
        """
        create_or_update_orders(orders)

        Update a batch of orders or create them if they don't exist.

        Arguments:
            orders {Iterable[OrderJsonType]} -- A list of order objects

        Returns:
            Response -- API Response
        """
        return self.session.post(f'{self.api_domain}/v3/{self.account_id}/shopper_activity/order/batch', json={'orders': orders})
