"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SourceRecreationRecreationEnum(str, Enum):
    RECREATION = 'recreation'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRecreation:
    r"""The values required to configure the source."""
    
    apikey: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apikey') }})
    r"""API Key"""  
    source_type: SourceRecreationRecreationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    query_campsites: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_campsites'), 'exclude': lambda f: f is None }})  
    