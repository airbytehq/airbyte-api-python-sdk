"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Todoist(str, Enum):
    TODOIST = 'todoist'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTodoist:
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""API authorization bearer token for authenticating the API"""
    SOURCE_TYPE: Final[Todoist] = dataclasses.field(default=Todoist.TODOIST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
