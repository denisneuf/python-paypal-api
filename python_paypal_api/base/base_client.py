import python_paypal_api.version as vd
from enum import Enum

class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-paypal-api'

    def __init__(self, account='default', credentials=None):

        try:
            version = vd.__version__
            self.user_agent += f'-{version}'
        except:
            pass