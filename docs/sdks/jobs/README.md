# Jobs
(*jobs*)

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
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.CancelJobRequest(
    job_id=801771,
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
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = shared.JobCreateRequest(
    connection_id='Seychelles',
    job_type=shared.JobTypeEnum.RESET,
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
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.GetJobRequest(
    job_id=131101,
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
import dateutil.parser
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.ListJobsRequest(
    connection_id='Account Brand District',
    created_at_end=dateutil.parser.isoparse('2023-07-31T08:36:30.681Z'),
    created_at_start=dateutil.parser.isoparse('2023-09-12T08:02:55.258Z'),
    job_type=shared.JobTypeEnum.RESET,
    limit=15461,
    offset=82575,
    order_by='reserved Chrysler deposit',
    status=shared.JobStatusEnum.SUCCEEDED,
    updated_at_end=dateutil.parser.isoparse('2021-02-15T00:19:53.913Z'),
    updated_at_start=dateutil.parser.isoparse('2022-01-10T07:46:53.710Z'),
    workspace_ids=[
        'bc4dea63-2e54-40b9-b441-91e8f146d646',
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

