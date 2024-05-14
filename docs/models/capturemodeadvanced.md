# CaptureModeAdvanced

Determines how Airbyte looks up the value of an updated document. If 'Lookup' is chosen, the current value of the document will be read. If 'Post Image' is chosen, then the version of the document immediately after an update will be read. WARNING : Severe data loss will occur if this option is chosen and the appropriate settings are not set on your Mongo instance : https://www.mongodb.com/docs/manual/changeStreams/#change-streams-with-document-pre-and-post-images.


## Values

| Name         | Value        |
| ------------ | ------------ |
| `LOOKUP`     | Lookup       |
| `POST_IMAGE` | Post Image   |