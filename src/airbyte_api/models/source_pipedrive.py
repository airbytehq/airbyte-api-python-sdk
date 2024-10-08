"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Pipedrive(str, Enum):
    PIPEDRIVE = 'pipedrive'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePipedrive:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""The Pipedrive API Token."""
    replication_start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_start_date') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated. When specified and not None, then stream will behave as incremental"""
    SOURCE_TYPE: Final[Pipedrive] = dataclasses.field(default=Pipedrive.PIPEDRIVE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

