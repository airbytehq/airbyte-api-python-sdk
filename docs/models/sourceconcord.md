# ~~SourceConcord~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `api_key`                                                                | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `env`                                                                    | [models.SourceConcordEnvironment](../models/sourceconcordenvironment.md) | :heavy_check_mark:                                                       | The environment from where you want to access the API.                   |
| `source_type`                                                            | [models.Concord](../models/concord.md)                                   | :heavy_check_mark:                                                       | N/A                                                                      |