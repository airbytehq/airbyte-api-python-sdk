# SourcePinterestAuthorizationMethodOAuth20


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `auth_method`                                                | *Optional[str]*                                              | :heavy_check_mark:                                           | N/A                                                          |
| `client_id`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | The Client ID of your OAuth application                      |
| `client_secret`                                              | *Optional[str]*                                              | :heavy_minus_sign:                                           | The Client Secret of your OAuth application.                 |
| `refresh_token`                                              | *Optional[str]*                                              | :heavy_check_mark:                                           | Refresh Token to obtain new Access Token, when it's expired. |