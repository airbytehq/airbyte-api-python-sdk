# SourcePostgresScanChangesWithUserDefinedCursor

Incrementally detects new inserts and updates using the <a href="https://docs.airbyte.com/understanding-airbyte/connections/incremental-append/#user-defined-cursor">cursor column</a> chosen when configuring a connection (e.g. created_at, updated_at).


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `method`                                                                                                         | [models.SourcePostgresSchemasReplicationMethodMethod](../models/sourcepostgresschemasreplicationmethodmethod.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |