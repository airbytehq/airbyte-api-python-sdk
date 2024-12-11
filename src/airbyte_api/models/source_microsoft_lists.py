"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class MicrosoftLists(str, Enum):
    MICROSOFT_LISTS = 'microsoft-lists'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMicrosoftLists:
    application_id_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id_uri') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    site_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_id') }})
    tenant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_id') }})
    SOURCE_TYPE: Final[MicrosoftLists] = dataclasses.field(default=MicrosoftLists.MICROSOFT_LISTS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

