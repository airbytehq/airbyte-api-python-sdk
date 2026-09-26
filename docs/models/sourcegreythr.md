# ~~SourceGreythr~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `base_url`                             | *str*                                  | :heavy_check_mark:                     | https://api.greythr.com                |
| `domain`                               | *str*                                  | :heavy_check_mark:                     | Your GreytHR Host URL                  |
| `password`                             | *Optional[str]*                        | :heavy_minus_sign:                     | N/A                                    |
| `source_type`                          | [models.Greythr](../models/greythr.md) | :heavy_check_mark:                     | N/A                                    |
| `username`                             | *str*                                  | :heavy_check_mark:                     | N/A                                    |