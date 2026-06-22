# JobTypeEnum

Enum that describes the different types of jobs that the platform runs.

## Example Usage

```python
from airbyte_api.models import JobTypeEnum

value = JobTypeEnum.SYNC
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SYNC`    | sync      |
| `RESET`   | reset     |
| `REFRESH` | refresh   |
| `CLEAR`   | clear     |