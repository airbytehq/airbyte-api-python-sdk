# SmartsheetsCredentials


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `access_token`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Access Token for making authenticated requests.                      |
| `client_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The API ID of the SmartSheets developer application.                 |
| `client_secret`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The API Secret the SmartSheets developer application.                |
| `refresh_token`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The key to refresh the expired access_token.                         |
| `token_expiry_date`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date-time when the access token should be refreshed.             |