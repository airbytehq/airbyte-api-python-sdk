"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connectionscheduleresponse as shared_connectionscheduleresponse
from ..shared import connectionstatusenum as shared_connectionstatusenum
from ..shared import geographyenum as shared_geographyenum
from ..shared import namespacedefinitionenum as shared_namespacedefinitionenum
from ..shared import nonbreakingschemaupdatesbehaviorenum as shared_nonbreakingschemaupdatesbehaviorenum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionResponse:
    r"""Provides details of a single connection."""
    
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId') }})
    data_residency: shared_geographyenum.GeographyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataResidency') }})
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    schedule: shared_connectionscheduleresponse.ConnectionScheduleResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""schedule for when the the connection should run, per the schedule type"""
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    status: shared_connectionstatusenum.ConnectionStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    namespace_definition: Optional[shared_namespacedefinitionenum.NamespaceDefinitionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Define the location where the data will be stored in the destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    non_breaking_schema_updates_behavior: Optional[shared_nonbreakingschemaupdatesbehaviorenum.NonBreakingSchemaUpdatesBehaviorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonBreakingSchemaUpdatesBehavior'), 'exclude': lambda f: f is None }})
    r"""Set how Airbyte handles syncs when it detects a non-breaking schema change in the source"""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    