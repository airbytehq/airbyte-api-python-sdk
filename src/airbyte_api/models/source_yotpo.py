"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Yotpo(str, Enum):
    YOTPO = 'yotpo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceYotpo:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access token recieved as a result of API call to https://api.yotpo.com/oauth/token (Ref- https://apidocs.yotpo.com/reference/yotpo-authentication)"""
    app_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_key') }})
    r"""App key found at settings (Ref- https://settings.yotpo.com/#/general_settings)"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date time filter for incremental filter, Specify which date to extract from."""
    email: Optional[str] = dataclasses.field(default='example@gmail.com', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email address registered with yotpo."""
    SOURCE_TYPE: Final[Yotpo] = dataclasses.field(default=Yotpo.YOTPO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
