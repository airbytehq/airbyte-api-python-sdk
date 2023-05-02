"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceLemlistLemlistEnum(str, Enum):
    LEMLIST = 'lemlist'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLemlist:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Lemlist API key."""
    source_type: SourceLemlistLemlistEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    