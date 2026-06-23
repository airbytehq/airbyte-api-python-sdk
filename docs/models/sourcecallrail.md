# ~~SourceCallrail~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `account_id`                             | *str*                                    | :heavy_check_mark:                       | Account ID                               |                                          |
| `api_key`                                | *str*                                    | :heavy_check_mark:                       | API access key                           |                                          |
| `source_type`                            | [models.Callrail](../models/callrail.md) | :heavy_check_mark:                       | N/A                                      |                                          |
| `start_date`                             | *str*                                    | :heavy_check_mark:                       | Start getting data from that date.       | %Y-%m-%d                                 |