"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class S3(str, Enum):
    S3 = 's3'


class DestinationS3SchemasCompressionCodec(str, Enum):
    r"""The compression algorithm used to compress data pages."""
    UNCOMPRESSED = 'UNCOMPRESSED'
    SNAPPY = 'SNAPPY'
    GZIP = 'GZIP'
    LZO = 'LZO'
    BROTLI = 'BROTLI'
    LZ4 = 'LZ4'
    ZSTD = 'ZSTD'


class DestinationS3SchemasFormatOutputFormatFormatType(str, Enum):
    PARQUET = 'Parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3ParquetColumnarStorage:
    block_size_mb: Optional[int] = dataclasses.field(default=128, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size_mb'), 'exclude': lambda f: f is None }})
    r"""This is the size of a row group being buffered in memory. It limits the memory usage when writing. Larger values will improve the IO when reading, but consume more memory when writing. Default: 128 MB."""
    compression_codec: Optional[DestinationS3SchemasCompressionCodec] = dataclasses.field(default=DestinationS3SchemasCompressionCodec.UNCOMPRESSED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec'), 'exclude': lambda f: f is None }})
    r"""The compression algorithm used to compress data pages."""
    dictionary_encoding: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_encoding'), 'exclude': lambda f: f is None }})
    r"""Default: true."""
    dictionary_page_size_kb: Optional[int] = dataclasses.field(default=1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dictionary_page_size_kb'), 'exclude': lambda f: f is None }})
    r"""There is one dictionary page per column per row group when dictionary encoding is used. The dictionary page size works like the page size but for dictionary. Default: 1024 KB."""
    format_type: Optional[DestinationS3SchemasFormatOutputFormatFormatType] = dataclasses.field(default=DestinationS3SchemasFormatOutputFormatFormatType.PARQUET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    max_padding_size_mb: Optional[int] = dataclasses.field(default=8, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_padding_size_mb'), 'exclude': lambda f: f is None }})
    r"""Maximum size allowed as padding to align row groups. This is also the minimum size of a row group. Default: 8 MB."""
    page_size_kb: Optional[int] = dataclasses.field(default=1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_size_kb'), 'exclude': lambda f: f is None }})
    r"""The page size is for compression. A block is composed of pages. A page is the smallest unit that must be read fully to access a single record. If this value is too small, the compression will deteriorate. Default: 1024 KB."""
    



class DestinationS3SchemasFormatOutputFormat3CompressionCodecCodec(str, Enum):
    SNAPPY = 'snappy'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Snappy:
    codec: Optional[DestinationS3SchemasFormatOutputFormat3CompressionCodecCodec] = dataclasses.field(default=DestinationS3SchemasFormatOutputFormat3CompressionCodecCodec.SNAPPY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasFormatOutputFormat3Codec(str, Enum):
    ZSTANDARD = 'zstandard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Zstandard:
    codec: Optional[DestinationS3SchemasFormatOutputFormat3Codec] = dataclasses.field(default=DestinationS3SchemasFormatOutputFormat3Codec.ZSTANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""Negative levels are 'fast' modes akin to lz4 or snappy, levels above 9 are generally for archival purposes, and levels above 18 use a lot of memory."""
    include_checksum: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_checksum'), 'exclude': lambda f: f is None }})
    r"""If true, include a checksum with each data block."""
    



class DestinationS3SchemasFormatOutputFormatCodec(str, Enum):
    XZ = 'xz'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Xz:
    codec: Optional[DestinationS3SchemasFormatOutputFormatCodec] = dataclasses.field(default=DestinationS3SchemasFormatOutputFormatCodec.XZ, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=6, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""See <a href=\\"https://commons.apache.org/proper/commons-compress/apidocs/org/apache/commons/compress/compressors/xz/XZCompressorOutputStream.html#XZCompressorOutputStream-java.io.OutputStream-int-\\">here</a> for details."""
    



class DestinationS3SchemasFormatCodec(str, Enum):
    BZIP2 = 'bzip2'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Bzip2:
    codec: Optional[DestinationS3SchemasFormatCodec] = dataclasses.field(default=DestinationS3SchemasFormatCodec.BZIP2, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasCodec(str, Enum):
    DEFLATE = 'Deflate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3Deflate:
    codec: Optional[DestinationS3SchemasCodec] = dataclasses.field(default=DestinationS3SchemasCodec.DEFLATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    compression_level: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_level'), 'exclude': lambda f: f is None }})
    r"""0: no compression & fastest, 9: best compression & slowest."""
    



class DestinationS3Codec(str, Enum):
    NO_COMPRESSION = 'no compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3SchemasFormatNoCompression:
    codec: Optional[DestinationS3Codec] = dataclasses.field(default=DestinationS3Codec.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('codec'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasFormatFormatType(str, Enum):
    AVRO = 'Avro'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3AvroApacheAvro:
    compression_codec: DestinationS3CompressionCodec = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_codec') }})
    r"""The compression algorithm used to compress data. Default to no compression."""
    format_type: Optional[DestinationS3SchemasFormatFormatType] = dataclasses.field(default=DestinationS3SchemasFormatFormatType.AVRO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasFormatOutputFormatCompressionType(str, Enum):
    GZIP = 'GZIP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3SchemasGZIP:
    compression_type: Optional[DestinationS3SchemasFormatOutputFormatCompressionType] = dataclasses.field(default=DestinationS3SchemasFormatOutputFormatCompressionType.GZIP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasFormatCompressionType(str, Enum):
    NO_COMPRESSION = 'No Compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3SchemasNoCompression:
    compression_type: Optional[DestinationS3SchemasFormatCompressionType] = dataclasses.field(default=DestinationS3SchemasFormatCompressionType.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasFlattening(str, Enum):
    r"""Whether the input json data should be normalized (flattened) in the output JSON Lines. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'


class DestinationS3SchemasFormatType(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3JSONLinesNewlineDelimitedJSON:
    compression: Optional[DestinationS3SchemasCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".jsonl.gz\\")."""
    flattening: Optional[DestinationS3SchemasFlattening] = dataclasses.field(default=DestinationS3SchemasFlattening.NO_FLATTENING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    r"""Whether the input json data should be normalized (flattened) in the output JSON Lines. Please refer to docs for details."""
    format_type: Optional[DestinationS3SchemasFormatType] = dataclasses.field(default=DestinationS3SchemasFormatType.JSONL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3SchemasCompressionType(str, Enum):
    GZIP = 'GZIP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3GZIP:
    compression_type: Optional[DestinationS3SchemasCompressionType] = dataclasses.field(default=DestinationS3SchemasCompressionType.GZIP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3CompressionType(str, Enum):
    NO_COMPRESSION = 'No Compression'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3NoCompression:
    compression_type: Optional[DestinationS3CompressionType] = dataclasses.field(default=DestinationS3CompressionType.NO_COMPRESSION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3Flattening(str, Enum):
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'


class DestinationS3FormatType(str, Enum):
    CSV = 'CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3CSVCommaSeparatedValues:
    compression: Optional[DestinationS3Compression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compression'), 'exclude': lambda f: f is None }})
    r"""Whether the output files should be compressed. If compression is selected, the output filename will have an extra extension (GZIP: \\".csv.gz\\")."""
    flattening: Optional[DestinationS3Flattening] = dataclasses.field(default=DestinationS3Flattening.NO_FLATTENING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    format_type: Optional[DestinationS3FormatType] = dataclasses.field(default=DestinationS3FormatType.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type'), 'exclude': lambda f: f is None }})
    



class DestinationS3S3BucketRegion(str, Enum):
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    UNKNOWN = ''
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTH_1 = 'ap-south-1'
    AP_SOUTH_2 = 'ap-south-2'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    AP_SOUTHEAST_3 = 'ap-southeast-3'
    AP_SOUTHEAST_4 = 'ap-southeast-4'
    CA_CENTRAL_1 = 'ca-central-1'
    CA_WEST_1 = 'ca-west-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_CENTRAL_2 = 'eu-central-2'
    EU_NORTH_1 = 'eu-north-1'
    EU_SOUTH_1 = 'eu-south-1'
    EU_SOUTH_2 = 'eu-south-2'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    IL_CENTRAL_1 = 'il-central-1'
    ME_CENTRAL_1 = 'me-central-1'
    ME_SOUTH_1 = 'me-south-1'
    SA_EAST_1 = 'sa-east-1'
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationS3:
    format: DestinationS3OutputFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Format of the data output. See <a href=\\"https://docs.airbyte.com/integrations/destinations/s3/#supported-output-schema\\">here</a> for more details"""
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""The name of the S3 bucket. Read more <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html\\">here</a>."""
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    r"""Directory under the S3 bucket where data will be written. Read more <a href=\\"https://docs.airbyte.com/integrations/destinations/s3#:~:text=to%20format%20the-,bucket%20path,-%3A\\">here</a>"""
    access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id'), 'exclude': lambda f: f is None }})
    r"""The access key ID to access the S3 bucket. Airbyte requires Read and Write permissions to the given bucket. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>."""
    DESTINATION_TYPE: Final[S3] = dataclasses.field(default=S3.S3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    role_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role_arn'), 'exclude': lambda f: f is None }})
    r"""The Role ARN"""
    s3_bucket_region: Optional[DestinationS3S3BucketRegion] = dataclasses.field(default=DestinationS3S3BucketRegion.UNKNOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region'), 'exclude': lambda f: f is None }})
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    s3_endpoint: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_endpoint'), 'exclude': lambda f: f is None }})
    r"""Your S3 endpoint url. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/s3.html#:~:text=Service%20endpoints-,Amazon%20S3%20endpoints,-When%20you%20use\\">here</a>"""
    s3_path_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_path_format'), 'exclude': lambda f: f is None }})
    r"""Format string on how data will be organized inside the S3 bucket directory. Read more <a href=\\"https://docs.airbyte.com/integrations/destinations/s3#:~:text=The%20full%20path%20of%20the%20output%20data%20with%20the%20default%20S3%20path%20format\\">here</a>"""
    secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key'), 'exclude': lambda f: f is None }})
    r"""The corresponding secret to the access key ID. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>"""
    


DestinationS3CompressionCodec = Union[DestinationS3SchemasFormatNoCompression, DestinationS3Deflate, DestinationS3Bzip2, DestinationS3Xz, DestinationS3Zstandard, DestinationS3Snappy]

DestinationS3SchemasCompression = Union[DestinationS3SchemasNoCompression, DestinationS3SchemasGZIP]

DestinationS3Compression = Union[DestinationS3NoCompression, DestinationS3GZIP]

DestinationS3OutputFormat = Union[DestinationS3CSVCommaSeparatedValues, DestinationS3JSONLinesNewlineDelimitedJSON, DestinationS3AvroApacheAvro, DestinationS3ParquetColumnarStorage]
