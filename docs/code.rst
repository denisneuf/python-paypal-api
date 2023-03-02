From Code
=========

You can override/set credentials from code by passing a ``dict`` to the client.

If you pass a value in credentials, other credentials from env variables or from a config file will be ignored.

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

    credentials = dict(
        refresh_token='your-refresh_token',
        client_id='your-client_id',
        client_secret='your-client_secret',
        profile_id='your-profile_id',
    )

    try:

        result = Identity(credentials=my_credentials).get_userinfo()

        payload = result.payload

        logging.info(payload)

    except PaypalApiException as error:

        logging.info(error)




