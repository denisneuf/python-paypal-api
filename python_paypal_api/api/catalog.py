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


class Catalog(Client):

    @PaypalEndpoint('/v1/catalogs/products', method='GET')
    def list_products(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='GET')
    def get_product(self, productId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='PATCH')
    def update_product(self, productId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products/{}', method='PATCH')
    def update_product_helper(self, productId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(productId), data=Utils.convert_updates(kwargs.pop('body')), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products', method='POST')
    def post_product(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        prefer = "return=representation" # "return=minimal"
        Utils.prefer(headers, prefer)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/catalogs/products', method='POST')
    def post_product_helper(self, body:(str or dict or list), **kwargs) -> ApiResponse:
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

