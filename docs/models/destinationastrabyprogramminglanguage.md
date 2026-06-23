# DestinationAstraByProgrammingLanguage

Split the text by suitable delimiters based on the programming language. This is useful for splitting code into chunks.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `language`                                                                         | [models.DestinationAstraLanguage](../models/destinationastralanguage.md)           | :heavy_check_mark:                                                                 | Split code in suitable places based on the programming language                    |
| `mode`                                                                             | [Optional[models.DestinationAstraModeCode]](../models/destinationastramodecode.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |