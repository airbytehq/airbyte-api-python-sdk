# Disabled

<b>This only applies to incremental syncs.</b> <br>
Enabling deletion mode informs your destination of deleted documents.<br>
Disabled - Leave this feature disabled, and ignore deleted documents.<br>
Enabled - Enables this feature. When a document is deleted, the connector exports a record with a "deleted at" column containing the time that the document was deleted.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `deletion_mode`                                                                  | [shared.SourceFaunaDeletionMode](../../models/shared/sourcefaunadeletionmode.md) | :heavy_check_mark:                                                               | N/A                                                                              |