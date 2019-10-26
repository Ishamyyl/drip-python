import os

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_tags(live_client):
    response = live_client.tags()

    assert type(response) == list
    assert len(response) == 1
    assert response == ['Test Tag']


def test_apply_tag(live_client):
    check = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]['tags']
    assert len(check) == 0

    response = live_client.apply_tag('ross.hodapp+drip-python@drip.com', 'Test Tag')
    assert type(response) == bool
    assert response

    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]['tags']
    assert len(confirm) == 1
    assert confirm == ['Test Tag']

    # cleanup
    live_client.session.delete('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com/tags/Test+Tag')


def test_remove_tag(live_client):
    # setup
    live_client.session.post('https://api.getdrip.com/v2/5706364/tags', json={'tags': [{'email': 'ross.hodapp+drip-python@drip.com', 'tag': 'Test Tag'}]})

    check = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]['tags']
    assert len(check) == 1

    response = live_client.remove_tag('ross.hodapp+drip-python@drip.com', 'Test Tag')
    assert type(response) == bool
    assert response

    confirm = live_client.session.get('https://api.getdrip.com/v2/5706364/subscribers/ross.hodapp+drip-python@drip.com').json()['subscribers'][0]['tags']
    assert len(confirm) == 0
