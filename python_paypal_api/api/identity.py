from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

class Identity(Client):

    @PaypalEndpoint('/v1/identity/oauth2/userinfo', method='GET')
    def get_userinfo(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        schema = "paypalv1.1"
        kwargs["schema"] = schema
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)  


    @PaypalEndpoint('/v1/identity/account-settings', method='POST')
    def post_set_account_properties(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @PaypalEndpoint('/v1/identity/account-settings/deactivate', method='POST')
    def post_disable_account_properties(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json" # headers = {'Content-Type': contentType}
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)