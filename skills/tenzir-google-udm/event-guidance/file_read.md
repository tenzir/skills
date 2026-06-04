# FILE_READ Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `FILE_CREATION`, `FILE_DELETION`, `FILE_MODIFICATION`, `FILE_READ`, `FILE_OPEN`
- Usage-guide section: `FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. (Optional) Populate principal.process with information about the process accessing the file.
- target: If the file is remote (for example SMB share), the target must include at least one machine identifier for the target machine, otherwise all machine identifiers must be blank. Populate target.file with information about the file.

## Optional Fields

- security_result: Describe the malicious activity detected.
- principal.user: Populate if user information is available about the process.

## Notes

No entries extracted.
