"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Xsolla(str, Enum):
    XSOLLA = 'xsolla'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceXsolla:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Go to Xsolla Dashboard and from company setting get the api_key"""
    project_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""You can find this parameter in your Publisher Account next to the name of the project . Example: 44056"""
    SOURCE_TYPE: Final[Xsolla] = dataclasses.field(default=Xsolla.XSOLLA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
