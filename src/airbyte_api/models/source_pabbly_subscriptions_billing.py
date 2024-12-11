"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class PabblySubscriptionsBilling(str, Enum):
    PABBLY_SUBSCRIPTIONS_BILLING = 'pabbly-subscriptions-billing'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePabblySubscriptionsBilling:
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[PabblySubscriptionsBilling] = dataclasses.field(default=PabblySubscriptionsBilling.PABBLY_SUBSCRIPTIONS_BILLING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

