# DestinationMilvusIndexingAuthenticationUsernamePassword

Authenticate using username and password (suitable for self-managed Milvus clusters)


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `mode`                           | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `password`                       | *Optional[str]*                  | :heavy_check_mark:               | Password for the Milvus instance |
| `username`                       | *Optional[str]*                  | :heavy_check_mark:               | Username for the Milvus instance |