# Hashing


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `field_name_suffix`                                   | *str*                                                 | :heavy_check_mark:                                    | The suffix to append to the field name after hashing. |
| `method`                                              | [models.HashingMethod](../models/hashingmethod.md)    | :heavy_check_mark:                                    | The hashing algorithm to use.                         |
| `target_field`                                        | *str*                                                 | :heavy_check_mark:                                    | The name of the field to be hashed.                   |