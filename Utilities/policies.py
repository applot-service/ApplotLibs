from ApplotLibs.Errors import Account as AccountErrors


class CheckPolicies(object):
    token = None

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, wrapped_func, *args, **kwargs):
        def wrapped(wrapped_self, *args, **kwargs):
            if self.token is None:
                print("Token is None")
                # raise AccountErrors.TokenMissing

            return wrapped_func(wrapped_self, *args, **kwargs)
        return wrapped