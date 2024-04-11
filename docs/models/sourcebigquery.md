# SourceBigquery


## Fields

| Field                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `credentials_json`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                         | The contents of your Service Account Key JSON file. See the <a href="https://docs.airbyte.com/integrations/sources/bigquery#setup-the-bigquery-source-in-airbyte">docs</a> for more information on how to obtain this key. |
| `project_id`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                         | The GCP project ID for the project containing the target BigQuery dataset.                                                                                                                                                 |
| `dataset_id`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                         | The dataset ID to search for tables and views. If you are only loading data from one dataset, setting this option could result in much faster schema discovery.                                                            |
| `source_type`                                                                                                                                                                                                              | [models.SourceBigqueryBigquery](../models/sourcebigquerybigquery.md)                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                        |