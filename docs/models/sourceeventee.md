# ~~SourceEventee~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `api_token`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | API token to use. Generate it at https://admin.eventee.co/ in 'Settings -> Features'. |
| `source_type`                                                                         | [models.Eventee](../models/eventee.md)                                                | :heavy_check_mark:                                                                    | N/A                                                                                   |