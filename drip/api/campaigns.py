from typing import TYPE_CHECKING

from drip.utils import json_list, json_object, raise_response

if TYPE_CHECKING:
    from requests import Session


class Campaigns:

    session: 'Session'

    @json_list('campaigns')
    def campaigns(self, marshall=True, **params):
        """
        campaigns(page=0, per_page=100, status='active', sort='created_at', direction='desc', marshall=True)

        List campaigns. Supports pagination and filtering.

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})
            status {str} -- Filter by status: all, draft, active, paused (default: {'all'})
            sort {str} -- Attribute to sort by: created_at, name (default: {'created_at'})
            direction {str} -- Directon to sort by: desc, asc (default: {'asc'})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Campaign objects
        """
        return self.session.get('campaigns', params=params)

    @json_object('campaigns')
    def campaign(self, campaign_id, marshall=True):
        """
        campaign(campaign_id, marshall=True)

        Fwtch a campaign.

        Arguments:
            campaign_id {int} -- Campaign ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Campaign object
        """
        return self.session.get(f'campaigns/{campaign_id}')

    @raise_response()
    def activate_campaign(self, campaign_id):
        """
        activate_campaign(campaign_id)

        Activate a campaign.

        Arguments:
            campaign_id {int} -- Campaign ID

        Returns:
            Response -- API Response
        """
        return self.session.post(f'campaigns/{campaign_id}/activate')

    @raise_response()
    def pause_campaign(self, campaign_id):
        """
        pause_campaign(campaign_id)

        Pause a campaign.

        Arguments:
            campaign_id {int} -- Campaign ID

        Returns:
            Response -- API Response
        """
        return self.session.post(f'campaigns/{campaign_id}/pause')

    @json_list('subscribers')
    def campaign_subscribers(self, campaign_id, marshall=True, **params):
        """
        campaign_subscribers(campaign_id, page=0, per_page=100, status='active', sort='created_at', direction='desc', marshall=True)

        List subscribers in a campaign. Supports pagination and filtering.

        Arguments:
            campaign_id {int} -- Campaign ID

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})
            status {str} -- Filter by status: active, unsubscribed, removed (default: {'active'})
            sort {str} -- Attribute to sort by: created_at, id (default: {'created_at'})
            direction {str} -- Directon to sort by: desc, asc (default: {'desc'})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Subscriber objects
        """
        return self.session.get(f'campaigns/{campaign_id}/subscribers', params=params)

    @json_object('subscribers')
    def subscribe(self, email, campaign_id, marshall=True, **options):
        """
        subscribe(campaign_id, email,
            user_id=None, time_zone='Etc/UTC', double_optin=None, starting_email_index=0, custom_fields=None, tags=None,
            reactivate_if_removed=True, prospect=True, base_lead_score=30, eu_consent=None, eu_consent_message=None, marshall=True)

        Subscribe a person to a campaign.

        Arguments:
            campaign_id {int} -- Campaign ID
            email {str} -- Subscriber email

        Call Options:
            user_id {str} -- A custom unique identifier (default: {None})
            time_zone {str} -- The person's timezone (default: {'Etc/UTC'})
            double_optin {bool} -- Send the double opt-in confirmation email (default: {None})
            starting_email_index {int} -- The index (zero-based) of the email to send first. (default: {0})
            custom_fields {Mapping[str, str]} -- Dictionary of custom fields and values (default: {None})
            tags {Iterable[str]} -- List of tags (default: {None})
            reactivate_if_removed {bool} -- Restart the campaign if they were removed (default: {True})
            prospect {bool} -- Person is a Prospect (default: {True})
            base_lead_score {int} -- Starting Leadscore (default: {30})
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
        return self.session.post(f'campaigns/{campaign_id}/subscribers', json={'subscribers': [payload, ]})

    @json_list('campaign_subscriptions')
    def campaign_subscriptions(self, email, marshall=True, **params):
        """
        campaign_subscriptions(email, page=0, per_page=100, marshall=True)

        List the campaigns for a subscriber. Supports pagination.

        Arguments:
            email {str} -- Subscriber email or id  (or visitor_uuid?)

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Campaign objects
        """
        return self.session.get(f'subscribers/{email}/campaign_subscriptions', params=params)
