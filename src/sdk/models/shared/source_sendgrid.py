"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class SourceSendgridSendgridEnum(str, Enum):
    SENDGRID = 'sendgrid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSendgrid:
    r"""The values required to configure the source."""
    
    apikey: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apikey') }})
    r"""API Key, use <a href=\\"https://app.sendgrid.com/settings/api_keys/\\">admin</a> to generate this key."""  
    source_type: SourceSendgridSendgridEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Start time in ISO8601 format. Any data before this time point will not be replicated."""  
    