import requests
from requests.auth import HTTPBasicAuth
import hashlib
import logging
import confuse
import os
import logging
import json
from json.decoder import JSONDecodeError
from datetime import datetime, timedelta
from cachetools import TTLCache
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
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
    config = confuse.Configuration('python-paypal-api')
    flags = os.O_WRONLY | os.O_CREAT

    @classmethod
    def get_return_key(self, file_path: str = None):

        file = file_path or ".key"

        if file_path is not None:

            path_file = file_path

        else:

            path_file = self.config.config_dir() + "/" + file

        if os.path.exists(path_file):
            with open(path_file, 'rb') as filekey:
                key = filekey.read()
        else:

            head_tail = os.path.split(path_file)
            key_folder = confuse.Configuration(head_tail[0])
            key = Fernet.generate_key()
            with os.fdopen(os.open(key_folder.config_dir() + "/" + head_tail[1], self.flags, 0o600), 'wb') as filekey:
                filekey.write(key)

        filekey.close()
        return key

    def __init__(self,
                 credentials: str or dict = None,
                 store_credentials: bool or dict = False,
                 safe: bool = False,
                 proxies: dict = None,
                 verify: bool = True,
                 timeout: int or float = None,
                 debug: bool = False
                 ):

        self.cred = Credentials(credentials)

        if isinstance(store_credentials, bool):
            self.store_credentials = store_credentials
            self.safe = safe
            if self.safe and self.store_credentials:
                self.key = self.get_return_key()

        elif isinstance(store_credentials, dict):
            self.store_credentials = True
            self.safe = store_credentials.get("safe")
            self.config = confuse.Configuration(store_credentials.get("token_path"))
            key_value = store_credentials.get("key_value")

            #TODO: make a real check dict configuration mapping
            # safe True or False, token path, key path or key value

            if key_value and self.safe:
                self.key = key_value
            elif key_value is None and self.safe:
                key_path_name = store_credentials.get("key_path_name")
                self.key = self.get_return_key(key_path_name)

        self.host = EndPoint[self.cred.client_mode].value if self.cred.client_mode is not None else EndPoint["SANDBOX"].value
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify
        self.debug = debug

    def delete_file_token(self):
        file = os.path.join(self.config.config_dir(), self._get_cache_key())
        if (os.path.isfile(file)):
            os.remove(file)
        else:
            logging.info("file {} dont exist".format(file))

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
            logging.info("access token client")
            raise AuthorizationError(error_code, error_message, response.status_code)

        return response_data

    def create_file_token(self, file:str):

        now_datetime = datetime.now()
        request_url = self.scheme + self.host + self.path

        try:

            access_token = self._request(request_url, self.data, self.headers)

        except AuthorizationError as error:
            logging.fatal(error)
            exit(0)
        
        future_datetime = now_datetime + timedelta(seconds=access_token["expires_in"])
        access_token["expire_time"] = future_datetime.isoformat()

        if self.safe:

            fernet = Fernet(self.key)
            json_object = json.dumps(access_token)
            bytes_object = bytes(json_object, "utf-8")
            token = fernet.encrypt(bytes_object)

            with os.fdopen(os.open(file, self.flags, 0o600), 'wb') as fout:
                fout.write(token)

        else:

            json_object = json.dumps(access_token)
            with open(file, 'w') as filetoken:
                filetoken.write(json_object)

        return access_token


    def replace_content_unsafe(self, encrypted_token:str):

        file = os.path.join(self.config.config_dir(), self._get_cache_key())
        fernet = Fernet(self.get_return_key())
        decrypted_token = fernet.decrypt(encrypted_token)

        with os.fdopen(os.open(file, self.flags, 0o600), 'wb') as fout:
            fout.seek(0)
            fout.truncate()
            fout.write(decrypted_token)

        return json.loads(decrypted_token)

    def replace_content_safe(self, content:str):
        file = os.path.join(self.config.config_dir(), self._get_cache_key())

        fernet = Fernet(self.key)
        bytes_object = bytes(content, "utf-8")
        token = fernet.encrypt(bytes_object)

        with os.fdopen(os.open(file, self.flags, 0o600), 'wb') as fout:
            fout.seek(0)
            fout.truncate()
            fout.write(token)

        return json.loads(content)

    def get_auth(self) -> AccessTokenResponse:

        if self.store_credentials:
            now_datetime = datetime.now()
            file = os.path.join(self.config.config_dir(), self._get_cache_key())
            if self.safe:

                try :
                    fernet = Fernet(self.key)
                except ValueError as error:

                    logging.info(ValueError)
                    logging.info(error)
                    exit(0)

                try:

                    openfile = open(file, 'r')
                    str_encrypted_token = openfile.read()
                    encrypted_token = bytes(str_encrypted_token, "utf-8")
                    decrypted_token = fernet.decrypt(encrypted_token)
                    logging.info(decrypted_token)
                    access_token = json.loads(decrypted_token)
                    openfile.close()

                except FileNotFoundError:

                    access_token = self.create_file_token(file)
                    if self.debug:
                        logging.info("AUTH TOKEN >> FILE >> NOT FOUND >> CREATE")
                        logging.info(access_token)
                    future_datetime = now_datetime + timedelta(seconds=access_token["expires_in"])

                except InvalidToken as error:

                    logging.info(InvalidToken)
                    access_token = self.replace_content_safe(str_encrypted_token)
                    # exit(0)

            else:

                #TODO: Avoid open file 2 times and consider if move from encrypt / decrypt has sense

                try:

                    openfile = open(file, 'r')
                    access_token = json.load(openfile)
                    openfile.close()

                except JSONDecodeError:

                    logging.error(JSONDecodeError)
                    logging.error(openfile)
                    openfile = open(file, 'r')
                    access_token = self.replace_content_unsafe(openfile.read())
                    openfile.close()
                    # exit(0)

                except FileNotFoundError:

                    access_token = self.create_file_token(file)
                    if self.debug:
                        logging.info("AUTH TOKEN >> FILE >> NOT FOUND >> CREATE")
                        logging.info(access_token)

            future_datetime = datetime.fromisoformat(access_token["expire_time"])

            if self.debug:
                logging.info("AUTH TOKEN >> FILE >> READ expires({})".format(access_token.get("expire_time")))
                logging.info(access_token)

            if now_datetime > future_datetime:
                self.delete_file_token()
                access_token = self.create_file_token(file)

            else:
                pass

        else:

            cache_key = self._get_cache_key()
            try:
                access_token = cache[cache_key]
                if self.debug:
                    logging.info("AUTH TOKEN >> CACHE >> READ")
                    logging.info(access_token)
            except KeyError:
                request_url = self.scheme + self.host + self.path
                access_token = self._request(request_url, self.data, self.headers)

                if self.debug:
                    logging.info("AUTH TOKEN >> CACHE >> KEY_ERROR >> CREATE")
                    logging.info(access_token)
                cache[cache_key] = access_token

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