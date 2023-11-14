# ConnectionScheduleResponse

schedule for when the the connection should run, per the schedule type


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `basic_timing`                                                                       | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `cron_expression`                                                                    | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `schedule_type`                                                                      | [shared.ScheduleTypeWithBasicEnum](../../models/shared/scheduletypewithbasicenum.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |