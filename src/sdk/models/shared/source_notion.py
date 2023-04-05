"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class SourceNotionCredentialsAccessTokenAuthTypeEnum(str, Enum):
    TOKEN = 'token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotionCredentialsAccessToken:
    r"""Pick an authentication method."""
    
    auth_type: SourceNotionCredentialsAccessTokenAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})  
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Notion API access token, see the <a href=\\"https://developers.notion.com/docs/authorization\\">docs</a> for more information on how to obtain this token."""  
    
class SourceNotionCredentialsOAuth20AuthTypeEnum(str, Enum):
    O_AUTH2_0 = 'OAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotionCredentialsOAuth20:
    r"""Pick an authentication method."""
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token is a token you received by complete the OauthWebFlow of Notion."""  
    auth_type: SourceNotionCredentialsOAuth20AuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})  
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The ClientID of your Notion integration."""  
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The ClientSecret of your Notion integration."""  
    
class SourceNotionNotionEnum(str, Enum):
    NOTION = 'notion'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNotion:
    r"""The values required to configure the source."""
    
    source_type: SourceNotionNotionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00.000Z. Any data before this date will not be replicated."""  
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Pick an authentication method."""  
    