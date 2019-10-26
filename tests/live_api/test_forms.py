import os
from functools import partial
from operator import contains

from pytest import mark

pytestmark = mark.skipif(os.getenv('TEST_LIVE') != "True", reason="tests against a real, live Drip account")


def test_forms(live_client):
    response = live_client.forms()

    assert type(response) == list
    assert len(response) == 2


def test_form(live_client):
    form_id = 857409151
    response = live_client.form(form_id)

    p_contains = partial(contains, response)

    assert len(response) == 25
    assert all(map(p_contains, ['id', 'href', 'headline', 'description', 'button_text', 'confirmation_heading', 'confirmation_text', 'send_ga_event', 'seconds_before_popup',
                                'days_between_popup', 'days_between_popup_after_close', 'orientation', 'opacity', 'show_labels', 'primary_color', 'secondary_color',
                                'is_widget_enabled', 'whitelist', 'blacklist', 'is_whitelist_enabled', 'is_blacklist_enabled', 'hide_on_mobile', 'is_embeddable', 'created_at', 'links']))
    assert response['id'] == str(form_id)
    assert response['headline'] == 'Test Form'
