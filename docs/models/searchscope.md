# SearchScope

Specifies the location(s) to search for files. Valid options are 'ACCESSIBLE_DRIVES' to search in the selected OneDrive drive, 'SHARED_ITEMS' for shared items the user has access to, and 'ALL' to search both.

## Example Usage

```python
from airbyte_api.models import SearchScope

value = SearchScope.ACCESSIBLE_DRIVES
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `ACCESSIBLE_DRIVES` | ACCESSIBLE_DRIVES   |
| `SHARED_ITEMS`      | SHARED_ITEMS        |
| `ALL`               | ALL                 |