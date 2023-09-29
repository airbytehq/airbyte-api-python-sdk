# DestinationLangchainIndexingPinecone

Pinecone is a popular vector store that can be used to store and retrieve embeddings. It is a managed service and can also be queried from outside of langchain.


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `index`                     | *Optional[str]*             | :heavy_check_mark:          | Pinecone index to use       |
| `mode`                      | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `pinecone_environment`      | *Optional[str]*             | :heavy_check_mark:          | Pinecone environment to use |
| `pinecone_key`              | *Optional[str]*             | :heavy_check_mark:          | N/A                         |