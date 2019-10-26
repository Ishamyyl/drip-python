

def test_accounts(client):
    client.session.get.return_value.json.return_value.update({'accounts': [1, ]})
    client.accounts()
    client.session.get.called_once_with('https://api.getdrip.com/v2/accounts/')


def test_account(client):
    client.session.get.return_value.json.return_value.update({'accounts': [1, ]})
    client.account(1234)
    client.session.get.called_once_with('https://api.getdrip.com/v2/accounts/1234')
