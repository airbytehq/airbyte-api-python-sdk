"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class APIEndpointPrefix(str, Enum):
    API = 'api'
    API_EU = 'api.eu'


class Sparkpost(str, Enum):
    SPARKPOST = 'sparkpost'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSparkpost:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    api_prefix: Optional[APIEndpointPrefix] = dataclasses.field(default=APIEndpointPrefix.API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_prefix'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Sparkpost] = dataclasses.field(default=Sparkpost.SPARKPOST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
