"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .actortypeenum import ActorTypeEnum
from .oauthactornames import OAuthActorNames
from .oauthcredentialsconfiguration import OAuthCredentialsConfiguration
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceOAuthCredentialsRequest:
    r"""POST body for creating/updating workspace level OAuth credentials"""
    actor_type: ActorTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actorType') }})
    r"""Whether you're setting this override for a source or destination"""
    configuration: OAuthCredentialsConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The values required to configure the source."""
    name: OAuthActorNames = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    

