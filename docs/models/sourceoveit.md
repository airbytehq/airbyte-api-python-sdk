# ~~SourceOveit~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `email`                            | *str*                              | :heavy_check_mark:                 | Oveit's login Email                |
| `password`                         | *str*                              | :heavy_check_mark:                 | Oveit's login Password             |
| `source_type`                      | [models.Oveit](../models/oveit.md) | :heavy_check_mark:                 | N/A                                |