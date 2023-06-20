# SourceGoogleWorkspaceAdminReports

The values required to configure the source.


## Fields

| Field                                                                                                                                                                                           | Type                                                                                                                                                                                            | Required                                                                                                                                                                                        | Description                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `credentials_json`                                                                                                                                                                              | *str*                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                              | The contents of the JSON service account key. See the <a href="https://developers.google.com/admin-sdk/reports/v1/guides/delegation">docs</a> for more information on how to generate this key. |
| `email`                                                                                                                                                                                         | *str*                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                              | The email of the user, which has permissions to access the Google Workspace Admin APIs.                                                                                                         |
| `lookback`                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Sets the range of time shown in the report. Reports API allows from up to 180 days ago.                                                                                                         |
| `source_type`                                                                                                                                                                                   | [SourceGoogleWorkspaceAdminReportsGoogleWorkspaceAdminReports](../../models/shared/sourcegoogleworkspaceadminreportsgoogleworkspaceadminreports.md)                                             | :heavy_check_mark:                                                                                                                                                                              | N/A                                                                                                                                                                                             |