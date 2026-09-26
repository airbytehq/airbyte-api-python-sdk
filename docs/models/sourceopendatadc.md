# ~~SourceOpenDataDc~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `api_key`                                        | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `location`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | address or place or block                        |
| `marid`                                          | *Optional[str]*                                  | :heavy_minus_sign:                               | A unique identifier (Master Address Repository). |
| `source_type`                                    | [models.OpenDataDc](../models/opendatadc.md)     | :heavy_check_mark:                               | N/A                                              |