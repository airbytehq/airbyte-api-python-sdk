# SourceDixa

The values required to configure the source.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_token`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Dixa API token                                                       |                                                                      |
| `batch_size`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Number of days to batch into one request. Max 31.                    | 1                                                                    |
| `source_type`                                                        | [shared.Dixa](../../models/shared/dixa.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The connector pulls records updated from this date onwards.          | YYYY-MM-DD                                                           |