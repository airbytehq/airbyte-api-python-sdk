"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class PunkAPI(str, Enum):
    PUNK_API = 'punk-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePunkAPI:
    brewed_after: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brewed_after') }})
    r"""To extract specific data with Unique ID"""
    brewed_before: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brewed_before') }})
    r"""To extract specific data with Unique ID"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""To extract specific data with Unique ID"""
    SOURCE_TYPE: Final[PunkAPI] = dataclasses.field(default=PunkAPI.PUNK_API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

