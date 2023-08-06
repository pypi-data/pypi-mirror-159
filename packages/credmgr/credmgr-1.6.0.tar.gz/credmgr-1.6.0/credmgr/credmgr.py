"""Provide the CredentialManager class."""

import configparser
import os

from requests import Response

from . import models
from .auth import ApiTokenAuth
from .config import Config
from .deprecation_decorator import warn_camel_case
from .exceptions import InitializationError
from .models.utils import cached_property
from .requestor import Requestor, _urljoin

User = models.User
Bot = models.Bot
RedditApp = models.RedditApp
RefreshToken = models.RefreshToken
UserVerification = models.UserVerification
SentryToken = models.SentryToken
DatabaseCredential = models.DatabaseCredential


class CredentialManager(object):
    """The CredentialManager class provides a way to interact with CredentialManager's API.

    The official way to initialize an instance of this class is to:

    .. code-block:: python

        from credmgr import CredentialManager

        credential_manager = CredentialManager(api_token="LIqbGjAeep3Ws5DH3LOEQPmw8UZ6ek")

    .. note::

        It is recommended to use environment variables or a ``.credmgr.ini`` file. See
        :ref:`Auth documentation <auth>` for more details.

    """

    _default = None
    _endpoint = "/api/v1"

    def _objectify_response(self, response: Response):
        """Return a deserialized object from a response.

        :param response: The response to deserialize.

        :returns: A deserialized object.

        """
        data = response.json()
        if data:
            if isinstance(data, list):
                return [self._objectify(item) for item in data]
            return self._objectify(data)

    def _objectify(self, data):
        """Deserialize a dict or list into an object.

        :param data: Data to be deserialized.

        :returns: A credmgr object.

        """
        if data:
            resource_type = data.get("resource_type", "")
            model = getattr(models, resource_type, None)
            data = self._inject(data)
            return model.schema.load(data) if model else data

    def _inject(self, data: dict):
        """Injects the credential manager into the data.

        :param data: Data to be injected.

        :returns: The injected data.

        """
        if isinstance(data, dict):
            if "resource_type" in data:
                data["credmgr"] = self
            for key, value in list(data.items()):
                if isinstance(value, dict):
                    data[key] = self._inject(value)
                elif isinstance(value, list):
                    data[key] = list(map(self._inject, value))
        return data

    @warn_camel_case("configName", "sessionClass", "sessionKwargs", "apiToken")
    def __init__(
        self, config_name=None, session_class=None, session_kwargs=None, **kwargs
    ):
        """Initialize a CredentialManager instance.

        :param str config_name: The name of a section in your ``.credmgr.ini`` file that
            credmgr will load its configuration is loaded from. If ``config_name`` is
            ``None``, then it will look for it in the environment variable
            ``credmgr_config_name``. If it is not found there, the ``default`` section
            is used.
        :param Session session_class: A Session class that will be used to create a
            requestor. If not set, use ``requests.Session`` (default: None).
        :param dict session_kwargs: Dictionary with additional keyword arguments used to
            initialize the session (default: None).

        Additional keyword arguments will be used to initialize the :class:`.Config`
        object. This can be used to specify configuration settings during instantiation
        of the :class:`.CredentialManager` instance. For more details please see
        :ref:`configuration`.

        Required settings are:

        - api_token

        OR

        - username
        - password

        .. warning::

            Using an API Token instead of a username/password is strongly recommended!

        The ``session_class`` and ``session_kwargs`` allow for customization of the
        session :class:`.CredentialManager` will use. This allows, e.g., easily adding
        behavior to the requestor or wrapping its |Session|_ in a caching layer. Example
        usage:

        .. |Session| replace:: ``Session``

        .. _session: https://2.python-requests.org/en/master/api/#requests.Session

        .. code-block:: python

            import json, betamax, requests


            class JSONDebugRequestor(Requestor):
                def request(self, *args, **kwargs):
                    response = super().request(*args, **kwargs)
                    print(json.dumps(response.json(), indent=4))
                    return response


            my_session = betamax.Betamax(requests.Session())
            credential_manager = CredentialManager(
                ..., session_class=JSONDebugRequestor, session=my_session
            )

        """
        if session_kwargs is None:
            session_kwargs = {}
        config_section = None
        try:
            config_section = (
                config_name or os.getenv("credmgr_config_name") or "DEFAULT"
            )
            self.config = Config(config_section, **kwargs)
        except configparser.NoSectionError as exc:
            if config_section is not None:
                exc.message += "\nYou provided the name of a .credmgr.ini section that doesn't exist."
            raise

        self._server = _urljoin(
            getattr(self.config, "server"), getattr(self.config, "endpoint")
        )
        api_token = getattr(self.config, "api_token")
        username = getattr(self.config, "username")
        password = getattr(self.config, "password")

        init_error_message = "Required settings are missing. Either 'api_token' OR 'username' and 'password' must be specified, These settings can be provided in a .credmgr.ini file, as a keyword argument during the initialization of the `CredentialManager` class, or as an environment variable."
        if all([api_token, username, password]):
            raise InitializationError(init_error_message)
        if api_token:
            self._auth = ApiTokenAuth(api_token)
        elif username and password:
            self._auth = (username, password)
        else:
            raise InitializationError(
                "API Token or a username/password pair must be set."
            )

        self._requestor = Requestor(
            self._server, self._auth, session_class, **session_kwargs
        )
        self._current_user = None
        self._user_defaults = None
        self.get_user_default = lambda key, default: self.user_defaults.get(
            key, default
        )
        self.user = models.UserHelper(self)
        """An instance of :class:`.UserHelper`.

        Provides an interface for interacting with :class:`.User`. For example, to get a
        :class:`.User` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            user = credential_manager.user(1)
            print(user.id)

        To create a :class:`.User` do:

        .. code-block:: python

            user = credential_manager.user.create(**user_kwargs)

        See :meth:`~.UserHelper.create` for the required params.

        """
        self.bot = models.BotHelper(self)
        """An instance of :class:`.BotHelper`.

        Provides an interface for interacting with :class:`.Bot`. For example, to get a
        :class:`.Bot` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            bot = credential_manager.bot(1)
            print(bot.id)

        To create a :class:`.Bot` do:

        .. code-block:: python

            bot = credential_manager.bot.create(**bot_kwargs)

        See :meth:`~.BotHelper.create` for the required params.

        """
        self.reddit_app = models.RedditAppHelper(self)
        """An instance of :class:`.RedditAppHelper`.

        Provides an interface for interacting with :class:`.RedditApp`. For example, to
        get a :class:`.RedditApp` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            reddit_app = credential_manager.reddit_app(1)
            print(reddit_app.id)

        To create a :class:`.RedditApp` do:

        .. code-block:: python

            reddit_app = credential_manager.reddit_app.create(**reddit_app_kwargs)

        See :meth:`~.RedditAppHelper.create` for the required params.

        """
        self.refresh_token = models.RefreshTokenHelper(self)
        """An instance of :class:`.RefreshTokenHelper`.

        Provides an interface for interacting with :class:`.RefreshToken`. For example
        to get a :class:`.RefreshToken` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            refresh_token = credential_manager.refresh_token(1)
            print(refresh_token.id)

        .. note::

            Refresh tokens cannot be manually created.

        """
        self.user_verification = models.UserVerificationHelper(self)
        """An instance of :class:`.UserVerificationHelper`.

        Provides an interface for interacting with :class:`.UserVerification`. For
        example to get a :class:`.UserVerification` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            user_verification = credential_manager.user_verification(1)
            print(user_verification.id)

        To create a :class:`.UserVerification` do:

        .. code-block:: python

            user_verification = credential_manager.user_verification.create(
                **user_verification_kwargs
            )

        See :meth:`~.UserVerificationHelper.create` for the required params.

        """
        self.sentry_token = models.SentryTokenHelper(self)
        """An instance of :class:`.SentryTokenHelper`.

        Provides an interface for interacting with :class:`.SentryToken`. For example to
        get a :class:`.SentryToken` with :attr:`id` of ``1`` you can do:

        .. code-block:: python

            sentry_token = credential_manager.sentry_token(1)
            print(sentry_token.id)

        To create a :class:`.SentryToken` do:

        .. code-block:: python

            sentry_token = credential_manager.sentry_token.create(**sentry_token_kwargs)

        See :meth:`~.SentryTokenHelper.create` for the required params.

        """
        self.database_credential = models.DatabaseCredentialHelper(self)
        """An instance of :class:`.DatabaseCredentialHelper`.

        Provides an interface for interacting with :class:`.DatabaseCredential`. For
        example to get a :class:`.DatabaseCredential` with :attr:`id` of ``1`` you can
        do:

        .. code-block:: python

            database_credential = credential_manager.database_credential(1)
            print(database_credential.id)

        To create a :class:`.DatabaseCredential` do:

        .. code-block:: python

            database_credential = credential_manager.database_credential.create(
                **database_credential_kwargs
            )

        See :meth:`~.DatabaseCredentialHelper.create` for the required params.

        """

    def users(self, batch_size=10, limit=None):
        """List Users.

        :param int batch_size: Number of Users to return in each batch (default: ``20``)
        :param int limit: Maximum number of Users to return

        :returns: A :class:`.Paginator` to iterate through the Users

        """
        return User(self).list_items(batch_size=batch_size, limit=limit)

    def bots(self, batch_size=20, limit=None, owner=None):
        """List Bots.

        :param int batch_size: Number of Bots to return in each batch (default: ``20``)
        :param int limit: Maximum number of Bots to return
        :param Union[int,str,User] owner: Return Bots that are owner by this user

        :returns: A :class:`.Paginator` to iterate through the Bots

        """
        return Bot(self).list_items(batch_size=batch_size, limit=limit, owner=owner)

    def reddit_apps(self, batch_size=20, limit=None, owner=None):
        """List RedditApps.

        :param int batch_size: Number of RedditApps to return in each batch (default:
            ``20``)
        :param int limit: Maximum number of RedditApps to return
        :param Union[int,str,User] owner: Return RedditApps that are owner by this user

        :returns: A :class:`.Paginator` to iterate through the Reddit Apps

        """
        return RedditApp(self).list_items(
            batch_size=batch_size, limit=limit, owner=owner
        )

    def refresh_tokens(self, batch_size=20, limit=None, owner=None):
        """List RefreshTokens.

        :param int batch_size: Number of RefreshTokens to return in each batch (default:
            ``20``)
        :param int limit: Maximum number of RefreshTokens to return
        :param Union[int,str,User] owner: Return RefreshTokens that are owned by this
            user

        :returns: A :class:`.Paginator` to iterate through the Refresh Tokens

        .. note::

            This is *not* the intended way to fetch refresh tokens. See:
            :meth:`~.RedditApp.reddit` for obtaining an authorized reddit instance.

        """
        return RefreshToken(self).list_items(
            batch_size=batch_size, limit=limit, owner=owner
        )

    def user_verifications(self, batch_size=20, limit=None, owner=None):
        """List UserVerifications.

        :param int batch_size: Number of UserVerifications to return in each batch
            (default: ``20``)
        :param int limit: Maximum number of UserVerifications to return
        :param Union[int,str,User] owner: Return UserVerifications that are owned by
            this user

        :returns: A :class:`.Paginator` to iterate through the UserVerifications.

        """
        return UserVerification(self).list_items(
            batch_size=batch_size, limit=limit, owner=owner
        )

    def sentry_tokens(self, batch_size=20, limit=None, owner=None):
        """List SentryTokens.

        :param int batch_size: Number of SentryTokens to return in each batch (default:
            ``20``)
        :param int limit: Maximum number of SentryTokens to return
        :param Union[int,str,User] owner: Return SentryTokens that are owned by this
            user

        :returns: A :class:`.Paginator` to iterate through the SentryTokens

        """
        return SentryToken(self).list_items(
            batch_size=batch_size, limit=limit, owner=owner
        )

    def database_credentials(self, batch_size=20, limit=None, owner=None):
        """List DatabaseCredentials.

        :param int batch_size: Number of DatabaseCredentials to return in each batch
            (default: ``20``)
        :param int limit: Maximum number of DatabaseCredentials to return
        :param Union[int,str,User] owner: Return DatabaseCredentials that are owned by
            this user

        :returns: A :class:`.Paginator` to iterate through the DatabaseCredentials

        """
        return DatabaseCredential(self).list_items(
            batch_size=batch_size, limit=limit, owner=owner
        )

    @cached_property
    def current_user(self) -> User:
        """Get the currently authenticated :class:`.User`."""
        if not self._current_user:
            self._current_user = self.get("/users/me")
        return self._current_user

    @cached_property
    def user_defaults(self):
        """Get the currently authenticated :class:`.User`'s default settings."""
        if not self._user_defaults:
            self._user_defaults = self.current_user.default_settings
        return self._user_defaults

    def get(self, path, params=None):
        """Return parsed objects returned from a GET request to ``path``.

        :param path: The path to fetch.
        :param params: The query parameters to add to the request (default: None).

        """
        return self._objectify_response(
            self._requestor.request(path, "GET", params=params)
        )

    def post(self, path, data):
        """Return parsed objects returned from a POST request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: None).

        """
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        return self._objectify_response(
            self._requestor.request(path, "POST", data=data, headers=headers)
        )

    def patch(self, path, data):
        """Return parsed objects returned from a PATCH request to ``path``.

        :param path: The path to fetch.
        :param data: Dictionary, bytes, or file-like object to send in the body of the
            request (default: None).

        """
        return self._objectify_response(
            self._requestor.request(path, "PATCH", json=data)
        )

    def delete(self, path):
        """Return parsed objects returned from a DELETE request to ``path``.

        :param path: The path to fetch.

        """
        self._requestor.request(path, "DELETE")
