# DestinationMotherduck


## Fields

| Field                                                                                                                                                                                           | Type                                                                                                                                                                                            | Required                                                                                                                                                                                        | Description                                                                                                                                                                                     | Example                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `motherduck_api_key`                                                                                                                                                                            | *str*                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                              | API access token to use for authentication to a MotherDuck database.                                                                                                                            |                                                                                                                                                                                                 |
| `destination_type`                                                                                                                                                                              | [models.Motherduck](../models/motherduck.md)                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                              | N/A                                                                                                                                                                                             |                                                                                                                                                                                                 |
| `destination_path`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Path to a .duckdb file or 'md:<DATABASE_NAME>' to connect to a MotherDuck database. If 'md:' is specified without a database name, the default MotherDuck database name ('my_db') will be used. | /local/destination.duckdb                                                                                                                                                                       |
| `schema`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Database schema name, defaults to 'main' if not specified.                                                                                                                                      | main                                                                                                                                                                                            |