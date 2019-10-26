import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_broadcasts(live_client):
    response = live_client.broadcasts()

    assert type(response) == list
    assert len(response) == 2

    response = live_client.broadcasts(status='sent')

    assert type(response) == list
    assert len(response) == 1
    assert response[0]['status'] == 'sent'


def test_broadcast(live_client):
    broadcast_id = 252718765
    response = live_client.broadcast(broadcast_id)

    p_contains = partial(contains, response)

    assert len(response) == 15
    assert all(map(p_contains, ['id', 'href', 'name', 'status', 'from_name', 'from_email', 'bcc', 'postal_address', 'send_at', 'localize_sending_time', 'created_at',
                                'subject', 'html_body', 'text_body', 'links']))
    assert response['id'] == str(broadcast_id)
    assert response['status'] == 'draft'
