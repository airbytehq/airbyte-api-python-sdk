# ~~SourceHarness~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `account_id`                               | *str*                                      | :heavy_check_mark:                         | Harness Account ID                         |                                            |
| `api_key`                                  | *str*                                      | :heavy_check_mark:                         | N/A                                        |                                            |
| `api_url`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | The API URL for fetching data from Harness | https://my-harness-server.example.com      |
| `source_type`                              | [models.Harness](../models/harness.md)     | :heavy_check_mark:                         | N/A                                        |                                            |