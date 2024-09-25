"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Kyve(str, Enum):
    KYVE = 'kyve'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKyve:
    pool_ids: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pool_ids') }})
    r"""The IDs of the KYVE storage pool you want to archive. (Comma separated)"""
    start_ids: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_ids') }})
    r"""The start-id defines, from which bundle id the pipeline should start to extract the data. (Comma separated)"""
    SOURCE_TYPE: Final[Kyve] = dataclasses.field(default=Kyve.KYVE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    url_base: Optional[str] = dataclasses.field(default='https://api.kyve.network', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    r"""URL to the KYVE Chain API."""
    

