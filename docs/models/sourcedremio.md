# ~~SourceDremio~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `api_key`                                                     | *str*                                                         | :heavy_check_mark:                                            | API Key that is generated when you authenticate to Dremio API |
| `base_url`                                                    | *Optional[str]*                                               | :heavy_minus_sign:                                            | URL of your Dremio instance                                   |
| `source_type`                                                 | [models.Dremio](../models/dremio.md)                          | :heavy_check_mark:                                            | N/A                                                           |