class AccessTokenResponse:
    def __init__(self, **kwargs):
        self.scope = kwargs.get('scope')
        self.access_token = kwargs.get('access_token')
        self.token_type = kwargs.get('token_type')
        self.app_id = kwargs.get('app_id')
        self.expires_in = kwargs.get('expires_in')
        self.nonce = kwargs.get('nonce')

