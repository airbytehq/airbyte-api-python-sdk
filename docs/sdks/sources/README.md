# Sources
(*sources*)

### Available Operations

* [create_source](#create_source) - Create a source
* [delete_source](#delete_source) - Delete a Source
* [get_source](#get_source) - Get Source details
* [initiate_o_auth](#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](#list_sources) - List sources
* [patch_source](#patch_source) - Update a Source
* [put_source](#put_source) - Update a Source and fully overwrite it

## create_source

Creates a source given a name, workspace id, and a json blob containing the configuration for the source.

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.SourceCreateRequest(
    configuration='<value>',
    name='<value>',
    workspace_id='a2cf0f31-f3dd-4c98-88c3-4bdfb109056a',
)

res = s.sources.create_source(req)

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [models.SourceCreateRequest](../../models/sourcecreaterequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[models.CreateSourceResponse](../../models/createsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_source

Delete a Source

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.DeleteSourceRequest(
    source_id='<value>',
)

res = s.sources.delete_source(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [models.DeleteSourceRequest](../../models/deletesourcerequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[models.DeleteSourceResponse](../../models/deletesourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_source

Get Source details

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.GetSourceRequest(
    source_id='<value>',
)

res = s.sources.get_source(req)

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.GetSourceRequest](../../models/getsourcerequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[models.GetSourceResponse](../../models/getsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## initiate_o_auth

Given a source ID, workspace ID, and redirect URL, initiates OAuth for the source.

This returns a fully formed URL for performing user authentication against the relevant source identity provider (IdP). Once authentication has been completed, the IdP will redirect to an Airbyte endpoint which will save the access and refresh tokens off as a secret and return the secret ID to the redirect URL specified in the `secret_id` query string parameter.

That secret ID can be used to create a source with credentials in place of actual tokens.

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.InitiateOauthRequest(
    redirect_url='https://cloud.airbyte.io/v1/api/oauth/callback',
    workspace_id='871d9b60-11d1-44cb-8c92-c246d53bf87e',
    o_auth_input_configuration=airbyte_api.OAuthInputConfiguration(),
)

res = s.sources.initiate_o_auth(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.InitiateOauthRequest](../../models/initiateoauthrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[models.InitiateOAuthResponse](../../models/initiateoauthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_sources

List sources

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.ListSourcesRequest()

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [models.ListSourcesRequest](../../models/listsourcesrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[models.ListSourcesResponse](../../models/listsourcesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## patch_source

Update a Source

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.PatchSourceRequest(
    source_id='<value>',
)

res = s.sources.patch_source(req)

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [models.PatchSourceRequest](../../models/patchsourcerequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[models.PatchSourceResponse](../../models/patchsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_source

Update a Source and fully overwrite it

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.PutSourceRequest(
    source_id='<value>',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.PutSourceRequest](../../models/putsourcerequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[models.PutSourceResponse](../../models/putsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
