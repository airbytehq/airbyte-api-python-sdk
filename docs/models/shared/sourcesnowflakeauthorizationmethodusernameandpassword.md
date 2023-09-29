# SourceSnowflakeAuthorizationMethodUsernameAndPassword


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `auth_type`                                                       | *Optional[str]*                                                   | :heavy_check_mark:                                                | N/A                                                               |                                                                   |
| `password`                                                        | *Optional[str]*                                                   | :heavy_check_mark:                                                | The password associated with the username.                        |                                                                   |
| `username`                                                        | *Optional[str]*                                                   | :heavy_check_mark:                                                | The username you created to allow Airbyte to access the database. | AIRBYTE_USER                                                      |