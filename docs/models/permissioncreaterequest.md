# PermissionCreateRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `permission_type`                                           | [models.PermissionType](../models/permissiontype.md)        | :heavy_check_mark:                                          | Describes what actions/endpoints the permission entitles to |
| `user_id`                                                   | *str*                                                       | :heavy_check_mark:                                          | Internal Airbyte user ID                                    |
| `organization_id`                                           | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `workspace_id`                                              | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |