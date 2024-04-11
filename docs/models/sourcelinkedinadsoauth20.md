# SourceLinkedinAdsOAuth20


## Fields

| Field                                                                                                                                                                                  | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                                                                            | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The client ID of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information.     |
| `client_secret`                                                                                                                                                                        | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The client secret of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information. |
| `refresh_token`                                                                                                                                                                        | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The key to refresh the expired access token. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information.     |
| `auth_method`                                                                                                                                                                          | [Optional[models.SourceLinkedinAdsAuthMethod]](../models/sourcelinkedinadsauthmethod.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                     | N/A                                                                                                                                                                                    |