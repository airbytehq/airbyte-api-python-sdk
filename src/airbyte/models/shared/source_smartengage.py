"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceSmartengageSmartengage(str, Enum):
    SMARTENGAGE = 'smartengage'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSmartengage:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    source_type: SourceSmartengageSmartengage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

