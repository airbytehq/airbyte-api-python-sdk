# AirbyteAPIConnectionSchedule

schedule for when the the connection should run, per the schedule type


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `schedule_type`                                          | [models.ScheduleTypeEnum](../models/scheduletypeenum.md) | :heavy_check_mark:                                       | N/A                                                      |
| `cron_expression`                                        | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |