"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Onfleet(str, Enum):
    ONFLEET = 'onfleet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOnfleet:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use for authenticating requests. You can create and manage your API keys in the API section of the Onfleet dashboard."""
    password: Optional[str] = dataclasses.field(default='x', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Placeholder for basic HTTP auth password - should be set to empty string"""
    SOURCE_TYPE: Final[Onfleet] = dataclasses.field(default=Onfleet.ONFLEET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
