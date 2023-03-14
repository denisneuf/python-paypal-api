.. _OS Environ:

OS Environ
~~~~~~~~~~

You can set credentials from environ by setting a:
``os.environ["client_id"]``
``os.environ["client_secret"]``
and optionally a ``os.environ["client_mode"]``.

Required fields:

..  code-block:: python


    os.environ["client_id"] = "your-client-id"
    os.environ["client_secret"] = "your-client-secret"
    os.environ["client_mode"] = "PRODUCTION" # default "SANDBOX" for testing

*****
Usage
*****

..  code-block:: python

    import logging
    import os
    from python_paypal_api.api import Identity
    from python_paypal_api.base import PaypalApiException

    os.environ["client_id"] = "your-client-id"
    os.environ["client_secret"] = "your-client-secret"

    try:

        result = Identity(debug=True).get_userinfo()

    except PaypalApiException as error:
        logging.error(error)



