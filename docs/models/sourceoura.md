# SourceOura


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `api_key`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | API Key                                                                    |
| `end_datetime`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | End datetime to sync until. Default is current UTC datetime.               |
| `source_type`                                                              | [models.Oura](../models/oura.md)                                           | :heavy_check_mark:                                                         | N/A                                                                        |
| `start_datetime`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | Start datetime to sync from. Default is current UTC datetime minus 1<br/>day.<br/> |