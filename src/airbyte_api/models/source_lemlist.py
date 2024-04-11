"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Lemlist(str, Enum):
    LEMLIST = 'lemlist'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLemlist:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Lemlist API key,"""
    SOURCE_TYPE: Final[Lemlist] = dataclasses.field(default=Lemlist.LEMLIST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

