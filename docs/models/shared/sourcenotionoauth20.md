# SourceNotionOAuth20

Pick an authentication method.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `access_token`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | Access Token is a token you received by complete the OauthWebFlow of Notion. |
| `auth_type`                                                                  | [shared.SourceNotionAuthType](../../models/shared/sourcenotionauthtype.md)   | :heavy_check_mark:                                                           | N/A                                                                          |
| `client_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | The ClientID of your Notion integration.                                     |
| `client_secret`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | The ClientSecret of your Notion integration.                                 |