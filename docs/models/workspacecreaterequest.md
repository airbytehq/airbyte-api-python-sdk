# WorkspaceCreateRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | Name of the workspace                                                    |
| `notifications`                                                          | [Optional[models.NotificationsConfig]](../models/notificationsconfig.md) | :heavy_minus_sign:                                                       | Configures workspace notifications.                                      |
| `organization_id`                                                        | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | ID of organization to add workspace to.                                  |
| `region_id`                                                              | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |