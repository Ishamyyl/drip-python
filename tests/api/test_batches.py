

def test_create_or_update_subscribers(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'batches': [
            {
                'subscribers': [
                    {
                        'email': 'email_address'
                    }
                ]
            }
        ]
    }
    client.create_or_update_subscribers([{'email': 'email_address'}])
    client.session.post.assert_called_once_with('subscribers/batches', json=expected_payload)


def test_unsubscribe_subscribers(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'batches': [
            {
                'subscribers': [
                    {
                        'email': 'email_address'
                    }
                ]
            }
        ]
    }
    client.unsubscribe_subscribers([{'email': 'email_address'}])
    client.session.post.assert_called_once_with('unsubscribes/batches', json=expected_payload)


def test_track_events(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'batches': [
            {
                'events': [
                    {
                        'email': 'email_address',
                        'action': 'event'
                    }
                ]
            }
        ]
    }
    client.track_events([{'email': 'email_address', 'action': 'event'}])
    client.session.post.assert_called_once_with('events/batches', json=expected_payload)


def test_orders(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'orders': [
            {
                'email': 'email_address',
            }
        ]
    }
    client.orders([{'email': 'email_address'}])
    client.session.post.assert_called_once_with(
        'https://api.getdrip.com/v3/1234/shopper_activity/order/batch', json=expected_payload)
