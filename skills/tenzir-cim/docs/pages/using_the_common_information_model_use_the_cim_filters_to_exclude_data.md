---
title: Use the CIM Filters to exclude data
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/use-the-cim-filters-to-exclude-data
last_modified: 2026-04-01T20:48:40.151Z
version: 8.5
---

# Use the CIM Filters to exclude data

The CIM Filter macros are available to help exclude data from your search results. The macros are a way to reduce false positives by whitelisting categories from lookups, data model objects, event severities, or extracted fields. They are available by default and located in the `CIM Filters `section of the `$SPLUNK_HOME/etc/apps/Splunk_SA_CIM/default/macros.conf `file for reference. There is no need to modify the stanzas in this section.

## Usage

To use the `cim_filter_known_scanners `macro, for example, the most common use case is with Splunk Enterprise Security.

In this case, a known scanner is a device on your network that is purposely doing active or passive vulnerability scans. You might get a lot of false positive alerts about this device because the scanning activity is generating a lot of notable events. You know that these events can be ignored because it's your own scanner. You can categorize this device as a known_scanner in the assets and identities system. Then you can use the macro to filter out that category, so you no longer see the device in the search results.

See the "Asset lookup header" section of Format an asset or identity list as a lookup in Splunk Enterprise Security in the Administer Splunk Enterprise Security manual for more information about where to add known_scanner as a category and how to maintain the asset and identity categories list, which is customized to your environment.

## Example

The macros are for use with piped searches or where clauses. For the example of `cim_filter_known_scanners `, you can see in the `macros.conf `file that you can use it in two ways.

One way to use the macro is with search:

`... | search `cim_filter_known_scanners` | ... `

The other way to use the macro allows you to pass the DataModel.DataSet object lineage with tstats:

`| tstats count from datamodel="Intrusion_Detection.IDS_Attacks" where `cim_filter_known_scanners(IDS_Attacks)` `

See Define search macros in Settings in the Splunk Enterprise Knowledge Manager Manual for further information on how to navigate to and edit the macro definition in Splunk Web.
