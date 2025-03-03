"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Fullstory(str, Enum):
    FULLSTORY = 'fullstory'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFullstory:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key for the fullstory.com API."""
    uid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uid') }})
    r"""User ID for the fullstory.com API."""
    SOURCE_TYPE: Final[Fullstory] = dataclasses.field(default=Fullstory.FULLSTORY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

