# SourceGoogleTasks


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `records_limit`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The maximum number of records to be returned per request             |
| `source_type`                                                        | [models.GoogleTasks](../models/googletasks.md)                       | :heavy_check_mark:                                                   | N/A                                                                  |