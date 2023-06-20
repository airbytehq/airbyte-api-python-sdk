# DestinationMariadbColumnstore

The values required to configure the destination.


## Fields

| Field                                                                                                                                                                                            | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      | Example                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `database`                                                                                                                                                                                       | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | Name of the database.                                                                                                                                                                            |                                                                                                                                                                                                  |
| `destination_type`                                                                                                                                                                               | [DestinationMariadbColumnstoreMariadbColumnstore](../../models/shared/destinationmariadbcolumnstoremariadbcolumnstore.md)                                                                        | :heavy_check_mark:                                                                                                                                                                               | N/A                                                                                                                                                                                              |                                                                                                                                                                                                  |
| `host`                                                                                                                                                                                           | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The Hostname of the database.                                                                                                                                                                    |                                                                                                                                                                                                  |
| `jdbc_url_params`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3). |                                                                                                                                                                                                  |
| `password`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | The Password associated with the username.                                                                                                                                                       |                                                                                                                                                                                                  |
| `port`                                                                                                                                                                                           | *int*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The Port of the database.                                                                                                                                                                        | 3306                                                                                                                                                                                             |
| `tunnel_method`                                                                                                                                                                                  | *Optional[Any]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                                                                             |                                                                                                                                                                                                  |
| `username`                                                                                                                                                                                       | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The Username which is used to access the database.                                                                                                                                               |                                                                                                                                                                                                  |