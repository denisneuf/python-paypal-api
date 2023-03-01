from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

class Transactions(Client):

    @PaypalEndpoint('/v1/reporting/transactions', method='GET')
    def get_list_transactions(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)


    @PaypalEndpoint('/v1/reporting/balances', method='GET')
    def get_balances(self, **kwargs) -> ApiResponse:
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)