# ~~SourceDelighted~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `api_key`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | A Delighted API key.                                                       |                                                                            |
| `since`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_check_mark:                                                         | The date from which you'd like to replicate the data                       | **Example 1:** 2022-05-30T04:50:23Z<br/>**Example 2:** 2022-05-30 04:50:23 |
| `source_type`                                                              | [models.Delighted](../models/delighted.md)                                 | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |