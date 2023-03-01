from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

import logging

class Tracking(Client):


    @PaypalEndpoint('/v1/shipping/trackers/{}', method='PUT')
    def put_traking(self, id: str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @PaypalEndpoint('/v1/shipping/trackers-batch', method='POST')
    def post_traking(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/shipping/trackers/{}', method='GET')
    def get_traking(self, id: str, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(PaypalEndpointParams(kwargs.pop('path')).fill(id), params=kwargs, headers=headers)    

