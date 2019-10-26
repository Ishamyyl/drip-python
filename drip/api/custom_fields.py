from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Session


class CustomFields:

    session: 'Session'

    def custom_fields(self):
        """
        custom_fields()

        List all custom fields.

        Returns:
            Iterable[str] -- A List of custom fields
        """
        return self.session.get('custom_field_identifiers').json()['custom_field_identifiers']
