"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Spotlercrm(str, Enum):
    SPOTLERCRM = 'spotlercrm'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSpotlercrm:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token to authenticate API requests. Generate it by logging into your CRM system, navigating to Settings / Integrations / API V4, and clicking 'generate new key'."""
    SOURCE_TYPE: Final[Spotlercrm] = dataclasses.field(default=Spotlercrm.SPOTLERCRM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
