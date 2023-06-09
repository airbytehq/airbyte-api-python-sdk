"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceYotpoYotpo(str, Enum):
    YOTPO = 'yotpo'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceYotpo:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access token recieved as a result of API call to https://api.yotpo.com/oauth/token (Ref- https://apidocs.yotpo.com/reference/yotpo-authentication)"""
    app_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_key') }})
    r"""App key found at settings (Ref- https://settings.yotpo.com/#/general_settings)"""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Email address registered with yotpo."""
    source_type: SourceYotpoYotpo = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Date time filter for incremental filter, Specify which date to extract from."""
    

