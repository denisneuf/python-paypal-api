import requests
from requests.auth import HTTPBasicAuth
import hashlib
import logging
import confuse
import os
import logging
import json
from datetime import datetime, timedelta
from cachetools import TTLCache
from python_paypal_api.base import BaseClient
from python_paypal_api.base.enum import EndPoint
from python_paypal_api.auth.credentials import Credentials
from python_paypal_api.auth.access_token_response import AccessTokenResponse
from python_paypal_api.auth.exceptions import AuthorizationError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

cache = TTLCache(maxsize=10, ttl=timedelta(seconds=32400), timer=datetime.now)

class AccessTokenClient(BaseClient):

    grant_type = 'client_credentials'
    path = '/v1/oauth2/token'

    def __init__(self, account='default', credentials=None, store_credentials=True, proxies=None, verify=True, timeout=None):

        self.cred = Credentials(credentials)
        self.store_credentials = store_credentials
        self.host = EndPoint[self.cred.client_mode].value if self.cred.client_mode is not None else EndPoint["SANDBOX"].value
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify

    def _request(self, url, data, headers):

        response = requests.post(
            url,
            data=data,
            headers=headers,
            timeout=self.timeout,
            proxies=self.proxies,
            verify=self.verify,
            auth=HTTPBasicAuth(data["client_id"], data["client_secret"])
        )

        response_data = response.json()

        if response.status_code != 200:
            error_message = response_data.get('error_description')
            error_code = response_data.get('error')
            raise AuthorizationError(error_code, error_message, response.status_code)
        return response_data


    def create_cache_token(self, file:str):

        now_datetime = datetime.now()
        request_url = self.scheme + self.host + self.path

        try:

            access_token = self._request(request_url, self.data, self.headers)

        except AuthorizationError as error:
            logging.fatal(error)
            exit(0)
        
        future_datetime = now_datetime + timedelta(seconds=access_token["expires_in"])
        access_token["expire_time"] = future_datetime.isoformat()
        json_object = json.dumps(access_token, indent=4)
        flags = os.O_WRONLY | os.O_CREAT
        with os.fdopen(os.open(file, flags, 0o600), 'w') as fout:
            fout.write(json_object)
        return access_token

    def get_auth(self) -> AccessTokenResponse:


        # logging.info("self.store_credentials")
        # logging.info(self.store_credentials)
        # logging.info(self.get_file_auth())

        if self.store_credentials:


            now_datetime = datetime.now()

            config = confuse.Configuration('python-paypal-api')
            file = os.path.join(config.config_dir(), self._get_cache_key())
            try:

                openfile = open(file, 'r')
                access_token = json.load(openfile)
                future_datetime = datetime.fromisoformat(access_token["expire_time"])
                openfile.close()

            except FileNotFoundError:

                access_token = self.create_cache_token(file)
                future_datetime = now_datetime + timedelta(seconds=access_token["expires_in"])

            if now_datetime > future_datetime:
                if (os.path.isfile(file)):
                    os.remove(file)
                access_token = self.create_cache_token(file)

            else:
                pass


        else:


            cache_key = self._get_cache_key()
            try:
                # logging.info("cache")
                access_token = cache[cache_key]
            except KeyError:
                # logging.info("request")
                request_url = self.scheme + self.host + self.path
                access_token = self._request(request_url, self.data, self.headers)
                cache[cache_key] = access_token
            # return AccessTokenResponse(**access_token)



        return AccessTokenResponse(**access_token)


    def authorize_auth_code(self, auth_code):
        request_url = self.scheme + self.host + self.path
        res = self._request(
            request_url,
            data=self._auth_code_request_body(auth_code),
            headers=self.headers
        )
        return res

    def _auth_code_request_body(self, auth_code):
        return {
            'grant_type': 'client_credentials',
            'client_id': self.cred.client_id,
            'client_secret': self.cred.client_secret
        }

    @property
    def data(self):
        return {
            'grant_type': self.grant_type,
            'client_id': self.cred.client_id,
            'client_secret': self.cred.client_secret
        }

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'content-type': self.content_type
        }

    def _get_cache_key(self, token_flavor=''):

        return '.' + hashlib.md5(
            (token_flavor + self.cred.client_id).encode('utf-8')
        ).hexdigest()