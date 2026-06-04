# PDFInfo

Information about the PDF file structure. See [https://developers.virustotal.com/reference/pdf_info](https://developers.virustotal.com/reference/pdf_info)

- **Full name**: `google.backstory.PDFInfo`
- **Fields**: `22`

## Fields

### `js`

- Type: `int64` (singular)

Number of /JS tags found in the PDF file. Should be the same as javascript field in normal scenarios.

### `javascript`

- Type: `int64` (singular)

Number of /JavaScript tags found in the PDF file. Should be the same as the js field in normal scenarios.

### `launchActionCount`

- Type: `int64` (singular)

Number of /Launch tags found in the PDF file.

### `objectStreamCount`

- Type: `int64` (singular)

Number of object streams.

### `endobjCount`

- Type: `int64` (singular)

Number of object definitions (endobj keyword).

### `header`

- Type: `string` (singular)

PDF version.

### `acroform`

- Type: `int64` (singular)

Number of /AcroForm tags found in the PDF.

### `autoaction`

- Type: `int64` (singular)

Number of /AA tags found in the PDF.

### `embeddedFile`

- Type: `int64` (singular)

Number of /EmbeddedFile tags found in the PDF.

### `encrypted`

- Type: `int64` (singular)

Whether the document is encrypted or not. This is defined by the /Encrypt tag.

### `flash`

- Type: `int64` (singular)

Number of /RichMedia tags found in the PDF.

### `jbig2Compression`

- Type: `int64` (singular)

Number of /JBIG2Decode tags found in the PDF.

### `objCount`

- Type: `int64` (singular)

Number of objects definitions (obj keyword).

### `endstreamCount`

- Type: `int64` (singular)

Number of defined stream objects (stream keyword).

### `pageCount`

- Type: `int64` (singular)

Number of pages in the PDF.

### `streamCount`

- Type: `int64` (singular)

Number of defined stream objects (stream keyword).

### `openaction`

- Type: `int64` (singular)

Number of /OpenAction tags found in the PDF.

### `startxref`

- Type: `int64` (singular)

Number of startxref keywords in the PDF.

### `suspiciousColors`

- Type: `int64` (singular)

Number of colors expressed with more than 3 bytes (CVE-2009-3459).

### `trailer`

- Type: `int64` (singular)

Number of trailer keywords in the PDF.

### `xfa`

- Type: `int64` (singular)

Number of \XFA tags found in the PDF.

### `xref`

- Type: `int64` (singular)

Number of xref keywords in the PDF.
