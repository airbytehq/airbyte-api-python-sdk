# ~~SourcePretix~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_token`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | API token to use. Obtain it from the pretix web interface by creating a new token under your team settings. |
| `source_type`                                                                                               | [models.Pretix](../models/pretix.md)                                                                        | :heavy_check_mark:                                                                                          | N/A                                                                                                         |