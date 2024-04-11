"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final

class Aircall(str, Enum):
    AIRCALL = 'aircall'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAircall:
    api_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_id') }})
    r"""App ID found at settings https://dashboard.aircall.io/integrations/api-keys"""
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""App token found at settings (Ref- https://dashboard.aircall.io/integrations/api-keys)"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date time filter for incremental filter, Specify which date to extract from."""
    SOURCE_TYPE: Final[Aircall] = dataclasses.field(default=Aircall.AIRCALL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
