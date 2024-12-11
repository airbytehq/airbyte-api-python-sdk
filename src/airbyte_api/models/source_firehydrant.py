"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Firehydrant(str, Enum):
    FIREHYDRANT = 'firehydrant'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFirehydrant:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Bot token to use for authenticating with the FireHydrant API. You can find or create a bot token by logging into your organization and visiting the Bot users page at https://app.firehydrant.io/organizations/bots."""
    SOURCE_TYPE: Final[Firehydrant] = dataclasses.field(default=Firehydrant.FIREHYDRANT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

