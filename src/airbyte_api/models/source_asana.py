"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Final, List, Optional, Union


class SourceAsanaSchemasCredentialsTitle(str, Enum):
    r"""PAT Credentials"""
    PAT_CREDENTIALS = 'PAT Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateWithPersonalAccessToken:
    personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_access_token') }})
    r"""Asana Personal Access Token (generate yours <a href=\\"https://app.asana.com/0/developer-console\\">here</a>)."""
    OPTION_TITLE: Final[Optional[SourceAsanaSchemasCredentialsTitle]] = dataclasses.field(default=SourceAsanaSchemasCredentialsTitle.PAT_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    r"""PAT Credentials"""
    



class SourceAsanaCredentialsTitle(str, Enum):
    r"""OAuth Credentials"""
    O_AUTH_CREDENTIALS = 'OAuth Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaAsanaOauth:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    OPTION_TITLE: Final[Optional[SourceAsanaCredentialsTitle]] = dataclasses.field(default=SourceAsanaCredentialsTitle.O_AUTH_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    r"""OAuth Credentials"""
    



class SourceAsanaAsana(str, Enum):
    ASANA = 'asana'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAsana:
    credentials: Optional[AuthenticationMechanism] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Github"""
    organization_export_ids: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_export_ids'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifiers for the organization exports"""
    SOURCE_TYPE: Final[Optional[SourceAsanaAsana]] = dataclasses.field(default=SourceAsanaAsana.ASANA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    


AuthenticationMechanism = Union[AuthenticateViaAsanaOauth, AuthenticateWithPersonalAccessToken]
