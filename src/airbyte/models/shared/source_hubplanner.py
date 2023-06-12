"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceHubplannerHubplanner(str, Enum):
    HUBPLANNER = 'hubplanner'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceHubplanner:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Hubplanner API key. See https://github.com/hubplanner/API#authentication for more details."""
    source_type: SourceHubplannerHubplanner = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

