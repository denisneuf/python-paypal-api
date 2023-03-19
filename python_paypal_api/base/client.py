import json
import logging
from requests import request
# from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
from python_paypal_api.auth.credentials import Credentials
from python_paypal_api.auth import AccessTokenClient, AccessTokenResponse
from python_paypal_api.base.credential_provider import CredentialProvider
from python_paypal_api.base.api_response import ApiResponse
from python_paypal_api.base.base_client import BaseClient
from python_paypal_api.base.enum import EndPoint
from python_paypal_api.base.exceptions import GetExceptionForCode
import os

log = logging.getLogger(__name__)

class Client(BaseClient):

    def __new__(
            cls,
            *args,
            **kwargs
    ):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Client, cls).__new__(cls)
        return cls.instance


    def __init__(
                self,
                credentials: str or dict or tuple or list = "default",
                store_credentials: bool or dict = False,
                safe: bool = False,
                proxies: dict = None,
                verify: bool = True,
                timeout: int or float = None,
                debug: bool = False
            ):

        super().__init__()
        self.debug = debug
        self.store_credentials = store_credentials

        if isinstance(credentials, tuple):
            self.credentials = credentials
            try:
                mode = credentials[2]
            except IndexError as error:
                mode = None

            self.host = EndPoint[mode].value if mode is not None else EndPoint["SANDBOX"].value

        else:

            self.credentials = CredentialProvider(
                credentials,
                debug=self.debug
            ).credentials

            self._auth = AccessTokenClient(
                credentials=self.credentials,
                store_credentials=self.store_credentials,
                safe=safe,
                proxies=proxies,
                verify=verify,
                timeout=timeout,
                debug=self.debug
            )

            self.host = EndPoint[self.credentials.client_mode].value if self.credentials.client_mode is not None else EndPoint["SANDBOX"].value

        self.endpoint = self.scheme + self.host
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'Authorization': 'Bearer %s' % self.auth.access_token,
        }

    @property
    def basic(self):

        return {
            'User-Agent': self.user_agent,
        }

    @property
    def get_store_credentials(self):

        if isinstance(self.credentials, tuple):
            client_id = self.credentials[0]
        else:
            client_id = self.credentials.client_id

        return {
            'Store-Credentials': self.store_credentials,
            'End-Point': self.endpoint,
            # 'Client-Id': self.credentials.client_id if self.credentials.client_id is not None else self.credentials[0]
            'Client-Id': client_id
        }
        return self.store_credentials

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth()

    def _request(self,
                 path: str,
                 data: str = None,
                 files = None,
                 params: dict = None,
                 headers = None,
                 ) -> ApiResponse:

        method = params.pop('method')

        if headers is not None and isinstance(self.credentials, tuple):
            base_header = self.basic.copy()
            base_header.update(headers)
            basic_header = base_header

        else:

            base_header = self.headers.copy()
            base_header.update(headers)
            token_headers = base_header

        request_data = data if method in ('POST', 'PUT', 'PATCH') else None

        res = request(
            method,
            self.endpoint + path,
            params=params,
            files=files,
            data=request_data,
            headers=basic_header if isinstance(self.credentials, tuple) else token_headers,
            timeout=self.timeout,
            proxies=self.proxies,
            verify=self.verify,
            auth=(
                self.credentials[0],
                self.credentials[1]
                ) if isinstance(self.credentials, tuple) else None
            )

        if self.debug:
            logging.info(res.request.headers)

            if params:
                message = method + " " + res.request.url
            else:
                message = method + " " + self.endpoint + path

            logging.info(message)
            if data is not None:
                logging.info(data)
            if files is not None:
                logging.info(files)

        return self._check_response(res)


    def _check_response(self, res) -> ApiResponse:

        if self.debug:
            logging.info(vars(res))

        content = vars(res).get('_content')
        headers = vars(res).get('headers')
        status_code = vars(res).get('status_code')

        if status_code == 204:
            data = None
        else:
            str_content = content.decode('utf8')
            data = json.loads(str_content)

        if status_code == 400:
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "message": data["message"], "details": data["details"]}
            exception = GetExceptionForCode(status_code).get_class_exception()
            raise exception(dictionary, headers=headers)

        if status_code == 401:
            dictionary = {"error": data["error"], "error_description":data["error_description"], "status_code": status_code}
            exception = GetExceptionForCode(status_code).get_class_exception()
            raise exception(dictionary, headers=headers)

        if status_code == 422:
            # UNPROCESSABLE_ENTITY (The requested action could not be performed, semantically incorrect, or failed business validation.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = GetExceptionForCode(status_code).get_class_exception()
            raise exception(dictionary, headers=headers)

        if status_code == 404:
            # RESOURCE_NOT_FOUND (The specified resource does not exist.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = GetExceptionForCode(status_code).get_class_exception()
            raise exception(dictionary, headers=headers)

        if status_code == 403:
            # RESOURCE_NOT_FOUND (The specified resource does not exist.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = GetExceptionForCode(status_code).get_class_exception()
            raise exception(dictionary, headers=headers)

        authorization = res.request.headers.get("Authorization")

        result_authorization = authorization.split()

        return ApiResponse(data,
                           result_authorization[0],
                           result_authorization[1],
                           self.get_store_credentials,
                           headers=headers
                           )

