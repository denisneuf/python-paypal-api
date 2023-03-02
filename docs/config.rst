Config File
===========

An example config file is provided in this repository, it supports multiple accounts.
The program looks for a file called `credentials.yml`_

The config is parsed by `confused`_, see their docs for more in depth information.
Search paths are:

..  code-block:: bash

    macOS: ~/.config/python-sp-api
    Other Unix: ~/.config/python-sp-api
    Windows: %APPDATA%\python-sp-api where the APPDATA environment variable falls back to %HOME%\AppData\Roaming if undefined

If you're only using one account, place it under default. You can pass the account's name to the client to use any other account used in the `credentials.yml`_ file.

..  code-block:: yaml

    version: '1.0'

    default:
      client_id: 'your-client-id-sandbox'
      client_secret: 'your-client-secret-sandbox'

    production:
      client_id: 'your-client-id'
      client_secret: 'your-client-secret'
      client_mode: 'PRODUCTION'


**************************
Usage with default account
**************************

..  code-block:: python

    Identity().get_userinfo()


**************************
Usage with another_account
**************************

You can use every account's name from the config file for account

..  code-block:: python

	result = Identity(account="production").get_userinfo()


**********
References
**********

.. target-notes::

.. _`credentials.yml`: https://github.com/denisneuf/python-amazon-ad-api/#credentials
.. _`confused`: https://confuse.readthedocs.io/en/latest/usage.html#search-paths


