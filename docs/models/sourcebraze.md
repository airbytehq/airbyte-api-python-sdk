# ~~SourceBraze~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `api_key`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API key                                                           |
| `source_type`                                                                | [models.Braze](../models/braze.md)                                           | :heavy_check_mark:                                                           | N/A                                                                          |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Rows after this date will be synced                                          |
| `url`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API endpoint                                                      |