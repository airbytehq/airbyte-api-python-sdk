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
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CancelJobRequest(
    job_id=708548,
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
    connection_id='vero',
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
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetJobRequest(
    job_id=293020,
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
        bearer_auth="",
    ),
)

req = operations.ListJobsRequest(
    connection_id='quibusdam',
    created_at_end=dateutil.parser.isoparse('2022-06-02T04:41:10.492Z'),
    created_at_start=dateutil.parser.isoparse('2021-06-15T11:19:41.363Z'),
    job_type=shared.JobTypeEnum.SYNC,
    limit=974259,
    offset=347233,
    order_by='nulla',
    status=shared.JobStatusEnum.PENDING,
    updated_at_end=dateutil.parser.isoparse('2020-01-21T21:31:25.345Z'),
    updated_at_start=dateutil.parser.isoparse('2021-07-26T04:25:41.517Z'),
    workspace_ids=[
        '70a45626-d436-4813-b16d-9f5fce6c5561',
        '46c3e250-fb00-48c4-ae14-1aac366c8dd6',
        'b1442907-4747-478a-bbd4-66d28c10ab3c',
        'dca42519-04e5-423c-be0b-c7178e4796f2',
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

