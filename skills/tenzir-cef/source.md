# Source

This skill is generated from two OpenText (Micro Focus) ArcSight documents: the CEF Implementation Standard from the SmartConnector documentation, and the Data Fields reference of the ESM Console User's Guide. The structured YAML files are the primary agent-facing reference; the Markdown docs carry the surrounding format guidance.

- **CEF document version**: `27` (the HTML topics additionally carry the CEF 1.2 dictionary additions that postdate the PDF)
- **Predefined extension keys**: `174` (139 producer, 52 consumer, 17 in both tables)
- **ESM version**: `7.9`
- **ESM event schema groups**: `18` with `479` data fields
- **Extension keys resolved to ESM groups**: `140`
- **PDF edition of the CEF standard**: https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/pdfdoc/cef-implementation-standard/cef-implementation-standard.pdf
- **PDF edition of the Console User's Guide**: https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/pdfdoc/ESM_ArcSightConsole_UserGuide/ESM_ArcSightConsole_UserGuide.pdf

## Source pages

- [`Chapter 2 ArcSight Extension.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF/Chapter%202%20ArcSight%20Extension.htm) -> [extensions.yaml](extensions.yaml)
- [`Chapter 1 What is CEF.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm) -> [docs/overview.md](docs/overview.md)
- [`Chapter 3 Special Mappings.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF/Chapter%203%20Special%20Mappings.htm) -> [docs/special-mappings.md](docs/special-mappings.md)
- [`Chapter 4 User Defined Extensions.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF/Chapter%204%20User%20Defined%20Extensions.htm) -> [docs/user-defined-extensions.md](docs/user-defined-extensions.md)
- [`Appendix A Date Formats.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF/Appendix%20A%20Date%20Formats.htm) -> [docs/date-formats.md](docs/date-formats.md)
- [`Data_Fields.htm`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Data_Fields.htm) -> [docs/esm-data-fields.md](docs/esm-data-fields.md)
- [`Attacker Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Attacker_Group.htm) -> [groups/attacker.yaml](groups/attacker.yaml)
- [`Connector Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Connector_Group.htm) -> [groups/connector.yaml](groups/connector.yaml)
- [`Category Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Category_Group.htm) -> [groups/category.yaml](groups/category.yaml)
- [`Destination Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Destination_Group.htm) -> [groups/destination.yaml](groups/destination.yaml)
- [`Device Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Device_Group.htm) -> [groups/device.yaml](groups/device.yaml)
- [`Device Custom Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Device_Custom_Group.htm) -> [groups/device_custom.yaml](groups/device_custom.yaml)
- [`Event Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Event_Group.htm) -> [groups/event.yaml](groups/event.yaml)
- [`Event Annotation Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Event_Annotation_Group.htm) -> [groups/event_annotation.yaml](groups/event_annotation.yaml)
- [`File Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/File_Group.htm) -> [groups/file.yaml](groups/file.yaml)
- [`Final Device Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Final_Device_Group.htm) -> [groups/final_device.yaml](groups/final_device.yaml)
- [`Flex Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Flex_Group.htm) -> [groups/flex.yaml](groups/flex.yaml)
- [`Manager Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Manager_Group.htm) -> [groups/manager.yaml](groups/manager.yaml)
- [`Old File Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Old_File_Group.htm) -> [groups/old_file.yaml](groups/old_file.yaml)
- [`Original Connector Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Original_Connector_Group.htm) -> [groups/original_connector.yaml](groups/original_connector.yaml)
- [`Request Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Request_Group.htm) -> [groups/request.yaml](groups/request.yaml)
- [`Source Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Source_Group.htm) -> [groups/source.yaml](groups/source.yaml)
- [`Target Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Target_Group.htm) -> [groups/target.yaml](groups/target.yaml)
- [`Threat Group`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Threat_Group.htm) -> [groups/threat.yaml](groups/threat.yaml)
- [`Geographical Attributes`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Geographical_Attributes.htm) -> [docs/field-suffixes.md](docs/field-suffixes.md)
- [`Resource Attributes`](https://www.microfocus.com/documentation/arcsight/arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide/Content/ESM_UserGuide/Resource_Attributes.htm) -> [docs/field-suffixes.md](docs/field-suffixes.md)

## Known spec quirks

- Key names and camelCase full names in the upstream tables contain mid-word line-wrap spaces (for example `destination DnsDomain` and `deviceCustomIPv6 Address1Label`) and occasional capitalized first letters (`Device Outbound Interface`, `DeviceCustomNumber2`, `Reason`); the generator joins the fragments and lowercases the first letter to restore the documented camelCase identifiers.
- The CEF 1.2 additions (zone keys, reportedResource*, frameworkName, threatActor, threatAttackID) carry prose full names such as `Agent Zone Key` instead of camelCase identifiers and are listed in both the producer and the consumer table; they appear here once with audience: both, full names verbatim.
- Data type spellings vary upstream (`MAC Address` vs `MAC address`, `Time Stamp` vs `TimeStamp`, `Floating Point` vs `Double`); the generator normalizes them to one vocabulary in extensions.yaml. ESM data types in groups/*.yaml are copied verbatim.
- Several consumer-table rows have empty Meaning cells upstream; the affected entries omit the description key.
- `dmac`: The upstream producer table lists dmac twice, in rows that differ only by a spelling fix in the description; the corrected row is kept.
