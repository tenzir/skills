# SecurityCategory

SecurityCategory is used to standardize security categories across products so one event is not categorized as "malware" and another as a "virus".

## Values

- `UNKNOWN_CATEGORY` (0): The default category.
- `SOFTWARE_MALICIOUS` (10000): Malware, spyware, rootkit.
- `SOFTWARE_SUSPICIOUS` (10100): Below the conviction threshold; probably bad.
- `SOFTWARE_PUA` (10200): Potentially Unwanted App (such as adware).
- `NETWORK_MALICIOUS` (20000): Includes C&C or network exploit.
- `NETWORK_SUSPICIOUS` (20100): Suspicious activity, such as potential reverse tunnel.
- `NETWORK_CATEGORIZED_CONTENT` (20200): Non-security related: URL has category like gambling or porn.
- `NETWORK_DENIAL_OF_SERVICE` (20300): DoS, DDoS.
- `NETWORK_RECON` (20400): Port scan detected by an IDS, probing of web app.
- `NETWORK_COMMAND_AND_CONTROL` (20500): If we know this is a C&C channel.
- `ACL_VIOLATION` (30000): Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc.
- `AUTH_VIOLATION` (40000): Authentication failed (e.g. bad password or bad 2-factor authentication).
- `EXPLOIT` (50000): Exploit: For all manner of exploits including attempted overflows, bad protocol encodings, ROP, SQL injection, etc. For both network and host- based exploits.
- `DATA_EXFILTRATION` (60000): DLP: Sensitive data transmission, copy to thumb drive.
- `DATA_AT_REST` (60100): DLP: Sensitive data found at rest in a scan.
- `DATA_DESTRUCTION` (60200): Attempt to destroy/delete data.
- `TOR_EXIT_NODE` (60300): TOR Exit Nodes.
- `MAIL_SPAM` (70000): Spam email, message, etc.
- `MAIL_PHISHING` (70100): Phishing email, chat messages, etc.
- `MAIL_SPOOFING` (70200): Spoofed source email address, etc.
- `POLICY_VIOLATION` (80000): Security-related policy violation (e.g. firewall/proxy/HIPS rule violated, NAC block action).
- `SOCIAL_ENGINEERING` (90001): Threats which manipulate to break normal security procedures.
- `PHISHING` (90002): Phishing pages, pops, https phishing etc.
