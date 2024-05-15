"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Zoom(str, Enum):
    ZOOM = 'zoom'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZoom:
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The account ID for your Zoom account. You can find this in the Zoom Marketplace under the \\"Manage\\" tab for your app."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID for your Zoom app. You can find this in the Zoom Marketplace under the \\"Manage\\" tab for your app."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret for your Zoom app. You can find this in the Zoom Marketplace under the \\"Manage\\" tab for your app."""
    authorization_endpoint: Optional[str] = dataclasses.field(default='https://zoom.us/oauth/token', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization_endpoint'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Zoom] = dataclasses.field(default=Zoom.ZOOM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

