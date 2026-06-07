---
title: Install the Splunk Common Information Model Add-on
url: https://help.splunk.com/en/data-management/common-information-model/8.5/introduction/install-the-splunk-common-information-model-add-on
last_modified: 2026-04-01T20:48:26.936Z
version: 8.5
---

# Install the Splunk Common Information Model Add-on

- Download the Common Information Model add-on from Splunkbase at https://apps.splunk.com/app/1621/ .
- Review the indexes defined in CIM.

- The previously deprecated `cim_summary `index definition is now removed. If you have a custom configuration for this in your local `indexes.conf `file, it will persist as-defined.

- If you are no longer using this index definition, remove the stanza from your local `indexes.conf `file before installation.
- If you are still using it, you will need to revise the stanza if you were previously relying on parts of the deprecated default `cim_summary `index definition.
- The `cim_modactions `index definition is used with the common action model alerts and auditing. Make sure that the index exists and assign the appropriate Roles to search the index.
-

Note: Install the Splunk Common Information Model Add-on to your search heads only. Refer to Installing add-ons for detailed instructions describing how to install a Splunk add-on in the following deployment scenarios:

- Single-instance Splunk Enterprise
- Distributed Splunk Enterprise
- Splunk Cloud Platform
- Splunk Light

Next: See Set up the Splunk Common Information Model Add-on to perform optional configurations to improve performance.
