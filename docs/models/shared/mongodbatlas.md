# MongoDBAtlas

MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `cluster_url`                                                                                                  | *str*                                                                                                          | :heavy_check_mark:                                                                                             | URL of a cluster to connect to.                                                                                |
| `instance`                                                                                                     | [Optional[shared.DestinationMongodbSchemasInstance]](../../models/shared/destinationmongodbschemasinstance.md) | :heavy_minus_sign:                                                                                             | N/A                                                                                                            |