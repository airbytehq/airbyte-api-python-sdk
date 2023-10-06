# DestinationGcsOutputFormatAvroApacheAvro

Output data format. One of the following formats must be selected - <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro">AVRO</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas">PARQUET</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table">CSV</a> format, or <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table">JSONL</a> format.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `compression_codec`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[Union[shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecNoCompression, shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecDeflate, shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecBzip2, shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecXz, shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecZstandard, shared.DestinationGcsOutputFormatAvroApacheAvroCompressionCodecSnappy]]](undefined/models/shared/destinationgcsoutputformatavroapacheavrocompressioncodec.md) | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The compression algorithm used to compress data. Default to no compression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `format_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[shared.DestinationGcsOutputFormatAvroApacheAvroFormatType]](undefined/models/shared/destinationgcsoutputformatavroapacheavroformattype.md)                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |