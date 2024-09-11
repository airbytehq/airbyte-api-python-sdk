"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class Firebolt(str, Enum):
    FIREBOLT = 'firebolt'


class DestinationFireboltSchemasMethod(str, Enum):
    S3 = 'S3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalTableViaS3:
    aws_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_id') }})
    r"""AWS access key granting read and write access to S3."""
    aws_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_secret') }})
    r"""Corresponding secret part of the AWS Key"""
    s3_bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket') }})
    r"""The name of the S3 bucket."""
    s3_region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_region') }})
    r"""Region name of the S3 bucket."""
    METHOD: Final[DestinationFireboltSchemasMethod] = dataclasses.field(default=DestinationFireboltSchemasMethod.S3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    



class DestinationFireboltMethod(str, Enum):
    SQL = 'SQL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SQLInserts:
    METHOD: Final[DestinationFireboltMethod] = dataclasses.field(default=DestinationFireboltMethod.SQL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationFirebolt:
    account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""Firebolt account to login."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Firebolt service account ID."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Firebolt secret, corresponding to the service account ID."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database to connect to."""
    engine: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('engine') }})
    r"""Engine name to connect to."""
    DESTINATION_TYPE: Final[Firebolt] = dataclasses.field(default=Firebolt.FIREBOLT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host'), 'exclude': lambda f: f is None }})
    r"""The host name of your Firebolt database."""
    loading_method: Optional[DestinationFireboltLoadingMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loading_method'), 'exclude': lambda f: f is None }})
    r"""Loading method used to select the way data will be uploaded to Firebolt"""
    


DestinationFireboltLoadingMethod = Union[SQLInserts, ExternalTableViaS3]
