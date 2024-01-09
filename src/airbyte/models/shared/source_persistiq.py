"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Persistiq(str, Enum):
    PERSISTIQ = 'persistiq'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePersistiq:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""PersistIq API Key. See the <a href=\\"https://apidocs.persistiq.com/#authentication\\">docs</a> for more information on where to find that key."""
    SOURCE_TYPE: Final[Persistiq] = dataclasses.field(default=Persistiq.PERSISTIQ, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

