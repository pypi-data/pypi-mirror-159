"""Provide the Bot class."""
from ..deprecation_decorator import warn_camel_case
from ..mixins import BaseApp
from .utils import _resolve_user


class Bot(BaseApp):
    """A class for Bot instances.

    To obtain an instance of this class execute:

    .. code-block:: python

        bot = credmgr.bot("bot_name")

    Bots is the intended way to use CredentialManager. Bots are for grouping credentials
    that would be used in a single app.

    The following is the intended usage:

    .. code-block:: python

        from credmgr import CredentialManager

        credential_manager = CredentialManager(api_token="api_token")
        bot = credmgr.bot("bot_name")

        reddit = bot.reddit("Lil_SpazJoekp")
        db_creds = bot.database_credentials
        sentryDSN = bot.sentry_token

    """

    _can_fetch_by_name = True
    _credmgr_callable = "bot"
    _editable_attrs = BaseApp._editable_attrs + [
        "database_credential_id",
        "reddit_app_id",
        "sentry_token_id",
    ]
    _path = "/bots"

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import BotSchema

            cls._schema = BotSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize a Bot instance.

        Bots are used for grouping credentials into a single app

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param id: ID of this Bot.
        :param name: Name of this Bot.
        :param owner_id: ID of the `.User` that owns this Bot.
        :param reddit_app: `.RedditApp` that will be used with this Bot.
        :param sentry_token: `.SentryToken` that will be used with this Bot.
        :param database_credential: `.DatabaseCredential` that will be used with this
            Bot.

        """
        super().__init__(credmgr, **kwargs)

    @staticmethod
    @_resolve_user
    @warn_camel_case("redditApp", "sentryToken", "databaseCredential")
    def _create(
        _credmgr, name, reddit_app, sentry_token, database_credential, owner=None
    ):
        """Create a new Bot.

        Bots are used for grouping credentials into a single app

        :param str name: Name of the Bot (required)
        :param Union[RedditApp,int] reddit_app: Reddit App the bot will use
        :param Union[SentryToken,int] sentry_token: Sentry Token the bot will use
        :param Union[DatabaseCredential,int] database_credential: Database Credentials
            the bot will use
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for
            other users.

        :returns: Bot

        """
        from . import DatabaseCredential, RedditApp, SentryToken

        additional_params = {}
        existing_objects = {}
        if isinstance(reddit_app, RedditApp):
            existing_objects["reddit_app"] = reddit_app
            reddit_app = reddit_app.id
        if reddit_app:
            additional_params["reddit_app_id"] = reddit_app
        if isinstance(sentry_token, SentryToken):
            existing_objects["sentry_token"] = sentry_token
            sentry_token = sentry_token.id
        if sentry_token:
            additional_params["sentry_token_id"] = sentry_token
        if isinstance(database_credential, DatabaseCredential):
            existing_objects["database_credential"] = database_credential
            database_credential = database_credential.id
        if database_credential:
            additional_params["database_credential_id"] = database_credential
        if owner:
            additional_params["owner_id"] = owner
        response = _credmgr.post("/bots", data={"app_name": name, **additional_params})
        for key, value in existing_objects.items():
            setattr(response, key, value)
        return response

    def edit(self, **kwargs):
        """Edit the bot.

        :param name: Changes the name of the :class:`.Bot`
        :param Union[RedditApp,int] reddit_app: Changes the :class:`.RedditApp` the Bot
            will use
        :param Union[SentryToken,int] sentry_token: Changes the :class:`.SentryToken`
            the Bot will use
        :param Union[DatabaseCredential,int] database_credential: Changes the
            :class:`.DatabaseCredential` the Bot will use

        .. note::

            Parameters, ``reddit_app``, ``sentry_token``, and ``database_credential``
            can accept the initialized object or its :attr:`id`. Passing a ``str`` to it
            will not work.

        :returns: The modified :class:`.Bot`

        """
        from . import DatabaseCredential, RedditApp, SentryToken

        for key, value in list(kwargs.items()):
            if key in ["reddit_app", "sentry_token", "database_credential"]:
                if isinstance(
                    kwargs[key], (RedditApp, SentryToken, DatabaseCredential)
                ):
                    new_key = f"{key}_id"
                    kwargs[new_key] = kwargs.pop(key).id
                else:
                    new_key = f"{key}_id"
                    kwargs[new_key] = kwargs.pop(key)
        super().edit(**kwargs)
