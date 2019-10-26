

def test_tags(client):
    client.session.get.return_value.json.return_value.update({'tags': [1, ]})
    client.tags()
    client.session.get.assert_called_once_with('tags')


def test_apply_tag(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'tags': [
            {
                'email': 'email_address',
                'tag': 'tag'
            }
        ]
    }
    client.apply_tag('email_address', 'tag')
    client.session.post.assert_called_once_with('tags', json=expected_payload)


def test_remove_tag(client):
    client.session.delete.return_value.status_code = 204
    client.remove_tag('email_address', 'tag')
    client.session.delete.assert_called_once_with('subscribers/email_address/tags/tag')
