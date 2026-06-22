# ChooseHowToPartitionData

Partition data by cursor fields when a cursor field is a date

## Example Usage

```python
from airbyte_api.models import ChooseHowToPartitionData

value = ChooseHowToPartitionData.NO_PARTITIONING
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `NO_PARTITIONING` | NO PARTITIONING   |
| `DATE`            | DATE              |
| `YEAR`            | YEAR              |
| `MONTH`           | MONTH             |
| `DAY`             | DAY               |
| `YEAR_MONTH`      | YEAR/MONTH        |
| `YEAR_MONTH_DAY`  | YEAR/MONTH/DAY    |