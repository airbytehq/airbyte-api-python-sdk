"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class CredentialType(str, Enum):
    HMAC_KEY = 'HMAC_KEY'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HMACKey:
    hmac_key_access_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_access_id') }})
    r"""When linked to a service account, this ID is 61 characters long; when linked to a user account, it is 24 characters long. Read more <a href=\\"https://cloud.google.com/storage/docs/authentication/hmackeys#overview\\">here</a>."""
    hmac_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hmac_key_secret') }})
    r"""The corresponding secret for the access ID. It is a 40-character base-64 encoded string.  Read more <a href=\\"https://cloud.google.com/storage/docs/authentication/hmackeys#secrets\\">here</a>."""
    credential_type: Optional[CredentialType] = dataclasses.field(default=CredentialType.HMAC_KEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential_type'), 'exclude': lambda f: f is None }})
    



class Gcs(str, Enum):
    GCS = 'gcs'


class DestinationGcsCompressionCodec(str, Enum):
    r"""The compression algorithm used to compress data pages."""
    UNCOMPRESSED = 'UNCOMPRESSED'
    SNAPPY = 'SNAPPY'
    GZIP = 'GZIP'
    LZO = 'LZO'
    BROTLI = 'BROTLI'
    LZ4 = 'LZ4'
    ZSTD = 'ZSTD'


class DestinationGcsSchemasFormatOutputFormatFormatType(str, Enum):
    PARQUET = 'Parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsParquetColumnarStorage:
    block_size_mb: Optional[int] = dataclasses.field(default=128, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size_mb'), 'exclude': lambda f: f is None }})
    r"""This is the size of a row group being buffered in memory. It limits the memory usage when writing. Larger values will improve the IO when reading, but consume more memory when writing. Default: 128 MB."""
    compression_codec: Optional[DestinationGcsCompressionCodec] = dataclasses.field(default=DestinationGcsCompressionCodec.UNCOMPRESSED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    r"""The compression algorithm used to compress data pages."""
    dictionary_encoding: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_encoding'), 'exclude': lambda f: f is None }})
    r"""Default: true."""
    dictionary_page_size_kb: Optional[int] = dataclasses.field(default=1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_page_size_kb'), 'exclude': lambda f: f is None }})
    r"""There is one dictionary page per column per row group when dictionary encoding is used. The dictionary page size works like the page size but for dictionary. Default: 1024 KB."""
    format_type: Optional[DestinationGcsSchemasFormatOutputFormatFormatType] = dataclasses.field(default=DestinationGcsSchemasFormatOutputFormatFormatType.PARQUET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    max_padding_size_mb: Optional[int] = dataclasses.field(default=8, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_padding_size_mb'), 'exclude': lambda f: f is None }})
    r"""Maximum size allowed as padding to align row groups. This is also the minimum size of a row group. Default: 8 MB."""
    page_size_kb: Optional[int] = dataclasses.field(default=1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size_kb'), 'exclude': lambda f: f is None }})
    r"""The page size is for compression. A block is composed of pages. A page is the smallest unit that must be read fully to access a single record. If this value is too small, the compression will deteriorate. Default: 1024 KB."""
    



class DestinationGcsSchemasFormatCompressionType(str, Enum):
    GZIP = 'GZIP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsGZIP:
    compression_type: Optional[DestinationGcsSchemasFormatCompressionType] = dataclasses.field(default=DestinationGcsSchemasFormatCompressionType.GZIP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationGcsSchemasCompressionType(str, Enum):
    NO_COMPRESSION = 'No Compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsSchemasNoCompression:
    compression_type: Optional[DestinationGcsSchemasCompressionType] = dataclasses.field(default=DestinationGcsSchemasCompressionType.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationGcsSchemasFormatFormatType(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsJSONLinesNewlineDelimitedJSON:
    compression: Optional[DestinationGcsCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".jsonl.gz\\")."""
    format_type: Optional[DestinationGcsSchemasFormatFormatType] = dataclasses.field(default=DestinationGcsSchemasFormatFormatType.JSONL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class DestinationGcsCompressionType(str, Enum):
    GZIP = 'GZIP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Gzip:
    compression_type: Optional[DestinationGcsCompressionType] = dataclasses.field(default=DestinationGcsCompressionType.GZIP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class CompressionType(str, Enum):
    NO_COMPRESSION = 'No Compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsNoCompression:
    compression_type: Optional[CompressionType] = dataclasses.field(default=CompressionType.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class Normalization(str, Enum):
    r"""Whether the input JSON data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'


class DestinationGcsSchemasFormatType(str, Enum):
    CSV = 'CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcsCSVCommaSeparatedValues:
    compression: Optional[Compression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".csv.gz\\")."""
    flattening: Optional[Normalization] = dataclasses.field(default=Normalization.NO_FLATTENING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    r"""Whether the input JSON data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    format_type: Optional[DestinationGcsSchemasFormatType] = dataclasses.field(default=DestinationGcsSchemasFormatType.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class DestinationGcsSchemasFormatOutputFormat1Codec(str, Enum):
    SNAPPY = 'snappy'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Snappy:
    codec: Optional[DestinationGcsSchemasFormatOutputFormat1Codec] = dataclasses.field(default=DestinationGcsSchemasFormatOutputFormat1Codec.SNAPPY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationGcsSchemasFormatOutputFormatCodec(str, Enum):
    ZSTANDARD = 'zstandard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Zstandard:
    codec: Optional[DestinationGcsSchemasFormatOutputFormatCodec] = dataclasses.field(default=DestinationGcsSchemasFormatOutputFormatCodec.ZSTANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""Negative levels are 'fast' modes akin to lz4 or snappy, levels above 9 are generally for archival purposes, and levels above 18 use a lot of memory."""
    include_checksum: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_checksum'), 'exclude': lambda f: f is None }})
    r"""If true, include a checksum with each data block."""
    



class DestinationGcsSchemasFormatCodec(str, Enum):
    XZ = 'xz'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Xz:
    codec: Optional[DestinationGcsSchemasFormatCodec] = dataclasses.field(default=DestinationGcsSchemasFormatCodec.XZ, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=6, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""The presets 0-3 are fast presets with medium compression. The presets 4-6 are fairly slow presets with high compression. The default preset is 6. The presets 7-9 are like the preset 6 but use bigger dictionaries and have higher compressor and decompressor memory requirements. Unless the uncompressed size of the file exceeds 8 MiB, 16 MiB, or 32 MiB, it is waste of memory to use the presets 7, 8, or 9, respectively. Read more <a href=\\"https://commons.apache.org/proper/commons-compress/apidocs/org/apache/commons/compress/compressors/xz/XZCompressorOutputStream.html#XZCompressorOutputStream-java.io.OutputStream-int-\\">here</a> for details."""
    



class DestinationGcsSchemasCodec(str, Enum):
    BZIP2 = 'bzip2'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Bzip2:
    codec: Optional[DestinationGcsSchemasCodec] = dataclasses.field(default=DestinationGcsSchemasCodec.BZIP2, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationGcsCodec(str, Enum):
    DEFLATE = 'Deflate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Deflate:
    codec: Optional[DestinationGcsCodec] = dataclasses.field(default=DestinationGcsCodec.DEFLATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""0: no compression & fastest, 9: best compression & slowest."""
    



class Codec(str, Enum):
    NO_COMPRESSION = 'no compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NoCompression:
    codec: Optional[Codec] = dataclasses.field(default=Codec.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationGcsFormatType(str, Enum):
    AVRO = 'Avro'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AvroApacheAvro:
    compression_codec: CompressionCodec = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec') }})
    r"""The compression algorithm used to compress data. Default to no compression."""
    format_type: Optional[DestinationGcsFormatType] = dataclasses.field(default=DestinationGcsFormatType.AVRO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class GCSBucketRegion(str, Enum):
    r"""Select a Region of the GCS Bucket. Read more <a href=\\"https://cloud.google.com/storage/docs/locations\\">here</a>."""
    NORTHAMERICA_NORTHEAST1 = 'northamerica-northeast1'
    NORTHAMERICA_NORTHEAST2 = 'northamerica-northeast2'
    US_CENTRAL1 = 'us-central1'
    US_EAST1 = 'us-east1'
    US_EAST4 = 'us-east4'
    US_WEST1 = 'us-west1'
    US_WEST2 = 'us-west2'
    US_WEST3 = 'us-west3'
    US_WEST4 = 'us-west4'
    SOUTHAMERICA_EAST1 = 'southamerica-east1'
    SOUTHAMERICA_WEST1 = 'southamerica-west1'
    EUROPE_CENTRAL2 = 'europe-central2'
    EUROPE_NORTH1 = 'europe-north1'
    EUROPE_WEST1 = 'europe-west1'
    EUROPE_WEST2 = 'europe-west2'
    EUROPE_WEST3 = 'europe-west3'
    EUROPE_WEST4 = 'europe-west4'
    EUROPE_WEST6 = 'europe-west6'
    ASIA_EAST1 = 'asia-east1'
    ASIA_EAST2 = 'asia-east2'
    ASIA_NORTHEAST1 = 'asia-northeast1'
    ASIA_NORTHEAST2 = 'asia-northeast2'
    ASIA_NORTHEAST3 = 'asia-northeast3'
    ASIA_SOUTH1 = 'asia-south1'
    ASIA_SOUTH2 = 'asia-south2'
    ASIA_SOUTHEAST1 = 'asia-southeast1'
    ASIA_SOUTHEAST2 = 'asia-southeast2'
    AUSTRALIA_SOUTHEAST1 = 'australia-southeast1'
    AUSTRALIA_SOUTHEAST2 = 'australia-southeast2'
    ASIA = 'asia'
    EU = 'eu'
    US = 'us'
    ASIA1 = 'asia1'
    EUR4 = 'eur4'
    NAM4 = 'nam4'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGcs:
    credential: DestinationGcsAuthentication = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential') }})
    r"""An HMAC key is a type of credential and can be associated with a service account or a user account in Cloud Storage. Read more <a href=\\"https://cloud.google.com/storage/docs/authentication/hmackeys\\">here</a>."""
    format: DestinationGcsOutputFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Output data format. One of the following formats must be selected - <a href=\\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro\\">AVRO</a> format, <a href=\\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas\\">PARQUET</a> format, <a href=\\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table\\">CSV</a> format, or <a href=\\"https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table\\">JSONL</a> format."""
    gcs_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_name') }})
    r"""You can find the bucket name in the App Engine Admin console Application Settings page, under the label Google Cloud Storage Bucket. Read more <a href=\\"https://cloud.google.com/storage/docs/naming-buckets\\">here</a>."""
    gcs_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_path') }})
    r"""GCS Bucket Path string Subdirectory under the above bucket to sync the data into."""
    DESTINATION_TYPE: Final[Gcs] = dataclasses.field(default=Gcs.GCS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    gcs_bucket_region: Optional[GCSBucketRegion] = dataclasses.field(default=GCSBucketRegion.US, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gcs_bucket_region'), 'exclude': lambda f: f is None }})
    r"""Select a Region of the GCS Bucket. Read more <a href=\\"https://cloud.google.com/storage/docs/locations\\">here</a>."""
    


DestinationGcsAuthentication = Union[HMACKey]

DestinationGcsCompression = Union[DestinationGcsSchemasNoCompression, DestinationGcsGZIP]

Compression = Union[DestinationGcsNoCompression, Gzip]

CompressionCodec = Union[NoCompression, Deflate, Bzip2, Xz, Zstandard, Snappy]

DestinationGcsOutputFormat = Union[AvroApacheAvro, DestinationGcsCSVCommaSeparatedValues, DestinationGcsJSONLinesNewlineDelimitedJSON, DestinationGcsParquetColumnarStorage]
