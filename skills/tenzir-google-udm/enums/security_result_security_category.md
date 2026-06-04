# SecurityResult.SecurityCategory

SecurityCategory is used to standardize security categories across products so one event is not categorized as "malware" and another as a "virus".

## Values

0. `UNKNOWN_CATEGORY`: The default category.
10000. `SOFTWARE_MALICIOUS`: Malware, spyware, rootkit.
10100. `SOFTWARE_SUSPICIOUS`: Below the conviction threshold; probably bad.
10200. `SOFTWARE_PUA`: Potentially Unwanted App (such as adware).
20000. `NETWORK_MALICIOUS`: Includes C&C or network exploit.
20100. `NETWORK_SUSPICIOUS`: Suspicious activity, such as potential reverse tunnel.
20200. `NETWORK_CATEGORIZED_CONTENT`: Non-security related: URL has category like gambling or porn.
20300. `NETWORK_DENIAL_OF_SERVICE`: DoS, DDoS.
20400. `NETWORK_RECON`: Port scan detected by an IDS, probing of web app.
20500. `NETWORK_COMMAND_AND_CONTROL`: If we know this is a C&C channel.
30000. `ACL_VIOLATION`: Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc.
40000. `AUTH_VIOLATION`: Authentication failed (e.g. bad password or bad 2-factor authentication).
50000. `EXPLOIT`: Exploit: For all manner of exploits including attempted overflows, bad protocol encodings, ROP, SQL injection, etc. For both network and host- based exploits.
60000. `DATA_EXFILTRATION`: DLP: Sensitive data transmission, copy to thumb drive.
60100. `DATA_AT_REST`: DLP: Sensitive data found at rest in a scan.
60200. `DATA_DESTRUCTION`: Attempt to destroy/delete data.
60300. `TOR_EXIT_NODE`: TOR Exit Nodes.
70000. `MAIL_SPAM`: Spam email, message, etc.
70100. `MAIL_PHISHING`: Phishing email, chat messages, etc.
70200. `MAIL_SPOOFING`: Spoofed source email address, etc.
80000. `POLICY_VIOLATION`: Security-related policy violation (e.g. firewall/proxy/HIPS rule violated, NAC block action).
90001. `SOCIAL_ENGINEERING`: Threats which manipulate to break normal security procedures.
90002. `PHISHING`: Phishing pages, pops, https phishing etc.
