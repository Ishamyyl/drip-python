import os
from time import sleep

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_create_or_update_subscribers(live_client):
    check = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]
    assert 'custom_fields' in check
    assert 'test_custom_field' in check['custom_fields']
    assert check['custom_fields']['test_custom_field'] == 'init'

    response = live_client.create_or_update_subscribers(
        [
            {'email': 'ross.hodapp+drip-python@drip.com', 'custom_fields': {'test_custom_field': '1'}}
        ]
    )
    assert type(response) == bool
    assert response

    sleep(2)  # (!)
    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]
    assert 'custom_fields' in confirm
    assert 'test_custom_field' in confirm['custom_fields']
    assert confirm['custom_fields']['test_custom_field'] == '1'

    # cleanup
    live_client.session.post(
        'https://api.getdrip.com/v2/5706364/subscribers',
        json={'subscribers': [{'email': 'ross.hodapp+drip-python@drip.com', 'custom_fields': {'test_custom_field': 'init'}}]}
    )


@mark.skip(reason="no way of currently testing this without manual setup, since the API can't re-subscribe someone")
def test_unsubscribe_subscribers(live_client):
    response = live_client.unsubscribe_subscribers(
        [
            {'email': 'ross.hodapp+drip-python@drip.com'}
        ]
    )
    assert type(response) == bool
    assert response


def test_track_events(live_client):
    response = live_client.track_events(
        [
            {'email': 'ross.hodapp+drip-python@drip.com', 'action': 'Test custom event', 'properties': {'a': 1}},
            {'email': 'ross.hodapp+drip-python@drip.com', 'action': 'Test custom event', 'properties': {'a': 2}}
        ]
    )

    assert type(response) == bool
    assert response


def test_orders(live_client):
    response = live_client.orders(
        [
            {
                'provider': 'drip-python',
                'email': 'ross.hodapp+drip-python@drip.com',
                'action': 'placed',
                'order_id': '1234'
            }
        ]
    )

    assert type(response) == bool
    assert response
