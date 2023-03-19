import pprint


class ApiResponse():
    
    def __init__(self, payload=None, authType=None, currentAuth=None, storeCredentials=None, **kwargs):

        # self.payload = payload or kwargs # will return headers if empty response
        self.payload = payload
        self.headers = kwargs
        self.auth_type = authType
        self.current_token = currentAuth if authType == "Bearer" else None
        self.current_basic = currentAuth if authType == "Basic" else None
        self.info = storeCredentials

    def __str__(self):
        return pprint.pformat(self.__dict__)


    def current_token(self):
        return self.current_token

    def current_basic(self):
        return self.current_basic
