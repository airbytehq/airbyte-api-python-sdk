# ~~SourceFreshchat~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_name`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The unique account name for your Freshchat instance                  |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `source_type`                                                        | [models.Freshchat](../models/freshchat.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |