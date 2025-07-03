# ResourceRequirements

optional resource requirements to run workers (blank for unbounded allocations)


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `cpu_limit`                 | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `cpu_request`               | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `ephemeral_storage_limit`   | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `ephemeral_storage_request` | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `memory_limit`              | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `memory_request`            | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |