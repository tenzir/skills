# EMAIL_TRANSACTION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `EMAIL_TRANSACTION`
- Usage-guide section: `EMAIL_TRANSACTION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: Populate with information about the machine that the email message originated from (for example, the IP address of the sender).
- network.email: Email sender or recipient information.

## Optional Fields

- about: URLs, IPs, domains, and any file attachments embedded in the email body.
- securityResult.about: Bad URLs, IPs, and files embedded within the email body.
- principal: If there is client machine data on who sent the email, populate the server details in principal (for example, the client process, port numbers, username, etc.).
- target: If there is destination email server data, populate the server details in target (for example, the IP address).
- intermediary: If there is mail server data or mail proxy data, populate the server details in intermediary.

## Notes

- Never populate principal.email or target.email.
- Only populate the email field in security_result.about or network.email.
- Top level security results generally have a noun set (optional for spam).
