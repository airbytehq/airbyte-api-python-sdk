"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectionscheduleresponse import ConnectionScheduleResponse
from .connectionstatusenum import ConnectionStatusEnum
from .geographyenum import GeographyEnum
from .namespacedefinitionenum import NamespaceDefinitionEnum
from .nonbreakingschemaupdatesbehaviorenum import NonBreakingSchemaUpdatesBehaviorEnum
from .streamconfigurations import StreamConfigurations
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionResponse:
    r"""Provides details of a single connection."""
    configurations: StreamConfigurations = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configurations') }})
    r"""A list of configured stream options for a connection."""
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    created_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    schedule: ConnectionScheduleResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""schedule for when the the connection should run, per the schedule type"""
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    status: ConnectionStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    data_residency: Optional[GeographyEnum] = dataclasses.field(default=GeographyEnum.AUTO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataResidency'), 'exclude': lambda f: f is None }})
    namespace_definition: Optional[NamespaceDefinitionEnum] = dataclasses.field(default=NamespaceDefinitionEnum.DESTINATION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Define the location where the data will be stored in the destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    non_breaking_schema_updates_behavior: Optional[NonBreakingSchemaUpdatesBehaviorEnum] = dataclasses.field(default=NonBreakingSchemaUpdatesBehaviorEnum.IGNORE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonBreakingSchemaUpdatesBehavior'), 'exclude': lambda f: f is None }})
    r"""Set how Airbyte handles syncs when it detects a non-breaking schema change in the source"""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    

