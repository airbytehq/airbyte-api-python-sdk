# SourceOktaOAuth20


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `client_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The Client ID of your OAuth application.                               |
| `client_secret`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | The Client Secret of your OAuth application.                           |
| `refresh_token`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | Refresh Token to obtain new Access Token, when it's expired.           |
| `auth_type`                                                            | [shared.SourceOktaAuthType](../../models/shared/sourceoktaauthtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |