import pprint


class ApiResponse():
    
    def __init__(self, payload=None, currentToken=None, storeCredentials=None, **kwargs):

        # self.payload = payload or kwargs # will return headers if empty response
        self.payload = payload
        self.headers = kwargs
        self.current_token = currentToken
        self.store_credentials = storeCredentials

    def __str__(self):
        return pprint.pformat(self.__dict__)


    def current_token(self):
        return self.current_token
