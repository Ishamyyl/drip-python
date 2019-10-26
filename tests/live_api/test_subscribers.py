import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_create_update_subscriber(live_client):
    check = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]
    assert 'custom_fields' in check
    assert 'test_custom_field' in check['custom_fields']
    assert check['custom_fields']['test_custom_field'] == 'init'

    response = live_client.create_or_update_subscriber('ross.hodapp+drip-python@drip.com', custom_fields={'test_custom_field': '1'})

    p_contains = partial(contains, response)

    assert type(response) == dict
    assert len(response) == 21
    assert all(map(p_contains, ['id', 'status', 'email', 'eu_consent', 'time_zone', 'utc_offset', 'visitor_uuid', 'custom_fields', 'tags',
                                'ip_address', 'user_agent', 'original_referrer', 'landing_url', 'prospect', 'lead_score', 'lifetime_value',
                                'created_at', 'href', 'user_id', 'base_lead_score', 'links']))

    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]
    assert 'custom_fields' in confirm
    assert 'test_custom_field' in confirm['custom_fields']
    assert confirm['custom_fields']['test_custom_field'] == '1'

    # cleanup
    live_client.session.post(
        'https://api.getdrip.com/v2/5706364/subscribers',
        json={'subscribers': [{'email': 'ross.hodapp+drip-python@drip.com', 'custom_fields': {'test_custom_field': 'init'}}]}
    )

    response = live_client.create_or_update_subscriber('ross.hodapp+drip-python@drip.com', option='option')


def test_subscribers(live_client):
    response = live_client.subscribers()

    assert type(response) == list
    assert len(response) == 1


def test_subscriber(live_client):
    response = live_client.subscriber('ross.hodapp+drip-python@drip.com')

    p_contains = partial(contains, response)

    assert type(response) == dict
    assert len(response) == 21
    assert all(map(p_contains, ['id', 'status', 'email', 'eu_consent', 'time_zone', 'utc_offset', 'visitor_uuid', 'custom_fields', 'tags',
                                'ip_address', 'user_agent', 'original_referrer', 'landing_url', 'prospect', 'lead_score', 'lifetime_value',
                                'created_at', 'href', 'user_id', 'base_lead_score', 'links']))
    assert response['email'] == 'ross.hodapp+drip-python@drip.com'


@mark.skip(reason="no way of currently testing this without manual setup, since the API can't re-subscribe someone")
def test_unsubscribe(live_client):
    response = live_client.unsubscribe('ross.hodapp+unsubscribed@drip.com')

    assert type(response) == dict


@mark.skip(reason="no way of currently testing this without manual setup, since the API can't re-subscribe someone")
def test_unsubscribe_from_all(live_client):
    response = live_client.unsubscribe_from_all('ross.hodapp+unsubscribed@drip.com')

    assert type(response) == dict


@mark.skip(reason="no way of currently testing this without manual setup, since the API can't un-delete someone")
def test_delete_subscriber(live_client):
    response = live_client.delete_subscriber('ross.hodapp+delete@drip.com')

    assert type(response) == bool
    assert response
