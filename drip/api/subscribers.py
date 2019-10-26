from typing import TYPE_CHECKING

from drip.utils import json_list, json_object, raise_response

if TYPE_CHECKING:
    from requests import Session


class Subscribers:

    session: 'Session'

    @json_object('subscribers')
    def create_or_update_subscriber(self, email, marshall=True, **options):
        """
        create_or_update_subscriber(email,
            new_email=None, user_id=None, time_zone='Etc/UTC', lifetime_value=None, ip_address=None,
            tags=None, remove_tags=None, prospect=True, base_lead_score=30, eu_consent=None, eu_consent_message=None, marshall=True)

        Update a subscriber or create it if it doesn't exist.

        Arguments:
            email {str} -- Person's email address

        Call Options:
            new_email {str} -- Update the subscriber's email address, taking precedence over 'email' while creating (default: {None})
            user_id {str} -- A custom unique identifier (default: {None})
            time_zone {str} -- Timezone (default: {'Etc/UTC'})
            lifetime_value {int} -- LifeTime Value, in cents (default: {None})
            ip_address {str} -- IP Address (default: {None})
            custom_fields {Mapping[str, Any]} -- Dictionary of custom fields and their values (default: {None})
            tags {Iterable[str]} -- List of tags to apply (default: {None})
            remove_tags {Iterable[str]} --  List of tags to remove (default: {None})
            prospect {bool} -- Person is a Prospect (default: {True})
            base_lead_score {int} -- Starting leadscore (default: {0})
            eu_consent {str} -- Status of consent for GDPR: granted, denied (default: {None})
            eu_consent_message {str} -- Message that was consented to (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Subscriber object
        """
        payload = {
            'email': email,
        }
        payload.update(options)
        return self.session.post('subscribers', json={'subscribers': [payload, ]})

    @json_list('subscribers')
    def subscribers(self, marshall=True, **params):
        """
        subscribers(page=0, per_page=100, marshall=True)

        List all subscribers. Supports pagination and filtering.

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})
            tags {Iterable[str]} -- List of tags to filter by (default: {None})
            subscribed_before {str} -- Include only people created before this date, Eg. "2016-01-01T00:00:00Z" (default: {None})
            subscribed_after {str} -- Include only people after before this date, Eg. "2016-01-01T00:00:00Z" (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Subscriber objects
        """
        return self.session.get('subscribers', params=params)

    @json_object('subscribers')
    def subscriber(self, email, marshall=True):
        """
        subscriber(email, marshall=True)

        Get a subscriber.

        Arguments:
            email {str} -- Person's email address

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Subscriber object
        """
        return self.session.get(f'subscribers/{email}')

    @json_object('subscribers')
    def unsubscribe(self, email, marshall=True, **params):
        """
        unsubscribe(email, campaign_id=None, marshall=True)

        Unsubscribe a subscriber from all campaigns, or optionally one specific campaign.

        Arguments:
            email {str} -- Person's email address

        Call Parameters:
            campaign_id {int} -- Campaign from which to remove the subscriber (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Subscriber object
        """
        return self.session.post(f'subscribers/{email}/remove', params=params)

    @json_object('subscribers')
    def unsubscribe_from_all(self, email, marshall=True):
        """
        unsubscribe_from_all(email, campaign_id=None, marshall=True)

        Unsubscribe a subscriber from all campaigns.

        Arguments:
            email {str} -- Person's email address

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Subscriber object
        """
        return self.session.post(f'subscribers/{email}/unsubscribe_all')

    @raise_response()
    def delete_subscriber(self, email):
        """
        delete_subscriber(email, campaign_id=None, marshall=True)

        Delete a subscriber.

        Arguments:
            email {str} -- Person's email address

        Returns:
            Response -- API Response
        """
        return self.session.delete(f'subscribers/{email}')

    # @pagination('subscribers')
    # def subscribers(self,
    #                 status: str = None,  # active, all, unsubscribed, active_or_unsubscribed, undeliverable. Default: active
    #                 tags: 'Iterable[str]' = None,
    #                 subscribed_before: str = None,  # "2017-01-01T00:00:00Z"
    #                 subscribed_after: str = None,
    #                 page: int = 0,
    #                 per_page: int = None,
    #                 marshall=True) -> 'Response':
    #     payload: 'MutableMapping[str, Any]' = {}
    #     if status:
    #         payload['status'] = status
    #     if tags:
    #         payload['tags'] = tags
    #     if subscribed_before:
    #         payload['subscribed_before'] = subscribed_before
    #     if subscribed_after:
    #         payload['subscribed_after'] = subscribed_after
    #     if page:
    #         payload['page'] = page
    #     if per_page:
    #         payload['per_page'] = per_page
    #     return self.session.get('subscribers', params=payload)
