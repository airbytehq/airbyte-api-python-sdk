# ~~SourceMode~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `api_secret`                                                | *str*                                                       | :heavy_check_mark:                                          | API secret to use as the password for Basic Authentication. |
| `api_token`                                                 | *str*                                                       | :heavy_check_mark:                                          | API token to use as the username for Basic Authentication.  |
| `source_type`                                               | [models.SourceModeMode](../models/sourcemodemode.md)        | :heavy_check_mark:                                          | N/A                                                         |
| `workspace`                                                 | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |