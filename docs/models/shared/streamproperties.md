# StreamProperties

The stream properties associated with a connection.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `default_cursor_field`                                                        | list[*str*]                                                                   | :heavy_minus_sign:                                                            | N/A                                                                           |
| `property_fields`                                                             | list[list[*str*]]                                                             | :heavy_minus_sign:                                                            | N/A                                                                           |
| `source_defined_cursor_field`                                                 | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | N/A                                                                           |
| `source_defined_primary_key`                                                  | list[list[*str*]]                                                             | :heavy_minus_sign:                                                            | N/A                                                                           |
| `stream_name`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `sync_modes`                                                                  | list[[ConnectionSyncModeEnum](../../models/shared/connectionsyncmodeenum.md)] | :heavy_minus_sign:                                                            | N/A                                                                           |