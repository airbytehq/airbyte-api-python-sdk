# SourceTrustpilotAuthorizationMethodOAuth20


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `access_token`                                                                     | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | Access Token for making authenticated requests.                                    |
| `auth_type`                                                                        | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `client_id`                                                                        | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | The API key of the Trustpilot API application. (represents the OAuth Client ID)    |
| `client_secret`                                                                    | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | The Secret of the Trustpilot API application. (represents the OAuth Client Secret) |
| `refresh_token`                                                                    | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | The key to refresh the expired access_token.                                       |
| `token_expiry_date`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_check_mark:                                                                 | The date-time when the access token should be refreshed.                           |