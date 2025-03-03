"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional


class Days(str, Enum):
    r"""The number of days of data for market chart."""
    ONE = '1'
    SEVEN = '7'
    FOURTEEN = '14'
    THIRTY = '30'
    NINETY = '90'
    ONE_HUNDRED_AND_EIGHTY = '180'
    THREE_HUNDRED_AND_SIXTY_FIVE = '365'
    MAX = 'max'


class CoingeckoCoins(str, Enum):
    COINGECKO_COINS = 'coingecko-coins'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoingeckoCoins:
    coin_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('coin_id') }})
    r"""CoinGecko coin ID (e.g. bitcoin). Can be retrieved from the
    `/coins/list` endpoint.
    """
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The start date for the historical data stream in dd-mm-yyyy format."""
    vs_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vs_currency') }})
    r"""The target currency of market data (e.g. usd, eur, jpy, etc.)"""
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    r"""API Key (for pro users)"""
    days: Optional[Days] = dataclasses.field(default=Days.THIRTY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days'), 'exclude': lambda f: f is None }})
    r"""The number of days of data for market chart."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The end date for the historical data stream in dd-mm-yyyy format."""
    SOURCE_TYPE: Final[CoingeckoCoins] = dataclasses.field(default=CoingeckoCoins.COINGECKO_COINS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

