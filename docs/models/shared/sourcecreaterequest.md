# SourceCreateRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `configuration`                                                        | *Any*                                                                  | :heavy_check_mark:                                                     | The values required to configure the source.                           |
| `name`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `secret_id`                                                            | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Optional secretID obtained through the public API OAuth redirect flow. |
| `workspace_id`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |