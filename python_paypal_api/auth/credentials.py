class Credentials:
    def __init__(self, credentials):
        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        self.client_mode = credentials.client_mode