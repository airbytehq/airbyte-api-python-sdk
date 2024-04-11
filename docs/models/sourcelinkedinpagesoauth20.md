# SourceLinkedinPagesOAuth20


## Fields

| Field                                                                                                                                                                                | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                                                          | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The client ID of the LinkedIn developer application.                                                                                                                                 |
| `client_secret`                                                                                                                                                                      | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The client secret of the LinkedIn developer application.                                                                                                                             |
| `refresh_token`                                                                                                                                                                      | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The token value generated using the LinkedIn Developers OAuth Token Tools. See the <a href="https://docs.airbyte.com/integrations/sources/linkedin-pages/">docs</a> to obtain yours. |
| `auth_method`                                                                                                                                                                        | [Optional[models.SourceLinkedinPagesAuthMethod]](../models/sourcelinkedinpagesauthmethod.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                                   | N/A                                                                                                                                                                                  |