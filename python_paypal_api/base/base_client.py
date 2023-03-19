import python_paypal_api.version as vd

class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-paypal-api'
    version = vd.__version__

    def __init__(self):

        try:
            version = vd.__version__
            self.user_agent += f'-{version}'

        except:
            pass

