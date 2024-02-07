# DestinationDatabend


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `database`                                         | *str*                                              | :heavy_check_mark:                                 | Name of the database.                              |                                                    |
| `host`                                             | *str*                                              | :heavy_check_mark:                                 | Hostname of the database.                          |                                                    |
| `username`                                         | *str*                                              | :heavy_check_mark:                                 | Username to use to access the database.            |                                                    |
| `destination_type`                                 | [shared.Databend](../../models/shared/databend.md) | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `password`                                         | *Optional[str]*                                    | :heavy_minus_sign:                                 | Password associated with the username.             |                                                    |
| `port`                                             | *Optional[int]*                                    | :heavy_minus_sign:                                 | Port of the database.                              | 443                                                |
| `table`                                            | *Optional[str]*                                    | :heavy_minus_sign:                                 | The default  table was written to.                 | default                                            |