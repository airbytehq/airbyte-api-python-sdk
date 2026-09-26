# ~~SourceLightspeedRetail~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `api_key`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | API key or access token                                                             |
| `source_type`                                                                       | [models.LightspeedRetail](../models/lightspeedretail.md)                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `subdomain`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | The subdomain for the retailer, e.g., 'example' in 'example.retail.lightspeed.app'. |