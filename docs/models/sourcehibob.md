# ~~SourceHibob~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `is_sandbox`                                     | *bool*                                           | :heavy_check_mark:                               | Toggle true if this instance is a HiBob sandbox  |
| `password`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `source_type`                                    | [models.Hibob](../models/hibob.md)               | :heavy_check_mark:                               | N/A                                              |
| `username`                                       | *str*                                            | :heavy_check_mark:                               | N/A                                              |