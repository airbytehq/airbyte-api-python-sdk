"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class SourceRevolutMerchantEnvironment(str, Enum):
    r"""The base url of your environment. Either sandbox or production"""
    SANDBOX_MERCHANT = 'sandbox-merchant'
    MERCHANT = 'merchant'


class RevolutMerchant(str, Enum):
    REVOLUT_MERCHANT = 'revolut-merchant'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRevolutMerchant:
    api_version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_version') }})
    r"""Specify the API version to use. This is required for certain API calls. Example: '2024-09-01'."""
    environment: SourceRevolutMerchantEnvironment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment') }})
    r"""The base url of your environment. Either sandbox or production"""
    secret_api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_api_key') }})
    r"""Secret API key to use for authenticating with the Revolut Merchant API. Find it in your Revolut Business account under APIs > Merchant API."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[RevolutMerchant] = dataclasses.field(default=RevolutMerchant.REVOLUT_MERCHANT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
