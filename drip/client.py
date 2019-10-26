#!/usr/bin/env python
# -*- coding: utf-8 -*-
from atexit import register
from typing import TYPE_CHECKING

from requests import __version__ as __requests_version__
from requests_toolbelt import user_agent
from requests_toolbelt.sessions import BaseUrlSession

from drip import __version__
from drip.api import *

if TYPE_CHECKING:
    from requests import Session
    from typing import Optional


class Client(
    Batches,
    Accounts,
    Broadcasts,
    Campaigns,
    Conversions,
    CustomFields,
    Events,
    Forms,
    Shoppers,
    Subscribers,
    Tags,
    Users,
    Webhooks,
    Workflows,
):

    session: 'Session'
    account_id: int

    drip_py_ua: str = user_agent("drip-python", __version__, extras=[('requests', __requests_version__), ])
    api_domain: str = "https://api.getdrip.com"
    api_version: str = 'v2'

    def __init__(self, api_token: str, account_id: int) -> None:
        self.account_id = account_id

        # Rather than assigning directly to `self`, this is the recommended idiom so atexit.register behaves nicely with GC.
        session = BaseUrlSession(base_url=f'{self.api_domain}/{self.api_version}/{account_id}/')
        session.auth = (api_token, '')
        session.headers.update({"User-Agent": self.drip_py_ua, "Content-Type": 'application/json'})
        register(session.close)
        self.session = session
