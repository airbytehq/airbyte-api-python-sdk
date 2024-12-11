# SourceSimplesat


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `end_date`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Date till when the sync should end                                   |
| `source_type`                                                        | [models.Simplesat](../models/simplesat.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Date from when the sync should start                                 |