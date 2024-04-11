# DestinationOracle


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `host`                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                           | The hostname of the database.                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                              |
| `sid`                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                           | The System Identifier uniquely distinguishes the instance from any other instance on the same computer.                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                              |
| `username`                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                           | The username to access the database. This user must have CREATE USER privileges in the database.                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                              |
| `destination_type`                                                                                                                                                                                                                                                                                                                                           | [models.Oracle](../models/oracle.md)                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                              |
| `jdbc_url_params`                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                           | Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3).                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                              |
| `password`                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                           | The password associated with the username.                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                              |
| `port`                                                                                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                           | The port of the database.                                                                                                                                                                                                                                                                                                                                    | 1521                                                                                                                                                                                                                                                                                                                                                         |
| `schema`                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                           | The default schema is used as the target schema for all statements issued from the connection that do not explicitly specify a schema name. The usual value for this field is "airbyte".  In Oracle, schemas and users are the same thing, so the "user" parameter is used as the login credentials and this is used for the default Airbyte message schema. | airbyte                                                                                                                                                                                                                                                                                                                                                      |
| `tunnel_method`                                                                                                                                                                                                                                                                                                                                              | [Optional[Union[models.DestinationOracleNoTunnel, models.DestinationOracleSSHKeyAuthentication, models.DestinationOraclePasswordAuthentication]]](../models/destinationoraclesshtunnelmethod.md)                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                           | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                              |