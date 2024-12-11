"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class Uservoice(str, Enum):
    USERVOICE = 'uservoice'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceUservoice:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    SOURCE_TYPE: Final[Uservoice] = dataclasses.field(default=Uservoice.USERVOICE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

