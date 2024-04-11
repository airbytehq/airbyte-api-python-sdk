# SourceS3ParsingStrategy

The strategy used to parse documents. `fast` extracts text directly from the document which doesn't work for all files. `ocr_only` is more reliable, but slower. `hi_res` is the most reliable, but requires an API key and a hosted instance of unstructured and can't be used with local mode. See the unstructured.io documentation for more details: https://unstructured-io.github.io/unstructured/core/partition.html#partition-pdf


## Values

| Name       | Value      |
| ---------- | ---------- |
| `AUTO`     | auto       |
| `FAST`     | fast       |
| `OCR_ONLY` | ocr_only   |
| `HI_RES`   | hi_res     |