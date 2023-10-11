"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class SourceE2eTestCloudMockCatalogMultiSchemaType(str, Enum):
    MULTI_STREAM = 'MULTI_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogMultiSchema:
    r"""A catalog with multiple data streams, each with a different schema."""
    stream_schemas: Optional[str] = dataclasses.field(default='{ "stream1": { "type": "object", "properties": { "field1": { "type": "string" } } }, "stream2": { "type": "object", "properties": { "field1": { "type": "boolean" } } } }', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schemas'), 'exclude': lambda f: f is None }})
    r"""A Json object specifying multiple data streams and their schemas. Each key in this object is one stream name. Each value is the schema for that stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""
    TYPE: Final[Optional[SourceE2eTestCloudMockCatalogMultiSchemaType]] = dataclasses.field(default=SourceE2eTestCloudMockCatalogMultiSchemaType.MULTI_STREAM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SourceE2eTestCloudMockCatalogSingleSchemaType(str, Enum):
    SINGLE_STREAM = 'SINGLE_STREAM'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceE2eTestCloudMockCatalogSingleSchema:
    r"""A catalog with one or multiple streams that share the same schema."""
    stream_duplication: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_duplication'), 'exclude': lambda f: f is None }})
    r"""Duplicate the stream for easy load testing. Each stream name will have a number suffix. For example, if the stream name is \\"ds\\", the duplicated streams will be \\"ds_0\\", \\"ds_1\\", etc."""
    stream_name: Optional[str] = dataclasses.field(default='data_stream', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name'), 'exclude': lambda f: f is None }})
    r"""Name of the data stream."""
    stream_schema: Optional[str] = dataclasses.field(default='{ "type": "object", "properties": { "column1": { "type": "string" } } }', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_schema'), 'exclude': lambda f: f is None }})
    r"""A Json schema for the stream. The schema should be compatible with <a href=\\"https://json-schema.org/draft-07/json-schema-release-notes.html\\">draft-07</a>. See <a href=\\"https://cswr.github.io/JsonSchema/spec/introduction/\\">this doc</a> for examples."""
    TYPE: Final[Optional[SourceE2eTestCloudMockCatalogSingleSchemaType]] = dataclasses.field(default=SourceE2eTestCloudMockCatalogSingleSchemaType.SINGLE_STREAM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SourceE2eTestCloudMockCatalog:
    pass

class SourceE2eTestCloudE2eTestCloud(str, Enum):
    E2E_TEST_CLOUD = 'e2e-test-cloud'

class SourceE2eTestCloudType(str, Enum):
    CONTINUOUS_FEED = 'CONTINUOUS_FEED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceE2eTestCloud:
    r"""The values required to configure the source."""
    mock_catalog: Union[SourceE2eTestCloudMockCatalogSingleSchema, SourceE2eTestCloudMockCatalogMultiSchema] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mock_catalog') }})
    SOURCE_TYPE: Final[SourceE2eTestCloudE2eTestCloud] = dataclasses.field(default=SourceE2eTestCloudE2eTestCloud.E2E_TEST_CLOUD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    max_messages: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_messages'), 'exclude': lambda f: f is None }})
    r"""Number of records to emit per stream. Min 1. Max 100 billion."""
    message_interval_ms: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_interval_ms'), 'exclude': lambda f: f is None }})
    r"""Interval between messages in ms. Min 0 ms. Max 60000 ms (1 minute)."""
    seed: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    r"""When the seed is unspecified, the current time millis will be used as the seed. Range: [0, 1000000]."""
    TYPE: Final[Optional[SourceE2eTestCloudType]] = dataclasses.field(default=SourceE2eTestCloudType.CONTINUOUS_FEED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

