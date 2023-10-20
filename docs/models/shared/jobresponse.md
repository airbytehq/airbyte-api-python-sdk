# JobResponse

Provides details of a single job.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `bytes_synced`                                                          | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connection_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `duration`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Duration of a sync in ISO_8601 format                                   |
| `job_id`                                                                | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `job_type`                                                              | [JobTypeEnum](../../models/shared/jobtypeenum.md)                       | :heavy_check_mark:                                                      | Enum that describes the different types of jobs that the platform runs. |
| `last_updated_at`                                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `rows_synced`                                                           | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `start_time`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `status`                                                                | [JobStatusEnum](../../models/shared/jobstatusenum.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |