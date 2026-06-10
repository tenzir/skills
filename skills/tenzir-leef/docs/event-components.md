# LEEF event components

The Log Event Extended Format (LEEF) is a customized event format for IBM QRadar that contains readable and easily processed events for QRadar®. The LEEF format consists of the following components.

## Syslog header

The syslog header contains the timestamp and IPv4 address or host name of the system that is providing the event. The syslog header is an optional component of the LEEF format. If you include a syslog header, you must separate the syslog header from the LEEF header with a space. The syslog header must conform to the formats specified in RFC 3164 or RFC 5424.

RFC 3164 header format:

> **Note:** The priority tag is optional for QRadar.

\<priority tag>\<timestamp> \<IP address or hostname>

The priority tag, if present, must be 1 - 3 digits and must be enclosed in angle brackets. For example, \<13>.

Examples of RFC 3164 header:

- \<13>Jan 18 11:07:53 192.168.1.1
- Jan 18 11:07:53 myhostname

RFC 5424 header format:

> **Note:** The priority tag is required.

\<priority tag>1 \<timestamp> \<IP address or hostname>

The priority tag must be 1 - 3 digits and must be enclosed in angle brackets. For example, \<13>. The timestamp must be in the format: yyyy-MM-ddTHH:mm:ss.SSSZ.

> **Note:**
> - The 'T' must be a literal T character.
> - The 'Z' can be a literal Z or it can be a timezone value in the following format: -04:00

Examples of RFC 5424 header:

- \<13>1 2019-01-18T11:07:53.520Z 192.168.1.1
- \<133>1 2019-01-18T11:07:53.520+07:00 myhostname

## LEEF header

The LEEF header is a required field for LEEF events. The LEEF header is a pipe delimited (|) set of values that identifies your software or appliance to QRadar.

Examples:

- LEEF:Version|Vendor|Product|Version|EventID|
- LEEF:1.0|Microsoft|MSExchange|4.0 SP1|15345|
- LEEF:2.0|Lancope|StealthWatch|1.0|41|^|

## Event attributes

The event attributes identify the payload information of the event that is produced by your appliance or software. Every event attribute is a key and value pair with a tab that separates individual payload events. The LEEF format contains a number of predefined event attributes, which allow QRadar to categorize and display the event.

> **Example:**
> - key=value\<tab>key=value\<tab>key=value\<tab>key=value\<tab>.
> - src=192.0.2.0 dst=172.50.123.1 sev=5 cat=anomaly srcPort=81 dstPort=21 usrName=joe.black

Use the `DelimiterCharacter` in the LEEF 2.0 header to specify an alternate delimiter to the attributes. You can use a single character or the hex value for that character. The hex value can be represented by the prefix 0x or x, followed by a series of 1-4 characters (0-9A-Fa-f).

*Table 1. Attribute Delimiter Character examples for LEEF 2.0*

| Delimiter | Header |
| --- | --- |
| Caret (^) | `LEEF:2.0\|Vendor\|Product\|Version\|EventID\|^\|` |
| Caret (hex value) | `LEEF:2.0\|Vendor\|Product\|Version\|EventID\|x5E\|` |
| Broken vertical bar (¦) | `LEEF:2.0\|Vendor\|Product\|Version\|EventID\|x7c\|` |

The following table provides descriptions for LEEF formats.

*Table 2. LEEF format descriptions*

| Type | Entry | Delimiter | Description |
| --- | --- | --- | --- |
| Syslog Header | IP address | Space | The IP address or the host name of the software or appliance that provides the event to QRadar.<br>**Example:**<br>192.168.1.1<br>myhostname<br>The IP address of the syslog header is used by QRadar to route the event to the correct log source in the event pipeline. It is not recommended that your syslog header contain an IPv6 address. QRadar cannot route an IPv6 address present in the syslog header for the event pipeline. Also, an IPv6 address might not display properly in the Log Source Identifier field of the user interface.<br>When an IP address of the syslog header cannot be understood by QRadar, the system defaults to the packet address to properly route the event. |
| LEEF Header | LEEF:version | Pipe | The LEEF version information is an integer value that identifies the major and minor version of the LEEF format that is used for the event.<br>For example, LEEF:1.0\|Vendor\|Product\|Version\|EventID\| |
| LEEF Header | Vendor or manufacturer name | Pipe | Vendor is a text string that identifies the vendor or manufacturer of the device that sends the syslog events in LEEF format.<br>For example, LEEF:1.0\|Microsoft\|Product\|Version\|EventID\|<br>The Vendor and Product fields must contain unique values when specified in the LEEF header. |
| LEEF Header | Product name | Pipe | The product field is a text string that identifies the product that sends the event log to QRadar.<br>For example, LEEF:1.0\|Microsoft\|MSExchange\|Version\|EventID\|<br>The Vendor and Product fields must contain unique values when specified in the LEEF header. |
| LEEF Header | Product version | Pipe | Version is a string that identifies the version of the software or appliance that sends the event log.<br>For example, LEEF:1.0\|Microsoft\|MSExchange\|4.0 SP1\|EventID\| |
| LEEF Header | EventID | Pipe | EventID is a unique identifier for an event in the LEEF header.<br>The purpose of the EventID is to provide a fine grain, unique identifier for an event without the need to examine the payload information. An EventID can contain either a numeric identified or a text description.<br>Examples:<br>- LEEF:1.0\|Microsoft\|MSExchange\|2007\|7732\|<br>- LEEF:1.0\|Microsoft\|MSExchange\|2007\|Logon Failure\|<br>Restrictions:<br>The value of the event ID must be a consistent and static across products that support multiple languages. If your product supports multi-language events, you can use a numeric or textual value in the EventID field, but it must not be translated when the language of your appliance or application is altered. The EventID field cannot exceed 255 characters. |
| LEEF Header | Delimiter Character | Pipe | Use the `DelimiterCharacter` in the LEEF 2.0 header to specify an alternate delimiter to the attributes. You can use a single character or the hex value for that character. The hex value can be represented by the prefix 0x or x, followed by a series of 1-4 characters (0-9A-Fa-f). |
| Event Attributes | Predefined Key Entries | Tab<br>Delimiter Character | Event attribute is a set of key value pairs that provide detailed information about the security event. Each event attribute must be separated by tab or the delimiter character, but the order of attributes is not enforced.<br>For example, src=172.16.77.100 |
