from typing import TYPE_CHECKING

from drip.utils import json_list, json_object

if TYPE_CHECKING:
    from requests import Session


class Conversions:

    session: 'Session'

    @json_list('goals')
    def conversions(self, marshall=True, **params):
        """
        conversions(status='all', sort='created_at', direction='asc', marshall=True)

        List conversions. Supports filtering.

        Call Parameters:
            status {str} -- Filter by status: enabled, disabled (default: {'enabled'})
            sort {str} -- Attribute to sort by: created_at, name (default: {'created_at'})
            direction {str} -- Directon to sort by: asc, desc  (default: {'asc'})

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled List of Conversion objects
        """
        return self.session.get('goals', params=params)

    @json_object('goals')
    def conversion(self, conversion_id, marshall=True):
        """
        conversion(conversion_id, marshall=True)

        List a conversion.

        Arguments:
            conversion_id {int} -- Campaign ID

        Other Keyword Arguments:
            marshall {bool} -- Unpack the Response object (default: {True})

        Returns:
            Response -- API Response, or the marshalled Conversion object
        """
        return self.session.get(f'goals/{conversion_id}')
