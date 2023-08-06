"""Provide helper utilities used by other models."""
from functools import wraps

from credmgr.exceptions import NotFound


def _resolve_model_from_input(credmgr, model, input_value, return_attr="id"):
    value = None
    if isinstance(input_value, model):
        value = getattr(input_value, return_attr)
    elif isinstance(input_value, int):
        value = input_value
    elif isinstance(input_value, str):
        try:
            found_item = getattr(credmgr, model._credmgr_callable)(input_value)
        except NotFound:
            found_item = None
        if found_item:
            value = getattr(found_item, return_attr)
    return value


def _resolve_user(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        from . import User

        value = None
        user = kwargs.get("owner", None)
        if user:
            if isinstance(user, User):
                value = getattr(user, "id")
            elif isinstance(user, int):
                value = user
            elif isinstance(user, str):
                found_user = self._credmgr.user(user)
                if found_user:
                    value = getattr(found_user, "id")
            kwargs["owner"] = value
        return func(self, *args, **kwargs)

    return wrapper


try:
    from functools import cached_property
except ImportError:  # pragma: no cover
    from cached_property import cached_property  # noqa: F401
