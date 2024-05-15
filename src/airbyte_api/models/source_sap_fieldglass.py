"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class SapFieldglass(str, Enum):
    SAP_FIELDGLASS = 'sap-fieldglass'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSapFieldglass:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    SOURCE_TYPE: Final[SapFieldglass] = dataclasses.field(default=SapFieldglass.SAP_FIELDGLASS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

