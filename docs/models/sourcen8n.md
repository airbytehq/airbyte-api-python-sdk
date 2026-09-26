# ~~SourceN8n~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `api_key`                                                                   | *str*                                                                       | :heavy_check_mark:                                                          | Your API KEY. See <a href="https://docs.n8n.io/api/authentication">here</a> |
| `host`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | Hostname of the n8n instance                                                |
| `source_type`                                                               | [models.N8n](../models/n8n.md)                                              | :heavy_check_mark:                                                          | N/A                                                                         |