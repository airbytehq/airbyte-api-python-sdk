"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Openfda(str, Enum):
    OPENFDA = 'openfda'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOpenfda:
    SOURCE_TYPE: Final[Openfda] = dataclasses.field(default=Openfda.OPENFDA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
