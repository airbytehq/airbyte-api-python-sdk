"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Dremio(str, Enum):
    DREMIO = 'dremio'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDremio:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key that is generated when you authenticate to Dremio API"""
    base_url: Optional[str] = dataclasses.field(default='https://app.dremio.cloud', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url'), 'exclude': lambda f: f is None }})
    r"""URL of your Dremio instance"""
    SOURCE_TYPE: Final[Dremio] = dataclasses.field(default=Dremio.DREMIO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

