# What is CEF?

Common Event Format (CEF) is an extensible, text-based format designed to support multiple device types by offering the most relevant information. Message syntaxes are reduced to work with ESM normalization. CEF specifically defines a syntax for log records containing a standard header and a variable extension, formatted as key-value pairs. The CEF format can be used with on-premise devices by implementing the ArcSight Syslog SmartConnector. CEF can also be used by cloud-based service providers by implementing the SmartConnector for ArcSight Common Event Format REST.

## The Case for ArcSight CEF

The central problem of any security information and event management (SIEM) environment is integration. Device vendors each have their own format for reporting event information, and such diversity can make customer site integration time consuming and expensive. The CEF standard format, developed by ArcSight, enables vendors and their customers to quickly integrate their product information into ESM.

The CEF standard format is an open log management standard that simplifies log management. CEF allows third parties to create their own device schemas that are compatible with a standard that is used industry-wide for normalizing security events. Technology companies and customers can use the standardized CEF format to facilitate data collection and aggregation, for later analysis by an enterprise management system.

### CEF Certification

The Enterprise Security Products Technology Alliance Program assists technology companies that want to adopt, test, and certify their compatibility with the CEF standard and by extension ArcSight interoperability. The CEF Technology Alliance Program provides a process that includes documentation, event categorization assistance, technical and marketing support along with access to a hosted ArcSight ESM solution for testing. For more information, see the Micro Focus Security Products [Program Guide](https://www.microfocus.com/media/guide/micro_focus_technology_alliances_partner_program_partner_with_micro_focus_security_products_guide.pdf).

## CEF Implementation

This document defines the CEF protocol and provides details about implementing the standard. It details the header and predefined extensions used within the standard, and explains the procedure to create user-defined extensions. It also includes a list of CEF supported date formats.

### Header Information

CEF uses Syslog as a transport mechanism. It uses the following format that contains a Syslog prefix, a header, and an extension:

`Jan 18 11:07:53 host CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]`

In which,

`CEF:Version` - is a mandatory header. The rest of the message is formatted using fields delimited by a pipe ("|") character. All of the following fields must be present and defined under Header Field Definitions.

`[Extension]` - is a placeholder for additional fields, but is not mandatory. Any additional fields are logged as key-value pairs. For a table of definitions, see [ArcSight Extension Dictionary](../extensions.yaml).

Pipe (|) used in a “value” part of a CEF header field must be escaped. The pipe delimiter must not be escaped.

The following examples illustrate a CEF message using Syslog transport:

For CEF 0.x version

`Sep 19 08:26:10 host CEF:0|Security|threatmanager|1.0|100|worm successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 spt=1232`

For CEF 1.x version

`Sep 29 08:26:10 host CEF:1|Security|threatmanager|1.0|100|worm successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 spt=1232`

### Using CEF Without Syslog

Syslog applies a syslog prefix to each message, no matter which device it arrives from, that contains the date and hostname in the following example:

`Jan 18 11:07:53 host CEF:Version|…`

Even if an event producer is unable to write Syslog messages, it is possible to write the events to a file by performing the following steps:

1. Discard the syslog prefix `(Jan 18 11:07:53 host)`.
2. Begin the message with the following format:
   `CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]`

### Header Field Definitions

| Field Name | Type | Size | Description |
| --- | --- | --- | --- |
| CEF Version | Numeric | N/A | **CEF Version** is an integer and identifies the version of the CEF format. Event consumers use this information to determine what the following fields represent.<br>The current CEF format versions are:<br>- 0 `(CEF:0)` - for CEF Specification version 0.1<br>- 1 `(CEF:1)` - for CEF Specification version 1.x<br>For example, for CEF Specification version 1.2, the value of the **CEF Version** header field will be " **1** ". |
| agentSeverity | AgentSeverityEnumeration | N/A | **agentSeverity** is a string or integer and it reflects the importance of the event.<br>- The valid string values are:<br>  **Unknown**, **Low**, **Medium**, **High**, and **Very-High**.<br>- The valid integer values are:<br>  **0-3=Low**, **4-6=Medium**, **7- 8=High**, and **9-10=Very-High**. |
| deviceEventClassId | String | 1023 | **deviceEventClassId** is a unique identifier for each event-type. This can be a string or an integer. **deviceEventClassId** identifies the type of event reported.<br>In the intrusion detection system (IDS) world, each signature or rule that detects certain activity has a unique **deviceEventClassId** assigned. This is a requirement for other types of devices as well, and helps correlation engines process the events. It is also known as **Signature ID**.<br>**Note**: The ‘ **=** ’, ‘ **%** ’, and ‘ **#** ’characters must be escaped in the vulnerability string that are mapped to **deviceEventClassId**, and if they are present in the description or name of the vulnerability. However, these characters must not be escaped when used as a delimiter. |
| deviceProduct | String | 63 | **deviceProduct**, **deviceVendor**, and **deviceVersion** are strings that uniquely identify the type of device that sent the message.<br>No two products might use the same **deviceVendor** and **deviceProduct** pair. There is no central authority managing these pairs. Event producers must ensure that they assign unique name pairs. |
| deviceVendor | String | 63 |
| deviceVersion | String | 31 |
| name | String | 512 | **name** is a string representing a human-readable and understandable description of the event.<br>The event name must not contain information that is specifically mentioned in other fields. For example: "Port scan from 10.0.0.1 targeting 20.1.1.1" is not a good event name. It must be: "Port scan". The other information is redundant and can be picked up from the rest of the fields. |

### The Extension Field

The **Extension** field contains a collection of key-value pairs. The keys are part of a predefined set. The standard allows to include additional keys as described in the [ArcSight Extension Dictionary](../extensions.yaml) section. An event can contain any number of key-value pairs in any order, separated by spaces (" "). If a field contains a space, such as a file name, this is valid and can be logged in exactly that manner, as shown in the following example:

`filePath=/user/username/dir/my file name.txt`

> **Note:**
>
> - If there are multiple spaces before a key, all spaces but the last space are treated as trailing spaces in the prior value in the key. If you need trailing spaces, use multiple spaces, otherwise, use one space between the end of a value and the start of the following key.
> - Trailing spaces are not preserved for the final key-value pair in the extension. It is highly recommended to not utilize leading or trailing spaces in CEF events unless absolutely necessary. If that is the case, ensure the ordering of key-value pairs in the extension is such that any value with trailing spaces is not the final value. For more information on best practices for creating CEF events, see the CEF Mapping Guidelines document.
> - Extension values must follow the escape character guidelines defined for encoding symbols in CEF. See, Character Encoding.

### Character Encoding

Because CEF uses the UTF-8 Unicode encoding method, certain symbols must use character encoding. Within this context, character encoding specifies how to represent characters that could be misinterpreted within the schema.

Ensure the following when encoding symbols in CEF:

- The entire message must be UTF-8 encoded.
- Spaces used in the header are valid. Do not encode a space character by using \<space>.
- If a pipe (|) is used in the header, it must be escaped with a backslash (\). But note that the pipes in the extension do not need escaping. For example:
  `Sep 19 08:26:10 host CEF:0|security|threatmanager|1.0|100|detected a \| in message|10|src=10.0.0.1 act=blocked a | dst=1.1.1.1`

- If a backslash (\) is used in the header or the extension, it must be escaped with another backslash (\). For example:
  `Sep 19 08:26:10 host CEF:0|security|threatmanager|1.0|100|detected a \\ in packet|10|src=10.0.0.1 act=blocked a \\ dst=1.1.1.1`

- If an equal sign (=) is used in the extensions, it has to be escaped with a backslash (\). Equal signs in the header need no escaping. For example:
  `Sep 19 08:26:10 host CEF:0|security|threatmanager|1.0|100|detected a = in message|10|src=10.0.0.1 act=blocked a \= dst=1.1.1.1`

- Multi-line fields can be sent by CEF by encoding the newline character as \n or \r. Note that multiple lines are only allowed in the value part of the extensions. For example:
  `Sep 19 08:26:10 host CEF:0|security|threatmanager|1.0|100|Detected a threat. No action needed.|10|src=10.0.0.1 msg=Detected a threat.\n No action needed`
