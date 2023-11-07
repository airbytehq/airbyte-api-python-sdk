# SourceMongodbStandaloneMongoDbInstance

The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `host`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The host name of the Mongo database.                                         |                                                                              |
| `instance`                                                                   | [shared.SourceMongodbInstance](../../models/shared/sourcemongodbinstance.md) | :heavy_check_mark:                                                           | N/A                                                                          |                                                                              |
| `port`                                                                       | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | The port of the Mongo database.                                              | 27017                                                                        |