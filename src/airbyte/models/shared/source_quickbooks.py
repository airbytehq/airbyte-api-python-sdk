"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceQuickbooksCredentialsOAuth20AuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceQuickbooksCredentialsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access token fot making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Identifies which app is making the request. Obtain this value from the Keys tab on the app profile via My Apps on the developer site. There are two versions of this key: development and production."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Obtain this value from the Keys tab on the app profile via My Apps on the developer site. There are two versions of this key: development and production."""
    realm_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('realm_id') }})
    r"""Labeled Company ID. The Make API Calls panel is populated with the realm id and the current access token."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""A token used when refreshing the access token."""
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date-time when the access token should be refreshed."""
    auth_type: Optional[SourceQuickbooksCredentialsOAuth20AuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceQuickbooksQuickbooks(str, Enum):
    QUICKBOOKS = 'quickbooks'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceQuickbooks:
    r"""The values required to configure the source."""
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    sandbox: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sandbox') }})
    r"""Determines whether to use the sandbox or production environment."""
    source_type: SourceQuickbooksQuickbooks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The default value to use if no bookmark exists for an endpoint (rfc3339 date string). E.g, 2021-03-20T00:00:00Z. Any data before this date will not be replicated."""
    

