# StandaloneMongoDbInstance

MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `host`                                                       | *str*                                                        | :heavy_check_mark:                                           | The Host of a Mongo database to be replicated.               |                                                              |
| `instance`                                                   | [Optional[shared.Instance]](../../models/shared/instance.md) | :heavy_minus_sign:                                           | N/A                                                          |                                                              |
| `port`                                                       | *Optional[int]*                                              | :heavy_minus_sign:                                           | The Port of a Mongo database to be replicated.               | 27017                                                        |