# SourceAppfigures


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_key`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `group_by`                                                           | [Optional[models.GroupBy]](../models/groupby.md)                     | :heavy_minus_sign:                                                   | Category term for grouping the search results                        |
| `search_store`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The store which needs to be searched in streams                      |
| `source_type`                                                        | [models.Appfigures](../models/appfigures.md)                         | :heavy_check_mark:                                                   | N/A                                                                  |