"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceDriftSchemasCredentials(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Drift Access Token. See the <a href=\\"https://docs.airbyte.com/integrations/sources/drift\\">docs</a> for more information on how to generate this key."""
    CREDENTIALS: Final[Optional[SourceDriftSchemasCredentials]] = dataclasses.field(default=SourceDriftSchemasCredentials.ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    



class SourceDriftCredentials(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDriftOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Drift developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Drift developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to renew the expired Access Token."""
    CREDENTIALS: Final[Optional[SourceDriftCredentials]] = dataclasses.field(default=SourceDriftCredentials.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    



class SourceDriftDrift(str, Enum):
    DRIFT = 'drift'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDrift:
    credentials: Optional[SourceDriftAuthorizationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default='test@test.com', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email used as parameter for contacts stream"""
    SOURCE_TYPE: Final[SourceDriftDrift] = dataclasses.field(default=SourceDriftDrift.DRIFT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


SourceDriftAuthorizationMethod = Union[SourceDriftOAuth20, AccessToken]