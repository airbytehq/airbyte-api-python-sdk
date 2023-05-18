"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import actortypeenum as shared_actortypeenum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceOAuthCredentialsRequest:
    r"""POST body for creating/updating workspace level OAuth credentials"""
    
    actor_type: shared_actortypeenum.ActorTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actorType') }})
    r"""Whether you're setting this override for a source or destination"""
    configuration: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    r"""The configuration for this source/destination based on the OAuth section of the relevant specification."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    