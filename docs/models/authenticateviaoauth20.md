# AuthenticateViaOAuth20


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `client_id`                                                    | *str*                                                          | :heavy_check_mark:                                             | The Client ID of your developer application                    |
| `client_secret`                                                | *str*                                                          | :heavy_check_mark:                                             | The client secret of your developer application                |
| `refresh_token`                                                | *str*                                                          | :heavy_check_mark:                                             | A refresh token generated using the above client ID and secret |
| `additional_properties`                                        | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            |