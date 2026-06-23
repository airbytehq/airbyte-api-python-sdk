# ~~SourcePicqer~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_name`                                                  | *str*                                                                | :heavy_check_mark:                                                   | The organization name which is used to login to picqer               |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `source_type`                                                        | [models.Picqer](../models/picqer.md)                                 | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `username`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |