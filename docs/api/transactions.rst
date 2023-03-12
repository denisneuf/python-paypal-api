Transaction Search API
======================

  .. role:: dax-def-type
        :class: dax-def-type
  .. role:: dax-def-note
        :class: dax-def-note
  .. role:: dax-operation-get
        :class: dax-operation-get
  .. role:: dax-operation-path
        :class: dax-operation-path
  .. role:: dax-def-meta
        :class: dax-def-meta




.. _Internet date and time format: https://tools.ietf.org/html/rfc3339#section-5.6

.. _three-character ISO-4217 currency code: https://developer.paypal.com/api/rest/reference/currency-codes/

.. _Transaction event codes: https://developer.paypal.com/docs/integration/direct/transaction-search/transaction-event-codes/


**Transaction Search API**

Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see `Partner with PayPal`_. For more information about the API, see the `Transaction Search API Integration Guide`_.


.. _Transaction Search API Integration Guide: https://developer.paypal.com/docs/transaction-search/


    .. note::

        Note: To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see `Partner with PayPal`_.

.. _Partner with PayPal: https://www.paypal.com/my/webapps/mpp/partner-program/global-programs?_ga=1.72234320.217415639.1675992033

.. autoclass:: python_paypal_api.api.Transactions

    .. autofunction:: python_paypal_api.api.Transactions.get_list_transactions

        ### Example python

        .. code-block:: python

            from python_paypal_api.api import Transactions
            from python_paypal_api.base import PaypalApiException
            import logging
            from datetime import datetime, timezone

            def py_get_list_transactions(**kwargs):

                logger.info("---------------------------------")
                logger.info("Transactions > py_get_list_transactions({})".format(kwargs))
                logger.info("---------------------------------")

                try:

                    result = Transactions(debug=True).get_list_transactions(
                        **kwargs
                    )
                    logger.info(result)

                except PaypalApiException as error:
                    logger.error(error)


            if __name__ == '__main__':

                logger = logging.getLogger("test")
                date_start = datetime(2023, 2, 1, 0, 0, 0, 0, timezone.utc).isoformat()
                date_end = datetime(2023, 3, 1, 0, 0, 0, 0, timezone.utc).isoformat()

                py_get_list_transactions(
                    page_size=1,
                    start_date=date_start,
                    end_date=date_end
                )



        ### Response JSON

        A successful request returns the HTTP 200 OK status code and a JSON response body that lists transactions.

        .. code-block:: javascript

            {
                'account_number': '2LBUCGLCSB***',
                'end_date': '2023-03-01T00:00:00+0000',
                'last_refreshed_datetime': '2023-03-12T01:59:59+0000',
                'links': [
                    {
                    'href': 'https://api.sandbox.paypal.com/v1/reporting/transactions?start_date=2023-02-01T00%3A00%3A00%2B00%3A00&end_date=2023-03-01T00%3A00%3A00%2B00%3A00&page_size=1&page=19',
                    'method': 'GET',
                    'rel': 'last'
                    },
                    {
                    'href': 'https://api.sandbox.paypal.com/v1/reporting/transactions?start_date=2023-02-01T00%3A00%3A00%2B00%3A00&end_date=2023-03-01T00%3A00%3A00%2B00%3A00&page_size=1&page=2',
                    'method': 'GET',
                    'rel': 'next'
                    },
                    {
                    'href': 'https://api.sandbox.paypal.com/v1/reporting/transactions?start_date=2023-02-01T00%3A00%3A00%2B00%3A00&end_date=2023-03-01T00%3A00%3A00%2B00%3A00&page_size=1&page=1',
                    'method': 'GET',
                    'rel': 'self'
                    }
                ],
                'page': 1,
                'start_date': '2023-02-01T00:00:00+0000',
                'total_items': 19,
                'total_pages': 19,
                'transaction_details': [
                    {
                    'transaction_info':
                        {
                        'available_balance':
                            {
                                'currency_code': 'EUR',
                                'value': '165488.69'
                            },
                            'custom_field': 'S1121674440646-1563665460',
                            'ending_balance':
                            {
                                'currency_code': 'EUR',
                                'value': '165488.69'
                            },
                            'paypal_account_id': 'UYZPMCTQDV***',
                            'paypal_reference_id': '4G8384171L5786***',
                            'paypal_reference_id_type': 'TXN',
                            'protection_eligibility': '02',
                            'transaction_amount':
                            {
                                'currency_code': 'EUR',
                                'value': '-50.00'
                            },
                            'transaction_event_code': 'T1110',
                            'transaction_id': '18670957S08679***',
                            'transaction_initiation_date': '2023-02-12T11:52:33+0000',
                            'transaction_status': 'P',
                            'transaction_updated_date': '2023-02-12T11:52:33+0000'
                        }
                    }
                ]
            }

    .. autofunction:: python_paypal_api.api.Transactions.get_balances


        ### Example python

        .. code-block:: python

            from python_paypal_api.api import Transactions
            from python_paypal_api.base import PaypalApiException
            import logging
            from datetime import datetime, timezone

            def py_get_balances(**kwargs):

                logger.info("---------------------------------")
                logger.info("Transactions > py_get_balances({})".format(kwargs)))
                logger.info("---------------------------------")

                try:

                    result = Transactions(debug=True).get_balances(
                        **kwargs
                    )
                    logger.info(result)

                except PaypalApiException as error:
                    logger.error(error)


            if __name__ == '__main__':

                logger = logging.getLogger("test")
                date_start = datetime(2023, 2, 1, 0, 0, 0, 0, timezone.utc).isoformat()
                py_get_balances(
                    as_of_time=date_start,
                    currency_code="USD"
                )




        ### Response JSON

        A successful request returns the HTTP 200 OK status code and a JSON response body that lists balances.

        .. code-block:: javascript

            {
                'account_id': '2LBUCGLCSB***',
                'as_of_time': '2023-03-12T01:59:59Z',
                'balances': [
                    {
                        'available_balance':
                        {
                            'currency_code': 'USD',
                            'value': '1304.05'
                        },
                        'currency': 'USD',
                         'total_balance':
                        {
                            'currency_code': 'USD',
                             'value': '1304.05'
                        },
                        'withheld_balance':
                        {
                            'currency_code': 'USD',
                             'value': '0.00'
                        }
                    }
                ],
                'last_refresh_time': '2023-03-12T01:59:59Z'
            }

