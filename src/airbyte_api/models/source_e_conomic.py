"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class EConomic(str, Enum):
    E_CONOMIC = 'e-conomic'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceEConomic:
    agreement_grant_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agreement_grant_token') }})
    r"""Token that identifies the grant issued by an agreement, allowing your app to access data. Obtain it from your e-conomic account settings."""
    app_secret_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_secret_token') }})
    r"""Your private token that identifies your app. Find it in your e-conomic account settings."""
    SOURCE_TYPE: Final[EConomic] = dataclasses.field(default=EConomic.E_CONOMIC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

