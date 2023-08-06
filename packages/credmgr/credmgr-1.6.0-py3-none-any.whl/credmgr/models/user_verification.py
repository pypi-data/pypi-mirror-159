"""Provide the UserVerification class."""
import json

from ..deprecation_decorator import warn_camel_case
from ..mixins import BaseApp, RedditAppMixin
from . import RedditApp
from .utils import _resolve_model_from_input, _resolve_user


class UserVerification(BaseApp, RedditAppMixin):
    """A class for UserVerification instances."""

    _can_fetch_by_name = True
    _credmgr_callable = "user_verification"
    _editable_attrs = ["user_id", "redditor", "reddit_app_id", "extra_data"]
    _get_by_name_path = "get_redditor"
    _name_attr = "user_id"
    _path = "/user_verifications"

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import UserVerificationSchema

            cls._schema = UserVerificationSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize an User Verification instance.

        User verifications are for associating an unique ID with a redditor.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param id: ID of this user verification.
        :param user_id: An unique ID to associate with a redditor.
        :param redditor: Redditor username to associate with an unique ID.
        :param reddit_app_id: ID of the :class:`.RedditApp` associated with this user
            verification.
        :param extra_data: Extra data to be associated with this user verification.
        :param owner_id: ID of the :class:`.User` that owns this user verification.

        """
        super().__init__(credmgr, **kwargs)

    @staticmethod
    @_resolve_user
    @warn_camel_case("userId", "redditApp", "extraData")
    def _create(
        _credmgr, user_id, reddit_app, redditor=None, extra_data=None, owner=None
    ):
        """Create a new User Verification.

        User verifications are for associating an unique ID with a redditor.

        :param str user_id: An unique ID to associate with a redditor.
        :param Union[RedditApp,int,str] reddit_app: Reddit app the user verification is
            for
        :param str redditor: Redditor the user verification is for. This is not usually
            set manually.
        :param dict extra_data: Extra JSON data to include with verification
        :param Union[User,int,str] owner: Owner of the verification. Requires admin to
            create for other users.

        :returns: The new :class:`.UserVerification` instance.

        """
        data = {
            "user_id": user_id,
            "reddit_app_id": _resolve_model_from_input(_credmgr, RedditApp, reddit_app),
        }
        if redditor:
            data["redditor"] = redditor
        if extra_data:
            data["extra_data"] = json.dumps(extra_data)
        if owner:
            data["owner_id"] = owner
        return _credmgr.post("/user_verifications", data=data)
