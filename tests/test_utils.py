from unittest.mock import MagicMock

import pytest
from requests import HTTPError, Response

from drip.utils import json_list, json_object, raise_response


def test_sanity():
    assert True


def test_all_pages(client, section, expected_response):
    paged_response = [expected_response[i:i+2] for i in range(0, len(expected_response), 2)]
    meta = {'total_pages': len(paged_response)}
    call_response = [{section: i, 'meta': meta} for i in paged_response]

    response_mock = MagicMock(spec=Response)
    response_mock.json.side_effect = call_response

    @json_list(section)
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client)
    assert r == expected_response


def test_unmarshalled_json_list(client, section):
    response_mock = MagicMock(spec=Response)

    @json_list(section)
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client, marshall=False, page=1)
    assert isinstance(r, Response)


def test_unmarshalled_json_object(client, section):
    response_mock = MagicMock(spec=Response)

    @json_object(section)
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client, marshall=False, page=1)
    assert isinstance(r, Response)


def test_specific_page(client, section, expected_response, page):
    paged_response = [expected_response[i:i+2] for i in range(0, len(expected_response), 2)]
    meta = {'total_pages': len(paged_response)}
    call_response = [{section: i, 'meta': meta} for i in paged_response]

    response_mock = MagicMock(spec=Response)
    response_mock.json.return_value = call_response[page-1]

    @json_list(section)
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client, page=page)
    assert r == call_response[page-1][section]


def test_json_object(client, section, expected_response):
    call_response = {section: [expected_response[0]], 'links': {}}

    response_mock = MagicMock(spec=Response)
    response_mock.json.return_value = call_response

    @json_object(section)
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client)
    assert r == call_response[section][0]


def test_raise_response(client, section):
    response_mock = MagicMock(spec=Response)
    response_mock.status_code = 204
    response_mock.raise_for_status.return_value = None

    @raise_response()
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    r = mock_api_call(client)
    assert r


def test_raise_response_error(client, section):

    response_mock = MagicMock(spec=Response)
    response_mock.raise_for_status.side_effect = HTTPError

    @raise_response()
    def mock_api_call(c, *args, marshall=True, **kwargs):
        return response_mock

    with pytest.raises(HTTPError):
        mock_api_call(client)
