# PermissionResponseRead

Reformat PermissionResponse with permission scope


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `permission_id`                                             | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `permission_type`                                           | [models.PermissionType](../models/permissiontype.md)        | :heavy_check_mark:                                          | Describes what actions/endpoints the permission entitles to |
| `scope`                                                     | [models.PermissionScope](../models/permissionscope.md)      | :heavy_check_mark:                                          | Scope of a single permission, e.g. workspace, organization  |
| `scope_id`                                                  | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `user_id`                                                   | *str*                                                       | :heavy_check_mark:                                          | Internal Airbyte user ID                                    |