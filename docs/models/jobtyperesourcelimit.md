# JobTypeResourceLimit

sets resource requirements for a specific job type for an actor or actor definition. these values override the default, if both are set.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `job_type`                                                                      | [models.JobType](../models/jobtype.md)                                          | :heavy_check_mark:                                                              | enum that describes the different types of jobs that the platform runs.         |
| `resource_requirements`                                                         | [models.ResourceRequirements](../models/resourcerequirements.md)                | :heavy_check_mark:                                                              | optional resource requirements to run workers (blank for unbounded allocations) |