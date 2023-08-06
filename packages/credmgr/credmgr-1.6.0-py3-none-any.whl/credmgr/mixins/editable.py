"""Provide the EditableMixin class."""
from ..deprecation_decorator import warn_camel_case
from . import BaseModel


class EditableMixin(BaseModel):
    """Interface for classes that are editable."""

    _editable_attrs = []

    @warn_camel_case()
    def edit(self, **kwargs):
        """Edit the object.

        :param kwargs: The params to update on the object.

        :returns: The edited object.

        """
        payload = []

        for attr in self._editable_attrs:
            if attr in kwargs:
                path = f"/{self._serialize_mapping.get(attr, attr)}"
                payload.append({"op": "replace", "path": path, "value": kwargs[attr]})
        updated_object = self._credmgr.patch(f"{self._path}/{self.id}", data=payload)
        from . import BaseApp

        for key, value in updated_object.__dict__.items():
            if key in self._editable_attrs or (
                issubclass(type(value), BaseApp) and f"{key}_id" in self._editable_attrs
            ):
                setattr(self, key, value)
        return self
