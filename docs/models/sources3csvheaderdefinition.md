# SourceS3CSVHeaderDefinition

How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows.


## Supported Types

### `models.SourceS3FromCSV`

```python
value: models.SourceS3FromCSV = /* values here */
```

### `models.SourceS3Autogenerated`

```python
value: models.SourceS3Autogenerated = /* values here */
```

### `models.SourceS3UserProvided`

```python
value: models.SourceS3UserProvided = /* values here */
```

