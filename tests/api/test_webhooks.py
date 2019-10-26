

def test_webhooks(client):
    client.session.get.return_value.json.return_value.update({'webhooks': [1, ]})
    client.webhooks()
    client.session.get.assert_called_once_with('webhooks')


def test_webhook(client):
    client.session.get.return_value.json.return_value = {'webhooks': [1, ]}
    client.webhook(1234)
    client.session.get.assert_called_once_with('webhooks/1234')


def test_create_webhook(client):
    client.session.post.return_value.json.return_value.update({'webhooks': [1, ]})
    expected_payload = {
        'post_url': 'url',
        'events': ['event']
    }
    client.create_webhook('url', events=['event'])
    client.session.post.assert_called_once_with('webhooks', json={'webhooks': [expected_payload, ]})


def test_delete_webhook(client):
    client.session.delete.return_value.status_code = 204
    client.delete_webhook(1234)
    client.session.delete.assert_called_once_with('webhooks/1234')
