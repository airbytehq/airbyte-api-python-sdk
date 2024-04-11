"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Greenhouse(str, Enum):
    GREENHOUSE = 'greenhouse'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGreenhouse:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Greenhouse API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/greenhouse\\">docs</a> for more information on how to generate this key."""
    SOURCE_TYPE: Final[Greenhouse] = dataclasses.field(default=Greenhouse.GREENHOUSE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
