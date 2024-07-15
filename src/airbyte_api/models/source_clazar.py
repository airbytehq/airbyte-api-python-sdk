"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Clazar(str, Enum):
    CLAZAR = 'clazar'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceClazar:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    SOURCE_TYPE: Final[Clazar] = dataclasses.field(default=Clazar.CLAZAR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

