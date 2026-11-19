# ~~SourceDrift~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `credentials`                                                                                  | [Optional[models.SourceDriftAuthorizationMethod]](../models/sourcedriftauthorizationmethod.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `email`                                                                                        | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Email used as parameter for contacts stream                                                    |
| `source_type`                                                                                  | [models.DriftEnum](../models/driftenum.md)                                                     | :heavy_check_mark:                                                                             | N/A                                                                                            |