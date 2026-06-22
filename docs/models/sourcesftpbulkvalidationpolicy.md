# SourceSftpBulkValidationPolicy

The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema.

## Example Usage

```python
from airbyte_api.models import SourceSftpBulkValidationPolicy

value = SourceSftpBulkValidationPolicy.EMIT_RECORD
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `EMIT_RECORD`       | Emit Record         |
| `SKIP_RECORD`       | Skip Record         |
| `WAIT_FOR_DISCOVER` | Wait for Discover   |