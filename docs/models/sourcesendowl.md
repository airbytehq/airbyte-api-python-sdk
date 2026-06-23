# ~~SourceSendowl~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Enter your API secret                                                |
| `source_type`                                                        | [models.Sendowl](../models/sendowl.md)                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `username`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Enter you API Key                                                    |