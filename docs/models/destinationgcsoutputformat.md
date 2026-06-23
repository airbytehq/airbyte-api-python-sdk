# DestinationGcsOutputFormat

Output data format. One of the following formats must be selected - <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro">AVRO</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas">PARQUET</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table">CSV</a> format, or <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table">JSONL</a> format.


## Supported Types

### `models.AvroApacheAvro`

```python
value: models.AvroApacheAvro = /* values here */
```

### `models.OutputFormatCSVCommaSeparatedValues`

```python
value: models.OutputFormatCSVCommaSeparatedValues = /* values here */
```

### `models.DestinationGcsOutputFormatJSONLinesNewlineDelimitedJSON`

```python
value: models.DestinationGcsOutputFormatJSONLinesNewlineDelimitedJSON = /* values here */
```

### `models.OutputFormatParquetColumnarStorage`

```python
value: models.OutputFormatParquetColumnarStorage = /* values here */
```

