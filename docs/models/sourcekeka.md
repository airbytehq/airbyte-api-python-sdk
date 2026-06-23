# ~~SourceKeka~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `api_key`                                     | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `client_id`                                   | *str*                                         | :heavy_check_mark:                            | Your client identifier for authentication.    |
| `client_secret`                               | *str*                                         | :heavy_check_mark:                            | Your client secret for secure authentication. |
| `grant_type`                                  | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `scope`                                       | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `source_type`                                 | [models.Keka](../models/keka.md)              | :heavy_check_mark:                            | N/A                                           |