"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class N8n(str, Enum):
    N8N = 'n8n'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceN8n:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your API KEY. See <a href=\\"https://docs.n8n.io/api/authentication\\">here</a>"""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the n8n instance"""
    SOURCE_TYPE: Final[N8n] = dataclasses.field(default=N8n.N8N, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

