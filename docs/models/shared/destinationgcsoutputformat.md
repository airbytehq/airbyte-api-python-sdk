# DestinationGcsOutputFormat

Output data format. One of the following formats must be selected - <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-avro#advantages_of_avro">AVRO</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#parquet_schemas">PARQUET</a> format, <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table">CSV</a> format, or <a href="https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#loading_json_data_into_a_new_table">JSONL</a> format.


## Supported Types

### AvroApacheAvro

```python
destinationGcsOutputFormat: shared.AvroApacheAvro = /* values here */
```

### DestinationGcsCSVCommaSeparatedValues

```python
destinationGcsOutputFormat: shared.DestinationGcsCSVCommaSeparatedValues = /* values here */
```

### DestinationGcsJSONLinesNewlineDelimitedJSON

```python
destinationGcsOutputFormat: shared.DestinationGcsJSONLinesNewlineDelimitedJSON = /* values here */
```

### DestinationGcsParquetColumnarStorage

```python
destinationGcsOutputFormat: shared.DestinationGcsParquetColumnarStorage = /* values here */
```

