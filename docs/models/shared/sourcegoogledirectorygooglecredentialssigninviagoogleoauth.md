# SourceGoogleDirectoryGoogleCredentialsSignInViaGoogleOAuth

For these scenario user only needs to give permission to read Google Directory data.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `client_id`                                     | *Optional[str]*                                 | :heavy_check_mark:                              | The Client ID of the developer application.     |
| `client_secret`                                 | *Optional[str]*                                 | :heavy_check_mark:                              | The Client Secret of the developer application. |
| `credentials_title`                             | *Optional[str]*                                 | :heavy_minus_sign:                              | Authentication Scenario                         |
| `refresh_token`                                 | *Optional[str]*                                 | :heavy_check_mark:                              | The Token for obtaining a new access token.     |