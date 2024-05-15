"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional, Union


class SourceAirtableAuthMethod(str, Enum):
    API_KEY = 'api_key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PersonalAccessToken:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The Personal Access Token for the Airtable account. See the <a href=\\"https://airtable.com/developers/web/guides/personal-access-tokens\\">Support Guide</a> for more information on how to obtain this token."""
    AUTH_METHOD: Final[Optional[SourceAirtableAuthMethod]] = dataclasses.field(default=SourceAirtableAuthMethod.API_KEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    



class SourceAirtableSchemasAuthMethod(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAirtableOAuth20:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of the Airtable developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret the Airtable developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access token."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests."""
    AUTH_METHOD: Final[Optional[SourceAirtableSchemasAuthMethod]] = dataclasses.field(default=SourceAirtableSchemasAuthMethod.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    token_expiry_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date-time when the access token should be refreshed."""
    



class SourceAirtableAirtable(str, Enum):
    AIRTABLE = 'airtable'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAirtable:
    credentials: Optional[Union[SourceAirtableOAuth20, PersonalAccessToken]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Optional[SourceAirtableAirtable]] = dataclasses.field(default=SourceAirtableAirtable.AIRTABLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    

