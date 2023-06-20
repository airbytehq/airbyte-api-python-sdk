# DestinationMongodbInstanceTypeStandaloneMongoDbInstance

MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.


## Fields

| Field                                                                                                                                                     | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host`                                                                                                                                                    | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The Host of a Mongo database to be replicated.                                                                                                            |                                                                                                                                                           |
| `instance`                                                                                                                                                | [DestinationMongodbInstanceTypeStandaloneMongoDbInstanceInstance](../../models/shared/destinationmongodbinstancetypestandalonemongodbinstanceinstance.md) | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |                                                                                                                                                           |
| `port`                                                                                                                                                    | *int*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The Port of a Mongo database to be replicated.                                                                                                            | 27017                                                                                                                                                     |