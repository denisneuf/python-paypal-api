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
    errors = []
    credentials = None

    def __init__(self, account: str = 'default', *args, **kwargs):
        self.account = account

    def __call__(self, *args, **kwargs):
        self.load_credentials()
        return self.check_credentials()

    @abc.abstractmethod
    def load_credentials(self):
        ...

    def check_credentials(self):
        try:
            self.errors = [c for c in required_credentials if
                           c not in self.credentials.keys() or not self.credentials[c]]
        except (AttributeError, TypeError):
            raise MissingCredentials(f'Credentials are missing: {", ".join(required_credentials)}')
        if not len(self.errors):
            return self.credentials
        raise MissingCredentials(f'Credentials are missing: {", ".join(self.errors)}')


class FromCodeCredentialProvider(BaseCredentialProvider):

    def load_credentials(self):
        return None

    def __init__(self, credentials: dict, *args, **kwargs):
        super(FromCodeCredentialProvider, self).__init__('default', credentials)
        self.credentials = credentials

class FromConfigFileCredentialProvider(BaseCredentialProvider):

    def load_credentials(self):

        try:
            config = confuse.Configuration('python-paypal-api')
            config_filename = os.path.join(config.config_dir(), 'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.account].get()
            self.credentials = account_data

        except (confuse.exceptions.NotFoundError, confuse.exceptions.ConfigReadError):
            logging.info(confuse.exceptions.NotFoundError)
            return


class CredentialProvider:
    credentials = None

    CREDENTIAL_PROVIDERS: Iterable[Type[BaseCredentialProvider]] = (
        FromCodeCredentialProvider,
        FromConfigFileCredentialProvider
    )

    def __init__(
        self,
        account: str = 'default',
        credentials: Optional[Dict[str, str]] = None,
        credential_providers: Optional[Iterable[Type[BaseCredentialProvider]]] = None,
    ):
        self.account = account
        providers = self.CREDENTIAL_PROVIDERS if credential_providers is None else credential_providers
        for cp in providers:
            try:
                self.credentials = cp(account=account, credentials=credentials)()
                break
            except MissingCredentials:
                continue
        if self.credentials:
            self.credentials = self.Config(**self.credentials)
        else:
            raise MissingCredentials(f'Credentials are missing: {", ".join(required_credentials)}')

    class Config:
        def __init__(self, **kwargs):
            self.client_id = kwargs.get('client_id')
            self.client_secret = kwargs.get('client_secret')
            self.client_mode = kwargs.get('client_mode')

