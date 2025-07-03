# StreamMapping

Describes the relationship between a source stream and a destination table and how to update the information.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `destination_table`                                                                        | *str*                                                                                      | :heavy_check_mark:                                                                         | The name for the table to update the data in the destination.                              |
| `source_stream`                                                                            | *str*                                                                                      | :heavy_check_mark:                                                                         | The name for the input stream.                                                             |
| `update_mode`                                                                              | [models.UpdateMode](../models/updatemode.md)                                               | :heavy_check_mark:                                                                         | How to update the data in the destination.                                                 |
| `upsert_key`                                                                               | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Given the operation is an upsert, a field representing an external ID needs to be provided |