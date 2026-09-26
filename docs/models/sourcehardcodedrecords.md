# ~~SourceHardcodedRecords~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `count`                                                  | *Optional[int]*                                          | :heavy_minus_sign:                                       | How many records per stream should be generated          |
| `source_type`                                            | [models.HardcodedRecords](../models/hardcodedrecords.md) | :heavy_check_mark:                                       | N/A                                                      |