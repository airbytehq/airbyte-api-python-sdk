"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class Calendly(str, Enum):
    CALENDLY = 'calendly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCalendly:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Go to Integrations → API & Webhooks to obtain your bearer token. https://calendly.com/integrations/api_webhooks"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[Calendly] = dataclasses.field(default=Calendly.CALENDLY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
