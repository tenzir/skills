# SecurityResult Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [SecurityResult](../messages/security_result.md)

## Fields

### `SecurityResult.about`

- **Purpose**: Provide a description of the security result.
- **Encoding**: Noun.

### `SecurityResult.action`

- **Purpose**: Specify a security action.
- **Encoding**: Enumerated type.
- **Possible values**: Google SecOps UDM defines the following security actions: ALLOW ALLOW_WITH_MODIFICATION-File or email was disinfected or rewritten and still forwarded. BLOCK QUARANTINE-Store for later analysis (does not mean block). UNKNOWN_ACTION

### `SecurityResult.action_details`

- **Purpose**: Vendor-provided details of the action taken as a result of the security incident. Security actions often best translate into the more general Security_Result.action UDM field. However, you might need to write rules for the exact vendor-provided description of the action.
- **Encoding**: String.
- **Examples**: drop, block, decrypt, encrypt.

#### Examples

- drop, block, decrypt, encrypt.

### `SecurityResult.category`

- **Purpose**: Specify a security category.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following security categories: ACL_VIOLATION-Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc. AUTH_VIOLATION-Authentication failed, such as a bad password or bad 2-factor authentication. DATA_AT_REST-DLP: sensor data found at rest in a scan. DATA_DESTRUCTION-Attempt to destroy/delete data. DATA_EXFILTRATION-DLP: sensor data transmission, copy to thumb drive. EXPLOIT-Attempted overflows, bad protocol encodings, ROP, SQL injection, etc, both network and host-based. MAIL_PHISHING-Phishing email, chat messages, etc. MAIL_SPAM-Spam email, message, etc. MAIL_SPOOFING-Spoofed source email address, etc. NETWORK_CATEGORIZED_CONTENT NETWORK_COMMAND_AND_CONTROL-If the command and control channel is known. NETWORK_DENIAL_OF_SERVICE NETWORK_MALICIOUS-Command and control, network exploit, suspicious activity, potential reverse tunnel, etc. NETWORK_SUSPICIOUS-Non-security related, for example, the URL is linked to gambling, etc. NETWORK_RECON-Port scan detected by an IDS, probing by a web application. POLICY_VIOLATION-Security policy violation, including firewall, proxy, and HIPS rule violations or NAC block actions. SOFTWARE_MALICIOUS-Malware, spyware, rootkits, etc. SOFTWARE_PUA-Potentially unwanted app, such as adware, etc. SOFTWARE_SUSPICIOUS UNKNOWN_CATEGORY

### `SecurityResult.confidence`

- **Purpose**: Specify a confidence with regards to a security event as estimated by the product.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product confidence categories: UNKNOWN_CONFIDENCE LOW_CONFIDENCE MEDIUM_CONFIDENCE HIGH_CONFIDENCE

### `SecurityResult.confidence_details`

- **Purpose**: Additional detail with regards to the confidence of a security event as estimated by the product vendor.
- **Encoding**: String.

### `SecurityResult.priority`

- **Purpose**: Specify a priority with regards to a security event as estimated by the product vendor.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product priority categories: UNKNOWN_PRIORITY LOW_PRIORITY MEDIUM_PRIORITY HIGH_PRIORITY

### `SecurityResult.priority_details`

- **Purpose**: Vendor-specific information about the security result priority.
- **Encoding**: String.

### `SecurityResult.rule_id`

- **Purpose**: Identifier for the security rule.
- **Encoding**: String.
- **Examples**: 08123 5d2b44d0-5ef6-40f5-a704-47d61d3babbe

#### Examples

- 08123
- 5d2b44d0-5ef6-40f5-a704-47d61d3babbe

### `SecurityResult.rule_name`

- **Purpose**: Name of the security rule.
- **Encoding**: String.
- **Example**: BlockInboundToOracle.

#### Examples

- BlockInboundToOracle.

### `SecurityResult.severity`

- **Purpose**: Severity of a security event as estimated by the product vendor using values defined by the Google SecOps UDM.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product severities: UNKNOWN_SEVERITY-Non-malicious INFORMATIONAL-Non-malicious ERROR-Non-malicious LOW-Malicious MEDIUM-Malicious HIGH-Malicious

### `SecurityResult.severity_details`

- **Purpose**: Severity for a security event as estimated by the product vendor.
- **Encoding**: String.

### `SecurityResult.threat_name`

- **Purpose**: Name of the security threat.
- **Encoding**: String.
- **Examples**: W32/File-A Slammer

#### Examples

- W32/File-A
- Slammer

### `SecurityResult.url_back_to_product`

- **Purpose**: URL to direct you to the source product console for this security event.
- **Encoding**: String.
