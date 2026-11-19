# ~~SourceDatascope~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `api_key`                                  | *str*                                      | :heavy_check_mark:                         | API Key                                    |                                            |
| `source_type`                              | [models.Datascope](../models/datascope.md) | :heavy_check_mark:                         | N/A                                        |                                            |
| `start_date`                               | *str*                                      | :heavy_check_mark:                         | Start date for the data to be replicated   | dd/mm/YYYY HH:MM                           |