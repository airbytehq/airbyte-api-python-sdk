"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Deputy(str, Enum):
    DEPUTY = 'deputy'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDeputy:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    r"""The base url for your deputy account to make API requests"""
    SOURCE_TYPE: Final[Deputy] = dataclasses.field(default=Deputy.DEPUTY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

