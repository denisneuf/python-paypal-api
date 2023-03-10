import json
import logging
from requests import request
from requests.exceptions import HTTPError
from python_paypal_api.auth.credentials import Credentials
from python_paypal_api.auth import AccessTokenClient, AccessTokenResponse
from python_paypal_api.base.credential_provider import CredentialProvider
from python_paypal_api.base.api_response import ApiResponse
from python_paypal_api.base.base_client import BaseClient
from python_paypal_api.base.enum import EndPoint
from python_paypal_api.base.exceptions import get_exception_for_content, get_exception_for_code, GetExceptionForCode
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
            credentials: str or dict = "default",
            store_credentials=True,
            safe=True,
            proxies=None,
            verify=True,
            timeout=None,
            debug=False
    ):

        super().__init__()
        self.debug = debug
        self.credentials = CredentialProvider(
            credentials,
            debug=self.debug
        ).credentials

        self.host = EndPoint[self.credentials.client_mode].value if self.credentials.client_mode is not None else EndPoint["SANDBOX"].value
        self.endpoint = self.scheme + self.host
        self.store_credentials = store_credentials
        self._auth = AccessTokenClient(
            credentials=self.credentials,
            store_credentials=self.store_credentials,
            safe=safe,
            proxies=proxies,
            verify=verify,
            timeout=timeout,
            debug=self.debug
        )

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
    def get_store_credentials(self):
        return {
            'Store-Credentials': self.store_credentials,
            'End-Point': self.endpoint,
            'Client-Id': self.credentials.client_id
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

        if params is None:
            params = {}

        method = params.pop('method')

        if headers is False:
            base_header = self.headers.copy()
            base_header.pop("Content-Type")
            headers = base_header

        elif headers is not None:

            base_header = self.headers.copy()
            base_header.update(headers)
            headers = base_header

        request_data = data if method in ('POST', 'PUT', 'PATCH') else None

        res = request(
            method,
            self.endpoint + path,
            params=params,
            files=files,
            data=request_data,
            headers=headers or self.headers,
            timeout=self.timeout,
            proxies=self.proxies,
            verify=self.verify,
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
            exception = get_exception_for_code(vars(res).get('status_code'))
            raise exception(dictionary, headers=vars(res).get('headers'))

        if status_code == 401:
            dictionary = {"error": data["error"], "error_description":data["error_description"], "status_code": status_code}

            '''

            try :

                dictionary["error_description"]: data["error_description"]

            except:

                dictionary["error_description"]: data["name"]
                
            '''


            exception = GetExceptionForCode(status_code).get_class_exception()
            # exception = get_exception_for_code(vars(res).get('status_code'))
            raise exception(dictionary, headers=headers)

        if status_code == 422:
            # UNPROCESSABLE_ENTITY (The requested action could not be performed, semantically incorrect, or failed business validation.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = get_exception_for_code(vars(res).get('status_code'))
            raise exception(dictionary, headers=vars(res).get('headers'))

        if status_code == 404:
            # RESOURCE_NOT_FOUND (The specified resource does not exist.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = get_exception_for_code(vars(res).get('status_code'))
            raise exception(dictionary, headers=vars(res).get('headers'))

        if status_code == 403:
            # RESOURCE_NOT_FOUND (The specified resource does not exist.)
            dictionary = {"name": data["name"], "status_code": vars(res).get('status_code'), "details": data["details"]}
            exception = get_exception_for_code(vars(res).get('status_code'))
            raise exception(dictionary, headers=vars(res).get('headers'))

        return ApiResponse(data, res.request.headers.get("Authorization")[7:], self.get_store_credentials, headers=headers)
