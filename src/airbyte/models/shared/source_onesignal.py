"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceOnesignalApplications:
    app_api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_api_key') }})
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id') }})
    app_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_name'), 'exclude': lambda f: f is None }})
    


class SourceOnesignalOnesignal(str, Enum):
    ONESIGNAL = 'onesignal'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceOnesignal:
    r"""The values required to configure the source."""
    applications: list[SourceOnesignalApplications] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applications') }})
    r"""Applications keys, see the <a href=\\"https://documentation.onesignal.com/docs/accounts-and-keys\\">docs</a> for more information on how to obtain this data"""
    outcome_names: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcome_names') }})
    r"""Comma-separated list of names and the value (sum/count) for the returned outcome data. See the <a href=\\"https://documentation.onesignal.com/reference/view-outcomes\\">docs</a> for more details"""
    source_type: SourceOnesignalOnesignal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for OneSignal API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    user_auth_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_auth_key') }})
    r"""OneSignal User Auth Key, see the <a href=\\"https://documentation.onesignal.com/docs/accounts-and-keys#user-auth-key\\">docs</a> for more information on how to obtain this key."""
    

