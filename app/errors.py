
class ApplicationError(object):

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def json(self):
        return {'error': self.error_msg}
