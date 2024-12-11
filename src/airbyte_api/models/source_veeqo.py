"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class Veeqo(str, Enum):
    VEEQO = 'veeqo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceVeeqo:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[Veeqo] = dataclasses.field(default=Veeqo.VEEQO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

