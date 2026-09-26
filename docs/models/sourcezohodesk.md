# ~~SourceZohoDesk~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `client_id`                              | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `client_secret`                          | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `include_custom_domain`                  | *Optional[bool]*                         | :heavy_minus_sign:                       | N/A                                      |
| `refresh_token`                          | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `source_type`                            | [models.ZohoDesk](../models/zohodesk.md) | :heavy_check_mark:                       | N/A                                      |
| `token_refresh_endpoint`                 | *str*                                    | :heavy_check_mark:                       | N/A                                      |