<!-- Start SDK Example Usage [usage] -->
```python
import airbyte_api

s = airbyte_api.AirbyteAPI()


res = s.root.get_documentation()

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->