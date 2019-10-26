import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_track_event(live_client):
    response = live_client.track_event('ross.hodapp+drip-python@drip.com', 'Test custom event', properties={'a': 1})

    assert type(response) == bool
    assert response


def test_event_actions(live_client):
    response = live_client.event_actions()

    assert type(response) == list
    assert len(response) == 3
    assert response == ['Created a cart', 'Placed an order', 'Test custom event']
