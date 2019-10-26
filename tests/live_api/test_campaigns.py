import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_campaigns(live_client):
    response = live_client.campaigns()

    assert type(response) == list
    assert len(response) == 4

    response = live_client.campaigns(status="active")

    assert type(response) == list
    assert len(response) == 1
    assert response[0]['status'] == 'active'


def test_campaign(live_client):
    campaign_id = 112916503
    response = live_client.campaign(campaign_id)

    p_contains = partial(contains, response)

    assert len(response) == 23
    assert all(map(p_contains, ['id', 'status', 'name', 'from_name', 'from_email', 'postal_address', 'minutes_from_midnight', 'localize_sending_time', 'days_of_the_week_mask',
                                'start_immediately', 'double_optin', 'send_to_confirmation_page', 'use_custom_confirmation_page', 'confirmation_url', 'notify_subscribe_email',
                                'notify_unsubscribe_email', 'bcc', 'email_count', 'active_subscriber_count', 'unsubscribed_subscriber_count', 'created_at', 'href', 'links']))
    assert response['id'] == str(campaign_id)
    assert response['status'] == 'active'


def test_activate_campaign(live_client):
    campaign_id = 562885259
    check = live_client.session.get(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}').json()['campaigns'][0]
    assert check['status'] == 'paused'

    response = live_client.activate_campaign(campaign_id)
    assert type(response) == bool
    assert response

    check = live_client.session.get(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}').json()['campaigns'][0]
    assert check['status'] == 'active'

    # cleanup
    live_client.session.post(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}/pause')


def test_pause_campaign(live_client):
    campaign_id = 112916503
    check = live_client.session.get(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}').json()['campaigns'][0]
    assert check['status'] == 'active'

    response = live_client.pause_campaign(campaign_id)
    assert type(response) == bool
    assert response

    check = live_client.session.get(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}').json()['campaigns'][0]
    assert check['status'] == 'paused'

    # cleanup
    live_client.session.post(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}/activate')


def test_campaign_subscribers(live_client):
    campaign_id = 112916503
    response = live_client.campaign_subscribers(campaign_id)

    assert type(response) == list
    assert len(response) == 1
    assert response[0]['email'] == 'ross.hodapp+drip-python@drip.com'


def test_subscribe(live_client):
    campaign_id = 112916503

    # setUp
    live_client.session.post(f'https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com/remove', params={'campaign_id': campaign_id})

    response = live_client.subscribe('ross.hodapp+drip-python@drip.com', campaign_id)
    assert type(response) == dict
    assert response['email'] == 'ross.hodapp+drip-python@drip.com'

    confirm = live_client.session.get(f'https://api.getdrip.com/v2/5706364/campaigns/{campaign_id}/subscribers').json()['subscribers'][0]
    assert confirm['email'] == 'ross.hodapp+drip-python@drip.com'


def test_campaign_subscriptions(live_client):
    response = live_client.campaign_subscriptions('ross.hodapp+drip-python@drip.com')
    assert type(response) == list
    assert len(response) == 1

    p_contains = partial(contains, response[0])

    assert len(response[0]) == 8
    assert all(map(p_contains, ['id', 'campaign_id', 'status', 'is_complete', 'lap', 'last_sent_email_index', 'last_sent_email_at', 'links']))
