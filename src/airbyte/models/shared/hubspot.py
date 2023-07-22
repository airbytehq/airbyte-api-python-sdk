"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class HubspotCredentials:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this ID."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The client secret for your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this secret."""
    refresh_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token'), 'exclude': lambda f: f is None }})
    r"""Refresh token to renew an expired access token. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this token."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Hubspot:
    r"""The values required to configure the source."""
    credentials: Optional[HubspotCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    
