"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationRocksetRocksetEnum(str, Enum):
    ROCKSET = 'rockset'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRockset:
    r"""The values required to configure the destination."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})

    r"""Rockset api key"""
    destination_type: DestinationRocksetRocksetEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})

    workspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace') }})

    r"""The Rockset workspace in which collections will be created + written to."""
    api_server: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_server'), 'exclude': lambda f: f is None }})

    r"""Rockset api URL"""
    