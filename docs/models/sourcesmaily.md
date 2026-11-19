# ~~SourceSmaily~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `api_password`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | API user password. See https://smaily.com/help/api/general/create-api-user/ |
| `api_subdomain`                                                             | *str*                                                                       | :heavy_check_mark:                                                          | API Subdomain. See https://smaily.com/help/api/general/create-api-user/     |
| `api_username`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | API user username. See https://smaily.com/help/api/general/create-api-user/ |
| `source_type`                                                               | [models.Smaily](../models/smaily.md)                                        | :heavy_check_mark:                                                          | N/A                                                                         |