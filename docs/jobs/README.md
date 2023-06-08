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
    job_id=240829,
)

res = s.jobs.cancel_job(req)

if res.job_response is not None:
    # handle response
```

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
    connection_id='dolorum',
    job_type=shared.JobTypeEnum.SYNC,
)

res = s.jobs.create_job(req)

if res.job_response is not None:
    # handle response
```

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
    job_id=63038,
)

res = s.jobs.get_job(req)

if res.job_response is not None:
    # handle response
```

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
    connection_id='aut',
    job_type=shared.JobTypeEnum.RESET,
    limit=929530,
    offset=9240,
)

res = s.jobs.list_jobs(req)

if res.jobs_response is not None:
    # handle response
```
