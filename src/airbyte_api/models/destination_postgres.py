"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class Postgres(str, Enum):
    POSTGRES = 'postgres'


class DestinationPostgresSchemasSSLModeSSLModes6Mode(str, Enum):
    VERIFY_FULL = 'verify-full'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VerifyFull:
    r"""Verify-full SSL mode."""
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    client_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate') }})
    r"""Client certificate"""
    client_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key') }})
    r"""Client key"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    MODE: Final[Optional[DestinationPostgresSchemasSSLModeSSLModes6Mode]] = dataclasses.field(default=DestinationPostgresSchemasSSLModeSSLModes6Mode.VERIFY_FULL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresSchemasSSLModeSSLModesMode(str, Enum):
    VERIFY_CA = 'verify-ca'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VerifyCa:
    r"""Verify-ca SSL mode."""
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    MODE: Final[Optional[DestinationPostgresSchemasSSLModeSSLModesMode]] = dataclasses.field(default=DestinationPostgresSchemasSSLModeSSLModesMode.VERIFY_CA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresSchemasSslModeMode(str, Enum):
    REQUIRE = 'require'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Require:
    r"""Require SSL mode."""
    MODE: Final[Optional[DestinationPostgresSchemasSslModeMode]] = dataclasses.field(default=DestinationPostgresSchemasSslModeMode.REQUIRE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresSchemasMode(str, Enum):
    PREFER = 'prefer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Prefer:
    r"""Prefer SSL mode."""
    MODE: Final[Optional[DestinationPostgresSchemasMode]] = dataclasses.field(default=DestinationPostgresSchemasMode.PREFER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresMode(str, Enum):
    ALLOW = 'allow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Allow:
    r"""Allow SSL mode."""
    MODE: Final[Optional[DestinationPostgresMode]] = dataclasses.field(default=DestinationPostgresMode.ALLOW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresSchemasSSLModeSSLModes1Mode(str, Enum):
    DISABLE = 'disable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Disable:
    r"""Disable SSL."""
    MODE: Final[Optional[DestinationPostgresSchemasSSLModeSSLModes1Mode]] = dataclasses.field(default=DestinationPostgresSchemasSSLModeSSLModes1Mode.DISABLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationPostgresSchemasTunnelMethodTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresPasswordAuthentication:
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[DestinationPostgresSchemasTunnelMethodTunnelMethod] = dataclasses.field(default=DestinationPostgresSchemasTunnelMethodTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



class DestinationPostgresSchemasTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSSHKeyAuthentication:
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[DestinationPostgresSchemasTunnelMethod] = dataclasses.field(default=DestinationPostgresSchemasTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



class DestinationPostgresTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresNoTunnel:
    TUNNEL_METHOD: Final[DestinationPostgresTunnelMethod] = dataclasses.field(default=DestinationPostgresTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgres:
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    DESTINATION_TYPE: Final[Postgres] = dataclasses.field(default=Postgres.POSTGRES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    disable_type_dedupe: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disable_type_dedupe'), 'exclude': lambda f: f is None }})
    r"""Disable Writing Final Tables. WARNING! The data format in _airbyte_data is likely stable but there are no guarantees that other metadata columns will remain the same in future versions"""
    drop_cascade: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('drop_cascade'), 'exclude': lambda f: f is None }})
    r"""Drop tables with CASCADE. WARNING! This will delete all data in all dependent objects (views, etc.). Use with caution. This option is intended for usecases which can easily rebuild the dependent objects."""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    port: Optional[int] = dataclasses.field(default=5432, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""
    raw_data_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw_data_schema'), 'exclude': lambda f: f is None }})
    r"""The schema to write raw tables into"""
    schema: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    ssl: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl'), 'exclude': lambda f: f is None }})
    r"""Encrypt data using SSL. When activating SSL, please select one of the connection modes."""
    ssl_mode: Optional[SSLModes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    r"""SSL connection modes.
     <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
     <b>allow</b> - Chose this mode to enable encryption only when required by the source database
     <b>prefer</b> - Chose this mode to allow unencrypted connection only if the source database does not support encryption
     <b>require</b> - Chose this mode to always require encryption. If the source database server does not support encryption, connection will fail
      <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the source database server has a valid SSL certificate
      <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the source database server
     See more information - <a href=\"https://jdbc.postgresql.org/documentation/head/ssl-client.html\"> in the docs</a>.
    """
    tunnel_method: Optional[DestinationPostgresSSHTunnelMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    


SSLModes = Union[Disable, Allow, Prefer, Require, VerifyCa, VerifyFull]

DestinationPostgresSSHTunnelMethod = Union[DestinationPostgresNoTunnel, DestinationPostgresSSHKeyAuthentication, DestinationPostgresPasswordAuthentication]
