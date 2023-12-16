# ByProgrammingLanguage

Split the text by suitable delimiters based on the programming language. This is useful for splitting code into chunks.


## Fields

| Field                                                                                                                                                                    | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `language`                                                                                                                                                               | [shared.DestinationMilvusLanguage](../../models/shared/destinationmilvuslanguage.md)                                                                                     | :heavy_check_mark:                                                                                                                                                       | Split code in suitable places based on the programming language                                                                                                          |
| `mode`                                                                                                                                                                   | [Optional[shared.DestinationMilvusSchemasProcessingTextSplitterTextSplitterMode]](../../models/shared/destinationmilvusschemasprocessingtextsplittertextsplittermode.md) | :heavy_minus_sign:                                                                                                                                                       | N/A                                                                                                                                                                      |