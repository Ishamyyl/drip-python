import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_conversions(live_client):
    response = live_client.conversions()

    assert type(response) == list
    assert len(response) == 1

    response = live_client.conversions(status='disabled')

    assert type(response) == list
    assert len(response) == 1
    assert response[0]['status'] == 'disabled'


def test_conversion(live_client):
    conversion_id = 926552633
    response = live_client.conversion(conversion_id)

    p_contains = partial(contains, response)

    assert len(response) == 9
    assert all(map(p_contains, ['id', 'status', 'name', 'url', 'default_value', 'counting_method', 'created_at', 'href', 'links']))
    assert response['id'] == str(conversion_id)
    assert response['status'] == 'enabled'
    assert response['name'] == 'Test Conversion'
    assert response['counting_method'] == 'all'
    assert response['default_value'] == 0
