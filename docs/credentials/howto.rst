===================
How to Authenticate
===================


.. role:: dax-def-type
    :class: dax-def-type

.. role:: dax-def-note
    :class: dax-def-note

.. _requests: https://docs.python-requests.org/en/latest/index.html

Please check as this example provides all ways to authenticate trough this API.

Paypal Rest API, support Basic and Bearer authentication so lets go from simple to complex.
For any test you need have at least a client_id and a client_secret to run it.

| **client_id** :dax-def-type:`string` The ID obtained from Paypal
| **client_secret** :dax-def-type:`string` The password obtained from Paypal
| **client_mode** :dax-def-type:`enum` ``PRODUCTION`` or ``SANDBOX``




HTTPBasicAuth
=============

The most simple way is to use the auth as a combination of client_id and client_secret, `requests`_ will create an HTTPBasicAuth that will allow you to get access to Paypal Rest API:


Pass Credentials As Tuple
-------------------------


**credentials** :dax-def-type:`tuple`

..  code-block:: python

    credentials = ("your-client-id", "your-client-secret", "SANDBOX")


### Example python

..  code-block:: python

    from python_paypal_api.api import Identity
    from python_paypal_api.base import PaypalApiException

    my_credentials = ("your-client-id", "your-client-secret", "SANDBOX")

    try:

        result = Identity(credentials=my_credentials).get_userinfo()
        payload = result.payload
        print(payload)

    except PaypalApiException as error:

        print(error)




OAuth 2.0 Bearer
================

Bearer Tokens are the predominant type of access token used with OAuth 2.0.
A Bearer Token is an opaque string, not intended to have any meaning to clients using it.
This way will call the paypal oauth2 api and request for a token that could be used for all the api calls until get expired.
There is 3 ways to achieve that: from environ, from code and from config.

Pass Credentials From Environ
-----------------------------

    | **client_id** :dax-def-type:`os._Environ` >> :dax-def-type:`str` :dax-def-note:`required`
    | **client_secret** :dax-def-type:`os._Environ` >> :dax-def-type:`str` :dax-def-note:`required`
    | **client_mode** :dax-def-type:`os._Environ` >> :dax-def-type:`str`

    ..  code-block:: python

        import os
        os.environ["client_id"] = "your-client-id"
        os.environ["client_secret"] = "your-client-secret"
        os.environ["client_mode"] = "your-client-mode"

    ### Example python

    ..  code-block:: python


        import os
        from python_paypal_api.api import Identity
        from python_paypal_api.base import PaypalApiException


        os.environ["client_id"] = "your-client-id"
        os.environ["client_secret"] = "your-client-secret"
        os.environ["client_mode"] = "your-client-mode"

        try:
            result = Identity().get_userinfo()
            payload = result.payload
            print(payload)
        except PaypalApiException as error:
            print(error)





Pass Credentials From Code
--------------------------

    **credentials** :dax-def-type:`dict`

    ..  code-block:: python

        credentials = dict(
            client_id="your-client-id",
            client_secret="your-client-secret",
            client_mode="SANDBOX"
        )


    ### Example python

    ..  code-block:: python

        from python_paypal_api.api import Products
        from python_paypal_api.base import PaypalApiException

        my_credentials = dict(
            client_id="your-client-id",
            client_secret="your-client-secret",
            client_mode="SANDBOX"
        )

        try:
            result = Products(credentials=my_credentials, debug=True).list_products()
            payload = result.payload
            print(payload)
        except PaypalApiException as error:
            print(error)



Pass Credentials From Config
----------------------------

    An example config file is provided in this repository, it supports multiple accounts.
    The confuse will search the system for a config file named ``config.yaml`` in the following search paths.

    * macOS: ``~/.config/python-paypal-api`` and ``~/Library/Application Support/python-paypal-api``
    * Other Unix: ``~/.config/python-paypal-api`` and ``/etc/python-paypal-api``
    * Windows: ``%APPDATA%\python-paypal-api`` where the APPDATA environment variable falls back to ``%HOME%\AppData\Roaming`` if undefined

    Content example of a ``config.yaml`` file.

        ..  code-block:: yaml

            version: '1.0'

            configuration:

                production:
                    client_id: 'your-client-id'
                    client_secret: 'your-client-secret'
                    client_mode: 'PRODUCTION'

                default:
                    client_id: 'your-client-id-sandbox'
                    client_secret: 'your-client-secret-sandbox'



    **credentials** :dax-def-type:`str`

    ..  code-block:: python

        credentials = "production"

    ### Example python

    ..  code-block:: python

        from python_paypal_api.api import Identity
        from python_paypal_api.base import PaypalApiException

        try:
            result = Identity(credentials="production", debug=True).get_userinfo(
            payload = result.payload
            print(payload)
        except PaypalApiException as error:
            print(error)

    View full possibilities :ref:`From Config File`

