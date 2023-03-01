from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

import logging

class Orders(Client):


    @PaypalEndpoint('/v2/checkout/orders', method='POST')
    def post_create_order(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        prefer = "return=representation" # return=minimal return=representation
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/checkout/orders/{}', method='PATCH')
    def patch_update_order(self, orderId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(orderId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v2/checkout/orders/{}', method='GET')
    def get_order(self, orderId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
    	# return self._request(fill_query_params(kwargs.pop('path'), orderId), params=kwargs, headers=headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(orderId), params=kwargs, headers=headers)

    @PaypalEndpoint('/v2/checkout/orders/{}/capture', method='POST')
    def post_capture_for_order(self, orderId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        prefer = "return=representation" # return=minimal return=representation
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(orderId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/checkout/orders/{}/authorize', method='POST')
    def post_authorize_for_order(self, orderId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        prefer = "return=representation" # return=minimal return=representation
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(orderId), params=kwargs, headers=headers)


    @PaypalEndpoint('/v2/checkout/orders/{}/confirm-payment-source', method='POST')
    def post_confirm_order(self, orderId:str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        prefer = "return=representation" # return=minimal return=representation
        Utils.contentType(headers, contentType)
        Utils.payPalRequestId(headers)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(orderId), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


