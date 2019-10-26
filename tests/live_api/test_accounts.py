import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_accounts(live_client):
    response = live_client.accounts()

    assert type(response) == list
    assert len(response) == 2


def test_account(live_client):
    account_id = os.getenv("ACCOUNT_ID")
    response = live_client.account(int(account_id))

    p_contains = partial(contains, response)

    assert type(response) == dict
    assert len(response) == 11
    assert all(map(p_contains, ['id', 'name', 'url', 'default_from_name', 'default_from_email', 'default_postal_address', 'primary_email', 'enable_third_party_cookies',
                                'phone_number', 'created_at', 'href']))
    assert response['name'] == 'drip-python test'
    assert response['id'] == account_id
