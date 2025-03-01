# WorkspaceResponse

Provides details of a single workspace.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `notifications`                                                | [models.NotificationsConfig](../models/notificationsconfig.md) | :heavy_check_mark:                                             | Configures workspace notifications.                            |
| `workspace_id`                                                 | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `data_residency`                                               | [Optional[models.GeographyEnum]](../models/geographyenum.md)   | :heavy_minus_sign:                                             | N/A                                                            |