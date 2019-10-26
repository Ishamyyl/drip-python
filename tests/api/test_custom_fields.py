

def test_custom_fields(client):
    client.session.get.return_value.json.return_value = {'custom_field_identifiers': [1, ]}
    client.custom_fields()
    client.session.get.assert_called_once_with('custom_field_identifiers')
