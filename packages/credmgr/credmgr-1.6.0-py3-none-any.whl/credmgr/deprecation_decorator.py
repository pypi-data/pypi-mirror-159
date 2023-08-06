"""Provide a decorator for deprecating camelCase arguments."""
import re
import warnings
from functools import wraps

regex = re.compile(r"([a-z])([A-Z])")


def camel_case_warning(attribute):
    """Warn about camelCase parameter names."""
    if regex.search(attribute):
        attribute = regex.sub(r"\1_\2", attribute).lower()
        warnings.warn(
            f"camelCase names have been deprecated. Please use {attribute} instead.",
            DeprecationWarning,
            stacklevel=3,
        )
    return attribute


def warn_camel_case(*items):
    """Warn about camelCase parameter names."""

    def wrapped(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if items:
                for item in items:
                    if item in list(kwargs.keys()):
                        new_name = camel_case_warning(item)
                        kwargs.setdefault(new_name, kwargs.pop(item))
            else:
                for item in list(kwargs.keys()):
                    new_name = camel_case_warning(item)
                    kwargs.setdefault(new_name, kwargs.pop(item))
            return func(*args, **kwargs)

        return wrapper

    return wrapped
