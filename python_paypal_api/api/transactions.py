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

        .. note::
            * If you specify one or more optional query parameters, the ending_balance response field is empty.
            * It takes a maximum of three hours for executed transactions to appear in the list transactions call.
            * This call lists transaction for the previous three years.


        \*\*\kwargs:

            | **payment_instrument_type** :dax-def-type:`string`

                | Filters the transactions in the response by a payment instrument type. Value is either:

                - ``CREDITCARD``. Returns a direct credit card transaction with a corresponding value.

                - ``DEBITCARD``. Returns a debit card transaction with a corresponding value.

                | If you omit this parameter, the API does not apply this filter.

            | **end_date** :dax-def-type:`string` :dax-def-note:`required`

                | Filters the transactions in the response by an end date and time, in `Internet date and time format`_. Seconds are required. Fractional seconds are optional. The maximum supported range is 31 days.

                | :dax-def-meta:`Minimum length:` ``20``.

                | :dax-def-meta:`Maximum length:` ``64``.

                | :dax-def-meta:`Pattern:` ``^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$``.

            | **start_date** :dax-def-type:`string` :dax-def-note:`required`

                | Filters the transactions in the response by a start date and time, in `Internet date and time format`_. Seconds are required. Fractional seconds are optional.

                | :dax-def-meta:`Minimum length:` ``20``.

                | :dax-def-meta:`Maximum length:` ``64``.

                | :dax-def-meta:`Pattern:` ``^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$``.


            | **balance_affecting_records_only** :dax-def-type:`string`

                | Indicates whether the response includes only balance-impacting transactions or all transactions.

                | Value is either:

                - ``Y``. The default. The response includes only balance transactions.

                - ``N``. The response includes all transactions.


            | **fields** :dax-def-type:`string`

                | Indicates which fields appear in the response. Value is a single field or a comma-separated list of fields. The ``transaction_info`` value returns only the transaction details in the response. To include all fields in the response, specify ``fields=all``. Valid fields are:

                - ``transaction_info``. The transaction information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID, the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and time when the transaction was initiated and was last updated, the transaction amounts including the PayPal fee, any discounts, insurance, the transaction status, and other information about the transaction.

                - ``payer_info``. The payer information. Includes the PayPal customer account ID and the payer's email address, primary phone number, name, country code, address, and whether the payer is verified or unverified.

                - ``shipping_info``. The shipping information. Includes the recipient's name, the shipping method for this order, the shipping address for this order, and the secondary address associated with this order.

                - ``auction_info``. The auction information. Includes the name of the auction site, the auction site URL, the ID of the customer who makes the purchase in the auction, and the date and time when the auction closes.

                - ``cart_info``. The cart information. Includes an array of item details, whether the item amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated invoices.

                - ``incentive_info``. An array of incentive detail objects. Each object includes the incentive, such as a special offer or coupon, the incentive amount, and the incentive program code that identifies a merchant loyalty or incentive program.

                - ``store_info``. The store information. Includes the ID of the merchant store and the terminal ID for the checkout stand in the merchant store.

            | **page** :dax-def-type:`integer`

                | The zero-relative start index of the entire list of items that are returned in the response. So, the combination of ``page=1`` and ``page_size=20`` returns the first 20 items.

                | :dax-def-meta:`Minimum value:` ``1``.

                | :dax-def-meta:`Maximum value:` ``2147483647``.

            | **page_size** :dax-def-type:`integer`

                | The number of items to return in the response. So, the combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns the next 20 items.

                | :dax-def-meta:`Minimum value:` ``1``.

                | :dax-def-meta:`Maximum value:` ``500``.

            | **store_id** :dax-def-type:`string`

                | Filters the transactions in the response by a store ID.

            | **terminal_id** :dax-def-type:`string`

                | Filters the transactions in the response by a terminal ID.

            | **transaction_amount** :dax-def-type:`string`

                | Filters the transactions in the response by a gross transaction amount range. Specify the range as ``<start-range> TO <end-range>``, where ``<start-range>`` is the lower limit of the gross PayPal transaction amount and ``<end-range>`` is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For example, to search for transactions from $5.00 to $10.05, specify ``[500 TO 1005]``.

                .. note::

                    The values must be URL encoded.

            | **transaction_currency** :dax-def-type:`string`

                 | Filters the transactions in the response by a `three-character ISO-4217 currency code`_ for the PayPal transaction currency.

            | **transaction_id** :dax-def-type:`string`

                | Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID is 17 characters long, except for an order ID, which is 19 characters long.

                .. note::

                    A transaction ID is not unique in the reporting system. The response can list two transactions with the same ID. One transaction can be balance affecting while the other is non-balance affecting.


                | :dax-def-meta:`Minimum length:` ``17``.

                | :dax-def-meta:`Maximum length:` ``19``.


            | **transaction_status** :dax-def-type:`string`

                | Filters the transactions in the response by a PayPal transaction status code. Value is:

                .. csv-table::
                   :header: "Status code", "Description"
                   :widths: 5, 50

                   "``D``", "PayPal or merchant rules denied the transaction."
                   "``P``", "The transaction is pending. The transaction was created but waits for another payment process to complete, such as an ACH transaction, before the status changes to ``S``."
                   "``S``", "The transaction successfully completed without a denial and after any pending statuses."
                   "``V``", "A successful transaction was reversed and funds were refunded to the original sender."



            | **transaction_type** :dax-def-type:`string`

                | Filters the transactions in the response by a PayPal transaction event code. See `Transaction event codes`_.


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

        List all balances. Specify date time to list balances for that time that appear in the response.

        .. note::
            * It takes a maximum of three hours for balances to appear in the list balances call.
            * This call lists balances upto the previous three years.

        \*\*\kwargs:

            | **as_of_time** :dax-def-type:`string`

                | List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.

                | :dax-def-meta:`Minimum length:` ``20``.

                | :dax-def-meta:`Maximum length:` ``64``.

                | :dax-def-meta:`Pattern:` ``^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$``.

            | **currency_code** :dax-def-type:`string`

                | Filters the transactions in the response by a `three-character ISO-4217 currency code`_ for the PayPal transaction currency.

                | :dax-def-meta:`Minimum length:` ``3``.

                | :dax-def-meta:`Maximum length:` ``3``.


        '''
        headers = {}
        contentType = "application/json"
        Utils.contentType(headers, contentType)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)