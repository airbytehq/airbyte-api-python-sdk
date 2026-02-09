# SourceOutlook


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `client_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | The Client ID of your Microsoft Azure application                         |
| `client_secret`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | The Client Secret of your Microsoft Azure application                     |
| `refresh_token`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | Refresh token obtained from Microsoft OAuth flow                          |
| `source_type`                                                             | [models.Outlook](../models/outlook.md)                                    | :heavy_check_mark:                                                        | N/A                                                                       |
| `tenant_id`                                                               | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Azure AD Tenant ID (optional for multi-tenant apps, defaults to 'common') |