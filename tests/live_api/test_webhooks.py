import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_webhooks(live_client):
    response = live_client.webhooks()

    assert type(response) == list
    assert len(response) == 1


def test_webhook(live_client):
    webhook_id = 65203
    response = live_client.webhook(webhook_id)

    p_contains = partial(contains, response)

    assert len(response) == 8
    assert all(map(p_contains, ['id', 'href', 'post_url', 'version', 'include_received_email', 'created_at', 'events', 'links']))
    assert response['id'] == str(webhook_id)
    assert response['post_url'] == 'http://spygot.herokuapp.com/api/subscriber.test_webhook'


def test_create_webhook(live_client):
    check = live_client.session.get('https://api.getdrip.com/v2/5706364/webhooks').json()['webhooks']
    assert len(check) == 1

    response = live_client.create_webhook('https://spygot.herokuapp.com/api/delete_webhook', events=['subscriber.applied_tag'])
    p_contains = partial(contains, response)
    assert type(response) == dict
    assert all(map(p_contains, ['id', 'href', 'post_url', 'version', 'include_received_email', 'events', 'created_at', 'links']))
    assert response['post_url'] == 'https://spygot.herokuapp.com/api/delete_webhook'
    cleanup_id = response['id']

    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/webhooks').json()['webhooks']
    assert len(confirm) == 2

    # cleanup
    live_client.session.delete(f'https://api.getdrip.com/v2/5706364/webhooks/{cleanup_id}')


def test_delete_webhook(live_client):
    # setup
    webhook_id = live_client.session.post(
        'https://api.getdrip.com/v2/5706364/webhooks',
        json={'webhooks': [{'post_url': 'https://spygot.herokuapp.com/api/delete_webhook', 'events': ['subscriber.applied_tag']}]}
    ).json()['webhooks'][0]['id']

    check = live_client.session.get('https://api.getdrip.com/v2/5706364/webhooks').json()['webhooks']
    assert len(check) == 2

    response = live_client.delete_webhook(webhook_id)
    assert type(response) == bool
    assert response

    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/webhooks').json()['webhooks']
    assert len(confirm) == 1
