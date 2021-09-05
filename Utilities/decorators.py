from ApplotLibs.Errors import Account as AccountErrors


class Authorization(object):

    def __init__(self, token):
        self.token = token

    def __call__(self, wrapped_func):
        def wrapped(wrapped_self):
            if self.token is None:
                raise AccountErrors.TokenMissing
        return wrapped