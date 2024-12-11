"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Copper(str, Enum):
    COPPER = 'copper'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCopper:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Copper API key"""
    user_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_email') }})
    r"""user email used to login in to Copper"""
    SOURCE_TYPE: Final[Copper] = dataclasses.field(default=Copper.COPPER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

