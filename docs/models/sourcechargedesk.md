# SourceChargedesk


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `username`                                                   | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `password`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `source_type`                                                | [models.Chargedesk](../models/chargedesk.md)                 | :heavy_check_mark:                                           | N/A                                                          |
| `start_date`                                                 | *Optional[int]*                                              | :heavy_minus_sign:                                           | Date from when the sync should start in epoch Unix timestamp |