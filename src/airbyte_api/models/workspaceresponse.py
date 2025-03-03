"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .geographyenum import GeographyEnum
from .notificationsconfig import NotificationsConfig
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceResponse:
    r"""Provides details of a single workspace."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    notifications: NotificationsConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notifications') }})
    r"""Configures workspace notifications."""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    data_residency: Optional[GeographyEnum] = dataclasses.field(default=GeographyEnum.AUTO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataResidency'), 'exclude': lambda f: f is None }})
    

