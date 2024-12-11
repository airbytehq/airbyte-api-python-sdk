# SourceTestrail


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `domain_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The unique domain name for accessing testrail                        |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `username`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `source_type`                                                        | [models.Testrail](../models/testrail.md)                             | :heavy_check_mark:                                                   | N/A                                                                  |