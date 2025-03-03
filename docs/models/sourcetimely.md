# SourceTimely


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The Account ID for your Timely account                               |
| `bearer_token`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The Bearer Token for your Timely account                             |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Earliest date from which you want to pull data from.                 |
| `source_type`                                                        | [models.Timely](../models/timely.md)                                 | :heavy_check_mark:                                                   | N/A                                                                  |