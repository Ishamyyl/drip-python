from typing import TYPE_CHECKING

from drip.utils import json_object, json_list

if TYPE_CHECKING:
    from requests import Session


class Shoppers:

    session: 'Session'
    api_domain: str
    account_id: int

    @json_list('request_id')
    def cart(self, provider, email, action, cart_id, cart_url, **options):
        """
        cart(provider, email, action, cart_id, cart_url,
            occurred_at=None, cart_public_id=None, grand_total=None,
            total_discounts=None, currency=None, items=None, **event_properties)

        Create or update a cart

        Arguments:
            provider {str} -- Source. The identifier for the provider from which the order data was received in lower snake-cased form
            email {str} -- Person's email address
            action {str} --  The event's action: created, updated
            cart_id {str} -- A unique, internal id for the cart
            cart_url {str} -- A URL that links back to the shopper’s cart on your ecommerce platform

        Keyword Arguments:
            occurred_at {str} -- Date + time the Cart happened, Eg. "2016-01-01T00:00:00Z" (default: {now})
            cart_public_id {str} -- A public, customer-facing identifier for the cart.
                This will be displayed in the Drip UI and should correspond to the identifier a customer might see in their own cart. (default: {None})
            grand_total {int} -- The total amount of the Cart. This should include any applicable discounts (default: {0})
            total_discounts {int} -- Discount on the Cart, in cents (default: {None})
            currency {str} -- Currency code, see ISO 4217 (default: {None})
            items {Iterable[ItemJsonType]} -- List of Item objects (default: {None})

            **Any other arguments included will be treated as custom Event Properties.

        Returns:
            Response -- API Response, or the unpacked request_id
        """
        cart = {
            'provider': provider,
            'email': email,
            'action': action,
            'cart_id': cart_id,
            'cart_url': cart_url
        }
        cart.update(options)
        return self.session.post(f'{self.api_domain}/v3/{self.account_id}/shopper_activity/cart', json=cart)

    @json_list('request_id')
    def order(self, provider, email, action, order_id, **options):
        """
        order(provider, email, action)

        Create, Update, Pay, Fulfill, Refund, or Cancel an Order.

        Arguments:
            provider {str} -- Source
            email {str} -- Person's email address
            action {str} --  The Order's action: placed, updated, paid, fulfilled, refunded, canceled
            order_id {str} -- A unique, internal id for the Order

        Keyword Arguments:
            occurred_at {str} -- Date + time the Order happened, Eg. "2016-01-01T00:00:00Z" (default: {now})
            order_public_id {str} -- A public, customer-facing identifier for the Order.
                This will be displayed in the Drip UI and should correspond to the identifier a customer might see in their own order. (default: {None})
            grand_total {int} -- The total amount of the Order. This should include any applicable discounts (default: {0})
            total_discounts {int} -- Discount on the Order, in cents (default: {None})
            total_taxes {int} -- Taxes on the Order, in cents (default: {None})
            total_fees {int} -- Fees on the Order, in cents (default: {None})
            total_shipping {int} -- Shipping on the Order, in cents (default: {None})
            refund_amount {int} -- To adjust a person’s lifetime value for a refund or cancelation,
                set `refund_amount` to the amount of the refund and leave `grand_total` unchanged (default: {0})
            currency {str} -- Currency code, see ISO 4217 (default: {None})
            order_url {str} -- A URL that links back to the Order on your ecommerce platform (default: {None})
            items {Iterable[ItemJsonType]} -- List of Item objects (default: {None})
            billing_address {AddressJsonType} -- An object containing billing address information (default: {None})
            shipping_address {AddressJsonType} -- An object containing shipping address information (default: {None})

            **Any other arguments included will be treated as custom Event Properties.

        Returns:
            Response -- API Response, or the unpacked request_id
        """
        order = {
            'provider': provider,
            'email': email,
            'action': action,
            'order_id': order_id
        }
        order.update(options)
        return self.session.post(f'{self.api_domain}/v3/{self.account_id}/shopper_activity/order', json=order)

    @json_list('request_id')
    def product(self, provider, action, product_id, name, price, **options):
        """
        product(provider, action, product_id, name, price)

        Create or Update an Product.

        Arguments:
            provider {str} -- Source
            action {str} --  The Product's action: created, updated
            product_id {str} -- A unique, internal id for the Product
            name {str} -- The Product's name
            price {float} -- The price of a single product

        Keyword Arguments:
            occurred_at {str} -- Date + time the Order happened, Eg. "2016-01-01T00:00:00Z" (default: {now})
            product_variant_id {str} -- If applicable, a unique identifier for the specific product variant from the provider. (default: {None})
            sku {str} -- The product SKU (default: {None})
            brand {str} -- The product's brand, vendor, or manufacturer. (default: {None})
            categories {Iterable[str]} -- An array of categories associated with the product (default: {None})
            inventory {int} -- The currently available inventory of the product (default: {None})
            product_url {str} -- A URL to the site containing product details (default: {None})
            image_url {str} -- A direct URL to an image of the product (default: {None})

            **Any other arguments included will be treated as custom Event Properties.

        Returns:
            Response -- API Response, or the unpacked request_id
        """
        product = {
            'provider': provider,
            'action': action,
            'product_id': product_id,
            'name': name,
            'price': price,
        }
        product.update(options)
        return self.session.post(f'{self.api_domain}/v3/{self.account_id}/shopper_activity/product', json=product)
