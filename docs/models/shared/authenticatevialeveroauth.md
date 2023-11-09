# AuthenticateViaLeverOAuth

Choose how to authenticate to Lever Hiring.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `auth_type`                                                                                    | [Optional[shared.SourceLeverHiringAuthType]](../../models/shared/sourceleverhiringauthtype.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `client_id`                                                                                    | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The Client ID of your Lever Hiring developer application.                                      |
| `client_secret`                                                                                | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The Client Secret of your Lever Hiring developer application.                                  |
| `refresh_token`                                                                                | *str*                                                                                          | :heavy_check_mark:                                                                             | The token for obtaining new access token.                                                      |