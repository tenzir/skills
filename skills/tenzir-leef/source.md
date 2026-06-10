# Source

This skill is generated from the IBM QRadar LEEF Version 2 format guide, fetched from the IBM Docs content API. The structured [attributes.yaml](attributes.yaml) is the primary agent-facing reference; the Markdown docs carry the surrounding format guidance.

- **Predefined attributes**: `45`
- **Normalized attributes**: `23`
- **Reserved (not implemented in QRadar)**: `6`
- **PDF edition of the guide**: https://www.ibm.com/docs/en/SS42VS_DSM/pdf/b_Leef_format_guide.pdf

## Source topics

- Predefined LEEF event attributes: [`c_LEEF_Format_Guide_predefinedAttrrs`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_predefinedAttrrs.html) -> [attributes.yaml](attributes.yaml)
- [`c_LEEF_Format_Guide_intro`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_intro.html) -> [docs/overview.md](docs/overview.md)
- [`c_LEEF_Format_Guide_LEEFeventcomps`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_LEEFeventcomps.html) -> [docs/event-components.md](docs/event-components.md)
- [`c_LEEF_Format_Guide_customkeys`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_customkeys.html) -> [docs/custom-keys.md](docs/custom-keys.md)
- [`c_LEEF_Format_Guide_bestpractices`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_bestpractices.html) -> [docs/best-practices.md](docs/best-practices.md)
- [`c_LEEF_Format_Guide_dateformat`](https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc/c_LEEF_Format_Guide_dateformat.html) -> [docs/date-format.md](docs/date-format.md)

## Known spec quirks preserved verbatim

- `identHostName`: IBM's table lists "Key" instead of "Yes" or "No" in the normalized column, in both the web guide and the PDF, so normalized is null.
- `identSecondlp`: The published key name contains an IBM documentation typo (likely intended identSecondIp). Both the web guide and the PDF spell it identSecondlp; use the key verbatim.
- [docs/event-components.md](docs/event-components.md): IBM's delimiter table labels the hex value x7c as a broken vertical bar (¦), but 0x7C is the regular pipe (|); the broken bar is 0xA6. The error is IBM's and is preserved verbatim.
