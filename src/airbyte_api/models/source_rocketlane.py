"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Rocketlane(str, Enum):
    ROCKETLANE = 'rocketlane'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRocketlane:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. Generate it from the API section in Settings of your Rocketlane account."""
    SOURCE_TYPE: Final[Rocketlane] = dataclasses.field(default=Rocketlane.ROCKETLANE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
