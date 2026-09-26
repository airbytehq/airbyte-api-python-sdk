# ~~SourceJamfPro~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `password`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `source_type`                                    | [models.JamfPro](../models/jamfpro.md)           | :heavy_check_mark:                               | N/A                                              |
| `subdomain`                                      | *str*                                            | :heavy_check_mark:                               | The unique subdomain for your Jamf Pro instance. |
| `username`                                       | *str*                                            | :heavy_check_mark:                               | N/A                                              |