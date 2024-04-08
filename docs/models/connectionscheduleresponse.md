# ConnectionScheduleResponse

schedule for when the the connection should run, per the schedule type


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `schedule_type`                                                            | [models.ScheduleTypeWithBasicEnum](../models/scheduletypewithbasicenum.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `basic_timing`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `cron_expression`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |