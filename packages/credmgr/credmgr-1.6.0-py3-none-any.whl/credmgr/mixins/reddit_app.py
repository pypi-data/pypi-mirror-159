"""Provide the RedditAppMixin class."""
from ..models.utils import cached_property
from . import BaseModel


class RedditAppMixin(BaseModel):
    """Interface for classes that have an associated :class:`RedditApp`."""

    _editable_attrs = []

    @cached_property
    def reddit_app(self):
        """Return the associated :class:`RedditApp`."""
        if not self._fetched:
            self._fetch()
        reddit_app = self._credmgr.reddit_app(id=self.reddit_app_id)
        return reddit_app
