.. _From Code:

From Code
~~~~~~~~~

You can set credentials from code by passing a ``dict`` to the client.

Required fields:

..  code-block:: python


    credentials = dict(
        client_id='your-client_id',
        client_secret='your-client_secret',
        client_mode='PRODUCTION',
    )

*****
Usage
*****

..  code-block:: python

    import logging
    from python_paypal_api.api import Identity
    from python_paypal_api.base import PaypalApiException

    my_credentials = dict(
        client_id='your-client_id',
        client_secret='your-client_secret',
        client_mode='your-client_mode', # SANDBOX OR PRODUCTION
    )

    try:

        result = Identity(credentials=my_credentials).get_userinfo()

        payload = result.payload

        logging.info(payload)

    except PaypalApiException as error:

        logging.info(error)




