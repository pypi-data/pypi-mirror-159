from functools import wraps

from superwise import Config


class MethodNotSupportedManagedEnv(Exception):
    pass


def not_supported_in_managed(func):
    @wraps(func)
    def wrapper_not_supported_in_managed(*args, **kwargs):
        if Config.IS_MANAGED_ENV:
            raise MethodNotSupportedManagedEnv(
                "The method you're trying to use is currently not supported in a managed environment. Read more - "
                "https://docs.superwise.ai/docs/4-log-production-predictions-2#batch-collector")
        else:
            return func(*args, **kwargs)

    return wrapper_not_supported_in_managed


def return_none_if_managed(func):
    # managed on prem environments don't require some actions that regular environments do.
    # this decorator skips those actions, and returns None.
    @wraps(func)
    def wrapper_get_none_if_managed(*args, **kwargs):
        if Config.IS_MANAGED_ENV:
            return None
        else:
            return func(*args, **kwargs)

    return wrapper_get_none_if_managed
