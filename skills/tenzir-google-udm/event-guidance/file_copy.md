# FILE_COPY Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `FILE_COPY`
- Usage-guide section: `FILE_COPY`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields as described.
- principal: At least one machine identifier. (Optional) Populate principal.process with information about the process performing the file copy operation.
- src: Populate src.file with information about the source file. If the file is remote (for example SMB share), src must include at least one machine identifier for the source machine storing the source file.
- target: Populate target.file with information about the target file. If the file is remote (for example SMB share), the target field must include at least one machine identifier for the target machine that holds the target file.

## Optional Fields

- security_result: Describe the malicious activity detected.
- principal.user: Populate if user information is available about the process.

## Notes

No entries extracted.
