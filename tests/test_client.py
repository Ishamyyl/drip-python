

def test_client(client):
    assert client.account_id == 1234
    assert client.session
    assert 'https://api.getdrip.com/' in client.session.base_url
    assert '/v2/' in client.session.base_url
    assert '/1234/' in client.session.base_url
    assert client.session.auth == ('a1b2c3', '')
    assert 'User-Agent' in client.session.headers
    assert 'drip-py' in client.session.headers['User-Agent']
    assert 'Content-Type' in client.session.headers
    assert client.session.headers['Content-Type'] == 'application/json'
