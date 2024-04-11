# FileBasedStreamConfig


## Fields

| Field                                                                                                                                                                                                    | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `format`                                                                                                                                                                                                 | [Union[models.AvroFormat, models.CSVFormat, models.JsonlFormat, models.ParquetFormat, models.DocumentFileTypeFormatExperimental]](../models/format.md)                                                   | :heavy_check_mark:                                                                                                                                                                                       | The configuration options that are used to alter how to read incoming files that deviate from the standard formatting.                                                                                   |
| `name`                                                                                                                                                                                                   | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | The name of the stream.                                                                                                                                                                                  |
| `days_to_sync_if_history_is_full`                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | When the state history of the file store is full, syncs will only read files that were last modified in the provided day range.                                                                          |
| `globs`                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                       | The pattern used to specify which files should be selected from the file system. For more information on glob pattern matching look <a href="https://en.wikipedia.org/wiki/Glob_(programming)">here</a>. |
| `input_schema`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | The schema that will be used to validate records extracted from the file. This will override the stream schema that is auto-detected from incoming files.                                                |
| `legacy_prefix`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | The path prefix configured in v3 versions of the S3 connector. This option is deprecated in favor of a single glob.                                                                                      |
| `primary_key`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | The column or columns (for a composite key) that serves as the unique identifier of a record. If empty, the primary key will default to the parser's default primary key.                                |
| `schemaless`                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | When enabled, syncs will not validate or structure records against the stream's schema.                                                                                                                  |
| `validation_policy`                                                                                                                                                                                      | [Optional[models.ValidationPolicy]](../models/validationpolicy.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                       | The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema.                                                                                        |