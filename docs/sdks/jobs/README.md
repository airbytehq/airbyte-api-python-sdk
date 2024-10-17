# Jobs
(*jobs*)

## Overview

### Available Operations

* [cancel_job](#cancel_job) - Cancel a running Job
* [create_job](#create_job) - Trigger a sync or reset job of a connection
* [get_job](#get_job) - Get Job status and details
* [list_jobs](#list_jobs) - List Jobs by sync type

## cancel_job

Cancel a running Job

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.jobs.cancel_job(request=api.CancelJobRequest(
    job_id=801771,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.CancelJobRequest](../../api/canceljobrequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |

### Response

**[api.CancelJobResponse](../../api/canceljobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_job

Trigger a sync or reset job of a connection

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.jobs.create_job(request=models.JobCreateRequest(
    connection_id='e735894a-e773-4938-969f-45f53957b75b',
    job_type=models.JobTypeEnum.SYNC,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.JobCreateRequest](../../models/jobcreaterequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |

### Response

**[api.CreateJobResponse](../../api/createjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_job

Get Job status and details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.jobs.get_job(request=api.GetJobRequest(
    job_id=131101,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `request`                                       | [api.GetJobRequest](../../api/getjobrequest.md) | :heavy_check_mark:                              | The request object to use for the request.      |

### Response

**[api.GetJobResponse](../../api/getjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_jobs

List Jobs by sync type

### Example Usage

```python
import airbyte_api
import dateutil.parser
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.jobs.list_jobs(request=api.ListJobsRequest(
    created_at_end=dateutil.parser.isoparse('1687450500000'),
    created_at_start=dateutil.parser.isoparse('1687450500000'),
    order_by='updatedAt|DESC',
    updated_at_end=dateutil.parser.isoparse('1687450500000'),
    updated_at_start=dateutil.parser.isoparse('1687450500000'),
))

if res.jobs_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                           | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `request`                                           | [api.ListJobsRequest](../../api/listjobsrequest.md) | :heavy_check_mark:                                  | The request object to use for the request.          |

### Response

**[api.ListJobsResponse](../../api/listjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |