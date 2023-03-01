# PYTHON-PAYPAL-API

![CodeQL](https://img.shields.io/github/v/release/denisneuf/python-paypal-api)

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
result = Identity(account="production").get_userinfo()
```



### Search path for credentials.yml

* macOS and Other Unix: `~/.config/python-paypal-api`
* Windows: `%APPDATA%\python-paypal-api` where the <cite>APPDATA</cite> environment variable falls
back to `%HOME%\AppData\Roaming` if undefined


[Confuse Help](https://confuse.readthedocs.io/en/latest/usage.html#search-paths)

