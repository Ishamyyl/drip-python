

def test_forms(client):
    client.session.get.return_value.json.return_value = {'forms': [1, ]}
    client.forms()
    client.session.get.assert_called_once_with('forms')


def test_form(client):
    client.session.get.return_value.json.return_value = {'forms': [1, ]}
    client.form(1234)
    client.session.get.assert_called_once_with('forms/1234')
