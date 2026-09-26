# ~~SourceTempo~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `api_token`                                                                                   | *str*                                                                                         | :heavy_check_mark:                                                                            | Tempo API Token. Go to Tempo>Settings, scroll down to Data Access and select API integration. |
| `source_type`                                                                                 | [models.Tempo](../models/tempo.md)                                                            | :heavy_check_mark:                                                                            | N/A                                                                                           |