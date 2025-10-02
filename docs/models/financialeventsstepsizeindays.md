# FinancialEventsStepSizeInDays

The time window size (in days) for fetching financial events data in chunks. Options are 1 day, 7 days, 14 days, 30 days, 60 days, and 190 days, based on API limitations.

- **Smaller step sizes (e.g., 1 day)** are better for large data volumes. They fetch smaller chunks per request, reducing the risk of timeouts or overwhelming the API, though more requests may slow syncing and increase the chance of hitting rate limits.
- **Larger step sizes (e.g., 14 days)** are better for smaller data volumes. They fetch more data per request, speeding up syncing and reducing the number of API calls, which minimizes strain on rate limits.

Select a step size that matches your data volume to optimize syncing speed and API performance.


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `ONE`                    | 1                        |
| `SEVEN`                  | 7                        |
| `FOURTEEN`               | 14                       |
| `THIRTY`                 | 30                       |
| `SIXTY`                  | 60                       |
| `NINETY`                 | 90                       |
| `ONE_HUNDRED_AND_EIGHTY` | 180                      |