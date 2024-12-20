"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Chargify(str, Enum):
    CHARGIFY = 'chargify'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceChargify:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Maxio Advanced Billing/Chargify API Key."""
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""Chargify domain. Normally this domain follows the following format"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Chargify] = dataclasses.field(default=Chargify.CHARGIFY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

