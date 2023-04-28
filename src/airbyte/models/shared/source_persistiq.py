"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourcePersistiqPersistiqEnum(str, Enum):
    PERSISTIQ = 'persistiq'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePersistiq:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})

    r"""PersistIq API Key. See the <a href=\\"https://apidocs.persistiq.com/#authentication\\">docs</a> for more information on where to find that key."""
    source_type: SourcePersistiqPersistiqEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})

    