# SourceMongodbV2


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database_config`                                                                                                                                                                                                                                                                                                                                                   | [Union[models.MongoDBAtlasReplicaSet, models.SelfManagedReplicaSet]](../models/clustertype.md)                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                  | Configures the MongoDB cluster type.                                                                                                                                                                                                                                                                                                                                |
| `discover_sample_size`                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | The maximum number of documents to sample when attempting to discover the unique fields for a collection.                                                                                                                                                                                                                                                           |
| `initial_waiting_seconds`                                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | The amount of time the connector will wait when it launches to determine if there is new data to sync or not. Defaults to 300 seconds. Valid range: 120 seconds to 1200 seconds.                                                                                                                                                                                    |
| `invalid_cdc_cursor_position_behavior`                                                                                                                                                                                                                                                                                                                              | [Optional[models.InvalidCDCPositionBehaviorAdvanced]](../models/invalidcdcpositionbehavioradvanced.md)                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | Determines whether Airbyte should fail or re-sync data in case of an stale/invalid cursor value into the WAL. If 'Fail sync' is chosen, a user will have to manually reset the connection before being able to continue syncing data. If 'Re-sync data' is chosen, Airbyte will automatically trigger a refresh but could lead to higher cloud costs and data loss. |
| `queue_size`                                                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                  | The size of the internal queue. This may interfere with memory consumption and efficiency of the connector, please be careful.                                                                                                                                                                                                                                      |
| `source_type`                                                                                                                                                                                                                                                                                                                                                       | [models.MongodbV2](../models/mongodbv2.md)                                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                 |