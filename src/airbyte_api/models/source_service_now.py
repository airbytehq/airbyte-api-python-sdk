"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class ServiceNow(str, Enum):
    SERVICE_NOW = 'service-now'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceServiceNow:
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[ServiceNow] = dataclasses.field(default=ServiceNow.SERVICE_NOW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

