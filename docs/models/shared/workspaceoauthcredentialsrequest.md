# WorkspaceOAuthCredentialsRequest

POST body for creating/updating workspace level OAuth credentials


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `actor_type`                                                                   | [Optional[shared.ActorTypeEnum]](undefined/models/shared/actortypeenum.md)     | :heavy_check_mark:                                                             | Whether you're setting this override for a source or destination               |
| `configuration`                                                                | *Optional[Any]*                                                                | :heavy_check_mark:                                                             | The values required to configure the source.                                   |
| `name`                                                                         | [Optional[shared.OAuthActorNames]](undefined/models/shared/oauthactornames.md) | :heavy_check_mark:                                                             | N/A                                                                            |