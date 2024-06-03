"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .permissiontype import PermissionType
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PermissionUpdateRequest:
    permission_type: PermissionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permissionType') }})
    r"""Describes what actions/endpoints the permission entitles to"""
    
