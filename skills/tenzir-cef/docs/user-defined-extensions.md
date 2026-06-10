# User-Defined Extensions

The Extension Dictionary provides a set of predefined extension names (CEF names such as "fname" and full names such as "filetype") that must cover most event log requirements. However, vendors' devices might generate more information that can be appropriately mapped into the predefined extensions or might generate information that does not fit the orientation of the predefined extensions. In such cases, vendors can define their own custom extensions.

## Custom Extension Naming Guidelines

Ensure the following when creating custom extensions:

### Format

Custom extension names must take the form: `VendornameProductnameExplanatoryKeyName`

### Requirements

Custom extension names must meet the following requirements. Custom extension name(s) must be:

- a single word, with no spaces.
- alphanumeric.
- as clear and concise as possible.
- named different than any name listed in ArcSight Extension Dictionary.

## Limitations of Custom Extensions

Custom extension names are recommended for use only when no reasonable mapping of the information can be established for a predefined CEF name. While the custom extension name mechanism can be used to safely send information to CEF consumers for storage, there are certain limitations as to when and how to access the data mapped into them.

Custom extension names also have significant limitations that implementers should be aware of. These limitations can fundamentally affect the experience of ArcSight product users.

### Limitations Affecting ArcSight ESM

- Data submitted to ArcSight ESM using custom name extensions is retained, but is largely inaccessible except when directly viewing events. This data shows up in a section called "Additional Data".
- Data submitted to ArcSight ESM using custom name extensions cannot be used directly for reporting, as these "Additional Data" fields are not made available in the reporting schema. Thus, any data in the "Additional Data" section of events is not available in reports.
- Data submitted to ArcSight ESM using custom name extensions cannot be used directly for event correlation (as within Rules, Data Monitors, etc.). Therefore, any data in the "Additional Data" section is not available as output for correlation activities within the ESM system.

### Limitations Affecting ArcSight Logger

- Data submitted to ArcSight Logger using custom name extensions is retained in the system, but is not available for use in the Logger reporting infrastructure.
- Data submitted to ArcSight Logger using custom name extensions is available for viewing by the customer using string-based search. Event export is also available for this purpose.
