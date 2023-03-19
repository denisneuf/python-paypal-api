:orphan:

.. _From Config File:

====================
From Config File
====================

.. role:: dax-def-type
    :class: dax-def-type

.. role:: dax-def-note
    :class: dax-def-note

An example config file is provided in this repository, it supports multiple accounts.
The confuse will search the system for a config file named `config.yaml`_

The config is parsed by `confused`_, see their docs for more in depth information.
Search paths are:

* macOS: ``~/.config/python-paypal-api`` and ``~/Library/Application Support/python-paypal-api``
* Other Unix: ``~/.config/python-paypal-api`` and ``/etc/python-paypal-api``
* Windows: ``%APPDATA%\python-paypal-api`` where the APPDATA environment variable falls back to ``%HOME%\AppData\Roaming`` if undefined

If you're only using one account, place it under default. You can pass the account's name to the client to use any other account used in the `config.yaml`_ file.

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



Cache Store
===========

The python paypal api will use cachetools by default to store the token.


Usage with default account
--------------------------

..  code-block:: python

    Identity().get_userinfo()


Usage with another account
--------------------------

You can use every account's name from the config file for account

..  code-block:: python

	Identity(credentials="production").get_userinfo()



File Store
==========

Next examples shows how to combine the ``store_credentials`` and ``safe`` kwargs to store the token in a file, encrypted or not:


Usage saving the token
----------------------

..  code-block:: python

    Identity(store_credentials=True).get_userinfo()


Usage saving encrypted token
----------------------------

..  code-block:: python

    Identity(store_credentials=True, safe=True).get_userinfo()



Custom Configurations
=====================

You can provide your own paths to the config.yaml instead of the default configuration search paths, even provide your own file name.
It is possible too to determine your own key to encrypt the token, or provide a path and name to store the key safely in a folder you determine.
Please be aware that the configuration files must follow the requirements to avoid different configurations in the same account.
For example change the path or the key value itself must lead that the .token file could not be read.
If you commit some error and the combination between key and token is lost, remove the token file (and the key if you want generate a new one) an run again to recreate the token.


Custom Credentials
------------------

The custom ``credentials`` need to be passed as a list:


**credentials** :dax-def-type:`list`



    list[0] = account :dax-def-type:`str` :dax-def-note:`required`

        The name of the account that will be used in the yaml configuration file.

    list[1] = path :dax-def-type:`str`  :dax-def-note:`required`

        The path to the folder where the configuration yaml file while be stored.

    list[2] = name :dax-def-type:`str` :dax-def-note:`optional`

        Optional the name of the file where the configuration is stored. If no name is provided or the file is missing will try config.yaml as default.


### Example python with required parameters

..  code-block:: python

    account = "default"

    path = "/Users/your-user/Desktop/python_paypal_api/credentials"

    # It will find a config.yaml file in the folder provided

    custom_credentials = [account, path]

    Identity(credentials=custom_credentials).get_userinfo()


### Example python with all parameters

..  code-block:: python

    account = "default"

    path = "/Users/your-user/Desktop/python_paypal_api/credentials"

    name = "test.yaml"

    custom_credentials = [account, path, name]

    Identity(credentials=custom_credentials).get_userinfo()


Custom Store Credentials
------------------------

The custom ``store_credentials`` need to be passed as a dict:

**credentials** :dax-def-type:`dict`

    | **safe** :dax-def-type:`bool` :dax-def-note:`required`

    | ``True`` will store the token encrypted.

    | Requires: **token_path** and **key_path_name** or **key_value**.

    | ``False`` will store the token in json format.

    | Require: **token_path**.

    Exclude: **key_path_name** and **key_value**.

    | **token_path** :dax-def-type:`str` :dax-def-note:`required`

    | The path to the folder where the token will be stored, if the folder doesn't exist it will be created.

    | **key_path_name** :dax-def-type:`str` :dax-def-note:`optional`

    | The path to the folder where the key will be stored, if the folder doesn't exist it will be created.

    | Require: **safe**: ``True``.

    | **key_value** :dax-def-type:`str` :dax-def-note:`optional`

    | The value of the key that will be used to encrypt the token. Fernet key must be 32 url-safe base64-encoded bytes.



### Example python with parameters, safe False and custom path token

..  code-block:: python

    custom_save_credentials = \
    {
        "safe": False,
        "token_path": "/Users/your-user/Desktop/python_paypal_api/store_unsafe_token",
    }

    Identity(store_credentials=custom_save_credentials, debug=True).get_userinfo()

### Example python with parameters, safe True, custom path token and custom file path for key

..  code-block:: python

    custom_save_credentials = \
    {
        "safe": True,
        "token_path": "/Users/your-user/Desktop/python_paypal_api/store_safe_token",
        "key_path_name": "/Users/your-user/Desktop/python_paypal_api/store_key/sandbox.secret.key",
    }

    Identity(store_credentials=custom_save_credentials, debug=True).get_userinfo()


### How to generate a key

..  code-block:: python

    from cryptography.fernet import Fernet

    key = Fernet.generate_key()

    print (key) # b'38Ooy2dq7hNyhGg3Z_26cirj5aa5M3wURLAeIb5RsNk='

### Example python with parameters, safe True, custom path token and custom key

..  code-block:: python

    custom_save_credentials = \
    {
        "safe": True,
        "token_path": "/Users/your-user/Desktop/python_paypal_api/store_safe_token",
        "key_value": "38Ooy2dq7hNyhGg3Z_26cirj5aa5M3wURLAeIb5RsNk="
    }

    Identity(store_credentials=custom_save_credentials, debug=True).get_userinfo()



Combining Custom Credentials and Custom Store Credentials
---------------------------------------------------------

You could customize the whole configuration, see an example:

### Example python

..  code-block:: python

    from python_paypal_api.api import Identity
    from python_paypal_api.base import PaypalApiException
    import logging

    def py_test_credentials_config_account_full(account: list = None, config: dict = None):

    logging.info("---------------------------------------")
    logging.info("py_test_credentials_config_account_full")
    logging.info("---------------------------------------")

    try:

        result = Identity(credentials=account, store_credentials=config, debug=True).get_userinfo()
        return result

    except PaypalApiException as error:
        logging.error(error)

    if __name__ == '__main__':

        logger = logging.getLogger("test")

        custom_credentials = [
            "production",
            "/Users/hanuman/Desktop/python_paypal_api/credentials",
            "users.yaml"
        ]

        custom_save_credentials = \
            {
                "safe": True,
                "token_path": "/Users/your-user/Desktop/python_paypal_api/store_token",
                "key_path_name": "/Users/your-user/Desktop/python_paypal_api/store_key/production.secret.key",
            }

        res = py_test_credentials_config_account_full(custom_credentials, custom_save_credentials)
        logger.info(res)

References
=====================

.. target-notes::

.. _`config.yaml`: https://github.com/denisneuf/python-paypal-api/#credentials
.. _`confused`: https://confuse.readthedocs.io/en/latest/usage.html#search-paths
