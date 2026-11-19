# ~~SourceUptick~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `base_url`                                             | *str*                                                  | :heavy_check_mark:                                     | eg. https://demo-fire.onuptick.com (no trailing slash) |
| `client_id`                                            | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `client_secret`                                        | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `password`                                             | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `source_type`                                          | [models.Uptick](../models/uptick.md)                   | :heavy_check_mark:                                     | N/A                                                    |
| `username`                                             | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |