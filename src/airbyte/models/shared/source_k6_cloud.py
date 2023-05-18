"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceK6CloudK6Cloud(str, Enum):
    K6_CLOUD = 'k6-cloud'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceK6Cloud:
    r"""The values required to configure the source."""
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Your API Token. See <a href=\\"https://k6.io/docs/cloud/integrations/token/\\">here</a>. The key is case sensitive."""
    source_type: SourceK6CloudK6Cloud = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    