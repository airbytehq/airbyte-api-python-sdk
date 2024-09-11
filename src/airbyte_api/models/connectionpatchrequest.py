"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .airbyteapiconnectionschedule import AirbyteAPIConnectionSchedule
from .connectionstatusenum import ConnectionStatusEnum
from .geographyenumnodefault import GeographyEnumNoDefault
from .namespacedefinitionenumnodefault import NamespaceDefinitionEnumNoDefault
from .nonbreakingschemaupdatesbehaviorenumnodefault import NonBreakingSchemaUpdatesBehaviorEnumNoDefault
from .streamconfigurations import StreamConfigurations
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionPatchRequest:
    configurations: Optional[StreamConfigurations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configurations'), 'exclude': lambda f: f is None }})
    r"""A list of configured stream options for a connection."""
    data_residency: Optional[GeographyEnumNoDefault] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataResidency'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Optional name of the connection"""
    namespace_definition: Optional[NamespaceDefinitionEnumNoDefault] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Define the location where the data will be stored in the destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    r"""Used when namespaceDefinition is 'custom_format'. If blank then behaves like namespaceDefinition = 'destination'. If \\"${SOURCE_NAMESPACE}\\" then behaves like namespaceDefinition = 'source'."""
    non_breaking_schema_updates_behavior: Optional[NonBreakingSchemaUpdatesBehaviorEnumNoDefault] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonBreakingSchemaUpdatesBehavior'), 'exclude': lambda f: f is None }})
    r"""Set how Airbyte handles syncs when it detects a non-breaking schema change in the source"""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""Prefix that will be prepended to the name of each stream when it is written to the destination (ex. “airbyte_” causes “projects” => “airbyte_projects”)."""
    schedule: Optional[AirbyteAPIConnectionSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""schedule for when the the connection should run, per the schedule type"""
    status: Optional[ConnectionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

