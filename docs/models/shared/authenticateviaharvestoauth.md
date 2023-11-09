# AuthenticateViaHarvestOAuth

Choose how to authenticate to Harvest.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `additional_properties`                                                                | Dict[str, *Any*]                                                                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `auth_type`                                                                            | [Optional[shared.SourceHarvestAuthType]](../../models/shared/sourceharvestauthtype.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `client_id`                                                                            | *str*                                                                                  | :heavy_check_mark:                                                                     | The Client ID of your Harvest developer application.                                   |
| `client_secret`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | The Client Secret of your Harvest developer application.                               |
| `refresh_token`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | Refresh Token to renew the expired Access Token.                                       |