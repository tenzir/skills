<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/475067/software-install-uninstall-data-model -->

# Software Install / Uninstall Data Model

This data model describes software installation/removal activity.

Example events via Windows Agent:

- AO-WUA-InstSw-Added
- AO-WUA-InstSw-Removed

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where software was installed or uninstalled |
| appName | string | Application Name | Installed/Uninstalled Application name |
| appVendor | string | Application Vendor | Installed/Uninstalled Application vendor name |
| appVersion | string | Application Version | Installed/Uninstalled Application version |
| osObjAction | string | Object Action | Added or Removed |
