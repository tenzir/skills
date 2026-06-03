# PDFInfo

Information about the PDF file structure. See [https://developers.virustotal.com/reference/pdf_info](https://developers.virustotal.com/reference/pdf_info)

- **Full name**: `google.backstory.PDFInfo`
- **Fields**: `22`

## Fields

### `js`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `js`

Number of /JS tags found in the PDF file. Should be the same as javascript field in normal scenarios.

### `javascript`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `javascript`

Number of /JavaScript tags found in the PDF file. Should be the same as the js field in normal scenarios.

### `launch_action_count`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `launchActionCount`

Number of /Launch tags found in the PDF file.

### `object_stream_count`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `objectStreamCount`

Number of object streams.

### `endobj_count`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `endobjCount`

Number of object definitions (endobj keyword).

### `header`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `header`

PDF version.

### `acroform`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `acroform`

Number of /AcroForm tags found in the PDF.

### `autoaction`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `autoaction`

Number of /AA tags found in the PDF.

### `embedded_file`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `embeddedFile`

Number of /EmbeddedFile tags found in the PDF.

### `encrypted`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `encrypted`

Whether the document is encrypted or not. This is defined by the /Encrypt tag.

### `flash`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `flash`

Number of /RichMedia tags found in the PDF.

### `jbig2_compression`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `jbig2Compression`

Number of /JBIG2Decode tags found in the PDF.

### `obj_count`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `objCount`

Number of objects definitions (obj keyword).

### `endstream_count`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `endstreamCount`

Number of defined stream objects (stream keyword).

### `page_count`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `pageCount`

Number of pages in the PDF.

### `stream_count`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `streamCount`

Number of defined stream objects (stream keyword).

### `openaction`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `openaction`

Number of /OpenAction tags found in the PDF.

### `startxref`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `startxref`

Number of startxref keywords in the PDF.

### `suspicious_colors`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `suspiciousColors`

Number of colors expressed with more than 3 bytes (CVE-2009-3459).

### `trailer`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `trailer`

Number of trailer keywords in the PDF.

### `xfa`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `xfa`

Number of \XFA tags found in the PDF.

### `xref`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `xref`

Number of xref keywords in the PDF.
