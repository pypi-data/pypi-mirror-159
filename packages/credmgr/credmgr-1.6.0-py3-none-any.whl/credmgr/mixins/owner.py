"""Provide the OwnerMixin class."""
from credmgr.mixins import BaseModel
from credmgr.models.utils import cached_property


class OwnerMixin(BaseModel):
    """Interface for classes that have an owner."""

    _editable_attrs = []

    @cached_property
    def owner(self):
        """Get the owner of the object."""
        if "owner_id" not in self.__dict__:
            if not self._fetched:
                self._fetch()
        user = self._credmgr.user(id=self.owner_id)
        return user
