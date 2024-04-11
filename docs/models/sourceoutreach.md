# SourceOutreach


## Fields

| Field                                                                                                                                                                         | Type                                                                                                                                                                          | Required                                                                                                                                                                      | Description                                                                                                                                                                   | Example                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                                                                   | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | The Client ID of your Outreach developer application.                                                                                                                         |                                                                                                                                                                               |
| `client_secret`                                                                                                                                                               | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | The Client Secret of your Outreach developer application.                                                                                                                     |                                                                                                                                                                               |
| `redirect_uri`                                                                                                                                                                | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | A Redirect URI is the location where the authorization server sends the user once the app has been successfully authorized and granted an authorization code or access token. |                                                                                                                                                                               |
| `refresh_token`                                                                                                                                                               | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | The token for obtaining the new access token.                                                                                                                                 |                                                                                                                                                                               |
| `start_date`                                                                                                                                                                  | *str*                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                            | The date from which you'd like to replicate data for Outreach API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated.                 | 2020-11-16T00:00:00Z                                                                                                                                                          |
| `source_type`                                                                                                                                                                 | [models.Outreach](../models/outreach.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                            | N/A                                                                                                                                                                           |                                                                                                                                                                               |