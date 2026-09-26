# ~~SourceTrackPms~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `api_key`                                | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `api_secret`                             | *Optional[str]*                          | :heavy_minus_sign:                       | N/A                                      |
| `customer_domain`                        | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `source_type`                            | [models.TrackPms](../models/trackpms.md) | :heavy_check_mark:                       | N/A                                      |