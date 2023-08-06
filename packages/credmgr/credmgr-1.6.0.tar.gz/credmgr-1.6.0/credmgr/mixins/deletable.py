"""Provide the DeletableMixin class."""
from . import BaseModel


class DeletableMixin(BaseModel):
    """Interface for classes that can be deleted."""

    def delete(self):
        """Delete the object.

        Example usage:

        .. code-block:: python

            bot = credential_manager.bot("name")

            reddit_app = bot.reddit_app
            reddit_app.delete()

            sentry_token = bot.sentry_token
            sentry_token.delete()

            database_credential = bot.database_credential
            database_credential.delete()

            user_verification = cre

        """
        self._credmgr.delete(f"{self._path}/{self.id}")
        del self
