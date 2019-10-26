import os

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_cart(live_client):
    # Difficult to confirm / check the actual results of the test
    response = live_client.cart('drip-python', 'ross.hodapp+drip-python@drip.com', 'created', '1234', 'https://www.example.com/')

    assert type(response) == str


def test_order(live_client):
    # Difficult to confirm / check the actual results of the test
    response = live_client.order('drip-python', 'ross.hodapp+drip-python@drip.com', 'placed', '12345')

    assert type(response) == str


def test_product(live_client):
    # Difficult to confirm / check the actual results of the test
    response = live_client.product('drip-python', 'created', '123456', 'Test Product', 1.0, categories=['Test Product Category'])

    assert type(response) == str
