# SourceWrike


## Fields

| Field                                                                                                                                                                  | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            | Example                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                         | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Permanent access token. You can find documentation on how to acquire a permanent access token  <a href="https://developers.wrike.com/oauth-20-authorization/">here</a> |                                                                                                                                                                        |
| `source_type`                                                                                                                                                          | [models.Wrike](../models/wrike.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                     | N/A                                                                                                                                                                    |                                                                                                                                                                        |
| `start_date`                                                                                                                                                           | *Optional[str]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | UTC date and time in the format 2017-01-25T00:00:00Z. Only comments after this date will be replicated.                                                                | 2017-01-25T00:00:00Z                                                                                                                                                   |
| `wrike_instance`                                                                                                                                                       | *Optional[str]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Wrike's instance such as `app-us2.wrike.com`                                                                                                                           |                                                                                                                                                                        |