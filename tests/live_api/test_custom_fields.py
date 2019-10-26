import os

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_custom_fields(live_client):
    resposne = live_client.custom_fields()

    assert resposne == ['test_custom_field']
