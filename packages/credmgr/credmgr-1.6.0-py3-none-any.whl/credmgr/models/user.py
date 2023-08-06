"""Provide the User class."""
import json
from datetime import datetime

from ..deprecation_decorator import warn_camel_case
from ..exceptions import InitializationError
from ..mixins import BaseModel, DeletableMixin, EditableMixin


class User(DeletableMixin, EditableMixin):
    """A class for User instances."""

    _attr_types = {
        **BaseModel._attr_types,
        "created": datetime,
        "updated": datetime,
    }
    _can_fetch_by_name = True
    _credmgr_callable = "user"
    _editable_attrs = [
        "default_settings",
        "is_active",
        "is_admin",
        "is_regular_user",
        "reddit_username",
        "username",
    ]
    _name_attr = "username"
    _path = "/users"

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import UserSchema

            cls._schema = UserSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize an User instance.

        Users are for logging into and accessing that user's credentials

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param int id: ID of the User.
        :param username: Username of the User.
        :param bool is_active: Indicates if the User can log in and access
            CredentialManager.
        :param bool is_regular_user: Indicates if this is a regular user.
        :param bool is_admin: Indicates if this User can create other users and their
            credentials.
        :param default_settings: Default settings used when creating new items without
            those settings explicitly set.
        :param str reddit_username: This User's Reddit username. Used for
            :class:`.RedditApp`'s user_agent.
        :param datetime.datetime created: Date and time this User was created.
        :param datetime.datetime updated: Date and time this User was last updated.
        :param list[RedditApp] reddit_apps: A list of Reddit Apps this User owns.
        :param list[SentryToken] sentry_tokens: A list of Sentry Tokens this User owns.
        :param list[DatabaseCredential] database_credentials: A list of Database
            Credentials this User owns.

        """
        super().__init__(credmgr, **kwargs)
        self._apps = {}
        if "reddit_apps" in kwargs:
            self._apps["reddit_apps"] = kwargs["reddit_apps"]
        if "sentry_tokens" in kwargs:
            self._apps["sentry_tokens"] = kwargs["sentry_tokens"]
        if "database_credentials" in kwargs:
            self._apps["database_credentials"] = kwargs["database_credentials"]

    @staticmethod
    @warn_camel_case(
        "defaultSettings",
        "redditUsername",
        "isAdmin",
        "isActive",
        "isRegularUser",
        "isInternal",
    )
    def _create(
        _credmgr,
        username,
        password,
        default_settings=None,
        reddit_username=None,
        is_admin=False,
        is_active=True,
        is_regular_user=True,
        is_internal=False,
    ):
        """Create a new User.

        **PERMISSIONS: Admin role is required.**

        :param str username: Username for new user (Example: ``spaz``) (required)
        :param str password: Password for new user (Example: ``supersecurepassword``)
            (required)
        :param dict default_settings: Default values to use for new apps (Example:
            ``{"database_flavor": "postgres", "database_host": "localhost"}``)
        :param str reddit_username: User's Reddit username (Example: ``Lil_SpazJoekp``)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects
            and create users (Default: ``False``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default:
            ``True``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)

        :returns: User

        """
        additional_params = {}
        if default_settings:
            additional_params["default_settings"] = json.dumps(default_settings)
        if is_admin:  # pragma: no cover
            additional_params["is_admin"] = is_admin
        if is_active:
            additional_params["is_active"] = is_active
        if is_regular_user:
            additional_params["is_regular_user"] = is_regular_user
        if is_internal:  # pragma: no cover
            additional_params["is_internal"] = is_internal
        if reddit_username:
            additional_params["reddit_username"] = reddit_username
        return _credmgr.post(
            "/users",
            data={"username": username, "password": password, **additional_params},
        )

    def apps(self, only=None):
        """Get apps that are owned by this user.

        :param str only: Pass one of ``reddit_apps``, ``sentry_tokens``,
            ``database_credentials`` to only get that type of apps

        :returns: The user's apps.

        """
        app_types = ["reddit_apps", "sentry_tokens", "database_credentials"]
        if only and only not in app_types:
            raise InitializationError(
                f"App type: {only} is not valid. Only 'reddit_apps', 'sentry_tokens', and 'database_credentials' are valid."
            )
        if not self._apps:
            response = self._credmgr.get(f"/users/{self.id}/apps")
            self._apps = response._apps
            for app in app_types:
                setattr(self, app, self._apps[app])
        return self._apps[only] if only else self._apps
