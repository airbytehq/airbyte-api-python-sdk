# sources

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
import airbyte
import dateutil.parser
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceRecharge(
        access_token='laborum',
        source_type=shared.SourceRechargeRecharge.RECHARGE,
        start_date=dateutil.parser.isoparse('2021-05-14T00:00:00Z'),
    ),
    name='Lee Kemmer',
    secret_id='quas',
    workspace_id='dd6b1442-9074-4747-b8a7-bd466d28c10a',
)

res = s.sources.create_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceCreateRequest](../../models/shared/sourcecreaterequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## delete_source

Delete a Source

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteSourceRequest(
    source_id='quidem',
)

res = s.sources.delete_source(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSourceRequest](../../models/operations/deletesourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSourceResponse](../../models/operations/deletesourceresponse.md)**


## get_source

Get Source details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSourceRequest(
    source_id='neque',
)

res = s.sources.get_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**


## initiate_o_auth

Given a source ID, workspace ID, and redirect URL, initiates OAuth for the source.

This returns a fully formed URL for performing user authentication against the relevant source identity provider (IdP). Once authentication has been completed, the IdP will redirect to an Airbyte endpoint which will save the access and refresh tokens off as a secret and return the secret ID to the redirect URL specified in the `secret_id` query string parameter.

That secret ID can be used to create a source with credentials in place of actual tokens.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.InitiateOauthRequest(
    o_auth_input_configuration=shared.OAuthInputConfiguration(),
    redirect_url='quo',
    source_type=shared.OAuthActorNames.TYPEFORM,
    workspace_id='ca425190-4e52-43c7-a0bc-7178e4796f2a',
)

res = s.sources.initiate_o_auth(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InitiateOauthRequest](../../models/shared/initiateoauthrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.InitiateOAuthResponse](../../models/operations/initiateoauthresponse.md)**


## list_sources

List sources

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListSourcesRequest(
    include_deleted=False,
    limit=475289,
    offset=35362,
    workspace_ids=[
        '688282aa-4825-462f-a22e-9817ee17cbe6',
        '1e6b7b95-bc0a-4b3c-a0c4-f3789fd871f9',
        '9dd2efd1-21aa-46f1-a674-bdb04f157560',
        '82d68ea1-9f1d-4170-9133-9d08086a1840',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListSourcesRequest](../../models/operations/listsourcesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSourcesResponse](../../models/operations/listsourcesresponse.md)**


## patch_source

Update a Source

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

req = operations.PatchSourceRequest(
    source_patch_request=shared.SourcePatchRequest(
        configuration=shared.SourceFacebookMarketing(
            access_token='occaecati',
            account_id='111111111111111',
            action_breakdowns_allow_empty=False,
            client_id='numquam',
            client_secret='impedit',
            custom_insights=[
                shared.SourceFacebookMarketingInsightConfig(
                    action_breakdowns=[
                        shared.SourceFacebookMarketingInsightConfigValidActionBreakdowns.ACTION_CANVAS_COMPONENT_NAME,
                        shared.SourceFacebookMarketingInsightConfigValidActionBreakdowns.ACTION_DEVICE,
                    ],
                    action_report_time=shared.SourceFacebookMarketingInsightConfigActionReportTime.CONVERSION,
                    breakdowns=[
                        shared.SourceFacebookMarketingInsightConfigValidBreakdowns.LINK_URL_ASSET,
                        shared.SourceFacebookMarketingInsightConfigValidBreakdowns.DESCRIPTION_ASSET,
                        shared.SourceFacebookMarketingInsightConfigValidBreakdowns.VIDEO_ASSET,
                        shared.SourceFacebookMarketingInsightConfigValidBreakdowns.FREQUENCY_VALUE,
                    ],
                    end_date=dateutil.parser.isoparse('2017-01-26T00:00:00Z'),
                    fields_=[
                        shared.SourceFacebookMarketingInsightConfigValidEnums.AD_ID,
                        shared.SourceFacebookMarketingInsightConfigValidEnums.CPP,
                        shared.SourceFacebookMarketingInsightConfigValidEnums.COST_PER_ESTIMATED_AD_RECALLERS,
                        shared.SourceFacebookMarketingInsightConfigValidEnums.CANVAS_AVG_VIEW_PERCENT,
                    ],
                    insights_lookback_window=831520,
                    level=shared.SourceFacebookMarketingInsightConfigLevel.CAMPAIGN,
                    name='Cody Nikolaus',
                    start_date=dateutil.parser.isoparse('2017-01-25T00:00:00Z'),
                    time_increment=65304,
                ),
            ],
            end_date=dateutil.parser.isoparse('2017-01-26T00:00:00Z'),
            fetch_thumbnail_images=False,
            include_deleted=False,
            insights_lookback_window=312753,
            max_batch_size=783235,
            page_size=801836,
            source_type=shared.SourceFacebookMarketingFacebookMarketing.FACEBOOK_MARKETING,
            start_date=dateutil.parser.isoparse('2017-01-25T00:00:00Z'),
        ),
        name='My source',
        secret_id='labore',
        workspace_id='13aa63aa-e8d6-4786-8dbb-675fd5e60b37',
    ),
    source_id='exercitationem',
)

res = s.sources.patch_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchSourceRequest](../../models/operations/patchsourcerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchSourceResponse](../../models/operations/patchsourceresponse.md)**


## put_source

Update a Source and fully overwrite it

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

req = operations.PutSourceRequest(
    source_put_request=shared.SourcePutRequest(
        configuration=shared.SourceXkcd(
            source_type=shared.SourceXkcdXkcd.XKCD,
        ),
        name='Jesus Yost',
    ),
    source_id='quidem',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PutSourceRequest](../../models/operations/putsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PutSourceResponse](../../models/operations/putsourceresponse.md)**

