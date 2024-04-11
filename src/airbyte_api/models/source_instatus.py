"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Instatus(str, Enum):
    INSTATUS = 'instatus'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceInstatus:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Instatus REST API key"""
    SOURCE_TYPE: Final[Instatus] = dataclasses.field(default=Instatus.INSTATUS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

