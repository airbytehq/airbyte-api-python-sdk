"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final


class Woocommerce(str, Enum):
    WOOCOMMERCE = 'woocommerce'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWoocommerce:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Customer Key for API in WooCommerce shop"""
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_secret') }})
    r"""Customer Secret for API in WooCommerce shop"""
    shop: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shop') }})
    r"""The name of the store. For https://EXAMPLE.com, the shop name is 'EXAMPLE.com'."""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date you would like to replicate data from. Format: YYYY-MM-DD"""
    SOURCE_TYPE: Final[Woocommerce] = dataclasses.field(default=Woocommerce.WOOCOMMERCE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

