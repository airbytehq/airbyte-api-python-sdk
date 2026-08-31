# Jobs

## Overview

### Available Operations

* [cancel_job](#cancel_job) - Cancel a running Job
* [create_job](#create_job) - Trigger a sync or reset job of a connection
* [get_job](#get_job) - Get Job status and details
* [list_jobs](#list_jobs) - List Jobs by sync type

## cancel_job

Cancel a running Job

### Example Usage

<!-- UsageSnippet language="python" operationID="cancelJob" method="delete" path="/jobs/{jobId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.jobs.cancel_job(request={
        "job_id": 621441,
    })

    assert res.job_response is not None

    # Handle response
    print(res.job_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.CancelJobRequest](../../api/canceljobrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.CancelJobResponse](../../api/canceljobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_job

Trigger a sync or reset job of a connection

### Example Usage: Job Creation Request Example

<!-- UsageSnippet language="python" operationID="createJob" method="post" path="/jobs" example="Job Creation Request Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.jobs.create_job(request={
        "connection_id": "e735894a-e773-4938-969f-45f53957b75b",
        "job_type": models.JobTypeEnum.SYNC,
    })

    assert res.job_response is not None

    # Handle response
    print(res.job_response)

```
### Example Usage: Job Creation Response Example

<!-- UsageSnippet language="python" operationID="createJob" method="post" path="/jobs" example="Job Creation Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.jobs.create_job(request={
        "connection_id": "18dccc91-0ab1-4f72-9ed7-0b8fc27c5826",
        "job_type": models.JobTypeEnum.SYNC,
    })

    assert res.job_response is not None

    # Handle response
    print(res.job_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.JobCreateRequest](../../models/jobcreaterequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.CreateJobResponse](../../api/createjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_job

Get Job status and details

### Example Usage

<!-- UsageSnippet language="python" operationID="getJob" method="get" path="/jobs/{jobId}" example="Job Get Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.jobs.get_job(request={
        "job_id": 245534,
    })

    assert res.job_response is not None

    # Handle response
    print(res.job_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetJobRequest](../../api/getjobrequest.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetJobResponse](../../api/getjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_jobs

List Jobs by sync type

### Example Usage

<!-- UsageSnippet language="python" operationID="listJobs" method="get" path="/jobs" example="Job List Response Example" -->
```python
from airbyte_api import AirbyteAPI, models
from airbyte_api.utils import parse_datetime


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.jobs.list_jobs(request={
        "created_at_start": parse_datetime("2024-04-14T21:55:04.172Z"),
        "created_at_end": parse_datetime("2024-11-05T02:58:38.581Z"),
        "updated_at_start": parse_datetime("2026-10-05T17:24:30.764Z"),
        "updated_at_end": parse_datetime("2025-11-15T07:41:11.221Z"),
        "order_by": "updatedAt|DESC",
    })

    assert res.jobs_response is not None

    # Handle response
    print(res.jobs_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListJobsRequest](../../api/listjobsrequest.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListJobsResponse](../../api/listjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |