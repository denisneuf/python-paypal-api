from io import BytesIO
from typing import TypeVar
import functools
import hashlib
import base64

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
