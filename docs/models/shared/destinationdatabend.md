# DestinationDatabend

The values required to configure the destination.


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `database`                              | *Optional[str]*                         | :heavy_check_mark:                      | Name of the database.                   |                                         |
| `destination_type`                      | *Optional[str]*                         | :heavy_check_mark:                      | N/A                                     |                                         |
| `host`                                  | *Optional[str]*                         | :heavy_check_mark:                      | Hostname of the database.               |                                         |
| `password`                              | *Optional[str]*                         | :heavy_minus_sign:                      | Password associated with the username.  |                                         |
| `port`                                  | *Optional[int]*                         | :heavy_minus_sign:                      | Port of the database.                   | 443                                     |
| `table`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | The default  table was written to.      | default                                 |
| `username`                              | *Optional[str]*                         | :heavy_check_mark:                      | Username to use to access the database. |                                         |