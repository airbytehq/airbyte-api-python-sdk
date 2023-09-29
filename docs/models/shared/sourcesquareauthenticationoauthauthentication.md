# SourceSquareAuthenticationOauthAuthentication

Choose how to authenticate to Square.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `auth_type`                                                    | *Optional[str]*                                                | :heavy_check_mark:                                             | N/A                                                            |
| `client_id`                                                    | *Optional[str]*                                                | :heavy_check_mark:                                             | The Square-issued ID of your application                       |
| `client_secret`                                                | *Optional[str]*                                                | :heavy_check_mark:                                             | The Square-issued application secret for your application      |
| `refresh_token`                                                | *Optional[str]*                                                | :heavy_check_mark:                                             | A refresh token generated using the above client ID and secret |