# DestinationScylla

The values required to configure the destination.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `address`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | Address to connect to.                                                    |
| `destination_type`                                                        | [DestinationScyllaScylla](../../models/shared/destinationscyllascylla.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `keyspace`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | Default Scylla keyspace to create data in.                                |
| `password`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | Password associated with Scylla.                                          |
| `port`                                                                    | *int*                                                                     | :heavy_check_mark:                                                        | Port of Scylla.                                                           |
| `replication`                                                             | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Indicates to how many nodes the data should be replicated to.             |
| `username`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | Username to use to access Scylla.                                         |