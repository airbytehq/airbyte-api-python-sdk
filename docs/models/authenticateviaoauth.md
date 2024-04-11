# AuthenticateViaOAuth


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `access_token`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | Access Token for making authenticated requests.                        |
| `client_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The Client ID of your Salesloft developer application.                 |
| `client_secret`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | The Client Secret of your Salesloft developer application.             |
| `refresh_token`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | The token for obtaining a new access token.                            |
| `token_expiry_date`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_check_mark:                                                     | The date-time when the access token should be refreshed.               |
| `auth_type`                                                            | [models.SourceSalesloftAuthType](../models/sourcesalesloftauthtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |