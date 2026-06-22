# SourceLeverHiringEnvironment

The environment in which you'd like to replicate data for Lever. This is used to determine which Lever API endpoint to use.

## Example Usage

```python
from airbyte_api.models import SourceLeverHiringEnvironment

value = SourceLeverHiringEnvironment.PRODUCTION
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PRODUCTION` | Production   |
| `SANDBOX`    | Sandbox      |