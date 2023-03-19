from io import BytesIO
from typing import TypeVar
import functools
import hashlib
import base64
from python_paypal_api.base.enum import EndPoint
import requests
import logging
import confuse
import os
from python_paypal_api.auth.exceptions import AuthorizationError


class PaypalEndpoint(object):

    def __init__(self, path, method="GET"):
        self.path = path
        self.method = method

    def __call__(self, fn, *args, **kwargs):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            kwargs.update({"path": self.path, "method": self.method})
            result = fn(*args, **kwargs)
            return result
        return decorated


class PaypalEndpointParams(object):
     def __init__(self, query: str):
        self.query = query
     def fill(self, *args):
        return self.query.format(*args)


class BaseTokenTerminate():
    user_agent = 'python-paypal-api'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'


class AccessTokenTerminate(BaseTokenTerminate):
    grant_type = 'client_credentials'  # refresh_token (refresh_token), authorization_code (code)
    token_type_hint = 'ACCESS_TOKEN'
    path = '/v1/oauth2/token/terminate'
    config = confuse.Configuration('python-paypal-api')

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'Authorization': 'Bearer %s' % self.token,
            'Content-Type': self.content_type
        }

    def __init__(self,
                 token: str = None,
                 mode: dict = None,
                 proxies: dict = None,
                 verify: bool = True,
                 timeout: int or float = None,
                 debug: bool = False):
        self.token = token
        self.host = mode.get("End-Point") if mode.get("End-Point") is not None else EndPoint["SANDBOX"].value
        self.store_credentials = mode.get("Store-Credentials")
        self.client_id = mode.get("Client-Id")
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify
        self.debug = debug

    @property
    def values(self):
        return {
            'token': self.token,
            'token_type_hint': self.token_type_hint
        }


    def get_link_file(self, token_flavor=''):

        return '.' + hashlib.md5(
            (token_flavor + self.client_id).encode('utf-8')
        ).hexdigest()


    def delete_file_token(self):
        file = os.path.join(self.config.config_dir(), self.get_link_file())
        if (os.path.isfile(file)):
            os.remove(file)
        else:
            logging.info("file {} dont exist".format(file))

    def terminate(self):

        url = self.host + self.path

        response = requests.post(
            url,
            data=self.values,
            headers=self.headers,
            timeout=self.timeout,
            proxies=self.proxies,
            verify=self.verify,
        )

        if response.status_code != 200:
            response_data = response.json()
            error_message = response_data.get('error_description')
            error_code = response_data.get('error')
            raise AuthorizationError(error_code, error_message, response.status_code)

        else:

            name_token = self.get_link_file()
            file_token = os.path.join(self.config.config_dir(), name_token)
            if (os.path.isfile(file_token)):
                os.remove(file_token)
            else:
                pass
                # logging.info("File do not exist: {}".format(file_token))

            name_key = ".key"
            file_key = os.path.join(self.config.config_dir(), name_key)
            if (os.path.isfile(file_key)):
                os.remove(file_key)
            else:
                pass
                # logging.info("File do not exist: {}".format(file_key))

            # print(len(self.token))
            return self.token[:5] + "***" + self.token[92:]

