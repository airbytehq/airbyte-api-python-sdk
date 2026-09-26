# ~~SourceGetlago~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `api_key`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | Your API Key. See <a href="https://doc.getlago.com/docs/api/intro">here</a>. |
| `api_url`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Your Lago API URL                                                            |
| `source_type`                                                                | [models.Getlago](../models/getlago.md)                                       | :heavy_check_mark:                                                           | N/A                                                                          |