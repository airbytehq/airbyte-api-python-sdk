# SourceChameleon


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `end_date`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `filter_`                                                            | [Optional[models.Filter]](../models/filter_.md)                      | :heavy_minus_sign:                                                   | Filter for using in the `segments_experiences` stream                |
| `limit`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Max records per page limit                                           |
| `source_type`                                                        | [models.Chameleon](../models/chameleon.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |