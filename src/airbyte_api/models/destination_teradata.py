"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class Teradata(str, Enum):
    TERADATA = 'teradata'


class DestinationTeradataSchemasSSLModeSSLModes6Mode(str, Enum):
    VERIFY_FULL = 'verify-full'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataVerifyFull:
    r"""Verify-full SSL mode."""
    ssl_ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_ca_certificate') }})
    r"""Specifies the file name of a PEM file that contains Certificate Authority (CA) certificates for use with SSLMODE=verify-full.
     See more information - <a href=\"https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#URL_SSLCA\"> in the docs</a>.
    """
    MODE: Final[Optional[DestinationTeradataSchemasSSLModeSSLModes6Mode]] = dataclasses.field(default=DestinationTeradataSchemasSSLModeSSLModes6Mode.VERIFY_FULL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationTeradataSchemasSSLModeSSLModes5Mode(str, Enum):
    VERIFY_CA = 'verify-ca'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataVerifyCa:
    r"""Verify-ca SSL mode."""
    ssl_ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_ca_certificate') }})
    r"""Specifies the file name of a PEM file that contains Certificate Authority (CA) certificates for use with SSLMODE=verify-ca.
     See more information - <a href=\"https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#URL_SSLCA\"> in the docs</a>.
    """
    MODE: Final[Optional[DestinationTeradataSchemasSSLModeSSLModes5Mode]] = dataclasses.field(default=DestinationTeradataSchemasSSLModeSSLModes5Mode.VERIFY_CA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationTeradataSchemasSSLModeSSLModesMode(str, Enum):
    REQUIRE = 'require'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataRequire:
    r"""Require SSL mode."""
    MODE: Final[Optional[DestinationTeradataSchemasSSLModeSSLModesMode]] = dataclasses.field(default=DestinationTeradataSchemasSSLModeSSLModesMode.REQUIRE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationTeradataSchemasSslModeMode(str, Enum):
    PREFER = 'prefer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataPrefer:
    r"""Prefer SSL mode."""
    MODE: Final[Optional[DestinationTeradataSchemasSslModeMode]] = dataclasses.field(default=DestinationTeradataSchemasSslModeMode.PREFER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationTeradataSchemasMode(str, Enum):
    ALLOW = 'allow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataAllow:
    r"""Allow SSL mode."""
    MODE: Final[Optional[DestinationTeradataSchemasMode]] = dataclasses.field(default=DestinationTeradataSchemasMode.ALLOW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationTeradataMode(str, Enum):
    DISABLE = 'disable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradataDisable:
    r"""Disable SSL."""
    MODE: Final[Optional[DestinationTeradataMode]] = dataclasses.field(default=DestinationTeradataMode.DISABLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTeradata:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    DESTINATION_TYPE: Final[Teradata] = dataclasses.field(default=Teradata.TERADATA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    schema: Optional[str] = dataclasses.field(default='airbyte_td', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    ssl: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl'), 'exclude': lambda f: f is None }})
    r"""Encrypt data using SSL. When activating SSL, please select one of the connection modes."""
    ssl_mode: Optional[DestinationTeradataSSLModes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    r"""SSL connection modes.
     <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
     <b>allow</b> - Chose this mode to enable encryption only when required by the destination database
     <b>prefer</b> - Chose this mode to allow unencrypted connection only if the destination database does not support encryption
     <b>require</b> - Chose this mode to always require encryption. If the destination database server does not support encryption, connection will fail
      <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the destination database server has a valid SSL certificate
      <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the destination database server
     See more information - <a href=\"https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#URL_SSLMODE\"> in the docs</a>.
    """
    


DestinationTeradataSSLModes = Union[DestinationTeradataDisable, DestinationTeradataAllow, DestinationTeradataPrefer, DestinationTeradataRequire, DestinationTeradataVerifyCa, DestinationTeradataVerifyFull]
