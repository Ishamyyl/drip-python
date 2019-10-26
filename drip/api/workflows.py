from typing import TYPE_CHECKING

from drip.utils import json_list, json_object, raise_response

if TYPE_CHECKING:
    from requests import Session


class Workflows:

    session: 'Session'

    @json_list('workflows')
    def workflows(self, marshall=True, **params):
        """
        workflows(page=0, per_page=100, status=None, sort=None, direction=None, marshall=True)

        List workflows. Supports pagination and filtering.

        Call Parameters:
            page {int} -- Page to get, or 0 for all pages (default: {0})
            per_page {int} -- Number of objects to get on each page (default: {100})
            status {str} -- Filter by status: all, draft, active, paused (default: {'all'})
            sort {str} -- Attribute to sort by: created_at, name (default: {'created_at'})
            direction {str} -- Directon to sort by: asc, desc (default: {'asc'})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Workflow object
        """
        return self.session.get('workflows', params=params)

    @json_object('workflows')
    def workflow(self, workflow_id, marshall=True):
        """
        workflow(workflow_id, marshall=True)

        Get a specific workflow.

        Arguments:
            workflow_id {int} -- Workflow ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Workflow object
        """
        return self.session.get(f'workflows/{workflow_id}')

    @raise_response()
    def activate_workflow(self, workflow_id):
        """
        activate_workflow(workflow_id)

        Activate a workflow.

        Arguments:
            workflow_id {int} -- Workflow ID

        Returns:
            Response -- API Response
        """
        return self.session.post(f'workflows/{workflow_id}/activate')

    @raise_response()
    def pause_workflow(self, workflow_id):
        """
        pause_workflow(workflow_id)

        Pause a workflow.

        Arguments:
            workflow_id {int} -- Workflow ID

        Returns:
            Response -- API Response
        """
        return self.session.post(f'workflows/{workflow_id}/pause')

    @raise_response()
    def start_subscriber_workflow(self, email, workflow_id, **options):
        """
        start_subscriber_workflow(email, workflow_id,
            user_id=None, time_zone=None, custom_fields=None, tags=None, prospect=True, eu_consent=None, eu_consent_message)

        Start a person on a workflow.

        Arguments:
            workflow_id {int} -- Workflow ID
            email {str} -- Subscriber email

        Call Options:
            user_id {str} -- A custom unique identifier (default: {None})
            time_zone {str} -- The person's timezone (default: {'Etc/UTC'})
            custom_fields {Mapping[str, str]} -- Dictionary of custom fields and values (default: {None})
            tags {Iterable[str]} -- List of tags (default: {None})
            prospect {bool} -- Person is a Prospect (default: {True})
            eu_consent {str} -- Status of consent for GDPR: granted, denied (default: {None})
            eu_consent_message {str} -- Message that was consented to (default: {None})

        Returns:
            Response -- API Response
        """
        payload = {
            'email': email,
        }
        if options:
            payload.update(options)
        return self.session.post(f'workflows/{workflow_id}/subscribers', json={'subscribers': [payload, ]})

    @raise_response()
    def remove_subscriber_workflow(self, workflow_id, email):
        """
        remove_subscriber_workflow(email, workflow_id)

        Remove a person from a workflow.

        Arguments:
            workflow_id {int} -- Workflow ID
            email {str} -- Subscriber email

        Returns:
            Response -- API Response
        """
        return self.session.delete(f'workflows/{workflow_id}/subscribers/{email}')

    @json_list('triggers')
    def workflow_triggers(self, workflow_id, marshall=True, **options):
        """
        workflow_triggers(workflow_id, marshall=True)

        List the Triggers in a Workflow.

        Arguments:
            workflow_id {int} -- Workflow ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Triggers objects
        """
        return self.session.get(f'workflows/{workflow_id}/triggers')

    @json_list('triggers')
    def create_workflow_trigger(self, workflow_id, provider, trigger_type, marshall=True, **options):
        """
        create_workflow_trigger(workflow_id, provider, trigger_type, properties=None, marshall=True)

        Create a Trigger on a Workflow.

        Arguments:
            workflow_id {int} -- Workflow ID
            provider {str} -- Source
            trigger_type {str} -- Automation trigger type

        Call Options:
            properties {Mapping[str, str]} -- Dictionary of custom properties (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Campaign objects
        """
        payload = {
            'provider': provider,
            'trigger_type': trigger_type,
        }
        payload.update(options)
        return self.session.post(f'workflows/{workflow_id}/triggers', json={"triggers": [payload, ]})

    @json_list('triggers')
    def update_workflow_trigger(self, workflow_id, provider, trigger_type, marshall=True, **options):
        """
        create_workflow_trigger(workflow_id, provider, trigger_type, properties=None, marshall=True)

        Update a Trigger on a Workflow.

        Arguments:
            workflow_id {int} -- Workflow ID
            provider {str} -- Source
            trigger_type {str} -- Automation trigger type

        Call Options:
            properties {Mapping[str, str]} -- Dictionary of custom properties (default: {None})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Campaign objects
        """
        payload = {
            'provider': provider,
            'trigger_type': trigger_type,
        }
        payload.update(options)
        return self.session.put(f'workflows/{workflow_id}/triggers', json={"triggers": [payload, ]})
