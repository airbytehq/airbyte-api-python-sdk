# SourceMyHours

The values required to configure the source.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `email`                                          | *Optional[str]*                                  | :heavy_check_mark:                               | Your My Hours username                           | john@doe.com                                     |
| `logs_batch_size`                                | *Optional[int]*                                  | :heavy_minus_sign:                               | Pagination size used for retrieving logs in days | 30                                               |
| `password`                                       | *Optional[str]*                                  | :heavy_check_mark:                               | The password associated to the username          |                                                  |
| `source_type`                                    | *Optional[str]*                                  | :heavy_check_mark:                               | N/A                                              |                                                  |
| `start_date`                                     | *Optional[str]*                                  | :heavy_check_mark:                               | Start date for collecting time logs              | %Y-%m-%d                                         |