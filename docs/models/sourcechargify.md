# ~~SourceChargify~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `api_key`                                                          | *str*                                                              | :heavy_check_mark:                                                 | Maxio Advanced Billing/Chargify API Key.                           |
| `domain`                                                           | *str*                                                              | :heavy_check_mark:                                                 | Chargify domain. Normally this domain follows the following format |
| `password`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `source_type`                                                      | [models.Chargify](../models/chargify.md)                           | :heavy_check_mark:                                                 | N/A                                                                |
| `username`                                                         | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |