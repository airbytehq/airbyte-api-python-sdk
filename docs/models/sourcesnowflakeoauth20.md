# SourceSnowflakeOAuth20


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `client_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The Client ID of your Snowflake developer application.                 |
| `client_secret`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | The Client Secret of your Snowflake developer application.             |
| `access_token`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Access Token for making authenticated requests.                        |
| `auth_type`                                                            | [models.SourceSnowflakeAuthType](../models/sourcesnowflakeauthtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `refresh_token`                                                        | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Refresh Token for making authenticated requests.                       |