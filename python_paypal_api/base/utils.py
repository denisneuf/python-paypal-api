import time
import os
import json
from json.decoder import JSONDecodeError
from io import TextIOWrapper
from python_paypal_api.base import PaypalTypeException
import uuid

class Utils:

    @staticmethod
    def payPalRequestId(headers: dict):
        headers["PayPal-Request-Id"] = str(uuid.uuid1())
        return headers

    def payPalClientMetadataId(headers: dict):
        headers["PayPal-Client-Metadata-Id"] = "p5AngF3dfz5uYeQq4Tjws21Qx48Z0Nt9cCX3"

    @staticmethod
    def prefer(headers: dict, value: str):
        headers["Prefer"] = value
        return headers
        
    @staticmethod
    def contentType(headers: dict, value: str):
        headers["Content-Type"] = value
        return headers

    @staticmethod
    def clean_dictionary(dictionary: dict, valid_keys: set):
        """Cleans a dictionary removing null entries and invalid keys
        
        Arguments:
            dictionary {dict} -- The dictionary to be checked
            valid_keys {set} -- The keys that should not be deleted
        """
        keys = list(dictionary.keys())
        for k in keys:
            if dictionary.get(k) == None or not k in valid_keys:
                del dictionary[k] 
        return dictionary


    @staticmethod
    def convert_updates(body):

        comp_keys = ['op', 'path', 'value']

        if isinstance(body, list):

            if isinstance(body[0], tuple):
                body = [ {'op': x[0], 'path': x[1], 'value': x[2]} for x in body ]

            elif isinstance(body[0], dict):
                res = all(sorted(list(body[x].keys())) == sorted(comp_keys) for x in range(len(body)))

        elif isinstance(body, dict):
            body = [body]

        elif isinstance(body, str):
            obj = json.loads(body)

            if isinstance(obj, dict):
                body = [obj]

            elif isinstance(obj, list):
                return body
        else:
            error = "Only type list, dict or str are allowed on body"
            raise PaypalTypeException('TypeError: '+ error)

        return(json.dumps(body))


    @staticmethod
    def convert_body(body, wrap: bool = True):

        if isinstance(body, str):

            if os.path.isfile(body):
                body = open(body, mode="r", encoding="utf-8")
                body = body.read()
                try:
                    json.loads(body)
                except JSONDecodeError as error:
                    raise AdvertisingTypeException(f"{type(error)}", error)
            else:
                try:
                    body = json.loads(body)
                except ValueError as error:
                    raise AdvertisingTypeException(f"{type(error)}", error)
                pass

        if isinstance(body, dict) and wrap:
            try:
                body = json.dumps([body])
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, dict) and wrap is False:
            try:
                body = json.dumps(body)
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, list):
            try:
                body = json.dumps(body)
            except TypeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        if isinstance(body, TextIOWrapper):
            body = body.read()
            try:
                json.loads(body)
            except JSONDecodeError as error:
                raise AdvertisingTypeException(f"{type(error)}", error)

        return body

    def load_all_pages(throttle_by_seconds: float = 2, next_token_param='NextToken',
                       use_rate_limit_header: bool = False,
                       extras: dict = None):
        """
        Load all pages if a next token is returned

        Args:
            throttle_by_seconds: float
            next_token_param: str | The param amazon expects to hold the next token
            use_rate_limit_header: if the function should try to use amazon's rate limit header
            extras: additional data to be sent with NextToken, e.g `dict(QueryType='NEXT_TOKEN')` for `FulfillmentInbound`
        Returns:
            Transforms the function in a generator, returning all pages
        """
        if not extras:
            extras = {}

        def decorator(function):
            def wrapper(*args, **kwargs):
                res = function(*args, **kwargs)
                yield res
                if "nextCursor" in res.payload.get("payload"):
                    kwargs.clear()
                    kwargs.update({next_token_param: res.payload.get("payload")["nextCursor"], **extras})
                    sleep_time = throttle_by_seconds
                    for x in wrapper(*args, **kwargs):
                        yield x
                        if sleep_time > 0:
                            time.sleep(throttle_by_seconds)

            wrapper.__doc__ = function.__doc__
            return wrapper

        return decorator


    def load_all_categories(throttle_by_seconds: float = 2, next_token_param='NextToken',
                       use_rate_limit_header: bool = False,
                       extras: dict = None):
        """
        Load all pages if a next token is returned

        Args:
            throttle_by_seconds: float
            next_token_param: str | The param amazon expects to hold the next token
            use_rate_limit_header: if the function should try to use amazon's rate limit header
            extras: additional data to be sent with NextToken, e.g `dict(QueryType='NEXT_TOKEN')` for `FulfillmentInbound`
        Returns:
            Transforms the function in a generator, returning all pages
        """
        if not extras:
            extras = {}

        def decorator(function):
            def wrapper(*args, **kwargs):
                res = function(*args, **kwargs)
                yield res
                if next_token_param in res.payload:
                    # kwargs.clear()
                    kwargs.update({next_token_param: res.payload[next_token_param], **extras})
                    sleep_time = throttle_by_seconds
                    for x in wrapper(*args, **kwargs):
                        yield x
                        if sleep_time > 0:
                            time.sleep(throttle_by_seconds)

            wrapper.__doc__ = function.__doc__
            return wrapper

        return decorator