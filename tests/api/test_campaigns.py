

def test_campaigns(client):
    client.session.get.return_value.json.return_value.update({'campaigns': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.campaigns(param='param')
    client.session.get.called_once_with('campaigns', params=expected_params)


def test_campaign(client):
    client.session.get.return_value.json.return_value.update({'campaigns': [1, ]})
    client.campaign(1234)
    client.session.get.called_once_with('campaigns/1234')


def test_activate_campaign(client):
    client.session.post.return_value.status_code = 204
    client.activate_campaign(1234)
    client.session.post.called_once_with('campaigns/1234/activate')


def test_pause_campaign(client):
    client.session.post.return_value.status_code = 204
    client.pause_campaign(1234)
    client.session.post.called_once_with('campaigns/1234/pause')


def test_campaign_subscribers(client):
    client.session.get.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.campaign_subscribers(1234, param='param')
    client.session.get.assert_called_once_with('campaigns/1234/subscribers', params=expected_params)


def test_subscribe(client):
    client.session.post.return_value.json.return_value.update({'subscribers': [1, ]})
    expected_payload = {
        'subscribers': [
            {
                'email': 'email_address',
                'param': 'param'
            }
        ]
    }
    client.subscribe('email_address', 1234, param='param')
    client.session.post.assert_called_once_with('campaigns/1234/subscribers', json=expected_payload)


def test_campaign_subscriptions(client):
    client.session.get.return_value.json.return_value.update({'campaign_subscriptions': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.campaign_subscriptions('email_address', param='param')
    client.session.get.assert_called_once_with(
        'subscribers/email_address/campaign_subscriptions', params=expected_params)
