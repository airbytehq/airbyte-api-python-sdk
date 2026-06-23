# OutputFormatCompressionCodec

The compression algorithm used to compress data pages.

## Example Usage

```python
from airbyte_api.models import OutputFormatCompressionCodec

value = OutputFormatCompressionCodec.UNCOMPRESSED
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `UNCOMPRESSED` | UNCOMPRESSED   |
| `SNAPPY`       | SNAPPY         |
| `GZIP`         | GZIP           |
| `LZO`          | LZO            |
| `BROTLI`       | BROTLI         |
| `LZ4`          | LZ4            |
| `ZSTD`         | ZSTD           |