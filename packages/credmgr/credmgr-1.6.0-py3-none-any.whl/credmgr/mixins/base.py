"""Provide the BaseModel class."""
from typing import TYPE_CHECKING

from ..deprecation_decorator import camel_case_warning, warn_camel_case
from ..exceptions import InitializationError
from ..models.utils import _resolve_user

if TYPE_CHECKING:  # pragma: no cover
    from credmgr import CredentialManager


class BaseModel(object):
    """Superclass for all models in credmgr."""

    _serialize_mapping = {}
    _attr_types = {}
    _can_fetch_by_name = False
    _credmgr_callable = None
    _get_by_name_path = "by_name"
    _name_attr = "name"
    _get_by_name_attrs = []  # falls back to _name_attr if empty
    _path = None
    _schema = None

    @warn_camel_case()
    def __init__(self, credmgr: "CredentialManager", **kwargs):
        """Initialize a BaseModel instance.

        :param credmgr: An instance of :class:`.CredentialManager`.

        """
        self._credmgr = credmgr
        if kwargs:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)
        self._fetched = False

    def __getattr__(self, attribute):  # pragma: no cover
        """Return the value of ``attribute``."""
        attribute = camel_case_warning(attribute)
        if attribute in self.__dict__:
            return self.__dict__[attribute]
        if not attribute.startswith("_") and not self._fetched:
            self._fetch()
            return getattr(self, attribute)
        raise AttributeError(
            f"{self.__class__.__name__!r} object has no attribute {attribute!r}"
        )

    def _get(self, id):
        self.__dict__ = self._credmgr.get(f"{self._path}/{id}").__dict__

    def _get_by_name(self):
        data = {}
        if not self._get_by_name_attrs:
            data[
                self._serialize_mapping.get(self._name_attr, self._name_attr)
            ] = getattr(self, self._name_attr)
        for attr in self._get_by_name_attrs:
            name = getattr(self, attr, None)
            if not name:  # pragma: no cover
                raise InitializationError(
                    f"Missing required keyword arg, {attr!r}, to fetch object by name"
                )
            data[self._serialize_mapping.get(attr, attr)] = name
        self.__dict__ = self._credmgr.post(
            f"{self._path}/{self._get_by_name_path}", data=data
        ).__dict__

    def _fetch(self, by_name=False):
        if by_name and self._can_fetch_by_name:
            self._get_by_name()
        else:
            self._get(self.id)
        self._fetched = True

    @_resolve_user
    @warn_camel_case("batchSize")
    def list_items(self, batch_size=20, limit=None, owner=None):
        """List items that are owned by ``owner``."""
        from credmgr.models.helpers import Paginator

        return Paginator(
            self._credmgr,
            self.__class__,
            batch_size=batch_size,
            limit=limit,
            items_owner=owner,
        )

    def __repr__(self):  # pragma: no cover
        """Return repr(self)."""
        return f"{self.__class__.__name__}(id={self.id}, {self._name_attr}={getattr(self, self._name_attr)!r})"

    def __eq__(self, other):
        """Check if both objects are equal."""
        if not isinstance(other, type(self)):
            return False

        return self.id == other.id and getattr(self, self._name_attr) == getattr(
            other, other._name_attr
        )
