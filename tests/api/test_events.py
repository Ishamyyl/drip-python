
def test_track_event(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'events': [
            {
                'email': 'email_address',
                'action': 'action',
                'param': 'param'
            }
        ]
    }
    client.track_event('email_address', 'action', param='param')
    client.session.post.assert_called_once_with('events', json=expected_payload)


def test_track_event_no_options(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'events': [
            {
                'email': 'email_address',
                'action': 'action'
            }
        ]
    }
    client.track_event('email_address', 'action')
    client.session.post.assert_called_once_with('events', json=expected_payload)


def test_event_actions(client):
    client.session.get.return_value.json.return_value.update({'event_actions': [1, ]})
    expected_params = {
        'page': 1,
        'per_page': 1000
    }
    client.event_actions()
    client.session.get.assert_called_once_with('event_actions', params=expected_params)
