# SourceMssqlReplicationMethodLogicalReplicationCDCDataToSync

What data should be synced under the CDC. "Existing and New" will read existing data as a snapshot, and sync new changes through CDC. "New Changes Only" will skip the initial snapshot, and only sync new changes through CDC.


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EXISTING_AND_NEW` | Existing and New   |
| `NEW_CHANGES_ONLY` | New Changes Only   |