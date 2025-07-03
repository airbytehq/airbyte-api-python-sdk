# StreamProperties

The stream properties associated with a connection.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `default_cursor_field`                                                     | List[*str*]                                                                | :heavy_minus_sign:                                                         | N/A                                                                        |
| `property_fields`                                                          | List[List[*str*]]                                                          | :heavy_minus_sign:                                                         | N/A                                                                        |
| `source_defined_cursor_field`                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `source_defined_primary_key`                                               | List[List[*str*]]                                                          | :heavy_minus_sign:                                                         | N/A                                                                        |
| `stream_name`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `streamnamespace`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `sync_modes`                                                               | List[[models.ConnectionSyncModeEnum](../models/connectionsyncmodeenum.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |