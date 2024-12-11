"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class Freshbooks(str, Enum):
    FRESHBOOKS = 'freshbooks'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFreshbooks:
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    business_uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('business_uuid') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_refresh_token') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    redirect_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirect_uri') }})
    oauth_access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_access_token'), 'exclude': lambda f: f is None }})
    r"""The current access token. This field might be overridden by the connector based on the token refresh endpoint response."""
    oauth_token_expiry_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_token_expiry_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date the current access token expires in. This field might be overridden by the connector based on the token refresh endpoint response."""
    SOURCE_TYPE: Final[Freshbooks] = dataclasses.field(default=Freshbooks.FRESHBOOKS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

