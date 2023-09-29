# SourceTypeformAuthorizationMethodOAuth20


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `access_token`                                                       | *Optional[str]*                                                      | :heavy_check_mark:                                                   | Access Token for making authenticated requests.                      |
| `auth_type`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `client_id`                                                          | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The Client ID of the Typeform developer application.                 |
| `client_secret`                                                      | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The Client Secret the Typeform developer application.                |
| `refresh_token`                                                      | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The key to refresh the expired access_token.                         |
| `token_expiry_date`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date-time when the access token should be refreshed.             |