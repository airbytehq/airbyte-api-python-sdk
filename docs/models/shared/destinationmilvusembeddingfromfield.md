# DestinationMilvusEmbeddingFromField

Use a field in the record as the embedding. This is useful if you already have an embedding for your data and want to store it in the vector store.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `dimensions`                                                | *Optional[int]*                                             | :heavy_check_mark:                                          | The number of dimensions the embedding model is generating  | 1536                                                        |
| `field_name`                                                | *Optional[str]*                                             | :heavy_check_mark:                                          | Name of the field in the record that contains the embedding | embedding                                                   |
| `mode`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |                                                             |