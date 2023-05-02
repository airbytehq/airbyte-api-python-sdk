"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationScyllaScyllaEnum(str, Enum):
    SCYLLA = 'scylla'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationScylla:
    r"""The values required to configure the destination."""
    
    address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Address to connect to."""
    destination_type: DestinationScyllaScyllaEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    keyspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keyspace') }})
    r"""Default Scylla keyspace to create data in."""
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password associated with Scylla."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""Port of Scylla."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access Scylla."""
    replication: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication'), 'exclude': lambda f: f is None }})
    r"""Indicates to how many nodes the data should be replicated to."""
    