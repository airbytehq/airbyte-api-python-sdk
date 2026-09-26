# ~~SourceAkeneo~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `api_username`                        | *str*                                 | :heavy_check_mark:                    | N/A                                   |
| `client_id`                           | *str*                                 | :heavy_check_mark:                    | N/A                                   |
| `host`                                | *str*                                 | :heavy_check_mark:                    | https://cb8715249e.trial.akeneo.cloud |
| `password`                            | *str*                                 | :heavy_check_mark:                    | N/A                                   |
| `secret`                              | *Optional[str]*                       | :heavy_minus_sign:                    | N/A                                   |
| `source_type`                         | [models.Akeneo](../models/akeneo.md)  | :heavy_check_mark:                    | N/A                                   |