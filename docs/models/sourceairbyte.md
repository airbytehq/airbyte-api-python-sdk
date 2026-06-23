# ~~SourceAirbyte~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `client_id`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `client_secret`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `host`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The Host URL of your Self-Managed Deployment (e.x. airbtye.mydomain.com) |
| `source_type`                                                            | [models.Airbyte](../models/airbyte.md)                                   | :heavy_check_mark:                                                       | N/A                                                                      |
| `start_date`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | N/A                                                                      |