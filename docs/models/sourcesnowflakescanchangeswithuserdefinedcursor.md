# SourceSnowflakeScanChangesWithUserDefinedCursor

Incrementally detects new inserts and updates using the <a href="https://docs.airbyte.com/understanding-airbyte/connections/incremental-append/#user-defined-cursor">cursor column</a> chosen when configuring a connection (e.g. created_at, updated_at).


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `additional_properties`                                                                  | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `cursor_method`                                                                          | [Optional[models.SourceSnowflakeCursorMethod]](../models/sourcesnowflakecursormethod.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |