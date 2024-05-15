"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional


class ActionReportTime(str, Enum):
    r"""Specifies the principle for conversion reporting."""
    CONVERSION = 'conversion'
    IMPRESSION = 'impression'


class SourceSnapchatMarketingSnapchatMarketing(str, Enum):
    SNAPCHAT_MARKETING = 'snapchat-marketing'


class SwipeUpAttributionWindow(str, Enum):
    r"""Attribution window for swipe ups."""
    ONE_DAY = '1_DAY'
    SEVEN_DAY = '7_DAY'
    TWENTY_EIGHT_DAY = '28_DAY'


class ViewAttributionWindow(str, Enum):
    r"""Attribution window for views."""
    ONE_HOUR = '1_HOUR'
    THREE_HOUR = '3_HOUR'
    SIX_HOUR = '6_HOUR'
    ONE_DAY = '1_DAY'
    SEVEN_DAY = '7_DAY'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSnapchatMarketing:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Snapchat developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Snapchat developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to renew the expired Access Token."""
    action_report_time: Optional[ActionReportTime] = dataclasses.field(default=ActionReportTime.CONVERSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_report_time'), 'exclude': lambda f: f is None }})
    r"""Specifies the principle for conversion reporting."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""Date in the format 2017-01-25. Any data after this date will not be replicated."""
    SOURCE_TYPE: Final[SourceSnapchatMarketingSnapchatMarketing] = dataclasses.field(default=SourceSnapchatMarketingSnapchatMarketing.SNAPCHAT_MARKETING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2022-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""Date in the format 2022-01-01. Any data before this date will not be replicated."""
    swipe_up_attribution_window: Optional[SwipeUpAttributionWindow] = dataclasses.field(default=SwipeUpAttributionWindow.TWENTY_EIGHT_DAY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('swipe_up_attribution_window'), 'exclude': lambda f: f is None }})
    r"""Attribution window for swipe ups."""
    view_attribution_window: Optional[ViewAttributionWindow] = dataclasses.field(default=ViewAttributionWindow.ONE_DAY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_attribution_window'), 'exclude': lambda f: f is None }})
    r"""Attribution window for views."""
    

