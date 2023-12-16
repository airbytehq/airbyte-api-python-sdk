# DeletionMode

<b>This only applies to incremental syncs.</b> <br>
Enabling deletion mode informs your destination of deleted documents.<br>
Disabled - Leave this feature disabled, and ignore deleted documents.<br>
Enabled - Enables this feature. When a document is deleted, the connector exports a record with a "deleted at" column containing the time that the document was deleted.


## Supported Types

### Disabled

```python
deletionMode: shared.Disabled = /* values here */
```

### Enabled

```python
deletionMode: shared.Enabled = /* values here */
```

