# ~~SourceApptivo~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `access_key`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `api_key`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | API key to use. Find it in your Apptivo account under Business Settings -> API Access. |
| `source_type`                                                                          | [models.Apptivo](../models/apptivo.md)                                                 | :heavy_check_mark:                                                                     | N/A                                                                                    |