# SourceLinnworks

The values required to configure the source.


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `application_id`                                                                                        | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Linnworks Application ID                                                                                |
| `application_secret`                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Linnworks Application Secret                                                                            |
| `source_type`                                                                                           | [SourceLinnworksLinnworks](../../models/shared/sourcelinnworkslinnworks.md)                             | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `start_date`                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                    | :heavy_check_mark:                                                                                      | UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated. |
| `token`                                                                                                 | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |