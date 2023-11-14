# WorkspaceOAuthCredentialsRequest

POST body for creating/updating workspace level OAuth credentials


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `actor_type`                                                     | [shared.ActorTypeEnum](../../models/shared/actortypeenum.md)     | :heavy_check_mark:                                               | Whether you're setting this override for a source or destination |
| `configuration`                                                  | *Any*                                                            | :heavy_check_mark:                                               | The values required to configure the source.                     |
| `name`                                                           | [shared.OAuthActorNames](../../models/shared/oauthactornames.md) | :heavy_check_mark:                                               | N/A                                                              |