---
title: Release notes for the Splunk Common Information Model Add-on
url: https://help.splunk.com/en/data-management/common-information-model/8.5/introduction/release-notes-for-the-splunk-common-information-model-add-on
last_modified: 2026-04-02T22:24:27.431Z
version: 8.5
---

# Release notes for the Splunk Common Information Model Add-on

Version 8.5.0 of the Splunk Common Information Model Add-on was released on April 2, 2026.

Note: The version number for the Common Information Model is synchronized with the version number of Splunk Enterprise Security from this release.

## New features or enhancements

Version 8.5.0 of the Common Information Model (CIM) includes the following new enhancement:

Table 1. Summary of changes | Enhancement | Description |
| --- | --- |
| Python support | Support for future deprecations of Python 3.9. |

## Upgrade requirements

| Splunk platform version | Upgrade activity |
| --- | --- |
| 8.0.x or later | If you apply custom tags to data mapped to CIM data models and you use these tags in searches and search filters, add these tags to the allowlists for those models. See Set up the Splunk Common Information Model Add-on for details about the tags allow list field. |

## Compatibility

Version 5.0.x and higher of the Splunk Common Information Model Add-on requires Splunk platform version 8.0.x or higher. Some workarounds, such as the data models spec workaround for tags_allowlist and poll_buckets, are no longer available in version 7.0.x and higher. This might lead to btool check warnings at startup.

## Fixed issues

CIM version 8.5.0 of the Splunk Common Information Model Add-on fixes the following issues. If this section is empty, this release has no reported fixed issues.

| Issue | Date fixed | Description |
| --- | --- | --- |
| CIM-1488 | 03-05-2026 | Remove adaptive response relays empty global alert actions settings. |
| CIM-1486 | 02-19-2026 | Update shared sub-module for detection failures in Splunk Enterprise Security. |

## Limitations

If you are in a search head cluster environment on Splunk Cloud Platform, you might see error messages related to adaptive response actions. To troubleshoot these issues, see Troubleshoot adaptive response actions in search head cluster deployments on Splunk Cloud Platform .

## Known issues

This version of the Splunk Common Information Model Add-on has the following reported known issues. If this section is empty, this release has no reported known issues.

## Deprecated or removed features

The following are deprecated or removed features:

As of version 8.5.0:

- N/A

As of version 6.4.0:

- N/A

As of version 6.3.0:

- N/A

As of version 6.2.0:

- N/A

As of version 6.1.0:

- N/A

As of version 6.0.4:

- N/A

As of version 6.0.3:

- N/A

As of version 6.0.2:

- N/A

As of version 6.0.1:

- N/A

As of version 6.0.0:

- N/A

As of version 5.3.3:

- N/A

As of version 5.3.2:

- N/A

As of version 5.3.1:

- N/A

As of version 5.2.0:

- N/A

As of version 5.1.1:

- N/A

As of version 5.1.0:

- N/A

As of version 5.0.1:

- N/A

As of version 5.0.0:

- N/A

As of version 4.20.2:

- N/A

As of version 4.20.0:

- N/A

As of version 4.19.0:

- N/A

As of version 4.18.0:

- The `body `field is deprecated in favor of the `description `field in the Alerts data model and will be removed in a future version.
- The `subject `field is deprecated in favor of the `signature `field in the Alerts data model and will be removed in a future version.

As of version 4.15.0:

- The Predictive Analytics dashboard is removed in favor of Machine Learning Toolkit functionality.

As of version 4.14.0:

- The Predictive Analytics dashboard is deprecated in favor of Machine Learning Toolkit functionality and will be removed in a future version.

As of version 4.13.0:

- N/A

## Third-party software attributions

The Splunk Common Information Model Add-on does not incorporate any third-party software or libraries.
