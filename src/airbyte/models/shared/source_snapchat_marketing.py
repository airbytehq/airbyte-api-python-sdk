"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSnapchatMarketingSnapchatMarketingEnum(str, Enum):
    SNAPCHAT_MARKETING = 'snapchat-marketing'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSnapchatMarketing:
    r"""The values required to configure the source."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Snapchat developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Snapchat developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to renew the expired Access Token."""
    source_type: SourceSnapchatMarketingSnapchatMarketingEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date in the format 2017-01-25. Any data after this date will not be replicated."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date in the format 2022-01-01. Any data before this date will not be replicated."""
    