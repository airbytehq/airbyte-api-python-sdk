# SourceSftpBulkViaAPI

Process files via an API, using the `hi_res` mode. This option is useful for increased performance and accuracy, but requires an API key and a hosted instance of unstructured.


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `api_key`                                                                                                | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The API key to use matching the environment                                                              |                                                                                                          |
| `api_url`                                                                                                | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The URL of the unstructured API to use                                                                   | https://api.unstructured.com                                                                             |
| `mode`                                                                                                   | [Optional[models.SourceSftpBulkSchemasMode]](../models/sourcesftpbulkschemasmode.md)                     | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |                                                                                                          |
| `parameters`                                                                                             | List[[models.SourceSftpBulkAPIParameterConfigModel](../models/sourcesftpbulkapiparameterconfigmodel.md)] | :heavy_minus_sign:                                                                                       | List of parameters send to the API                                                                       |                                                                                                          |