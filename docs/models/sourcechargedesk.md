# ~~SourceChargedesk~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `password`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `source_type`                                                | [models.Chargedesk](../models/chargedesk.md)                 | :heavy_check_mark:                                           | N/A                                                          |
| `start_date`                                                 | *Optional[int]*                                              | :heavy_minus_sign:                                           | Date from when the sync should start in epoch Unix timestamp |
| `username`                                                   | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |