# ~~SourceCirca~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `api_key`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | API key to use. Find it at https://app.circa.co/settings/integrations/api |
| `source_type`                                                             | [models.Circa](../models/circa.md)                                        | :heavy_check_mark:                                                        | N/A                                                                       |
| `start_date`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)      | :heavy_check_mark:                                                        | N/A                                                                       |