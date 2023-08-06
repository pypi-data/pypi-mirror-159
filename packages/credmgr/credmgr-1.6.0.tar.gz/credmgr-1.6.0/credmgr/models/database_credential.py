"""Provide the DatabaseCredential class."""
from ..deprecation_decorator import warn_camel_case
from ..mixins import BaseApp
from .utils import _resolve_user


class DatabaseCredential(BaseApp):
    """A class for DatabaseCredential instances."""

    _credmgr_callable = "database_credential"
    _editable_attrs = BaseApp._editable_attrs + [
        "database",
        "database_flavor",
        "database_host",
        "database_password",
        "database_port",
        "database_username",
        "private_key",
        "private_key_passphrase",
        "ssh_host",
        "ssh_password",
        "ssh_port",
        "ssh_username",
        "use_ssh",
        "use_ssh_key",
    ]
    _path = "/database_credentials"

    @classmethod
    @property
    def schema(cls):
        """Return the schema for this model."""
        if cls._schema is None:
            from .schemas import DatabaseCredentialSchema

            cls._schema = DatabaseCredentialSchema()
        return cls._schema

    def __init__(self, credmgr, **kwargs):
        """Initialize a Database Credential instance.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param id: The ID of the Database Credential.
        :param str name: Name of the Database Credential.
        :param str database_flavor: Type of database.
        :param str database: Working database to use.
        :param str database_host: Database server address.
        :param int database_port: Port the database server listens on.
        :param str database_username: Username used to connect and authenticate the
            database.
        :param str database_password: Password used to connect and authenticate the
            database.
        :param bool use_ssh: Determines if the database will be connected to through a
            tunnel.
        :param str ssh_host: The address of the server that the SSH tunnel will connect
            to.
        :param str ssh_port: The port the SSH tunnel will use.
        :param str ssh_username: Username for the SSH tunnel.
        :param str ssh_password: Password for the SSH tunnel.
        :param bool use_ssh_key: Determines if the SSH tunnel will use private key
            authentication.
        :param str private_key: SSH private key. Note: No validation will be performed.
        :param str private_key_passphrase: Passphrase for the SSH key.
        :param owner_id: ID of the `.User` that owns this Database Credential.

        """
        super().__init__(credmgr, **kwargs)

    @staticmethod
    @_resolve_user
    @warn_camel_case(
        "databaseFlavor",
        "database",
        "databaseHost",
        "databasePort",
        "databaseUsername",
        "databasePassword",
        "useSsh",
        "sshHost",
        "sshPort",
        "sshUsername",
        "sshPassword",
        "useSshKey",
        "privateKey",
        "privateKeyPassphrase",
    )
    def _create(
        _credmgr,
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
    ):
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
        :param Union[User,int,str] owner: Owner of the Database Credential. Requires
            Admin to create for other users.

        :returns: DatabaseCredential

        """
        data = {}
        if database_flavor:
            data["database_flavor"] = database_flavor
        if database:
            data["database"] = database
        if database_host:
            data["database_host"] = database_host
        if database_port:
            data["database_port"] = database_port
        if database_username:
            data["database_username"] = database_username
        if database_password:
            data["database_password"] = database_password
        if use_ssh:
            data["use_ssh"] = use_ssh
        if ssh_host:
            data["ssh_host"] = ssh_host
        if ssh_port:
            data["ssh_port"] = ssh_port
        if ssh_username:
            data["ssh_username"] = ssh_username
        if ssh_password:
            data["ssh_password"] = ssh_password
        if use_ssh_key:
            data["use_ssh_key"] = use_ssh_key
        if private_key:
            data["private_key"] = private_key
        if private_key_passphrase:
            data["private_key_passphrase"] = private_key_passphrase
        if enabled:
            data["enabled"] = enabled
        if owner:
            data["owner_id"] = owner
        return _credmgr.post("/database_credentials", data={"app_name": name, **data})
