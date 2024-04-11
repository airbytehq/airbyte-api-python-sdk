# SourceFirebolt


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `database`                               | *str*                                    | :heavy_check_mark:                       | The database to connect to.              |                                          |
| `password`                               | *str*                                    | :heavy_check_mark:                       | Firebolt password.                       |                                          |
| `username`                               | *str*                                    | :heavy_check_mark:                       | Firebolt email address you use to login. | username@email.com                       |
| `account`                                | *Optional[str]*                          | :heavy_minus_sign:                       | Firebolt account to login.               |                                          |
| `engine`                                 | *Optional[str]*                          | :heavy_minus_sign:                       | Engine name or url to connect to.        |                                          |
| `host`                                   | *Optional[str]*                          | :heavy_minus_sign:                       | The host name of your Firebolt database. | api.app.firebolt.io                      |
| `source_type`                            | [models.Firebolt](../models/firebolt.md) | :heavy_check_mark:                       | N/A                                      |                                          |