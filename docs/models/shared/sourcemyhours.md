# SourceMyHours


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `email`                                          | *str*                                            | :heavy_check_mark:                               | Your My Hours username                           | john@doe.com                                     |
| `logs_batch_size`                                | *Optional[int]*                                  | :heavy_minus_sign:                               | Pagination size used for retrieving logs in days | 30                                               |
| `password`                                       | *str*                                            | :heavy_check_mark:                               | The password associated to the username          |                                                  |
| `source_type`                                    | [shared.MyHours](../../models/shared/myhours.md) | :heavy_check_mark:                               | N/A                                              |                                                  |
| `start_date`                                     | *str*                                            | :heavy_check_mark:                               | Start date for collecting time logs              | %Y-%m-%d                                         |