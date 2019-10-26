

def test_workflows(client):
    client.session.get.return_value.json.return_value.update({'workflows': [1, ]})
    expected_params = {
        'param': 'param',
        'page': 1,
        'per_page': 1000
    }
    client.workflows(param='param')
    client.session.get.assert_called_once_with('workflows', params=expected_params)


def test_workflow(client):
    client.session.get.return_value.json.return_value.update({'workflows': [1, ]})
    client.workflow(1234)
    client.session.get.assert_called_once_with('workflows/1234')


def test_activate_workflow(client):
    client.session.post.return_value.status_code = 204
    client.activate_workflow(1234)
    client.session.post.assert_called_once_with('workflows/1234/activate')


def test_pause_workflow(client):
    client.session.post.return_value.status_code = 204
    client.pause_workflow(1234)
    client.session.post.assert_called_once_with('workflows/1234/pause')


def test_start_subscriber_workflow(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'subscribers': [
            {
                'email': 'email_address',
                'param': 'param'
            }
        ]
    }
    client.start_subscriber_workflow('email_address', 1234, param='param')
    client.session.post.assert_called_once_with('workflows/1234/subscribers', json=expected_payload)


def test_start_subscriber_workflow_no_options(client):
    client.session.post.return_value.status_code = 204
    expected_payload = {
        'subscribers': [
            {
                'email': 'email_address',
            }
        ]
    }
    client.start_subscriber_workflow('email_address', 1234)
    client.session.post.assert_called_once_with('workflows/1234/subscribers', json=expected_payload)


def test_remove_subscriber_workflow(client):
    client.session.delete.return_value.status_code = 204
    client.remove_subscriber_workflow(1234, 'email_address')
    client.session.delete.assert_called_once_with('workflows/1234/subscribers/email_address')


def test_workflow_triggers(client):
    client.session.get.return_value.json.return_value.update({'triggers': [1, ]})
    client.workflow_triggers(1234)
    client.session.get.assert_called_once_with('workflows/1234/triggers')


def test_create_workflow_trigger(client):
    client.session.post.return_value.json.return_value.update({'triggers': [1, ]})
    expected_payload = {
        'provider': 'test',
        'trigger_type': 'type',
        'properties': {
            'param': 'param'
        },
        'page': 1,
        'per_page': 1000
    }
    client.create_workflow_trigger(1234, 'test', 'type', properties={'param': 'param'})
    client.session.post.assert_called_once_with('workflows/1234/triggers', json={'triggers': [expected_payload, ]})


def test_update_workflow_trigger(client):
    client.session.put.return_value.json.return_value.update({'triggers': [1, ]})
    expected_payload = {
        'provider': 'test',
        'trigger_type': 'type',
        'properties': {
            'param': 'param'
        },
        'page': 1,
        'per_page': 1000
    }
    client.update_workflow_trigger(1234, 'test', 'type', properties={'param': 'param'})
    client.session.put.assert_called_once_with('workflows/1234/triggers', json={'triggers': [expected_payload, ]})
