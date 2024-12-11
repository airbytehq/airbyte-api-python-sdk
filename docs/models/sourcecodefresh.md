# SourceCodefresh


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `account_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `report_date_range`                                                  | List[*Any*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `report_granularity`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `source_type`                                                        | [models.Codefresh](../models/codefresh.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |