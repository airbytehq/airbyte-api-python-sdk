# SourceMissive


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `kind`                                                               | [Optional[models.Kind]](../models/kind.md)                           | :heavy_minus_sign:                                                   | Kind parameter for `contact_groups` stream                           |
| `limit`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Max records per page limit                                           |
| `source_type`                                                        | [models.Missive](../models/missive.md)                               | :heavy_check_mark:                                                   | N/A                                                                  |