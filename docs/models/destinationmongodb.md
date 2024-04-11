# DestinationMongodb


## Fields

| Field                                                                                                                                                                                                | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_type`                                                                                                                                                                                          | [Union[models.NoneT, models.LoginPassword]](../models/authorizationtype.md)                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                   | Authorization type.                                                                                                                                                                                  |
| `database`                                                                                                                                                                                           | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | Name of the database.                                                                                                                                                                                |
| `destination_type`                                                                                                                                                                                   | [models.Mongodb](../models/mongodb.md)                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  |
| `instance_type`                                                                                                                                                                                      | [Optional[Union[models.StandaloneMongoDbInstance, models.ReplicaSet, models.MongoDBAtlas]]](../models/mongodbinstancetype.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                                   | MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.                                                                                                 |
| `tunnel_method`                                                                                                                                                                                      | [Optional[Union[models.DestinationMongodbNoTunnel, models.DestinationMongodbSSHKeyAuthentication, models.DestinationMongodbPasswordAuthentication]]](../models/destinationmongodbsshtunnelmethod.md) | :heavy_minus_sign:                                                                                                                                                                                   | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                                                                                 |