# ~~SourcePostmarkapp~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `x_postmark_account_token`                     | *str*                                          | :heavy_check_mark:                             | API Key for account                            |
| `x_postmark_server_token`                      | *str*                                          | :heavy_check_mark:                             | API Key for server                             |
| `source_type`                                  | [models.Postmarkapp](../models/postmarkapp.md) | :heavy_check_mark:                             | N/A                                            |