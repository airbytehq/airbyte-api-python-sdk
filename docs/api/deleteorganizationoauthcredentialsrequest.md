# DeleteOrganizationOAuthCredentialsRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `organization_id`                                                | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `actor_type`                                                     | [models.ActorTypeEnum](../models/actortypeenum.md)               | :heavy_check_mark:                                               | Whether you're setting this override for a source or destination |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | The name of the source or destination i.e. google-ads            |