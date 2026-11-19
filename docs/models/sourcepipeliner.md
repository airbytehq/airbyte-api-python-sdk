# ~~SourcePipeliner~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `password`                                                                 | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `service`                                                                  | [models.SourcePipelinerDataCenter](../models/sourcepipelinerdatacenter.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `source_type`                                                              | [models.Pipeliner](../models/pipeliner.md)                                 | :heavy_check_mark:                                                         | N/A                                                                        |
| `spaceid`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `username`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |