# DestinationLangchain


## Fields

| Field                                                                                                                                             | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `embedding`                                                                                                                                       | [Union[models.DestinationLangchainOpenAI, models.DestinationLangchainFake]](../models/destinationlangchainembedding.md)                           | :heavy_check_mark:                                                                                                                                | Embedding configuration                                                                                                                           |
| `indexing`                                                                                                                                        | [Union[models.DestinationLangchainPinecone, models.DocArrayHnswSearch, models.ChromaLocalPersistance]](../models/destinationlangchainindexing.md) | :heavy_check_mark:                                                                                                                                | Indexing configuration                                                                                                                            |
| `processing`                                                                                                                                      | [models.DestinationLangchainProcessingConfigModel](../models/destinationlangchainprocessingconfigmodel.md)                                        | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `destination_type`                                                                                                                                | [models.Langchain](../models/langchain.md)                                                                                                        | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |