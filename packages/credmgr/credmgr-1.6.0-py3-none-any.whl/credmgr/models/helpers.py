"""Provide the helper classes."""
from ..deprecation_decorator import warn_camel_case
from ..exceptions import InitializationError
from ..mixins import BaseModel
from . import (
    Bot,
    DatabaseCredential,
    RedditApp,
    RefreshToken,
    SentryToken,
    User,
    UserVerification,
)
from .utils import _resolve_user


class Paginator:
    """Class to handle paginated requests."""

    @_resolve_user
    def __init__(self, credmgr, model, batch_size=20, limit=None, items_owner=None):
        """Initialize a Paginator instance.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param model: A CredentialManager model to list.
        :param batch_size: The number of items to fetch at a time. If ``batch_size`` is
            None, it will fetch them 100 at a time. (default: 20).
        :param limit: The maximum number of items to get.
        :param items_owner: Owner to filter the items by.

        """
        self._completed = False
        self._credmgr = credmgr
        self._current_item_index = None
        self._items_returned = 0
        self._model = model(self._credmgr)
        self._offset = 0
        self._response = None
        self.batch_size = batch_size
        self.items_owner = items_owner
        self.limit = limit

    def __iter__(self):
        """Allow Paginator to operate as an iterator."""
        return self

    def __next__(self):
        """Allow Paginator to operate as an generator."""
        if self.limit is not None and self._items_returned >= self.limit:
            raise StopIteration()  # pragma: no cover

        if self._response is None or self._current_item_index >= len(self._response):
            self._next()

        self._current_item_index += 1
        self._items_returned += 1
        return self._response[self._current_item_index - 1]

    def _next(self):
        if self._completed:
            raise StopIteration()
        params = dict(limit=self.batch_size, offset=self._offset)
        if self.items_owner:
            params["owner_id"] = self.items_owner
        self._response = self._credmgr.get(self._model._path, params=params)
        self._current_item_index = 0
        if not self._response:
            raise StopIteration()  # pragma: no cover
        if self._response and len(self._response) == self.batch_size:
            self._offset += self.batch_size  # pragma: no cover
        else:
            self._completed = True


class BaseHelper(BaseModel):
    """Base Helper class."""

    _model = None

    @warn_camel_case()
    def __call__(self, id=None, **kwargs):
        """Fetch and return an instance of the object."""
        model_kwargs = {}
        by_name = False
        if isinstance(id, str):
            name = id
            id = None
            if self._model._can_fetch_by_name:
                by_name = True
                kwargs[self._model._name_attr] = name
            else:
                raise InitializationError(
                    f"Cannot get {self._model.__name__!r} by name"
                )
        if id:
            model_kwargs["id"] = id
        elif self._model._can_fetch_by_name:
            by_name = True
            if not self._model._get_by_name_attrs:
                model_kwargs[self._model._name_attr] = kwargs[self._model._name_attr]
            for key in self._model._get_by_name_attrs:
                name = kwargs.get(key, None)
                if name:
                    model_kwargs[key] = name
                else:
                    raise InitializationError(
                        f"Missing required keyword argument, {key!r}, to fetch object by name"
                    )
        else:
            raise InitializationError("'id' is required")
        item = self._model(self._credmgr, **model_kwargs)
        item._fetch(by_name)
        return item


class UserHelper(BaseHelper):
    """Interface for interacting with Users."""

    _model = User

    def __call__(self, id=None, username=None):
        """Fetch a :class:`.User` instance by :attr:`id` or :attr:`name`.

        :param Union[int,str] id: ID of the :class:`.User` to fetch. .. note:: If a
            ``str`` is passed it will be treated as the :attr:`username` attr.
        :param str username: Username of the :class:`.User` to fetch. .. note:: If both
            :attr:`id` and :attr:`username` are passed the :attr:`id` will take
            precedence. If :attr:`id` is a ``str`` it will be treated as an
            :attr:`username` and will also take precedence.

        :returns: An initialized :class:`.User` instance.

        """
        kwargs = {}
        by_name = False
        if isinstance(id, str):
            by_name = True
            username = id
            id = None
        if id:
            kwargs["id"] = id
        if username:
            kwargs["username"] = username
        if not (id or username):
            raise InitializationError("At least 'id' or 'username' is required")
        item = User(self._credmgr, **kwargs)
        item._fetch(by_name)
        return item

    def create(
        self,
        username,
        password,
        default_settings=None,
        is_admin=False,
        is_active=True,
        is_regular_user=True,
        is_internal=False,
        reddit_username=None,
    ) -> User:
        """Create a new user.

        **PERMISSIONS: At least ``is_admin`` is required.**

        :param str username: Username for new user (Example: ``spaz``) (required)
        :param str password: Password for new user (Example: ``supersecurepassword``)
            (required)
        :param dict default_settings: Default values to use for new apps (Example:
            ``{"database_flavor": "postgres", "database_host": "localhost"}``)
        :param bool is_admin: Is the user an admin? Allows the user to see all objects
            and create users (Default: ``False``)
        :param bool is_active: Is the user active? Allows the user to sign in (Default:
            ``True``)
        :param bool is_regular_user: (Internal use only)
        :param bool is_internal: (Internal use only)
        :param str reddit_username: The user's Reddit username.

        :returns: User

        """
        return self._model._create(
            self._credmgr,
            username=username,
            password=password,
            default_settings=default_settings,
            is_admin=is_admin,
            is_active=is_active,
            is_regular_user=is_regular_user,
            is_internal=is_internal,
            reddit_username=reddit_username,
        )


class BotHelper(BaseHelper):
    """Interface for interacting with Bots."""

    _model = Bot

    def create(
        self,
        name,
        reddit_app=None,
        sentry_token=None,
        database_credential=None,
        owner=None,
    ) -> Bot:
        """Create a new Bot.

        Bots are used for grouping credentials into a single app.

        :param str name: Name of the Bot (required).
        :param Union[RedditApp,int] reddit_app: Reddit App the bot will use.
        :param Union[SentryToken,int] sentry_token: Sentry Token the bot will use.
        :param Union[DatabaseCredential,int] database_credential: Database Credentials
            the bot will use.
        :param Union[User,int,str] owner: Owner of the bot. Requires Admin to create for
            other users.

        :returns: Bot

        """
        return self._model._create(
            self._credmgr,
            name=name,
            reddit_app=reddit_app,
            sentry_token=sentry_token,
            database_credential=database_credential,
            owner=owner,
        )


class RedditAppHelper(BaseHelper):
    """Interface for interacting with RedditApps."""

    _model = RedditApp

    def create(
        self,
        name,
        client_id,
        user_agent=None,
        app_type="web",
        redirect_uri=None,
        client_secret=None,
        app_description=None,
        enabled=True,
        owner=None,
    ) -> RedditApp:
        """Create a new RedditApp.

        Reddit Apps are used for interacting with reddit.

        :param str name: Name of the RedditApp (required).
        :param str client_id: Client ID of the Reddit App (required).
        :param str user_agent: User agent used for requests to Reddit's API (required,
            defaults to user set default, then to 'python:{name} by
            /u/{reddit_username}' if current_user.reddit_username is set or
            'python:{name}' if it is not set).
        :param str app_type: Type of the app. One of `web`, `installed`, or `script`
            (required, default: 'web').
        :param str redirect_uri: Redirect URI for Oauth2 flow. (required, defaults to
            user set default then to
            `https://credmgr.jesassn.org/oauth2/reddit_callback` if neither are set).
        :param str client_secret: Client secret of the Reddit App.
        :param str app_description: Description of the Reddit App.
        :param bool enabled: Allows the app to be used.
        :param Union[User,int,str] owner: Owner of the Reddit App. Requires Admin to
            create for other users.

        :returns: RedditApp

        """
        if not user_agent:
            reddit_username = self._credmgr.current_user.reddit_username
            reddit_username_str = ""
            if reddit_username:
                reddit_username_str = f" by u/{reddit_username}"
            user_agent = self._credmgr.get_user_default(
                "user_agent", f"python:{name}{reddit_username_str}"
            )
        redirect_uri = self._credmgr.get_user_default(
            "redirect_uri",
            redirect_uri or "https://credmgr.jesassn.org/oauth2/reddit_callback",
        )
        return self._model._create(
            self._credmgr,
            name=name,
            client_id=client_id,
            user_agent=user_agent,
            app_type=app_type,
            redirect_uri=redirect_uri,
            client_secret=client_secret,
            app_description=app_description,
            enabled=enabled,
            owner=owner,
        )


class UserVerificationHelper(BaseHelper):
    """Interface for interacting with UserVerifications."""

    _model = UserVerification

    def create(
        self, user_id, reddit_app, redditor=None, extra_data=None, owner=None
    ) -> UserVerification:
        """Create a new User Verification.

        User verifications for verifying a redditor with a user ID.

        :param str user_id: User ID to associate redditor with (required).
        :param Union[RedditApp,int,str] reddit_app: Reddit app the user verification is
            for (required).
        :param str redditor: Redditor the user verification is for.
        :param dict extra_data: Extra JSON data to include with verification.
        :param int owner: Owner of the verification. Requires Admin to create for other
            users.

        :returns: UserVerification

        """
        return self._model._create(
            self._credmgr,
            user_id=user_id,
            reddit_app=reddit_app,
            redditor=redditor,
            extra_data=extra_data,
            owner=owner,
        )


class SentryTokenHelper(BaseHelper):
    """Interface for interacting with SentryTokens."""

    _model = SentryToken

    def create(self, name, dsn, owner=None) -> SentryToken:
        """Create a new Sentry Token.

        Sentry Tokens are used for logging and error reporting in applications

        :param str name: Name of the Sentry Token (required).
        :param str dsn: DSN of the Sentry Token (required).
        :param Union[User,int,str] owner: Owner of the verification. Requires Admin to
            create for other users.

        :returns: SentryToken

        """
        return self._model._create(self._credmgr, name=name, dsn=dsn, owner=owner)


class DatabaseCredentialHelper(BaseHelper):
    """Interface for interacting with DatabaseCredentials."""

    _model = DatabaseCredential

    def create(
        self,
        name,
        database_flavor="postgres",
        database="postgres",
        database_host="localhost",
        database_port=5432,
        database_username="postgres",
        database_password=None,
        use_ssh=False,
        ssh_host=None,
        ssh_port=None,
        ssh_username=None,
        ssh_password=None,
        use_ssh_key=False,
        private_key=None,
        private_key_passphrase=None,
        enabled=True,
        owner=None,
    ) -> DatabaseCredential:
        """Create a new Database Credential.

        Database Credentials are used for..ya know..databases

        :param str name: Name of the Database Credential (required)
        :param str database_flavor: Type of database, (default: ``postgres``)
        :param str database: Working database to use, (default: ``postgres``)
        :param str database_host: Database server address, (default: ``localhost``)
        :param int database_port: Port the database server listens on, (default:
            ``5432``)
        :param str database_username: Username to use to connect to the database
        :param str database_password: Password to use to connect to the database
        :param bool use_ssh: Determines if the database will be connected to through a
            tunnel
        :param str ssh_host: The address of the server that the SSH tunnel will connect
            to
        :param str ssh_port: The port the SSH tunnel will use
        :param str ssh_username: Username for the SSH tunnel
        :param str ssh_password: Password for the SSH tunnel
        :param bool use_ssh_key: Allows the credentials to be used
        :param str private_key: SSH private key. Note: No validation will be performed.
        :param str private_key_passphrase: Passphrase for the SSH key
        :param bool enabled: Allows the credentials to be used
        :param Union[User,int,str] owner: Owner of the app. Requires Admin to create for
            other users.

        :returns: DatabaseCredential

        """
        return self._model._create(
            self._credmgr,
            name=name,
            database_flavor=database_flavor,
            database=database,
            database_host=database_host,
            database_port=database_port,
            database_username=database_username,
            database_password=database_password,
            use_ssh=use_ssh,
            ssh_host=ssh_host,
            ssh_port=ssh_port,
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            use_ssh_key=use_ssh_key,
            private_key=private_key,
            private_key_passphrase=private_key_passphrase,
            enabled=enabled,
            owner=owner,
        )


class RefreshTokenHelper(BaseHelper):
    """Interface for interacting with RefreshTokens."""

    _model = RefreshToken

    def __call__(self, id=None, redditor=None, reddit_app_id=None):
        """Fetch an instance of :class:`RefreshToken`."""
        kwargs = {}
        if isinstance(id, str):
            if redditor:
                reddit_app_id = redditor
            redditor = id
            id = None
        if id:
            kwargs["id"] = id
        if redditor:
            kwargs["redditor"] = redditor
        if reddit_app_id:
            kwargs["reddit_app_id"] = reddit_app_id
        return super().__call__(**kwargs)
