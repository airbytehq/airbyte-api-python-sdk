# SourceGoogleAnalyticsDataAPIGranularity

The granularity used to interpret the startOffset and endOffset for the extended reporting date range for a cohort report.

## Example Usage

```python
from airbyte_api.models import SourceGoogleAnalyticsDataAPIGranularity

value = SourceGoogleAnalyticsDataAPIGranularity.GRANULARITY_UNSPECIFIED
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `GRANULARITY_UNSPECIFIED` | GRANULARITY_UNSPECIFIED   |
| `DAILY`                   | DAILY                     |
| `WEEKLY`                  | WEEKLY                    |
| `MONTHLY`                 | MONTHLY                   |