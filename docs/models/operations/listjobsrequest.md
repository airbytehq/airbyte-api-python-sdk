# ListJobsRequest


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `connection_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | Filter the Jobs by connectionId.                                      |
| `job_type`                                                            | [Optional[shared.JobTypeEnum]](../../models/shared/jobtypeenum.md)    | :heavy_minus_sign:                                                    | Filter the Jobs by jobType.                                           |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Set the limit on the number of Jobs returned. The default is 20 Jobs. |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Set the offset to start at when returning Jobs. The default is 0.     |