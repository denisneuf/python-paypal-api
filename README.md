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
You can use your credentials as follows passing it to the client as a dict. Please review the full [documentation](https://github.com/sponsors/denisneuf) to see all posibilities to include your credentials.

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
Use a credentials.yml file with your credentials for more convenience and manage diferent accounts or profiles. You can store a Sandbox and Production (Live) credentials to comvenient switch from sandbox to live environment.
Note: default credentials without client_mode will use SANDBOX paypal endpoint for testing

Create a file credentials.yml

```javascript
version: '1.0'

default:
  client_id: 'your-client-id-sandbox'
  client_secret: 'your-client-secret-sandbox'

production:
  client_id: 'your-client-id'
  client_secret: 'your-client-secret'
  client_mode: 'PRODUCTION'

```

Python code

```python
from python_paypal_api.api import Identity

# Leave empty will use the 'default' account
result = Identity().get_userinfo()
# will use germany account data
result = Identity(credentials="production").get_userinfo()
```



### Search path for credentials.yml

* macOS and Other Unix: `~/.config/python-paypal-api`
* Windows: `%APPDATA%\python-paypal-api` where the <cite>APPDATA</cite> environment variable falls
back to `%HOME%\AppData\Roaming` if undefined


[Confuse Help](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)


### Exceptions

You can use a [try](https://docs.python.org/3.10/reference/compound_stmts.html#try) except statement when you call the API and catch exceptions if some problem ocurred:

```python
from python_paypal_api.api import Identity, Catalog
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
from python_paypal_api.api import Identity, Catalog
from python_paypal_api.base import PaypalApiException
import logging

try:
	result = Identity(debug=True).get_userinfo()
    logging.info(result)

except PaypalApiException as error:
    logging.error(error)
```

### Paypal Current Resources
* Catalog
* Disputes
* Identity
* Invoices
* Orders
* Partner Referral
* Tracking
* Transactions


### API NOTICE

This API is based on the [API Client](https://github.com/saleweaver/rapid_rest_client) created by [@saleweaver](https://github.com/saleweaver) but adapted to paypal auth requeriments and improved system for token call

### DISCLAIMER

We are not affiliated with PayPal

### LICENSE

![License](https://img.shields.io/badge/license-apache-green)
