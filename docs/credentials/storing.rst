.. _Storing Credentials:

.. role:: dax-def-type
    :class: dax-def-type

..  warning::

	If you are using HTTPBasicAuth this do not applies as every call will be based on client_id and client_secret combination. No token is involved.


Storing Credentials
~~~~~~~~~~~~~~~~~~~

If you use OAuth 2.0 Bearer to avoid calls to the oauth paypal authentication api to obtain the token for Bearer authentication, there is 2 ways to deal with that:


*****
Cache
*****

The python paypal api will use the `cachetools`_ package to store the token in a LRU cache.
This provides you a way that the token is stored in cache however it will be alive since the python script is executing and includes all possible calls to the api.
When the script is ended the cache is flushed and other script will not be able to obtain a cached token one and will call the api to obtain a current or new one.


****
File
****

If you provide a store_credentials bool in the client, True or False (default)
The python paypal api will store the token in a file linked as an md5 of the client_id.
All next calls will find the file first, check if the token is not expired and use it.
If the token is expired will recreate a new file with the new token and the actual expiring time.
For security reasons the token file could be encrypted or not, using safe bool in the client, True or False (default).
If safe=True, will use `cryptography`_ package to generate a Fernet key and encrypt the content.
The .key file and the .token file will be stored in the confuse config folder ``config = confuse.Configuration('python-paypal-api')``
View more details about `confuse`_ in the :ref:`From Config File` help.


------
Simple
------

Pass the keywords parameters to the client as bool:

    ..  code-block:: python

        Identity(store_credentials=True).get_userinfo() # Mode Store Safe No


    ..  code-block:: python

        Identity(store_credentials=True, safe=True).get_userinfo() # Mode Store Safe Yes



-------
Complex
-------

You could also pass the configuration as a dict. In that way you could overwrite the default storing folders for both token and key.
Be aware that the folders need to exist and changing the configuration without moving the files will create a new token with a new key.
Please check full examples to see the way you can use and choose it wisely.

| **safe** :dax-def-type:`bool` Whether if the token will be encrypted or not. True or False
| **token_path** :dax-def-type:`string` The absolut path to the folder wish to store the token
| **key_path_name** :dax-def-type:`string` The absolut path to the file where you wish to store the key.
| **key_value** :dax-def-type:`string` Fernet key must be 32 url-safe base64-encoded bytes. Use key_value will invalidate a key_path_name.



This examples store an encrypted token in the folder ``store_encrypted`` and a key named ``sandbox_secret.key`` in the folder ``store_key``.


..  code-block:: python

        config = \
        {
            "safe": True,
            "token_path": "/Users/your-user/Desktop/store_encrypted",
            "key_path_name": "/Users/your-user/Desktop/store_key/sandbox_secret.key",
        }

        Identity(store_credentials=config, safe=True).get_userinfo() # Mode Store Safe Yes



You could also use your own key and not store it, so in that way you will not use a ``key_path_name`` and you should use a ``key_value``.

..  code-block:: python

        config = \
        {
            "safe": True,
            "token_path": "/Users/your-user/Desktop/store_encrypted",
            "key_value": "4BekoTZNO5aK4HOtIwkGYbq0IegqE5Y6w0bUoqVJqzk=",
        }

        Identity(store_credentials=config, safe=True).get_userinfo() # Mode Store Safe Yes


.. warning::

    Take care about that the token filename is inmutable and if you use diferent configuration could result in overwriting the token with a new key if you change it.


.. _`cachetools`: https://pypi.org/project/cachetools/
.. _`cryptography`: https://pypi.org/project/cryptography/
.. _`confuse`: https://pypi.org/project/confuse/

