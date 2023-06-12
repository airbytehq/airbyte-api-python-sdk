# DestinationPulsarTopicType

It identifies type of topic. Pulsar supports two kind of topics: persistent and non-persistent. In persistent topic, all messages are durably persisted on disk (that means on multiple disks unless the broker is standalone), whereas non-persistent topic does not persist message into storage disk.


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `PERSISTENT`     | persistent       |
| `NON_PERSISTENT` | non-persistent   |