# jobs

### Available Operations

* [cancel_job](#cancel_job) - Cancel a running Job
* [create_job](#create_job) - Trigger a sync or reset job of a connection
* [get_job](#get_job) - Get Job status and details
* [list_jobs](#list_jobs) - List Jobs by sync type

## cancel_job

Cancel a running Job

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CancelJobRequest(
    job_id=961937,
)

res = s.jobs.cancel_job(req)

if res.job_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CancelJobRequest](../../models/operations/canceljobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CancelJobResponse](../../models/operations/canceljobresponse.md)**


## create_job

Trigger a sync or reset job of a connection

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.JobCreateRequest(
    connection_id='dolorem',
    job_type=shared.JobTypeEnum.SYNC,
)

res = s.jobs.create_job(req)

if res.job_response is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobCreateRequest](../../models/shared/jobcreaterequest.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CreateJobResponse](../../models/operations/createjobresponse.md)**


## get_job

Get Job status and details

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetJobRequest(
    job_id=286915,
)

res = s.jobs.get_job(req)

if res.job_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetJobRequest](../../models/operations/getjobrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GetJobResponse](../../models/operations/getjobresponse.md)**


## list_jobs

List Jobs by sync type

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListJobsRequest(
    connection_id='adipisci',
    job_type=shared.JobTypeEnum.RESET,
    limit=100294,
    offset=63038,
    workspace_ids=[
        '8e0adcf4-b921-4879-bce9-53f73ef7fbc7',
    ],
)

res = s.jobs.list_jobs(req)

if res.jobs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListJobsRequest](../../models/operations/listjobsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**

