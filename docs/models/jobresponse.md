# JobResponse

Provides details of a single job.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `connection_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `job_id`                                                                | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `job_type`                                                              | [models.JobTypeEnum](../models/jobtypeenum.md)                          | :heavy_check_mark:                                                      | Enum that describes the different types of jobs that the platform runs. |
| `start_time`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `status`                                                                | [models.JobStatusEnum](../models/jobstatusenum.md)                      | :heavy_check_mark:                                                      | N/A                                                                     |
| `bytes_synced`                                                          | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `duration`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Duration of a sync in ISO_8601 format                                   |
| `last_updated_at`                                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `rows_synced`                                                           | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |