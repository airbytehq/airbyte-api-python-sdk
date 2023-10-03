# JobCreateRequest

Creates a new Job from the configuration provided in the request body.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `connection_id`                                                         | *Optional[str]*                                                         | :heavy_check_mark:                                                      | N/A                                                                     |
| `job_type`                                                              | [Optional[shared.JobTypeEnum]](undefined/models/shared/jobtypeenum.md)  | :heavy_check_mark:                                                      | Enum that describes the different types of jobs that the platform runs. |