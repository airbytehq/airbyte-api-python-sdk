# NonBreakingSchemaUpdatesBehaviorEnum

Set how Airbyte handles syncs when it detects a non-breaking schema change in the source


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `IGNORE`             | ignore               |
| `DISABLE_CONNECTION` | disable_connection   |
| `PROPAGATE_COLUMNS`  | propagate_columns    |
| `PROPAGATE_FULLY`    | propagate_fully      |