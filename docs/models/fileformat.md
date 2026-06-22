# FileFormat

The Format of the file which should be replicated (Warning: some formats may be experimental, please refer to the docs).

## Example Usage

```python
from airbyte_api.models import FileFormat

value = FileFormat.CSV
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `CSV`          | csv            |
| `JSON`         | json           |
| `JSONL`        | jsonl          |
| `EXCEL`        | excel          |
| `EXCEL_BINARY` | excel_binary   |
| `FWF`          | fwf            |
| `FEATHER`      | feather        |
| `PARQUET`      | parquet        |
| `YAML`         | yaml           |