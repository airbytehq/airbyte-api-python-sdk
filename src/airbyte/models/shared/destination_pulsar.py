"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationPulsarCompressionType(str, Enum):
    r"""Compression type for the producer."""
    NONE = 'NONE'
    LZ4 = 'LZ4'
    ZLIB = 'ZLIB'
    ZSTD = 'ZSTD'
    SNAPPY = 'SNAPPY'

class DestinationPulsarPulsar(str, Enum):
    PULSAR = 'pulsar'

class DestinationPulsarTopicType(str, Enum):
    r"""It identifies type of topic. Pulsar supports two kind of topics: persistent and non-persistent. In persistent topic, all messages are durably persisted on disk (that means on multiple disks unless the broker is standalone), whereas non-persistent topic does not persist message into storage disk."""
    PERSISTENT = 'persistent'
    NON_PERSISTENT = 'non-persistent'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPulsar:
    r"""The values required to configure the destination."""
    
    batching_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_enabled') }})
    r"""Control whether automatic batching of messages is enabled for the producer."""
    batching_max_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_max_messages') }})
    r"""Maximum number of messages permitted in a batch."""
    batching_max_publish_delay: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batching_max_publish_delay') }})
    r"""Time period in milliseconds within which the messages sent will be batched."""
    block_if_queue_full: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_if_queue_full') }})
    r"""If the send operation should block when the outgoing message queue is full."""
    brokers: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brokers') }})
    r"""A list of host/port pairs to use for establishing the initial connection to the Pulsar cluster."""
    compression_type: DestinationPulsarCompressionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type') }})
    r"""Compression type for the producer."""
    destination_type: DestinationPulsarPulsar = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    max_pending_messages: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_pending_messages') }})
    r"""The maximum size of a queue holding pending messages."""
    max_pending_messages_across_partitions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_pending_messages_across_partitions') }})
    r"""The maximum number of pending messages across partitions."""
    send_timeout_ms: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('send_timeout_ms') }})
    r"""If a message is not acknowledged by a server before the send-timeout expires, an error occurs (in ms)."""
    topic_namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_namespace') }})
    r"""The administrative unit of the topic, which acts as a grouping mechanism for related topics. Most topic configuration is performed at the namespace level. Each tenant has one or multiple namespaces."""
    topic_pattern: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_pattern') }})
    r"""Topic pattern in which the records will be sent. You can use patterns like '{namespace}' and/or '{stream}' to send the message to a specific topic based on these values. Notice that the topic name will be transformed to a standard naming convention."""
    topic_tenant: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_tenant') }})
    r"""The topic tenant within the instance. Tenants are essential to multi-tenancy in Pulsar, and spread across clusters."""
    topic_type: DestinationPulsarTopicType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_type') }})
    r"""It identifies type of topic. Pulsar supports two kind of topics: persistent and non-persistent. In persistent topic, all messages are durably persisted on disk (that means on multiple disks unless the broker is standalone), whereas non-persistent topic does not persist message into storage disk."""
    use_tls: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('use_tls') }})
    r"""Whether to use TLS encryption on the connection."""
    producer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('producer_name'), 'exclude': lambda f: f is None }})
    r"""Name for the producer. If not filled, the system will generate a globally unique name which can be accessed with."""
    producer_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('producer_sync'), 'exclude': lambda f: f is None }})
    r"""Wait synchronously until the record has been sent to Pulsar."""
    topic_test: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic_test'), 'exclude': lambda f: f is None }})
    r"""Topic to test if Airbyte can produce messages."""
    