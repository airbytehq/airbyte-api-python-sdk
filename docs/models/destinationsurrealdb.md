# DestinationSurrealdb


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `surrealdb_password`                       | *str*                                      | :heavy_check_mark:                         | The password to use in SurrealDB.          |
| `surrealdb_url`                            | *str*                                      | :heavy_check_mark:                         | The URL of the SurrealDB instance.         |
| `surrealdb_username`                       | *str*                                      | :heavy_check_mark:                         | The username to use in SurrealDB.          |
| `destination_type`                         | [models.Surrealdb](../models/surrealdb.md) | :heavy_check_mark:                         | N/A                                        |
| `surrealdb_database`                       | *Optional[str]*                            | :heavy_minus_sign:                         | The database to use in SurrealDB.          |
| `surrealdb_namespace`                      | *Optional[str]*                            | :heavy_minus_sign:                         | The namespace to use in SurrealDB.         |