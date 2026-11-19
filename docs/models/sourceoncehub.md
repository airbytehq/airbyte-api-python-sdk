# ~~SourceOncehub~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `api_key`                                                                                  | *str*                                                                                      | :heavy_check_mark:                                                                         | API key to use. Find it in your OnceHub account under the API & Webhooks Integration page. |
| `source_type`                                                                              | [models.Oncehub](../models/oncehub.md)                                                     | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `start_date`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                       | :heavy_check_mark:                                                                         | N/A                                                                                        |