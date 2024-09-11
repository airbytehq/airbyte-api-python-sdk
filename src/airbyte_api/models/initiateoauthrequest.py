"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .oauthactornames import OAuthActorNames
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InitiateOauthRequest:
    r"""POST body for initiating OAuth via the public API"""
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirectUrl') }})
    r"""The URL to redirect the user to with the OAuth secret stored in the secret_id query string parameter after authentication is complete."""
    source_type: OAuthActorNames = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""The workspace to create the secret and eventually the full source."""
    o_auth_input_configuration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oAuthInputConfiguration'), 'exclude': lambda f: f is None }})
    r"""The values required to configure OAuth flows. The schema for this must match the `OAuthConfigSpecification.oauthUserInputFromConnectorConfigSpecification` schema."""
    

