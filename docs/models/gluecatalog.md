# GlueCatalog

The GlueCatalog connects to a AWS Glue Catalog


## Fields

| Field                                                                                                                                                                        | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  | Example                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `catalog_type`                                                                                                                                                               | [Optional[models.DestinationIcebergSchemasCatalogConfigIcebergCatalogConfigCatalogType]](../models/destinationicebergschemascatalogconfigicebergcatalogconfigcatalogtype.md) | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |                                                                                                                                                                              |
| `database`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | The default schema tables are written to if the source does not specify a namespace. The usual value for this field is "public".                                             | public                                                                                                                                                                       |