# drip-python [![Coverage Status](https://coveralls.io/repos/github/Ishamyyl/drip-python/badge.svg?branch=master)](https://coveralls.io/github/Ishamyyl/drip-python?branch=master) [![CircleCI](https://circleci.com/gh/Ishamyyl/drip-python.svg?style=svg)](https://circleci.com/gh/Ishamyyl/drip-python)
Python wrapper for the Drip REST API at [developer.drip.com](https://developer.drip.com)

----
# Installation

```sh
pip install drip-python
```

# Usage

Initialize the client

```py
>>> from drip import Client
>>> d = Client(API_TOKEN, ACCOUNT_ID)
```

Use the client's methods

```py
>>> d.fetch_user()
{'email': 'ross.hodapp@drip.com', 'name': 'Ross Hodapp', 'time_zone': 'America/Chicago'}
```

# Main Concepts

Be sure to check out [the Wiki](https://github.com/Ishamyyl/drip-python/wiki)!

## 1. Additional Options

Beyond the required arguments, any additional keyword arguments will be added to the call as well. Check the docs for what's available.

```py
>>> cfs = {'first_name': 'Ross'}
>>> d.create_or_update_subscriber('ross.hodapp@drip.com', custom_fields=cfs)
{'email': 'ross.hodapp+test@drip.com', 'custom_fields': {'first_name': 'Ross'}, ... }
```

## 2. Unpacking the response

The Drip REST API often returns extra data along side the results you're asking for.

The Client takes care of unpacking that data for you, returning lists, dictionaries, or strings as necessary. If the response doesn't have a body, result will return `True` or `False` if the call was [successful or not](http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes).

If you'd like the raw [response](http://docs.python-requests.org/en/master/user/quickstart/#response-content), pass the keyward argument `marshall=False` to the method call.

```py
>>> d.fetch_user(marshall=False)
<Response [200]>
```

## 3. Pagination

Most calls that return a list are paginated. By default, the Client automatically gets the maximum amount of objects per page and automatically gets all available pages.

Use the `page` and `per_page` keyword arguments. If a valid `page` is passed to the function, then this will fetch that page only (or the single Response if not `marshall`ed per above).

Otherwise-- that is, if `page` is 0 (default) or negative-- then this will fetch the entire collection and return the full list. This will ignore the `per_page` keyword argument and use `1000` for maximum efficiency.

Currently, I won't support getting all pages of 1 object per page for example, since I don't see a valid use-case for this.

This means essentially that `per_page` only makes sense when asking for a specific 'page'.
This also means that you can only `marshall` a specific `page` (this may change in the future).

Anyway, the default case will be what you want most of the time, so don't worry about this too much.

```py
>>> all_subscribers = d.subscribers()
>>> len(all_subscribers)
1234

>>> first_page = d.subscribers(page=1)
>>> len(first_page)
100

>>> last_page = d.subscribers(page=13)
>>> len(last_page)
34

>>> big_first_page = d.subscribers(page=1, per_page=1000)
>>> len(big_first_page)
1000

>>> big_last_page = d.subscribers(page=2, per_page=1000)
>>> len(big_last_page)
234

>>> marshall_without_page = d.subscribers(marshall=False)
>>> len(marshall_without_a_page)
1234

>>> marshall_with_page = d.subscribers(page=1, marshall=False)
>>> marshall_with_page
<Response [200]>
```

# FAQ

# Status - v0.3.0 Beta
While devotedly and enthusiastically maintained, this is an un-official side-project and Drip Support is unable to fix issues you run into. Create an Issue on GitHub here instead. Thanks!

Purpose

- [x] Full API coverage, including "v3" Shopper Activity and future endpoints
- [x] Full unittest code coverage
- [x] Every endpoint tested live
- [x] Documentation ~~(readthedocs? github wiki?)~~ wiki!
- [ ] Web framework support, namely Django and [Responder](https://python-responder.org/en/latest/)
- [ ] NoSQL utilities
- [X] ~~AsyncIO support~~ Basically needs a differend repo?

# Changelog

### `v0.3.0`

* Repostiry updates

### `v0.1.4`

* Added raising Errors for when the HTTP call is successful but the API returned that there were errors

### `v0.1.3`

* Added Product support for the Shopper Activity API! Check that out here: [Product Activity](https://developer.drip.com/?shell#product-activity)
