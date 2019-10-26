

def test_fetch_user(client):
    client.session.get.return_value.json.return_value.update({'users': [1, ]})
    client.fetch_user()
    client.session.get.called_once_with('https://api.getdrip.com/v2/user/')
