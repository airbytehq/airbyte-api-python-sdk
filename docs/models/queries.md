# Queries


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data_source`                                                          | [models.SourceDatadogDataSource](../models/sourcedatadogdatasource.md) | :heavy_check_mark:                                                     | A data source that is powered by the platform.                         |
| `name`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | The variable name for use in queries.                                  |
| `query`                                                                | *str*                                                                  | :heavy_check_mark:                                                     | A classic query string.                                                |