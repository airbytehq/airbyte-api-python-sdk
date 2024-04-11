# SSHTunnelMethod

Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.


## Supported Types

### NoTunnel

```python
sshTunnelMethod: models.NoTunnel = /* values here */
```

### SSHKeyAuthentication

```python
sshTunnelMethod: models.SSHKeyAuthentication = /* values here */
```

### PasswordAuthentication

```python
sshTunnelMethod: models.PasswordAuthentication = /* values here */
```

