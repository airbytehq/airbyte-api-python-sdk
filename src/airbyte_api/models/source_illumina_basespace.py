"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class IlluminaBasespace(str, Enum):
    ILLUMINA_BASESPACE = 'illumina-basespace'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIlluminaBasespace:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""BaseSpace access token. Instructions for obtaining your access token can be found in the BaseSpace Developer Documentation."""
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""Domain name of the BaseSpace instance (e.g., euw2.sh.basespace.illumina.com)"""
    SOURCE_TYPE: Final[IlluminaBasespace] = dataclasses.field(default=IlluminaBasespace.ILLUMINA_BASESPACE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    user: Optional[str] = dataclasses.field(default='current', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""Providing a user ID restricts the returned data to what that user can access. If you use the default ('current'), all data accessible to the user associated with the API key will be shown."""
    
