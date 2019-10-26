import os
from unittest.mock import MagicMock, Mock

import pytest
from requests import Response

from drip import Client


@pytest.fixture
def live_client():
    c = Client(os.getenv("API_TOKEN"), int(os.getenv("ACCOUNT_ID")))
    return c


@pytest.fixture
def client():
    c = Client('a1b2c3', 1234)
    c.session.get = Mock()
    c.session.get.return_value = MagicMock(spec=Response)
    c.session.get.return_value.json.return_value = {'meta': {'total_pages': 1}}
    c.session.post = Mock()
    c.session.post.return_value = MagicMock(spec=Response)
    c.session.post.return_value.json.return_value = {'meta': {'total_pages': 1}}
    c.session.put = Mock()
    c.session.put.return_value = MagicMock(spec=Response)
    c.session.put.return_value.json.return_value = {'meta': {'total_pages': 1}}
    c.session.delete = Mock()
    c.session.delete.return_value = MagicMock(spec=Response)
    return c


@pytest.fixture
def section():
    return 'testsection'


@pytest.fixture
def expected_response():
    return [
        {'p1o1': 'v1'},
        {'p1o2': 'v2'},
        {'p2o1': 'v3'},
        {'p2o2': 'v4'},
        {'p3o1': 'v5'},
        {'p3o2': 'v6'}
    ]


@pytest.fixture(params=[1, 2, 3])
def page(request):
    return request.param
