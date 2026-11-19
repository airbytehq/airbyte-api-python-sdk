# ~~SourceGridly~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `api_key`                              | *str*                                  | :heavy_check_mark:                     | N/A                                    |
| `grid_id`                              | *str*                                  | :heavy_check_mark:                     | ID of a grid, or can be ID of a branch |
| `source_type`                          | [models.Gridly](../models/gridly.md)   | :heavy_check_mark:                     | N/A                                    |