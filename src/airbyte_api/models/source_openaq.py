"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Final, List


class Openaq(str, Enum):
    OPENAQ = 'openaq'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOpenaq:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    country_ids: List[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_ids') }})
    r"""The list of IDs of countries (comma separated) you need the data for, check more: https://docs.openaq.org/resources/countries"""
    SOURCE_TYPE: Final[Openaq] = dataclasses.field(default=Openaq.OPENAQ, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
