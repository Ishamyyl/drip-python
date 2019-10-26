from typing import Any, Iterable, Mapping
from typing_extensions import Protocol

from mypy_extensions import TypedDict

JsonMappingType = Mapping[str, Any]
JsonListType = Iterable[JsonMappingType]


class EmailJsonType(TypedDict):
    email: str


class EventJsonType(TypedDict, total=False):
    email: str
    action: str
    prospect: bool  # Default: True
    properties: Mapping[str, str]
    occurred_at: str  # http://en.wikipedia.org/wiki/ISO_8601


class AddressJsonType(TypedDict, total=False):
    name: str
    first_name: str
    last_name: str
    company: str
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
    phone: str
    email: str


class ItemJsonType(TypedDict, total=False):
    product_id: str
    product_variant_id: str
    sku: str
    name: str
    brand: str
    categories: Iterable[str]
    price: int
    quantity: int
    discount: int
    total: int
    product_url: str
    image_url: str


class OrderJsonType(TypedDict, total=False):
    provider: str
    email: str
    action: str
    occurred_at: str
    order_id: str
    order_public_id: str
    grand_total: int
    total_discounts: int
    total_taxes: int
    total_fees: int
    total_shipping: int
    refund_amount: int
    currency: str  # https://en.wikipedia.org/wiki/ISO_4217
    order_url: str
    items: Iterable[ItemJsonType]
    billing_address: AddressJsonType
    shipping_address: AddressJsonType


class SubscriberJsonType(TypedDict, total=False):
    email: str
    id: str
    status: str
    eu_consent: str
    time_zone: str
    utc_offset: int
    visitor_uuid: str
    custom_fields: Mapping[str, str]
    tags: Iterable[str]
    ip_address: str
    user_agent: str
    original_referrer: str
    landing_url: str
    prospect: bool
    lead_score: int
    lifetime_value: int
    created_at: str
    href: str
    user_id: int
    base_lead_score: int
