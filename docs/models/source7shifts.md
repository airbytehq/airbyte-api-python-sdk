# ~~Source7shifts~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `access_token`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | Access token to use for authentication. Generate it in the 7shifts Developer Tools. |
| `source_type`                                                                       | [models.Sevenshifts](../models/sevenshifts.md)                                      | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `start_date`                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                | :heavy_check_mark:                                                                  | N/A                                                                                 |