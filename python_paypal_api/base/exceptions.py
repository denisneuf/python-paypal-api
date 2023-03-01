class PaypalApiException(Exception):
    code = 999

    def __init__(self, error, headers):

        try:
            self.message = error.get('message')
            self.details = error.get('details')
            self.paypal_code = error.get('status_code')
        except IndexError:
            pass

        self.error = error
        self.headers = headers


class PaypalTypeException(TypeError):
    def __init__(self, error):
        super(TypeError, self).__init__(error)

class PaypalApiRequestException(PaypalApiException):
    code = 400

    def __init__(self, error, headers):

        try:
            self.name = error.get('name')
            self.message = error.get('message')
            self.details = error.get('details')
            self.paypal_code = error.get('status_code')
        except IndexError:
            pass

        self.error = error
        self.headers = headers


class PaypalApiBadRequestException(PaypalApiRequestException):
    """
    400 Request has missing or invalid parameters and cannot be parsed.
    """
    def __init__(self, error, headers=None):
        super(PaypalApiBadRequestException, self).__init__(error, headers)

class PaypalApiUnprocessableEntityException(PaypalApiRequestException):
    """
    400 Request has missing or invalid parameters and cannot be parsed.
    """
    def __init__(self, error, headers=None):
        super(PaypalApiUnprocessableEntityException, self).__init__(error, headers)


class PaypalApiForbiddenException(PaypalApiException):
    """
    401 Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """

    def __init__(self, error, headers=None):
        super(PaypalApiForbiddenException, self).__init__(error, headers)


class PaypalApiResourceNotFound(PaypalApiException):
    """
    401 Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """
    def __init__(self, error, headers=None):
        super(PaypalApiResourceNotFound, self).__init__(error, headers)


def get_exception_for_code(code: int):
    return {
        400: PaypalApiBadRequestException,
        422: PaypalApiUnprocessableEntityException,
        401: PaypalApiForbiddenException,
        403: PaypalApiForbiddenException,
        404: PaypalApiResourceNotFound
    }.get(code, PaypalApiException)




def get_exception_for_content(content: object):
    return {
        'UNAUTHORIZED': PaypalApiForbiddenException
    }.get(content.get('code'), PaypalApiException)
