"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional


class SourceDatadogDataSource(str, Enum):
    r"""A data source that is powered by the platform."""
    METRICS = 'metrics'
    CLOUD_COST = 'cloud_cost'
    LOGS = 'logs'
    RUM = 'rum'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Queries:
    data_source: SourceDatadogDataSource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source') }})
    r"""A data source that is powered by the platform."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The variable name for use in queries."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""A classic query string."""
    



class Site(str, Enum):
    r"""The site where Datadog data resides in."""
    DATADOGHQ_COM = 'datadoghq.com'
    US3_DATADOGHQ_COM = 'us3.datadoghq.com'
    US5_DATADOGHQ_COM = 'us5.datadoghq.com'
    DATADOGHQ_EU = 'datadoghq.eu'
    DDOG_GOV_COM = 'ddog-gov.com'


class Datadog(str, Enum):
    DATADOG = 'datadog'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDatadog:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Datadog API key"""
    application_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_key') }})
    r"""Datadog application key"""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Data after this date will  not be replicated. An empty value will represent the current datetime for each  execution. This just applies to Incremental syncs."""
    max_records_per_request: Optional[int] = dataclasses.field(default=5000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_records_per_request'), 'exclude': lambda f: f is None }})
    r"""Maximum number of records to collect per request."""
    queries: Optional[List[Queries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queries'), 'exclude': lambda f: f is None }})
    r"""List of queries to be run and used as inputs."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""The search query. This just applies to Incremental syncs. If empty, it'll collect all logs."""
    site: Optional[Site] = dataclasses.field(default=Site.DATADOGHQ_COM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site'), 'exclude': lambda f: f is None }})
    r"""The site where Datadog data resides in."""
    SOURCE_TYPE: Final[Datadog] = dataclasses.field(default=Datadog.DATADOG, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated. This just applies to Incremental syncs."""
    
