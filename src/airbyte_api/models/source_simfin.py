"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Simfin(str, Enum):
    SIMFIN = 'simfin'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSimfin:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    SOURCE_TYPE: Final[Simfin] = dataclasses.field(default=Simfin.SIMFIN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
