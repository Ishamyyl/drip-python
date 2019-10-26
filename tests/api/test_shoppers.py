
def test_cart(client):
    client.session.post.return_value.json.return_value.update({'request_id': 1234})
    expected_payload = {
        'provider': 'test',
        'email': 'email_address',
        'action': 'action',
        'cart_id': '1234',
        'cart_url': 'url',
        'option': 'option',
        'page': 1,
        'per_page': 1000
    }
    r = client.cart('test', 'email_address', 'action', '1234', 'url', option='option')
    assert r == 1234
    client.session.post.assert_called_once_with(
        'https://api.getdrip.com/v3/1234/shopper_activity/cart', json=expected_payload)


def test_order(client):
    client.session.post.return_value.json.return_value.update({'request_id': 1234})
    expected_payload = {
        'provider': 'test',
        'email': 'email_address',
        'action': 'action',
        'order_id': '12345',
        'option': 'option',
        'page': 1,
        'per_page': 1000
    }
    r = client.order('test', 'email_address', 'action', '12345', option='option')
    assert r == 1234
    client.session.post.assert_called_once_with(
        'https://api.getdrip.com/v3/1234/shopper_activity/order', json=expected_payload)


def test_product(client):
    client.session.post.return_value.json.return_value.update({'request_id': 1234})
    expected_payload = {
        'provider': 'provider',
        'action': 'action',
        'product_id': 'product_id',
        'name': 'name',
        'price': 1.0,
        'option': 'option',
        'page': 1,
        'per_page': 1000
    }
    r = client.product('provider', 'action', 'product_id', 'name', 1.0, option='option')
    assert r == 1234
    client.session.post.assert_called_once_with(
        'https://api.getdrip.com/v3/1234/shopper_activity/product', json=expected_payload)
