import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_fetch_user(live_client):
    response = live_client.fetch_user()
    print(response)
    p_contains = partial(contains, response)

    assert type(response) == dict
    assert all(map(p_contains, ['email', 'name', 'time_zone']))
    assert response['email'] == 'ross.hodapp@drip.com'
    assert response['name'] == 'Ross Hodapp'
    assert response['time_zone'] == 'America/Chicago'
