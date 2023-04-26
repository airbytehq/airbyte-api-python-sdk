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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CancelJobRequest(
    job_id=565421,
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.JobCreateRequest(
    connection_id="temporibus",
    job_type="sync",
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetJobRequest(
    job_id=204865,
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListJobsRequest(
    connection_id="fugit",
    job_type="sync",
    limit=488056,
    offset=124833,
)

res = s.jobs.list_jobs(req)

if res.jobs_response is not None:
    # handle response
```
