# ~~SourceTavus~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `api_key`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | Your Tavus API key. You can find this in your Tavus account settings or API dashboard. |
| `source_type`                                                                          | [models.Tavus](../models/tavus.md)                                                     | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `start_date`                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                   | :heavy_check_mark:                                                                     | N/A                                                                                    |