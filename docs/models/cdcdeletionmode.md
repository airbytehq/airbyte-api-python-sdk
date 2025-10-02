# CDCDeletionMode

Whether to execute CDC deletions as hard deletes (i.e. propagate source deletions to the destination), or soft deletes (i.e. leave a tombstone record in the destination). Defaults to hard deletes.


## Values

| Name          | Value         |
| ------------- | ------------- |
| `HARD_DELETE` | Hard delete   |
| `SOFT_DELETE` | Soft delete   |