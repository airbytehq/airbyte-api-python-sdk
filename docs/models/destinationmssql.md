# DestinationMssql


## Fields

| Field                                                                                                                                                                                            | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      | Example                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `database`                                                                                                                                                                                       | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The name of the MSSQL database.                                                                                                                                                                  |                                                                                                                                                                                                  |
| `host`                                                                                                                                                                                           | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The host name of the MSSQL database.                                                                                                                                                             |                                                                                                                                                                                                  |
| `username`                                                                                                                                                                                       | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | The username which is used to access the database.                                                                                                                                               |                                                                                                                                                                                                  |
| `destination_type`                                                                                                                                                                               | [models.Mssql](../models/mssql.md)                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                               | N/A                                                                                                                                                                                              |                                                                                                                                                                                                  |
| `jdbc_url_params`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3). |                                                                                                                                                                                                  |
| `password`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | The password associated with this username.                                                                                                                                                      |                                                                                                                                                                                                  |
| `port`                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | The port of the MSSQL database.                                                                                                                                                                  | 1433                                                                                                                                                                                             |
| `schema`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                               | The default schema tables are written to if the source does not specify a namespace. The usual value for this field is "public".                                                                 | public                                                                                                                                                                                           |
| `ssl_method`                                                                                                                                                                                     | [Optional[Union[models.EncryptedTrustServerCertificate, models.EncryptedVerifyCertificate]]](../models/sslmethod.md)                                                                             | :heavy_minus_sign:                                                                                                                                                                               | The encryption method which is used to communicate with the database.                                                                                                                            |                                                                                                                                                                                                  |
| `tunnel_method`                                                                                                                                                                                  | [Optional[Union[models.DestinationMssqlNoTunnel, models.DestinationMssqlSSHKeyAuthentication, models.DestinationMssqlPasswordAuthentication]]](../models/destinationmssqlsshtunnelmethod.md)     | :heavy_minus_sign:                                                                                                                                                                               | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                                                                             |                                                                                                                                                                                                  |