"""Provide the BaseApp class."""
from .deletable import DeletableMixin
from .editable import EditableMixin
from .owner import OwnerMixin


class BaseApp(DeletableMixin, EditableMixin, OwnerMixin):
    """The base class for all app classes."""

    _deserialize_mapping = {"app_name": "name"}
    _editable_attrs = ["name"]
    _name_attr = "name"
    _serialize_mapping = {"name": "app_name"}
