# ~~DestinationSurrealdb~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'destinationType' key instead..


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `destination_type`                         | [models.Surrealdb](../models/surrealdb.md) | :heavy_check_mark:                         | N/A                                        |
| `surrealdb_database`                       | *Optional[str]*                            | :heavy_minus_sign:                         | The database to use in SurrealDB.          |
| `surrealdb_namespace`                      | *Optional[str]*                            | :heavy_minus_sign:                         | The namespace to use in SurrealDB.         |
| `surrealdb_password`                       | *str*                                      | :heavy_check_mark:                         | The password to use in SurrealDB.          |
| `surrealdb_url`                            | *str*                                      | :heavy_check_mark:                         | The URL of the SurrealDB instance.         |
| `surrealdb_username`                       | *str*                                      | :heavy_check_mark:                         | The username to use in SurrealDB.          |