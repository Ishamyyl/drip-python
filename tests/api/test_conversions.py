

def test_conversions(client):
    client.session.get.return_value.json.return_value = {'goals': [1, ]}
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.conversions(param='param')
    client.session.get.assert_called_once_with('goals', params=expected_params)


def test_conversion(client):
    client.session.get.return_value.json.return_value.update({'goals': [1, ]})
    client.conversion(1234)
    client.session.get.called_once_with('goals/1234')
