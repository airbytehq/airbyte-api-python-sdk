"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class RocketChat(str, Enum):
    ROCKET_CHAT = 'rocket-chat'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRocketChat:
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    r"""Your rocket.chat instance URL."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Your API Token. See <a href=\\"https://developer.rocket.chat/reference/api/rest-api/endpoints/other-important-endpoints/access-tokens-endpoints\\">here</a>. The token is case sensitive."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""Your User Id."""
    SOURCE_TYPE: Final[RocketChat] = dataclasses.field(default=RocketChat.ROCKET_CHAT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

