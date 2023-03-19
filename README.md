# PYTHON-PAYPAL-API

![CodeQL](https://img.shields.io/github/v/release/denisneuf/python-paypal-api)
[![Documentation Status](https://readthedocs.org/projects/python-paypal-api/badge/?version=latest)](https://python-paypal-api.readthedocs.io/en/latest/?badge=latest)

## Paypal's Rest API

A python 3 wrapper to access Paypal Rest API with an easy-to-use interface.

### Install

[![Badge](https://img.shields.io/pypi/v/python-paypal-api?style=for-the-badge)](https://pypi.org/project/python-paypal-api/)

```
pip install python-paypal-api
```

### Donate

If you find this project is useful consider donating or [sponsor](https://github.com/sponsors/denisneuf) it to keep on going on it, thank you.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=G3KB6M2G9YV9C)

![alt text](https://github.com/denisneuf/python-amazon-ad-api/blob/main/test/codigo-QR.png?raw=true)


### Overview

You need obtain your own credentials with Paypal that may include a paypal personal or business account and access as developer. Please view the official [Paypal Developer](https://developer.paypal.com/home) 

You can also check how use the credentials on the [documentation](https://python-paypal-api.readthedocs.io/en/latest/credentials/howto.html) of this Python Paypal API. 


### Environment Credentials
```python
from python_paypal_api.api import Identity

os.environ["client_id"] = "your-client-id"
os.environ["client_secret"] = "your-client-secret"
# os.environ["client_mode"] = "PRODUCTION"

# Can omit client_mode if using SANDBOX

result = Identity().get_userinfo()

```


### Code Credentials
You can use your credentials as follows passing it to the client as a dict. Please review the full [documentation](https://python-paypal-api.readthedocs.io/en/latest/credentials/howto.html) to see all posibilities to include your credentials.

Python code

```python
from python_paypal_api.api import Identity

my_credentials = dict(
    client_id="your-client-id",
    client_secret="your-client-secret",
    client_mode="PRODUCTION"
)

# Can omit client_mode to use SANDBOX

result = Identity(credentials=my_credentials).get_userinfo()

```

### YAML Credentials
Use a config.yaml file with your credentials for more convenience and manage diferent accounts or profiles. You can store a Sandbox and Production (Live) credentials to comvenient switch from sandbox to live environment.
Note: default credentials without client_mode will use SANDBOX paypal endpoint for testing

Create a file config.yaml (From version 0.1.1 the file use the default name provided by confuse package and use template validation)

Please review the full [documentation](https://python-paypal-api.readthedocs.io/en/latest/credentials/config.html) to see all posibilities to include in your configuration.

```javascript
version: '1.0'

configuration:

  production:
    client_id: 'your-client-id'
    client_secret: 'your-client-secret'
    client_mode: 'PRODUCTION'
  default:
    client_id: 'your-client-id-sandbox'
    client_secret: 'your-client-secret-sandbox'

```

Python code

```python
from python_paypal_api.api import Identity

# Leave empty will use the 'default' account
result = Identity().get_userinfo()
# will use germany account data
result = Identity(credentials="production").get_userinfo()
```



### Search path for config.yaml 

* macOS: ``~/.config/python-paypal-api`` and ``~/Library/Application Support/python-paypal-api``
* Other Unix: ``~/.config/python-paypal-api`` and ``/etc/python-paypal-api``
* Windows: ``%APPDATA%\python-paypal-api`` where the APPDATA environment variable falls back to ``%HOME%\AppData\Roaming`` if undefined


[Confuse Help](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)


### Managing obtained credentials

By default the package will store it in cache to use the LRU Cache from cachetools but the cache will be available only during the script living environment, so once you get the token, any call will use the cached token but since the script terminates the cached key will be gone.

There is a way to create a 600 permissions file in the configuration search path. This is because the token obtained it will ve valid for 32400 seconds and storing it will reduce the calls to the oauth paypal endpoint.
The token also can be stored encrypted, for complex configurations read the [Python Paypal API Help](https://python-paypal-api.readthedocs.io/en/latest/credentials/storing.html).



```python
from python_paypal_api.api import Identity
from python_paypal_api.base import PaypalApiException
import logging

try:

    result = Identity(store_credentials=True).get_userinfo()
    logging.info(result)

except PaypalApiException as error:
    logging.error(error)
```



### Exceptions

You can use a [try](https://docs.python.org/3.10/reference/compound_stmts.html#try) except statement when you call the API and catch exceptions if some problem ocurred:

```python
from python_paypal_api.api import Identity
from python_paypal_api.base import PaypalApiException
import logging

try:

    result = Identity().get_userinfo()
    logging.info(result)

except PaypalApiException as error:
    logging.error(error)
```

### Debug

Use debug=True if you want see some logs like the header you submit to the api endpoint, the method and path used among the params and the data submitted if any, to trace possible errors.

```python
from python_paypal_api.api import Identity,
from python_paypal_api.base import PaypalApiException
import logging

try:

    result = Identity(debug=True).get_userinfo()
    logging.info(result)

except PaypalApiException as error:
    logging.error(error)
```

### Paypal Current Resources
* [Catalog](https://python-paypal-api.readthedocs.io/en/latest/api/products.html)
* Disputes
* Identity
* Invoices
* Orders
* Partner Referral
* [Tracking](https://python-paypal-api.readthedocs.io/en/latest/api/tracking.html)
* [Transactions](https://python-paypal-api.readthedocs.io/en/latest/api/transactions.html)


### API NOTICE

This API is based on the [API Client](https://github.com/saleweaver/rapid_rest_client) created by [@saleweaver](https://github.com/saleweaver) but adapted to paypal auth requeriments and improved system for token call

### DISCLAIMER

We are not affiliated with PayPal

### LICENSE

![License](https://img.shields.io/badge/license-apache-green)
