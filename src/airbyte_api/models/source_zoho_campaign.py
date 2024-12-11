"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class SourceZohoCampaignDataCenter(str, Enum):
    COM = 'com'
    EU = 'eu'
    IN = 'in'
    COM_AU = 'com.au'
    DOT_JP = '.jp'
    DOT_COM_CN = '.com.cn'


class ZohoCampaign(str, Enum):
    ZOHO_CAMPAIGN = 'zoho-campaign'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZohoCampaign:
    client_id_2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id_2') }})
    client_refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_refresh_token') }})
    client_secret_2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret_2') }})
    data_center: SourceZohoCampaignDataCenter = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_center') }})
    SOURCE_TYPE: Final[ZohoCampaign] = dataclasses.field(default=ZohoCampaign.ZOHO_CAMPAIGN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

