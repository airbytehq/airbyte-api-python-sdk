# LSNCommitBehaviour

Determines when Airbyte should flush the LSN of processed WAL logs in the source database. `After loading Data in the destination` is default. If `While reading Data` is selected, in case of a downstream failure (while loading data into the destination), next sync would result in a full sync.


## Values

| Name                                    | Value                                   |
| --------------------------------------- | --------------------------------------- |
| `WHILE_READING_DATA`                    | While reading Data                      |
| `AFTER_LOADING_DATA_IN_THE_DESTINATION` | After loading Data in the destination   |