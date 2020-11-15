class Request(object):

    def __init__(self, endpoint, method, headers):
        self.endpoint = endpoint
        self.method = method
        self.headers = headers
