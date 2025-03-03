"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TagResponse:
    r"""Provides details of a single tag."""
    color: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color') }})
    r"""A hexadecimal color value"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    tag_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tagId') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    

