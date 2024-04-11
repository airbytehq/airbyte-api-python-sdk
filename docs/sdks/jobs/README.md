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
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.CancelJobRequest(
    job_id=801771,
)

res = s.jobs.cancel_job(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_job

Trigger a sync or reset job of a connection

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = models.JobCreateRequest(
    connection_id='18dccc91-0ab1-4f72-9ed7-0b8fc27c5826',
    job_type=models.JobTypeEnum.SYNC,
)

res = s.jobs.create_job(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_job

Get Job status and details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.GetJobRequest(
    job_id=131101,
)

res = s.jobs.get_job(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_jobs

List Jobs by sync type

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.ListJobsRequest()

res = s.jobs.list_jobs(req)

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
