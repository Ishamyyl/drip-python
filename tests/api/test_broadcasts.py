
def test_broadcasts(client):
    client.session.get.return_value.json.return_value.update({'broadcasts': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.broadcasts(param='param')
    client.session.get.called_once_with('broadcasts', params=expected_params)


def test_broadcast(client):
    client.session.get.return_value.json.return_value.update({'broadcasts': [1, ]})
    client.broadcast(1234)
    client.session.get.called_once_with('broadcasts/1234')
