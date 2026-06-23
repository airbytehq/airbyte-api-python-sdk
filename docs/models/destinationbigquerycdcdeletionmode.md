# DestinationBigqueryCDCDeletionMode

Whether to execute CDC deletions as hard deletes (i.e. propagate source deletions to the destination), or soft deletes (i.e. leave a tombstone record in the destination). Defaults to hard deletes.

## Example Usage

```python
from airbyte_api.models import DestinationBigqueryCDCDeletionMode

value = DestinationBigqueryCDCDeletionMode.HARD_DELETE
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `HARD_DELETE` | Hard delete   |
| `SOFT_DELETE` | Soft delete   |