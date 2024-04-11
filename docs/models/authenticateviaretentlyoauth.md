# AuthenticateViaRetentlyOAuth


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                       | *str*                                                                                             | :heavy_check_mark:                                                                                | The Client ID of your Retently developer application.                                             |
| `client_secret`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | The Client Secret of your Retently developer application.                                         |
| `refresh_token`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | Retently Refresh Token which can be used to fetch new Bearer Tokens when the current one expires. |
| `additional_properties`                                                                           | Dict[str, *Any*]                                                                                  | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `auth_type`                                                                                       | [Optional[models.SourceRetentlyAuthType]](../models/sourceretentlyauthtype.md)                    | :heavy_minus_sign:                                                                                | N/A                                                                                               |