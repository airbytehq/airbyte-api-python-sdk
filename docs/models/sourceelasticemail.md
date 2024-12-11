# SourceElasticemail


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `scope_type`                                                         | [Optional[models.ScopeType]](../models/scopetype.md)                 | :heavy_minus_sign:                                                   | N/A                                                                  |
| `source_type`                                                        | [models.Elasticemail](../models/elasticemail.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |