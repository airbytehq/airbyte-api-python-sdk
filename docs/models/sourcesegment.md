# ~~SourceSegment~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_token`                                                          | *str*                                                                | :heavy_check_mark:                                                   | API token to use. Generate it in Segment's Workspace settings.       |
| `region`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The region for the API, e.g., 'api' for US or 'eu1' for EU           |
| `source_type`                                                        | [models.Segment](../models/segment.md)                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |