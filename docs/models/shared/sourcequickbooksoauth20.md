# SourceQuickbooksOAuth20


## Fields

| Field                                                                                                                                                                                                 | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                                                        | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | Access token fot making authenticated requests.                                                                                                                                                       |
| `auth_type`                                                                                                                                                                                           | [Optional[shared.SourceQuickbooksAuthType]](../../models/shared/sourcequickbooksauthtype.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `client_id`                                                                                                                                                                                           | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | Identifies which app is making the request. Obtain this value from the Keys tab on the app profile via My Apps on the developer site. There are two versions of this key: development and production. |
| `client_secret`                                                                                                                                                                                       | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    |  Obtain this value from the Keys tab on the app profile via My Apps on the developer site. There are two versions of this key: development and production.                                            |
| `realm_id`                                                                                                                                                                                            | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | Labeled Company ID. The Make API Calls panel is populated with the realm id and the current access token.                                                                                             |
| `refresh_token`                                                                                                                                                                                       | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | A token used when refreshing the access token.                                                                                                                                                        |
| `token_expiry_date`                                                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date-time when the access token should be refreshed.                                                                                                                                              |