
def test_create_update_subscriber(client):
    client.session.post.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_payload = {
        'subscribers': [
            {
                'email': 'email_address',
                'option': 'option',
            }
        ]
    }
    client.create_or_update_subscriber('email_address', option='option')
    client.session.post.assert_called_once_with('subscribers', json=expected_payload)


def test_create_update_subscriber_from_docs(client):
    client.session.post.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_payload = {
        "subscribers": [{
            "email": "john@acme.com",
            "time_zone": "America/Los_Angeles",
            "custom_fields": {
                "name": "John Doe"
            }
        }]
    }
    client.create_or_update_subscriber('john@acme.com', time_zone='America/Los_Angeles',
                                       custom_fields={"name": "John Doe"})
    client.session.post.assert_called_once_with('subscribers', json=expected_payload)


def test_subscribers(client):
    client.session.get.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.subscribers(**expected_params)
    client.session.get.assert_called_once_with('subscribers', params=expected_params)


def test_subscriber(client):
    client.session.get.return_value.json.return_value.update({'subscribers': [1, ]})
    client.subscriber('email_address')
    client.session.get.assert_called_once_with('subscribers/email_address')


def test_unsubscribe(client):
    client.session.post.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.unsubscribe('email_address', **expected_params)
    client.session.post.assert_called_once_with('subscribers/email_address/remove', params=expected_params)


def test_unsubscribe_from_all(client):
    client.session.post.return_value.json.return_value.update({'subscribers': [1, ]})
    client.unsubscribe_from_all('email_address')
    client.session.post.assert_called_once_with('subscribers/email_address/unsubscribe_all')


def test_delete_subscriber(client):
    client.session.delete.return_value.status_code = 204
    client.delete_subscriber('email_address')
    client.session.delete.assert_called_once_with('subscribers/email_address')
