# ~~SourcePiwik~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `client_id`                                                | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `client_secret`                                            | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `organization_id`                                          | *str*                                                      | :heavy_check_mark:                                         | The organization id appearing at URL of your piwik website |
| `source_type`                                              | [models.Piwik](../models/piwik.md)                         | :heavy_check_mark:                                         | N/A                                                        |