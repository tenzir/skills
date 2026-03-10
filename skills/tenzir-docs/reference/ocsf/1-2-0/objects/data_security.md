# Data Security

> The Data Security object describes the characteristics, techniques and content of a Data Loss Prevention (DLP), Data Loss Detection (DLD), Data Classification, or similar tools' finding, alert, or detection mechanism(s).


The Data Security object describes the characteristics, techniques and content of a Data Loss Prevention (DLP), Data Loss Detection (DLD), Data Classification, or similar tools’ finding, alert, or detection mechanism(s).

* **Extends**: `data_classification`

## Attributes

**`category_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is not mapped. See the `data_type` attribute, which contains a data source specific value.
  * `1` - `Personal`: Any Personally Identifiable Information (PII), Electronic Personal Health Information (ePHI), or similarly personal information. E.g., full name, home address, date of birth, etc.
  * `2` - `Governmental`: Any sensitive government identification number related to a person or other classified material. E.g., Passport numbers, driver license numbers, business identification, taxation identifiers, etc.
  * `3` - `Financial`: Any financially-related sensitive information or Cardholder Data (CHD). E.g., banking account numbers, credit card numbers, International Banking Account Numbers (IBAN), SWIFT codes, etc.
  * `4` - `Business`: Any business-specific sensitive data such as intellectual property, trademarks, copyrights, human resource data, Board of Directors meeting minutes, and similar.
  * `5` - `Military and Law Enforcement`: Any mission-specific sensitive data for military, law enforcement, or other government agencies such as specifically classified data, weapon systems information, or other planning data.
  * `6` - `Security`: Any sensitive security-related data such as passwords, passkeys, IP addresses, API keys, credentials and similar secrets. E.g., AWS Access Secret Key, SaaS API Keys, user passwords, database credentials, etc.
  * `99` - `Other`: Any other type of data classification or a multi-variate classification made up of several other classification categories.

The normalized identifier of the data classification category.

**`confidentiality_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The confidentiality is unknown.
  * `1` - `Not Confidential`
  * `2` - `Confidential`
  * `3` - `Secret`
  * `4` - `Top Secret`
  * `5` - `Private`
  * `6` - `Restricted`
  * `99` - `Other`: The confidentiality is not mapped. See the `confidentiality` attribute, which contains a data source specific value.

The normalized identifier of the file content confidentiality indicator.

**`data_lifecycle_state_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is not mapped. See the `data_lifecycle_state` attribute, which contains a data source specific value.
  * `1` - `Data at-Rest`: The data was stored on physical or logcial media and was not actively moving through the network nor was being processed. E.g., data stored in a database, PDF files in a file share, or EHR records in object storage.
  * `2` - `Data in-Transit`: The data was actively moving through the network or from one physical or logical location to another. E.g., emails being send, data replication or Change Data Capture (CDC) streams, or sensitive data processed on an API.
  * `3` - `Data in-Use`: The data was being processed, accessed, or read by a system, making it active in memory or CPU. E.g., sensitive data in a Business Intelligence tool, ePHI being processed in an EHR application or a user viewing data stored in a spreadsheet or PDF.

The stage or state that the data was in when it was assessed or scanned by a data security tool.

**`detection_pattern`**

* **Type**: `string_t`
* **Requirement**: recommended

Specific pattern, algorithm, fingerpint, or model used for detection.

**`detection_system_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is not mapped. See the `detection_system` attribute, which contains a data source specific value.
  * `1` - `Endpoint`: A dedicated agent or sensor installed on a device, either a dedicated data security tool or an Endpoint Detection & Response (EDR) tool that can detect sensitive data and/or enforce data security policies. E.g., Forcepoint DLP, Symantec DLP, Microsoft Defender for Endpoint (MDE).
  * `2` - `DLP Gateway`: A Data Loss Prevention (DLP) gateway that is positioned in-line of an information store such as a network share, a database, or otherwise that can detect sensitive data and/or enforce data security policies.
  * `3` - `Mobile Device Management`: A Mobile Device Management (MDM) or Enterprise Mobility Management (EMM) tool that can detect sensitive data and/or enforce data security policies on mobile devices (e.g., cellphones, tablets, End User Devices \[EUDs]).
  * `4` - `Data Discovery & Classification`: A tool that actively identifies and classifies sensitive data in digitial media and information stores in accordance with a policy or automated functionality. E.g, Amazon Macie, Microsoft Purview.
  * `5` - `Secure Web Gateway`: A Secure Web Gateway (SWG) is any tool that can detect sensitive data and/or enforce data security policies at a network-edge such as within a proxy or firewall service.
  * `6` - `Secure Email Gateway`: A Secure Email Gateway (SEG) is any tool that can detect sensitive data and/or enforce data security policies within email systems. E.g., Microsoft Defender for Office, Google Workspaces.
  * `7` - `Digital Rights Management`: A Digital Rights Management (DRM) or a dedicated Information Rights Management (IRM) are tools which can detect sensitive data and/or enforce data security policies on digitial media via policy or user access rights.
  * `8` - `Cloud Access Security Broker`: A Cloud Access Security Broker (CASB) that can detect sensitive data and/or enforce data security policies in-line to cloud systems such as the public cloud or Software-as-a-Service (SaaS) tool. E.g., Forcepoint CASB, SkyHigh Security.
  * `9` - `Database Activity Monitoring`: A Database Activity Monitoring (DAM) tool that can detect sensitive data and/or enforce data security policies as part of a dedicated database or warehouse monitoring solution.
  * `10` - `Application-Level DLP`: A built in Data Loss Prevention (DLP) or other data security capability within a tool or platform such as an Enterprise Resource Planning (ERP) or Customer Relations Management (CRM) tool that can detect sensitive data and/or enforce data security policies.
  * `11` - `Developer Security`: Any Developer Security tool such as an Infrastrucre-as-Securty (IAC) scanner, Secrets Detection, or Secure Software Development Lifecycle (SSDLC) tool that can detect sensitive data and/or enforce data security policies. E.g., TruffleHog, GitGuardian, Git-Secrets.
  * `12` - `Data Security Posture Management`: A Data Security Posture Management (DSPM) tool is a continuous monitoring and data discovery solution that can detect sensitive data and/or enforce data security policies for local and cloud environments. E.g., Cyera, Sentra, IBM Polar Security.
  * `99` - `Other`: Any other type of detection system or a multi-variate system made up of several other systems.

The type of data security tool or system that the finding, detection, or alert originated from.

**`policy`**

* **Type**: [`policy`](policy.md)
* **Requirement**: recommended

Details about the policy that triggered the finding.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the data classification category that data matched into, e.g. Financial, Personal, Governmental, etc.

**`confidentiality`**

* **Type**: `string_t`
* **Requirement**: optional

The file content confidentiality, normalized to the confidentiality\_id value. In the case of ‘Other’, it is defined by the event source.

**`data_lifecycle_state`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the stage or state that the data was in. E.g., Data-at-Rest, Data-in-Transit, etc.

**`detection_system`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the type of data security tool or system that the finding, detection, or alert originated from. E.g., Endpoint, Secure Email Gateway, etc.

**`pattern_match`**

* **Type**: `string_t`
* **Requirement**: optional

A text, binary, file name, or datastore that matched against a detection rule.

## Constraints

At least one of: `data_lifecycle_state_id`, `detection_pattern`, `detection_system_id`, `policy`

## Used By

* [`data_security_finding`](../classes/data_security_finding.md)