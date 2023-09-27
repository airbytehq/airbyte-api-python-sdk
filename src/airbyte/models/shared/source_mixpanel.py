"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Optional, Union

class SourceMixpanelAuthenticationWildcardProjectSecretOptionTitle(str, Enum):
    PROJECT_SECRET = 'Project Secret'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceMixpanelAuthenticationWildcardProjectSecret:
    r"""Choose how to authenticate to Mixpanel"""
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_secret') }})
    r"""Mixpanel project secret. See the <a href=\\"https://developer.mixpanel.com/reference/project-secret#managing-a-projects-secret\\">docs</a> for more information on how to obtain this."""
    option_title: Optional[SourceMixpanelAuthenticationWildcardProjectSecretOptionTitle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    


class SourceMixpanelAuthenticationWildcardServiceAccountOptionTitle(str, Enum):
    SERVICE_ACCOUNT = 'Service Account'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceMixpanelAuthenticationWildcardServiceAccount:
    r"""Choose how to authenticate to Mixpanel"""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Mixpanel Service Account Secret. See the <a href=\\"https://developer.mixpanel.com/reference/service-accounts\\">docs</a> for more information on how to obtain this."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Mixpanel Service Account Username. See the <a href=\\"https://developer.mixpanel.com/reference/service-accounts\\">docs</a> for more information on how to obtain this."""
    option_title: Optional[SourceMixpanelAuthenticationWildcardServiceAccountOptionTitle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SourceMixpanelAuthenticationWildcard:
    pass

class SourceMixpanelRegion(str, Enum):
    r"""The region of mixpanel domain instance either US or EU."""
    US = 'US'
    EU = 'EU'

class SourceMixpanelMixpanel(str, Enum):
    MIXPANEL = 'mixpanel'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceMixpanel:
    r"""The values required to configure the source."""
    attribution_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution_window'), 'exclude': lambda f: f is None }})
    r"""A period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted. Default attribution window is 5 days."""
    credentials: Optional[Union[SourceMixpanelAuthenticationWildcardServiceAccount, SourceMixpanelAuthenticationWildcardProjectSecret]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Mixpanel"""
    date_window_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_window_size'), 'exclude': lambda f: f is None }})
    r"""Defines window size in days, that used to slice through data. You can reduce it, if amount of data in each window is too big for your environment."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date in the format YYYY-MM-DD. Any data after this date will not be replicated. Left empty to always sync to most recent date"""
    project_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id'), 'exclude': lambda f: f is None }})
    r"""Your project ID number. See the <a href=\\"https://help.mixpanel.com/hc/en-us/articles/115004490503-Project-Settings#project-id\\">docs</a> for more information on how to obtain this."""
    project_timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_timezone'), 'exclude': lambda f: f is None }})
    r"""Time zone in which integer date times are stored. The project timezone may be found in the project settings in the <a href=\\"https://help.mixpanel.com/hc/en-us/articles/115004547203-Manage-Timezones-for-Projects-in-Mixpanel\\">Mixpanel console</a>."""
    region: Optional[SourceMixpanelRegion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""The region of mixpanel domain instance either US or EU."""
    select_properties_by_default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('select_properties_by_default'), 'exclude': lambda f: f is None }})
    r"""Setting this config parameter to TRUE ensures that new properties on events and engage records are captured. Otherwise new properties will be ignored."""
    source_type: Optional[SourceMixpanelMixpanel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date in the format YYYY-MM-DD. Any data before this date will not be replicated. If this option is not set, the connector will replicate data from up to one year ago by default."""
    

