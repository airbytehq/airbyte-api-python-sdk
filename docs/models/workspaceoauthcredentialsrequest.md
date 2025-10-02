# WorkspaceOAuthCredentialsRequest

POST body for creating/updating workspace level OAuth credentials


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `actor_type`                                                     | [models.ActorTypeEnum](../models/actortypeenum.md)               | :heavy_check_mark:                                               | Whether you're setting this override for a source or destination |
| `configuration`                                                  | *Any*                                                            | :heavy_check_mark:                                               | The values required to configure the source.                     |
| `name`                                                           | [models.OAuthActorNames](../models/oauthactornames.md)           | :heavy_check_mark:                                               | N/A                                                              |