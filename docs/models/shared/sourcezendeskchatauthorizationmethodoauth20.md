# SourceZendeskChatAuthorizationMethodOAuth20


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `access_token`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | Access Token for making authenticated requests.              |
| `client_id`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | The Client ID of your OAuth application                      |
| `client_secret`                                              | *Optional[str]*                                              | :heavy_minus_sign:                                           | The Client Secret of your OAuth application.                 |
| `credentials`                                                | *Optional[str]*                                              | :heavy_check_mark:                                           | N/A                                                          |
| `refresh_token`                                              | *Optional[str]*                                              | :heavy_minus_sign:                                           | Refresh Token to obtain new Access Token, when it's expired. |