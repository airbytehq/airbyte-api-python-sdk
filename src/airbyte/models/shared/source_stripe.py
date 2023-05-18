"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceStripeStripe(str, Enum):
    STRIPE = 'stripe'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceStripe:
    r"""The values required to configure the source."""
    
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Your Stripe account ID (starts with 'acct_', find yours <a href=\\"https://dashboard.stripe.com/settings/account\\">here</a>)."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Stripe API key (usually starts with 'sk_live_'; find yours <a href=\\"https://dashboard.stripe.com/apikeys\\">here</a>)."""
    source_type: SourceStripeStripe = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Only data generated after this date will be replicated."""
    lookback_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    r"""When set, the connector will always re-export data from the past N days, where N is the value set here. This is useful if your data is frequently updated after creation. More info <a href=\\"https://docs.airbyte.com/integrations/sources/stripe#requirements\\">here</a>"""
    slice_range: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    r"""The time increment used by the connector when requesting data from the Stripe API. The bigger the value is, the less requests will be made and faster the sync will be. On the other hand, the more seldom the state is persisted."""
    