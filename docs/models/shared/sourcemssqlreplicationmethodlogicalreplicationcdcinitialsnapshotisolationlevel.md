# SourceMssqlReplicationMethodLogicalReplicationCDCInitialSnapshotIsolationLevel

Existing data in the database are synced through an initial snapshot. This parameter controls the isolation level that will be used during the initial snapshotting. If you choose the "Snapshot" level, you must enable the <a href="https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server">snapshot isolation mode</a> on the database.


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `SNAPSHOT`       | Snapshot         |
| `READ_COMMITTED` | Read Committed   |