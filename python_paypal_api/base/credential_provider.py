import abc
import functools
import json
import os

from typing import Dict, Iterable, Optional, Type

import confuse
import logging
# from cachetools import Cache

logger = logging.getLogger(__name__)
required_credentials = [
    'client_id',
    'client_secret'
]


class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class BaseCredentialProvider(abc.ABC):

    def __init__(self, credentials: dict or str, *args, **kwargs):
        self.credentials = credentials

    @abc.abstractmethod
    def load_credentials(self):
        pass


    def _get_env(self, key):
        return os.environ.get(f'{key}',
                              os.environ.get(key))

    def check_credentials(self):
        try:
            self.errors = [c for c in required_credentials if
                           c not in self.credentials.keys() or not self.credentials[c]]
        except (AttributeError, TypeError):
            raise MissingCredentials(f'Credentials are missing: {", ".join(required_credentials)}')
        if not len(self.errors):
            return self.credentials
        raise MissingCredentials(f'Credentials are missing: {", ".join(self.errors)}')



class FromEnvCredentialProvider(BaseCredentialProvider):

    def __init__(self, *args, **kwargs):
        pass

    def load_credentials(self):
        account_data = dict(
            client_id=self._get_env('client_id'),
            client_secret=self._get_env('client_secret'),
            client_mode=self._get_env('client_mode'),
        )
        self.credentials = account_data
        self.check_credentials()
        return self.credentials

class FromCodeCredentialProvider(BaseCredentialProvider):

    def __init__(self, credentials: dict, *args, **kwargs):
        super().__init__(credentials)

    def load_credentials(self):
        self.check_credentials()
        return self.credentials


class FromConfigFileCredentialProvider(BaseCredentialProvider):

    def __init__(self, credentials: str, *args, **kwargs):
        self.credentials = credentials

    def load_credentials(self):

        try:
            config = confuse.Configuration('python-paypal-api')
            config_filename = os.path.join(config.config_dir(), 'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.credentials].get()
            super().__init__(account_data)
            self.check_credentials()
            return(account_data)

        except (confuse.exceptions.NotFoundError, confuse.exceptions.ConfigReadError):
            logging.error(confuse.exceptions.NotFoundError)
            return


class CredentialProvider():
    credentials = None
    debug = False

    def load_credentials(self):
        pass


    def __init__(
        self,
        credentials: str or dict,
        debug
    ):

        self.debug = debug

        client_id_env = os.environ.get('client_id')
        client_secret_env = os.environ.get('client_secret')

        if client_id_env is not None and client_secret_env is not None:



            # print(self.debug)

            try:
                self.credentials = FromEnvCredentialProvider().load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > ENVIRONMENT ({}, {}, {})".format(self.credentials.get("client_id")[:5]+"*",
                                                                                      self.credentials.get("client_secret")[:5]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)


        elif isinstance(credentials, dict):
            try:
                self.credentials = FromCodeCredentialProvider(credentials).load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > CODE ({}, {}, {})".format(self.credentials.get("client_id")[:5]+"*",
                                                                                      self.credentials.get("client_secret")[:5]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)


        elif isinstance(credentials, str):
            try:
                self.credentials = FromConfigFileCredentialProvider(credentials).load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > ACCOUNT ({}, {}, {})".format(self.credentials.get("client_id")[:5]+"*",
                                                                                      self.credentials.get("client_secret")[:5]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)

        else:
            raise MissingCredentials

        self.credentials = self.Config(**self.credentials)

    class Config:
        def __init__(self, **kwargs):
            self.client_id = kwargs.get('client_id')
            self.client_secret = kwargs.get('client_secret')
            self.client_mode = kwargs.get('client_mode')