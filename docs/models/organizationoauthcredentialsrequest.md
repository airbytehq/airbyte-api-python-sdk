# OrganizationOAuthCredentialsRequest

POST body for creating/updating organization level OAuth credentials


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `actor_type`                                                     | [models.ActorTypeEnum](../models/actortypeenum.md)               | :heavy_check_mark:                                               | Whether you're setting this override for a source or destination |
| `configuration`                                                  | *Any*                                                            | :heavy_check_mark:                                               | The values required to configure the source.                     |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | The name of the source i.e. google-ads                           |