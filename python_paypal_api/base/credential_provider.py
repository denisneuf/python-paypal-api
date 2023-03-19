import abc
import functools
import json
import os
import pprint

from typing import Dict, Iterable, Optional, Type

import confuse
import logging

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

    folder = 'python-paypal-api'
    # file = 'credentials.yml' Moved to default confuse config.yaml
    file = None

    def __init__(self, credentials: str, *args, **kwargs):

        self.credentials = credentials

        if kwargs.get("config_folder") is not None:
            self.folder = kwargs.get("config_folder")

        if kwargs.get("config_filename") is not None:
            self.file = kwargs.get("config_filename")

    def load_credentials(self):

        config = confuse.Configuration(self.folder)

        if self.file is None:

            # TODO: make a debug if needed to show which configuration is being loaded
            # logging.info("Must load a default config.yaml in the folder: {}".format(self.folder))

            if os.path.isfile(config.user_config_path()):
                logging.info(config.user_config_path())
            else:
                logging.fatal("The configuration file {} is not in the folder {}".format(os.path.split(config.user_config_path())[1], config.config_dir()))
                exit(0)

        else:

            # logging.info("Must load a file named: {} in the folder {}".format(self.file, os.path.split(config.user_config_path())[0]))
            try:

                config.set_file(config.config_dir() + "/" + self.file)

            except confuse.exceptions.ConfigReadError as err:
                logging.error(confuse.exceptions.ConfigReadError)
                logging.error(err)
                # pass

            except Exception:
                logging.error(Exception)


        # valid template

        template = \
            {
                'configuration': confuse.MappingValues({
                    'client_id': confuse.String(pattern='^[A-Za-z0-9-_]{80,80}$'),
                    'client_secret': confuse.String(pattern='^[A-Za-z0-9-_]{80,80}$'),
                }),
            }

        try:
            valid_config = config.get(template)
        except confuse.ConfigError as err:
            logging.error(confuse.ConfigError)
            logging.error(err)
            exit(0)
        except Exception:
            # print(Exception)
            logging.error(Exception)


        # TODO check if possible remove level configuration or rename to configurations

        try:
            account_data = config["configuration"][self.credentials].get()
        except (confuse.exceptions.NotFoundError,
                confuse.exceptions.ConfigReadError,
                confuse.exceptions.ConfigValueError,
                confuse.exceptions.ConfigTemplateError
                ) as error:
            logging.error(confuse.exceptions.NotFoundError)
            logging.error(error)
            exit(0)

        super().__init__(account_data)
        self.check_credentials()
        return (account_data)


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

            try:
                self.credentials = FromEnvCredentialProvider().load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > ENVIRONMENT ({}, {})".format(self.credentials.get("client_id")[:10]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)


        elif isinstance(credentials, dict):
            try:
                self.credentials = FromCodeCredentialProvider(credentials).load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > CODE ({}, {})".format(self.credentials.get("client_id")[:10]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)


        elif isinstance(credentials, str):
            try:
                self.credentials = FromConfigFileCredentialProvider(credentials).load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > ACCOUNT ({}, {})".format(self.credentials.get("client_id")[:10]+"*",
                                                                                      self.credentials.get("client_mode")))
            except MissingCredentials:
                logging.error("MissingCredentials")
                logging.error(MissingCredentials)

        elif isinstance(credentials, list):

            # TODO: Find a proper validation
            account = credentials[0]
            _config_folder = credentials[1]
            # credentials[2] is optional
            try:
                 _config_filename = credentials[2]
            except IndexError as error:
                # logging.info("The Configuration do not provide a file")
                _config_filename = None

            try:
                self.credentials = FromConfigFileCredentialProvider(account, config_folder=_config_folder, config_filename=_config_filename).load_credentials()
                if self.debug:
                    logging.info("CREDENTIALS MODE > CUSTOM ({}, {})".format(self.credentials.get("client_id")[:10]+"*",
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