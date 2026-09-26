# ~~SourceNocrm~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `api_key`                                                                                       | *str*                                                                                           | :heavy_check_mark:                                                                              | API key to use. Generate it from the admin section of your noCRM.io account.                    |
| `source_type`                                                                                   | [models.Nocrm](../models/nocrm.md)                                                              | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `subdomain`                                                                                     | *str*                                                                                           | :heavy_check_mark:                                                                              | The subdomain specific to your noCRM.io account, e.g., 'yourcompany' in 'yourcompany.nocrm.io'. |