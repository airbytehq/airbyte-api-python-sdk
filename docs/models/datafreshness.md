# DataFreshness

If set to 'final', the returned data will include only finalized, stable data. If set to 'all', fresh data will be included. When using Incremental sync mode, we do not recommend setting this parameter to 'all' as it may cause data loss. More information can be found in our <a href='https://docs.airbyte.com/integrations/source/google-search-console'>full documentation</a>.


## Values

| Name    | Value   |
| ------- | ------- |
| `FINAL` | final   |
| `ALL`   | all     |