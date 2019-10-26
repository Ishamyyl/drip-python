from typing import TYPE_CHECKING

from drip.utils import raise_response

if TYPE_CHECKING:
    from requests import Session


class Tags:

    session: 'Session'

    def tags(self):
        """
        tags()

        List all tags.

        Returns:
            Iterable[str] -- A List of tags
        """
        return self.session.get('tags').json()['tags']

    @raise_response()
    def apply_tag(self, email, tag):
        """
        apply_tag(email, tag)

        Apply a Tag to a subscriber.

        Arguments:
            email {str} -- Person's email address
            tag {str} -- Tag to apply

        Returns:
            Response -- API Response
        """
        return self.session.post('tags', json={'tags': [{'email': email, 'tag': tag}]})

    @raise_response()
    def remove_tag(self, email, tag):
        """
        remove_tag(email, tag)

        Remove a Tag from a subscriber.

        Arguments:
            email {str} -- Person's email address
            tag {str} -- Tag to remove

        Returns:
            Response -- API Response
        """
        return self.session.delete(f'subscribers/{email}/tags/{tag}')
