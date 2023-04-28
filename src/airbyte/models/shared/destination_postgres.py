"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationPostgresPostgresEnum(str, Enum):
    POSTGRES = 'postgres'

class DestinationPostgresSslModeVerifyFullModeEnum(str, Enum):
    VERIFY_FULL = 'verify-full'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeVerifyFull:
    r"""Verify-full SSL mode."""
    
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})

    r"""CA certificate"""
    client_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate') }})

    r"""Client certificate"""
    client_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key') }})

    r"""Client key"""
    mode: DestinationPostgresSslModeVerifyFullModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})

    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    
class DestinationPostgresSslModeVerifyCaModeEnum(str, Enum):
    VERIFY_CA = 'verify-ca'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeVerifyCa:
    r"""Verify-ca SSL mode."""
    
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})

    r"""CA certificate"""
    mode: DestinationPostgresSslModeVerifyCaModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})

    r"""Password for keystorage. This field is optional. If you do not add it - the password will be generated automatically."""
    
class DestinationPostgresSslModeRequireModeEnum(str, Enum):
    REQUIRE = 'require'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeRequire:
    r"""Require SSL mode."""
    
    mode: DestinationPostgresSslModeRequireModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    
class DestinationPostgresSslModePreferModeEnum(str, Enum):
    PREFER = 'prefer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModePrefer:
    r"""Prefer SSL mode."""
    
    mode: DestinationPostgresSslModePreferModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    
class DestinationPostgresSslModeAllowModeEnum(str, Enum):
    ALLOW = 'allow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeAllow:
    r"""Allow SSL mode."""
    
    mode: DestinationPostgresSslModeAllowModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    
class DestinationPostgresSslModeDisableModeEnum(str, Enum):
    DISABLE = 'disable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresSslModeDisable:
    r"""Disable SSL."""
    
    mode: DestinationPostgresSslModeDisableModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    
class DestinationPostgresTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})

    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationPostgresTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})

    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})

    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})

    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})

    r"""OS-level password for logging into the jump server host"""
    
class DestinationPostgresTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})

    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})

    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationPostgresTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})

    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})

    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})

    r"""OS-level username for logging into the jump server host."""
    
class DestinationPostgresTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgresTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_method: DestinationPostgresTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})

    r"""No ssh tunnel needed to connect to database"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPostgres:
    r"""The values required to configure the destination."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})

    r"""Name of the database."""
    destination_type: DestinationPostgresPostgresEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})

    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})

    r"""Hostname of the database."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})

    r"""Port of the database."""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})

    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})

    r"""Username to use to access the database."""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})

    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})

    r"""Password associated with the username."""
    ssl_mode: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})

    r"""SSL connection modes.
     <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
     <b>allow</b> - Chose this mode to enable encryption only when required by the source database
     <b>prefer</b> - Chose this mode to allow unencrypted connection only if the source database does not support encryption
     <b>require</b> - Chose this mode to always require encryption. If the source database server does not support encryption, connection will fail
      <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the source database server has a valid SSL certificate
      <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the source database server
     See more information - <a href=\"https://jdbc.postgresql.org/documentation/head/ssl-client.html\"> in the docs</a>.
    """
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})

    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    