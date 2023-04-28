"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceSentrySentryEnum(str, Enum):
    SENTRY = 'sentry'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSentry:
    r"""The values required to configure the source."""
    
    auth_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_token') }})

    r"""Log into Sentry and then <a href=\\"https://sentry.io/settings/account/api/auth-tokens/\\">create authentication tokens</a>.For self-hosted, you can find or create authentication tokens by visiting \\"{instance_url_prefix}/settings/account/api/auth-tokens/\\" """
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})

    r"""The slug of the organization the groups belong to."""
    project: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project') }})

    r"""The name (slug) of the Project you want to sync."""
    source_type: SourceSentrySentryEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})

    discover_fields: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discover_fields'), 'exclude': lambda f: f is None }})

    r"""Fields to retrieve when fetching discover events"""
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})

    r"""Host name of Sentry API server.For self-hosted, specify your host name here. Otherwise, leave it empty."""
    