"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union

class SourceMixpanelSchemasOptionTitle(str, Enum):
    PROJECT_SECRET = 'Project Secret'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectSecret:
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_secret') }})
    r"""Mixpanel project secret. See the <a href=\\"https://developer.mixpanel.com/reference/project-secret#managing-a-projects-secret\\">docs</a> for more information on how to obtain this."""
    OPTION_TITLE: Final[Optional[SourceMixpanelSchemasOptionTitle]] = dataclasses.field(default=SourceMixpanelSchemasOptionTitle.PROJECT_SECRET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    


class SourceMixpanelOptionTitle(str, Enum):
    SERVICE_ACCOUNT = 'Service Account'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServiceAccount:
    project_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""Your project ID number. See the <a href=\\"https://help.mixpanel.com/hc/en-us/articles/115004490503-Project-Settings#project-id\\">docs</a> for more information on how to obtain this."""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Mixpanel Service Account Secret. See the <a href=\\"https://developer.mixpanel.com/reference/service-accounts\\">docs</a> for more information on how to obtain this."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Mixpanel Service Account Username. See the <a href=\\"https://developer.mixpanel.com/reference/service-accounts\\">docs</a> for more information on how to obtain this."""
    OPTION_TITLE: Final[Optional[SourceMixpanelOptionTitle]] = dataclasses.field(default=SourceMixpanelOptionTitle.SERVICE_ACCOUNT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    


class SourceMixpanelRegion(str, Enum):
    r"""The region of mixpanel domain instance either US or EU."""
    US = 'US'
    EU = 'EU'

class Mixpanel(str, Enum):
    MIXPANEL = 'mixpanel'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMixpanel:
    credentials: Union[ServiceAccount, ProjectSecret] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose how to authenticate to Mixpanel"""
    attribution_window: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution_window'), 'exclude': lambda f: f is None }})
    r"""A period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted. Default attribution window is 5 days. (This value should be non-negative integer)"""
    date_window_size: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_window_size'), 'exclude': lambda f: f is None }})
    r"""Defines window size in days, that used to slice through data. You can reduce it, if amount of data in each window is too big for your environment. (This value should be positive integer)"""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date in the format YYYY-MM-DD. Any data after this date will not be replicated. Left empty to always sync to most recent date"""
    project_timezone: Optional[str] = dataclasses.field(default='US/Pacific', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_timezone'), 'exclude': lambda f: f is None }})
    r"""Time zone in which integer date times are stored. The project timezone may be found in the project settings in the <a href=\\"https://help.mixpanel.com/hc/en-us/articles/115004547203-Manage-Timezones-for-Projects-in-Mixpanel\\">Mixpanel console</a>."""
    region: Optional[SourceMixpanelRegion] = dataclasses.field(default=SourceMixpanelRegion.US, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""The region of mixpanel domain instance either US or EU."""
    select_properties_by_default: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('select_properties_by_default'), 'exclude': lambda f: f is None }})
    r"""Setting this config parameter to TRUE ensures that new properties on events and engage records are captured. Otherwise new properties will be ignored."""
    SOURCE_TYPE: Final[Mixpanel] = dataclasses.field(default=Mixpanel.MIXPANEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date in the format YYYY-MM-DD. Any data before this date will not be replicated. If this option is not set, the connector will replicate data from up to one year ago by default."""
    
