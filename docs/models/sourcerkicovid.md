# ~~SourceRkiCovid~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `source_type`                                                                        | [models.RkiCovid](../models/rkicovid.md)                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `start_date`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | UTC date in the format 2017-01-25. Any data before this date will not be replicated. |