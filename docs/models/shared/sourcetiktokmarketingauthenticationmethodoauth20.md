# SourceTiktokMarketingAuthenticationMethodOAuth20

Authentication method


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `access_token`                                                                   | *Optional[str]*                                                                  | :heavy_check_mark:                                                               | Long-term Authorized Access Token.                                               |
| `advertiser_id`                                                                  | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | The Advertiser ID to filter reports and streams. Let this empty to retrieve all. |
| `app_id`                                                                         | *Optional[str]*                                                                  | :heavy_check_mark:                                                               | The Developer Application App ID.                                                |
| `auth_type`                                                                      | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              |
| `secret`                                                                         | *Optional[str]*                                                                  | :heavy_check_mark:                                                               | The Developer Application Secret.                                                |