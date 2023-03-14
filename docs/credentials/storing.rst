.. _Storing Credentials:


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

..  code-block:: python

    Identity(store_credentials=True).get_userinfo() # Mode Store Safe No


..  code-block:: python

    Identity(store_credentials=True, safe=True).get_userinfo() # Mode Store Safe Yes



.. _`cachetools`: https://pypi.org/project/cachetools/
.. _`cryptography`: https://pypi.org/project/cryptography/
.. _`confuse`: https://pypi.org/project/confuse/

