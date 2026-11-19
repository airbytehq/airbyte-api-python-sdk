# ~~SourceRecreation~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `apikey`                                     | *str*                                        | :heavy_check_mark:                           | API Key                                      |
| `query_campsites`                            | *Optional[str]*                              | :heavy_minus_sign:                           | N/A                                          |
| `source_type`                                | [models.Recreation](../models/recreation.md) | :heavy_check_mark:                           | N/A                                          |