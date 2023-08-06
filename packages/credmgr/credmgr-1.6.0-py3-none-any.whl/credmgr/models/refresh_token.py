"""Provide the RefreshToken class."""
from ..mixins import BaseApp, RedditAppMixin


class RefreshToken(BaseApp, RedditAppMixin):
    """A class for RefreshToken instances."""

    _can_fetch_by_name = True
    _credmgr_callable = "refresh_token"
    _editable_attrs = ["refresh_token"]
    _get_by_name_attrs = ["redditor", "reddit_app_id"]
    _get_by_name_path = "by_redditor"
    _name_attr = "redditor"
    _path = "/refresh_tokens"

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import RefreshTokenSchema

            cls._schema = RefreshTokenSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize a Refresh Token instance.

        Refresh Tokens are for authenticating with Reddit as a Reddit that has
        authorized a `.RedditApp` to access their Reddit account.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param int id: ID of this Refresh Token.
        :param str redditor: Redditor this Refresh Token is for.
        :param str reddit_app_id: ID of the `.RedditApp` this Refresh Token is for.
        :param str refresh_token: The Refresh Token to pass to a Reddit instance.
        :param list[str] scopes: The OAuth2 scopes this Refresh Token grants access to.
        :param int owner_id: ID of the `.User` that owns this Refresh Token.
        :param datetime.datetime issued_at: Date and time this Refresh Token was issued.
        :param bool revoked: Indicates if this Refresh Token was revoked or superseded
            by another Refresh Token.
        :param datetime.datetime revoked_at: Date and time this Refresh Token was
            revoked or superseded.

        """
        super().__init__(credmgr, **kwargs)
