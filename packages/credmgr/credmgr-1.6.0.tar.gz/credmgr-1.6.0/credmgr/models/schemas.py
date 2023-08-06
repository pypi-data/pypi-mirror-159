"""Provide CredentialManager schemas."""
from marshmallow import Schema, post_load
from marshmallow.fields import (
    AwareDateTime,
    Boolean,
    Dict,
    Integer,
    List,
    Nested,
    Raw,
    String,
)

from . import (
    Bot,
    DatabaseCredential,
    RedditApp,
    RefreshToken,
    SentryToken,
    User,
    UserVerification,
)


class BaseSchema(Schema):
    """Base schema for all schemas."""

    _model = None
    credmgr = Raw(load_only=True)
    id = Integer()
    name = String(data_key="app_name")
    resource_type = String(load_only=True)

    def get_attribute(self, obj, attr, default):  # pragma: no cover
        """Get an attribute from an object. Used for dumping."""
        return super().get_attribute(obj, f"__dict__.{attr}", default)

    @post_load
    def objectify(self, data, **_):
        """Return an object if the schema's specified model."""
        return self._model(**data)


class BaseAppSchema(BaseSchema):
    """Base schema for all app schemas."""

    enabled = Boolean()
    owner_id = Integer()


class RedditAppSchema(BaseAppSchema):
    """Schema for :class:`.RedditApp`."""

    _model = RedditApp
    app_description = String(allow_none=True)
    app_type = String()
    client_id = String()
    client_secret = String(allow_none=True)
    redirect_uri = String()
    state = String()
    user_agent = String()


class DatabaseCredentialSchema(BaseAppSchema):
    """Schema for :class:`.DatabaseCredential`."""

    _model = DatabaseCredential
    database_username = String()
    database_host = String()
    database = String()
    database_flavor = String()
    database_port = Integer()
    database_password = String(allow_none=True)
    use_ssh = Boolean()
    ssh_host = String(allow_none=True)
    ssh_port = Integer(allow_none=True)
    ssh_username = String(allow_none=True)
    ssh_password = String(allow_none=True)
    use_ssh_key = Boolean()
    private_key = String(allow_none=True)
    private_key_passphrase = String(allow_none=True)


class SentryTokenSchema(BaseAppSchema):
    """Schema for :class:`.SentryToken`."""

    _model = SentryToken
    dsn = String()


class UserVerificationSchema(BaseAppSchema):
    """Schema for :class:`.UserVerification`."""

    _model = UserVerification
    extra_data = Dict(keys=String(), allow_none=True)
    reddit_app_id = Integer(allow_none=True)
    redditor = String(allow_none=True)
    user_id = String()


class RefreshTokenSchema(BaseSchema):
    """Schema for :class:`.RefreshToken`."""

    _model = RefreshToken
    issued_at = AwareDateTime()
    owner_id = Integer()
    reddit_app_id = Integer()
    redditor = String()
    refresh_token = String()
    revoked = Boolean()
    revoked_at = AwareDateTime(allow_none=True)
    scopes = List(String())


class BotSchema(BaseAppSchema):
    """Schema for :class:`.Bot`."""

    _model = Bot
    database_credential = Nested(DatabaseCredentialSchema, allow_none=True)
    reddit_app = Nested(RedditAppSchema, allow_none=True)
    sentry_token = Nested(SentryTokenSchema, allow_none=True)


class UserSchema(BaseSchema):
    """Schema for :class:`.User`."""

    _model = User
    bots = List(Nested(BotSchema))
    created = AwareDateTime()
    database_credentials = List(Nested(DatabaseCredentialSchema))
    default_settings = Dict()
    is_active = Boolean()
    is_admin = Boolean()
    is_regular_user = Boolean()
    reddit_apps = List(Nested(RedditAppSchema))
    reddit_username = String(allow_none=True)
    sentry_tokens = List(Nested(SentryTokenSchema))
    updated = AwareDateTime()
    username = String()
