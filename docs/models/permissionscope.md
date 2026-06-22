# PermissionScope

Scope of a single permission, e.g. workspace, organization

## Example Usage

```python
from airbyte_api.models import PermissionScope

value = PermissionScope.WORKSPACE
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `WORKSPACE`    | workspace      |
| `ORGANIZATION` | organization   |
| `NONE`         | none           |