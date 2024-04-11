"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, Final, Optional, Union

class SourceE2eTestCloudType(str, Enum):
    MULTI_STREAM = 'MULTI_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MultiSchema:
    r"""A catalog with multiple data streams, each with a different schema."""
    stream_schemas: Optional[str] = dataclasses.field(default='{ "stream1": { "type": "object", "properties": { "field1": { "type": "string" } } }, "stream2": { "type": "object", "properties": { "field1": { "type": "boolean" } } } }', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schemas'), 'exclude': lambda f: f is None }})
    r"""A Json object specifying multiple data streams and their schemas. Each key in this object is one stream name. Each value is the schema for that stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""
    TYPE: Final[Optional[SourceE2eTestCloudType]] = dataclasses.field(default=SourceE2eTestCloudType.MULTI_STREAM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SourceE2eTestCloudSchemasType(str, Enum):
    SINGLE_STREAM = 'SINGLE_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SingleSchema:
    r"""A catalog with one or multiple streams that share the same schema."""
    stream_duplication: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_duplication'), 'exclude': lambda f: f is None }})
    r"""Duplicate the stream for easy load testing. Each stream name will have a number suffix. For example, if the stream name is \\"ds\\", the duplicated streams will be \\"ds_0\\", \\"ds_1\\", etc."""
    stream_name: Optional[str] = dataclasses.field(default='data_stream', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name'), 'exclude': lambda f: f is None }})
    r"""Name of the data stream."""
    stream_schema: Optional[str] = dataclasses.field(default='{ "type": "object", "properties": { "column1": { "type": "string" } } }', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schema'), 'exclude': lambda f: f is None }})
    r"""A Json schema for the stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""
    TYPE: Final[Optional[SourceE2eTestCloudSchemasType]] = dataclasses.field(default=SourceE2eTestCloudSchemasType.SINGLE_STREAM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class E2eTestCloud(str, Enum):
    E2E_TEST_CLOUD = 'e2e-test-cloud'

class Type(str, Enum):
    CONTINUOUS_FEED = 'CONTINUOUS_FEED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContinuousFeed:
    UNSET='__SPEAKEASY_UNSET__'
    mock_catalog: Union[SingleSchema, MultiSchema] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mock_catalog') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    max_messages: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_messages'), 'exclude': lambda f: f is None }})
    r"""Number of records to emit per stream. Min 1. Max 100 billion."""
    message_interval_ms: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_interval_ms'), 'exclude': lambda f: f is None }})
    r"""Interval between messages in ms. Min 0 ms. Max 60000 ms (1 minute)."""
    seed: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    r"""When the seed is unspecified, the current time millis will be used as the seed. Range: [0, 1000000]."""
    SOURCE_TYPE: Final[Optional[E2eTestCloud]] = dataclasses.field(default=E2eTestCloud.E2E_TEST_CLOUD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    TYPE: Final[Optional[Type]] = dataclasses.field(default=Type.CONTINUOUS_FEED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    
