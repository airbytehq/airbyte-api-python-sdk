# ConversionReportTime

The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event..

## Example Usage

```python
from airbyte_api.models import ConversionReportTime

value = ConversionReportTime.TIME_OF_AD_ACTION
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `TIME_OF_AD_ACTION`  | TIME_OF_AD_ACTION    |
| `TIME_OF_CONVERSION` | TIME_OF_CONVERSION   |