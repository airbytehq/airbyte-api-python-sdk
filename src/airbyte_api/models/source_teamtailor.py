"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Teamtailor(str, Enum):
    TEAMTAILOR = 'teamtailor'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTeamtailor:
    api: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api') }})
    x_api_version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('x_api_version') }})
    r"""The version of the API"""
    SOURCE_TYPE: Final[Teamtailor] = dataclasses.field(default=Teamtailor.TEAMTAILOR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
