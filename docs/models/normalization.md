# Normalization

Whether the input JSON data should be normalized (flattened) in the output CSV. Please refer to docs for details.

## Example Usage

```python
from airbyte_api.models import Normalization

value = Normalization.NO_FLATTENING
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `NO_FLATTENING`         | No flattening           |
| `ROOT_LEVEL_FLATTENING` | Root level flattening   |