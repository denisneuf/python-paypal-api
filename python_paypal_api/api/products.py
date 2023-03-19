from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils,
    ProductType,
    CategoryType
)

# import logging
# import json


PRODUCT_PROPERTIES = { 
'name', 'type', 'id', 'category', 'home_url',
'image_url', 'description', 'update_time', 'create_time'
}

# PRODUCT_UPDATE = {'category', 'home_url', 'image_url', 'description'}
PRODUCT_UPDATE = {'name', 'category', 'home_url', 'image_url', 'description'}


class Products(Client):

    r"""
    Use ``/products`` resource to create and manage products.
    """

    @PaypalEndpoint('/v1/catalogs/products', method='GET')
    def list_products(self, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`GET` :dax-operation-path:`/v1/catalogs/products`

        Lists products.

        \*\*\kwargs:

            | **page** :dax-def-type:`integer`

                | A non-zero integer which is the start index of the entire list of items that are returned in the response. So, the combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns the next 20 items.

                | :dax-def-meta:`Minimum value:` ``1``.

                | :dax-def-meta:`Maximum value:` ``100000``.

            | **page_size** :dax-def-type:`integer`

                | The number of items to return in the response.

                | :dax-def-meta:`Minimum value:` ``1``.

                | :dax-def-meta:`Maximum value:` ``20``.

            | **total_required** :dax-def-type:`boolean`

                | Indicates whether to show the total items and total pages in the response.


        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='GET')
    def get_product(self, productId:str, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`GET` :dax-operation-path:`/v1/catalogs/products/{product_id}`
        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='PATCH')
    def update_product(self, productId:str, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`PATCH` :dax-operation-path:`/v1/catalogs/products/{product_id}`
        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='PATCH')
    def update_product_helper(self, productId:str, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`PATCH` :dax-operation-path:`/v1/catalogs/products/{product_id}`
        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), data=Utils.convert_updates(kwargs.pop('body')), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products', method='POST')
    def post_product(self, **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`POST` :dax-operation-path:`/v1/catalogs/products`
        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        prefer = "return=representation" # "return=minimal"
        Utils.prefer(headers, prefer)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products', method='POST')
    def post_product_helper(self, body:(str or dict or list), **kwargs) -> ApiResponse:
        r"""
        :dax-operation-get:`POST` :dax-operation-path:`/v1/catalogs/products`
        """
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        prefer = "return=representation" # "return=minimal"
        Utils.prefer(headers, prefer)
        dictionary = body.copy()

        if isinstance(dictionary["type"], ProductType):
           dictionary["type"] = dictionary["type"].value
        else:
            raise TypeError("Only ProductType are allowed")

        if isinstance(dictionary["category"], CategoryType):
           dictionary["category"] = dictionary["category"].value
        else:
            raise TypeError("Only CategoryType are allowed")

        return self._request(kwargs.pop('path'), data=Utils.convert_body(dictionary, False), params=kwargs, headers=headers)

