"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class LightspeedRetail(str, Enum):
    LIGHTSPEED_RETAIL = 'lightspeed-retail'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLightspeedRetail:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key or access token"""
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    r"""The subdomain for the retailer, e.g., 'example' in 'example.retail.lightspeed.app'."""
    SOURCE_TYPE: Final[LightspeedRetail] = dataclasses.field(default=LightspeedRetail.LIGHTSPEED_RETAIL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
