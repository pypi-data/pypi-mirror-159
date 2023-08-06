"""Provide the RedditApp class."""
import base64
from typing import TYPE_CHECKING, Union

import praw

from ..deprecation_decorator import warn_camel_case
from ..mixins import BaseApp
from .utils import _resolve_model_from_input, _resolve_user

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw


class RedditApp(BaseApp):
    """A class for Reddit Apps.

    To obtain an instance of this class execute:

    .. code-block:: python

        bot = credmgr.bot("BotName")
        reddit_app = bot.reddit_app

    """

    _credmgr_callable = "reddit_app"
    _editable_attrs = BaseApp._editable_attrs + [
        "app_description",
        "app_type",
        "client_id",
        "client_secret",
        "redirect_uri",
        "user_agent",
    ]
    _path = "/reddit_apps"
    _reddit = None

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import RedditAppSchema

            cls._schema = RedditAppSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize a Reddit App instance.

        Reddit Apps are used for interacting with reddit

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param int id: ID of this Reddit App.
        :param str name: Name of this Reddit App.
        :param str client_id: Client ID of this Reddit App.
        :param str client_secret: Client secret of the Reddit App.
        :param str app_description: Description of what this Reddit App is used for.
        :param str user_agent: The user agent used to identify this Reddit App to
            Reddit.
        :param str app_type: Type of app this Reddit App is. One of: ``web``,
            ``installed``, or ``script``.
        :param str redirect_uri: URL that redditors are redirected to after authorizing
            this Reddit App to access their account.
        :param str state: Used to identify this Reddit App during the OAuth2 flow.
        :param int owner_id: ID of the `.User` that owns this Reddit App.

        """
        super().__init__(credmgr, **kwargs)

        if "state" in kwargs:
            self._fetched = True

    @staticmethod
    @_resolve_user
    @warn_camel_case(
        "clientId",
        "userAgent",
        "appType",
        "redirectUri",
        "clientSecret",
        "appDescription",
    )
    def _create(
        _credmgr,
        name,
        client_id,
        user_agent,
        app_type,
        redirect_uri,
        client_secret,
        app_description,
        enabled,
        owner=None,
    ):
        """Create a new Reddit App.

        Reddit Apps are used for interacting with Reddit

        :param str name: (required)
        :param str client_id: Client ID of the Reddit App (required)
        :param str user_agent: User agent used for requests to Reddit's API (required)
        :param str app_type: Type of the app. One of `web`, `installed`, or `script`
            (required)
        :param str redirect_uri: Redirect URI for Oauth2 flow. Defaults to user set
            redirect uri (required)
        :param str client_secret: Client secret of the Reddit App
        :param str app_description: Description of the Reddit App
        :param bool enabled: Allows the app to be used (defaults to `True`)
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for
            other users.

        :returns: RedditApp

        """
        data = {
            "app_name": name,
            "client_id": client_id,
            "user_agent": user_agent,
            "app_type": app_type,
            "redirect_uri": redirect_uri,
        }
        if client_secret:
            data["client_secret"] = client_secret
        if app_description:
            data["app_description"] = app_description
        if enabled:
            data["enabled"] = enabled
        if owner:
            data["owner_id"] = owner
        return _credmgr.post("/reddit_apps", data=data)

    def reddit(
        self,
        redditor=None,
        *,
        use_async=False,
        use_cache=True,
        reddit_class: Union[praw.Reddit, "asyncpraw.Reddit", None] = None,
        extra_reddit_kwargs=None,
    ) -> praw.Reddit:
        """Provide an optionally authenticated [Async] PRAW instance.

        :param str redditor: The redditor that you want the Reddit instance authorized
            as.
        :param bool use_async: Whether to return an asyncpraw instance.
        :param bool use_cache: Whether to fetch a new instance regardless if it was
            cached already.
        :param reddit_class: The Reddit class to use. Useful if you have a local version
            of PRAW.
        :param dict extra_reddit_kwargs: Extra kwargs to pass to the Reddit class.

        :returns: Reddit instance.

        """
        if extra_reddit_kwargs is None:
            extra_reddit_kwargs = {}
        if not (isinstance(self._reddit, praw.Reddit) == (not use_async)):
            self._reddit = None
        if not (use_cache and self._reddit):
            if not reddit_class:
                if use_async:
                    import asyncpraw

                    reddit_class = asyncpraw.Reddit
                else:
                    reddit_class = praw.Reddit
            if redditor:
                refresh_token = self._credmgr.refresh_token(redditor, self.id)
                if refresh_token:
                    extra_reddit_kwargs["refresh_token"] = refresh_token.refresh_token
            self._reddit = reddit_class(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
                redirect_uri=self.redirect_uri,
                **extra_reddit_kwargs,
            )
        return self._reddit

    def gen_auth_url(self, scopes=None, permanent=False, user_verification=None):
        """Generate a URL for users to verify or authenticate their Reddit account.

        :param Union[list,str] scopes: List of scopes needed. Pass ``'all'`` for all
            scopes. The ``identity`` scope will always be included. (default:
            ``['identity']``)
        :param bool permanent: Determines if a refresh token will be provided. (default:
            ``False``)
        :param Union[UserVerification,int,str] user_verification: Link to a
                :class:`.UserVerification`
                object. Accepted values are:

                - An :class:`.UserVerification` object
                - An :class:`.UserVerification` ``id``
                - An ``user_id`` of a :class:`.UserVerification` record.

            If a :class:`.UserVerification` record does not exist, one will be created.

        :returns: Auth URL

        """
        from credmgr.models import UserVerification

        if scopes is None or scopes == "identity":
            scopes = ["identity"]
        elif scopes == "all":
            scopes = ["*"]
        if "identity" not in scopes and scopes != ["*"]:
            scopes = [scopes, "identity"]
        if permanent:
            duration = "permanent"
        else:
            duration = "temporary"
        u_verification = _resolve_model_from_input(
            self._credmgr, UserVerification, user_verification, "user_id"
        )
        if not u_verification and user_verification:
            u_verification = self._credmgr.user_verification.create(
                user_verification, self.id
            ).user_id
        if u_verification:
            state = base64.urlsafe_b64encode(
                f"{self.state}:{u_verification}".encode()
            ).decode()
        else:
            state = self.state
        return self.reddit().auth.url(scopes, state, duration)
