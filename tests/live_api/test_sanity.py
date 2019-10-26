import os

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_sanity():
    assert True


def test_client(live_client):
    assert live_client.account_id == int(os.getenv('ACCOUNT_ID'))
