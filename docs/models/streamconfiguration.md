# StreamConfiguration

Configurations for a single stream.


## Fields

| Field                                                                                                                                                                                  | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                 | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | N/A                                                                                                                                                                                    |
| `cursor_field`                                                                                                                                                                         | List[*str*]                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                     | Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental` unless there is a default. |
| `primary_key`                                                                                                                                                                          | List[List[*str*]]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                     | Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup` unless it is already supplied by the source schema.               |
| `sync_mode`                                                                                                                                                                            | [Optional[models.ConnectionSyncModeEnum]](../models/connectionsyncmodeenum.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                     | N/A                                                                                                                                                                                    |