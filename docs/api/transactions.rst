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



**Transaction Search API**

Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see `Partner with PayPal`_. For more information about the API, see the `Transaction Search API Integration Guide`_.


.. _Transaction Search API Integration Guide: https://developer.paypal.com/docs/transaction-search/


    .. note::

        Note: To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see `Partner with PayPal`_.

.. _Partner with PayPal: https://www.paypal.com/my/webapps/mpp/partner-program/global-programs?_ga=1.72234320.217415639.1675992033

.. autoclass:: python_paypal_api.api.Transactions

    .. autofunction:: python_paypal_api.api.Transactions.get_list_transactions

        .. note::
            * If you specify one or more optional query parameters, the ending_balance response field is empty.
            * It takes a maximum of three hours for executed transactions to appear in the list transactions call.
            * This call lists transaction for the previous three years.


        ### Example python

        .. code-block:: python

            from python_paypal_api.api import Transactions
            from python_paypal_api.base import PaypalApiException
            import logging

            def py_get_list_transactions(**kwargs):

                logging.info("---------------------------------")
                logging.info("Transactions > py_get_list_transactions()")
                logging.info("---------------------------------")

                try:

                    result = Transactions(debug=True).get_list_transactions(
                        **kwargs
                    )
                    logging.info(result)

                except PaypalApiException as error:
                    logging.error(error)


            if __name__ == '__main__':

                logger = logging.getLogger("test")

                py_get_list_transactions(
                    start_date="2023-02-01T00:00:00-0700",
                    end_date="2023-03-01T00:00:00-0700"
                )



        ### Respose python

        .. code-block:: python

            {
              "transaction_details": [
                {
                  "transaction_info": {
                    "paypal_account_id": "6STWC2LSUYYYE",
                    "transaction_id": "5TY05013RG002845M",
                    "transaction_event_code": "T0006",
                    "transaction_initiation_date": "2014-07-11T04:03:52+0000",
                    "transaction_updated_date": "2014-07-11T04:03:52+0000",
                    "transaction_amount": {
                      "currency_code": "USD",
                      "value": "465.00"
                    },
                    "fee_amount": {
                      "currency_code": "USD",
                      "value": "-13.79"
                    },
                    "insurance_amount": {
                      "currency_code": "USD",
                      "value": "15.00"
                    },
                    "shipping_amount": {
                      "currency_code": "USD",
                      "value": "30.00"
                    },
                    "shipping_discount_amount": {
                      "currency_code": "USD",
                      "value": "10.00"
                    },
                    "transaction_status": "S",
                    "transaction_subject": "Bill for your purchase",
                    "transaction_note": "Check out the latest sales",
                    "invoice_id": "Invoice-005",
                    "custom_field": "Thank you for your business",
                    "protection_eligibility": "01"
                  },
                  "payer_info": {
                    "account_id": "6STWC2LSUYYYE",
                    "email_address": "consumer@example.com",
                    "address_status": "Y",
                    "payer_status": "Y",
                    "payer_name": {
                      "given_name": "test",
                      "surname": "consumer",
                      "alternate_full_name": "test consumer"
                    },
                    "country_code": "US"
                  },
                  "shipping_info": {
                    "name": "Sowmith",
                    "address": {
                      "line1": "Eco Space, bellandur",
                      "line2": "OuterRingRoad",
                      "city": "Bangalore",
                      "country_code": "IN",
                      "postal_code": "560103"
                    }
                  },
                  "cart_info": {
                    "item_details": [
                      {
                        "item_code": "ItemCode-1",
                        "item_name": "Item1 - radio",
                        "item_description": "Radio",
                        "item_quantity": "2",
                        "item_unit_price": {
                          "currency_code": "USD",
                          "value": "50.00"
                        },
                        "item_amount": {
                          "currency_code": "USD",
                          "value": "100.00"
                        },
                        "tax_amounts": [
                          {
                            "tax_amount": {
                              "currency_code": "USD",
                              "value": "20.00"
                            }
                          }
                        ],
                        "total_item_amount": {
                          "currency_code": "USD",
                          "value": "120.00"
                        },
                        "invoice_number": "Invoice-005"
                      },
                      {
                        "item_code": "ItemCode-2",
                        "item_name": "Item2 - Headset",
                        "item_description": "Headset",
                        "item_quantity": "3",
                        "item_unit_price": {
                          "currency_code": "USD",
                          "value": "100.00"
                        },
                        "item_amount": {
                          "currency_code": "USD",
                          "value": "300.00"
                        },
                        "tax_amounts": [
                          {
                            "tax_amount": {
                              "currency_code": "USD",
                              "value": "60.00"
                            }
                          }
                        ],
                        "total_item_amount": {
                          "currency_code": "USD",
                          "value": "360.00"
                        },
                        "invoice_number": "Invoice-005"
                      },
                      {
                        "item_name": "3",
                        "item_quantity": "1",
                        "item_unit_price": {
                          "currency_code": "USD",
                          "value": "-50.00"
                        },
                        "item_amount": {
                          "currency_code": "USD",
                          "value": "-50.00"
                        },
                        "total_item_amount": {
                          "currency_code": "USD",
                          "value": "-50.00"
                        },
                        "invoice_number": "Invoice-005"
                      }
                    ]
                  },
                  "store_info": {},
                  "auction_info": {},
                  "incentive_info": {}
                }
                ],
                "account_number": "XZXSPECPDZHZU",
                "last_refreshed_datetime": "2017-01-02T06:59:59+0000",
                "page": 1,
                "total_items": 1,
                "total_pages": 1,
                "links": [
                {
                  "href": "https://api-m.sandbox.paypal.com/v1/reporting/transactions?start_date=2014-07-01T00:00:00-0700&end_date=2014-07-30T23:59:59-0700&transaction_id=5TY05013RG002845M&fields=all&page_size=100&page=1",
                  "rel": "self",
                  "method": "GET"
                }
                ]
            }

    .. autofunction:: python_paypal_api.api.Transactions.get_balances

