# OauthAuthentication


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `client_id`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | The Square-issued ID of your application                                   |
| `client_secret`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | The Square-issued application secret for your application                  |
| `refresh_token`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | A refresh token generated using the above client ID and secret             |
| `auth_type`                                                                | [shared.SourceSquareAuthType](../../models/shared/sourcesquareauthtype.md) | :heavy_check_mark:                                                         | N/A                                                                        |