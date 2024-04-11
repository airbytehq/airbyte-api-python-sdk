# CustomReportConfig


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      | Example                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                                           | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | The name of the custom report, this name would be used as stream name                                                                            | Account Performance                                                                                                                              |
| `report_columns`                                                                                                                                 | List[*str*]                                                                                                                                      | :heavy_check_mark:                                                                                                                               | A list of available report object columns. You can find it in description of reporting object that you want to add to custom report.             |                                                                                                                                                  |
| `reporting_object`                                                                                                                               | [models.ReportingDataObject](../models/reportingdataobject.md)                                                                                   | :heavy_check_mark:                                                                                                                               | The name of the the object derives from the ReportRequest object. You can find it in Bing Ads Api docs - Reporting API - Reporting Data Objects. |                                                                                                                                                  |
| `report_aggregation`                                                                                                                             | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | A list of available aggregations.                                                                                                                |                                                                                                                                                  |