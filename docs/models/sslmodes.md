# SSLModes

SSL connection modes. 
 <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
 <b>allow</b> - Chose this mode to enable encryption only when required by the source database
 <b>prefer</b> - Chose this mode to allow unencrypted connection only if the source database does not support encryption
 <b>require</b> - Chose this mode to always require encryption. If the source database server does not support encryption, connection will fail
  <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the source database server has a valid SSL certificate
  <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the source database server
 See more information - <a href="https://jdbc.postgresql.org/documentation/head/ssl-client.html"> in the docs</a>.


## Supported Types

### Disable

```python
sslModes: models.Disable = /* values here */
```

### Allow

```python
sslModes: models.Allow = /* values here */
```

### Prefer

```python
sslModes: models.Prefer = /* values here */
```

### Require

```python
sslModes: models.Require = /* values here */
```

### VerifyCa

```python
sslModes: models.VerifyCa = /* values here */
```

### VerifyFull

```python
sslModes: models.VerifyFull = /* values here */
```

