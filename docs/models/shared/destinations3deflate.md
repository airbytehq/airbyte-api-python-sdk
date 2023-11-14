# DestinationS3Deflate

The compression algorithm used to compress data. Default to no compression.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `codec`                                                                                        | [Optional[shared.DestinationS3SchemasCodec]](../../models/shared/destinations3schemascodec.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `compression_level`                                                                            | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | 0: no compression & fastest, 9: best compression & slowest.                                    |