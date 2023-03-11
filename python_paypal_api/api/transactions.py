from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    ApiResponse,
    Utils
)

class Transactions(Client):
    r"""
    Use the /transactions resource to list transactions.
    """

    @PaypalEndpoint('/v1/reporting/transactions', method='GET')
    def get_list_transactions(self, **kwargs) -> ApiResponse:
        '''
        :dax-operation-get:`GET` :dax-operation-path:`/v1/reporting/transactions`

        Lists transactions. Specify one or more query parameters to filter the transaction that appear in the response.

        \*\*\kwargs:

            | **payment_instrument_type** :dax-def-type:`string`

                | Filters the transactions in the response by a payment instrument type. Value is either:

                - ``CREDITCARD``. Returns a direct credit card transaction with a corresponding value.

                - ``DEBITCARD``. Returns a debit card transaction with a corresponding value.

                | If you omit this parameter, the API does not apply this filter.

            | **end_date** :dax-def-type:`string` :dax-def-note:`required`
            | **start_date** :dax-def-type:`string` :dax-def-note:`required`
            | **balance_affecting_records_only** (string):
            | **fields** (string)
            | **page** (integer)
            | **page_size** (integer)
            | **store_id** (string)
            | **terminal_id** (string)
            | **transaction_amount** (string)
            | **transaction_currency** (string)
            | **transaction_id** (string)
            | **transaction_status** (string)
            | **transaction_type** (string)

        :return: ApiResponse
        '''
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)


    @PaypalEndpoint('/v1/reporting/balances', method='GET')
    def get_balances(self, **kwargs) -> ApiResponse:
        '''
        :dax-operation-get:`GET` :dax-operation-path:`/v1/reporting/balances`
        '''
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)