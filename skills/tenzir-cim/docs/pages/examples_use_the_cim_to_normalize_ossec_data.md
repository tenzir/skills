---
title: Use the CIM to normalize OSSEC data
url: https://help.splunk.com/en/data-management/common-information-model/8.5/examples/use-the-cim-to-normalize-ossec-data
last_modified: 2026-04-01T20:48:40.672Z
version: 8.5
---

# Use the CIM to normalize OSSEC data

This example demonstrates how to create an add-on for OSSEC, an open-source host-based intrusion detection system (IDS).

Note: Splunk offers an add-on that provides the capabilities in this example for OSSEC data, so you do not need to build one yourself. Find the add-on on Splunkbase at https://splunkbase.splunk.com/app/2808/ .

This example illustrates how to perform the following tasks:

- Evaluate data in the context of the CIM and Splunk Enterprise Security requirements.
- Use regular expressions to extract the necessary fields.
- Convert the values in the severity field to match the format required in the Common Information Model.
- Create multiple event types to identify different types of events within a single data source.
- Package the results as an add-on to share with the community.

## Step 1: Get the data in

To get started, set up a data input in order to get OSSEC data into Splunk Enterprise Security. OSSEC submits logs via `syslog `over port UDP:514, so you can use a network-based data input. Once you have built and installed the add-on, it will detect OSSEC data and automatically assign it the correct source type when it receives data over UDP port 514.

1. Configure folder and source type naming. Create a folder for the new add-on at `$SPLUNK_HOME/etc/apps/Splunk_TA-ossec `. (The name of this add-on is `Splunk_TA-ossec `.) For this add-on, use the source type `ossec `to identify data associated with the OSSEC intrusion detection system.

2. Configure line breaking. Because each log message separates itself with an end-line, you must disable line-merging to prevent the add-on from combining multiple messages. To do so, set `SHOULD_LINEMERGE `to false in the `default/props.conf `.

For example:

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]

   SHOULD_LINEMERGE = false

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

3. Restart the Splunk platform so that it recognizes the add-on and source type you defined.

## Step 2: Examine your data to identify relevant IT security events

1. Identify which events you want to display in the Intrusion Center dashboard in Splunk Enterprise Security. Use the CIM reference tables to find fields that are relevant for intrusion detection data. The data maps to the Intrusion Detection data model.

2. Open the reference table for that model to use as a reference. In Splunk Web, open the Data Model Editor for the IDS model to refer to the dataset structure and constraints.

## Step 3: Tag events

1. Identify the tags you must create. The Common Information Model dictates that you must tag intrusion detection data with " `attack `" and " `ids `" to indicate that the data comes from an attack detection event.

2. Create the event types to which you can assign tags. To do so, create an event type in the `eventtypes.conf `file that assigns the "ossec_attack" event type to all data with the source type `ossec `and a `severity_id `greater than or equal to 6.

```text
[ossec_attack]
search = sourcetype=ossec severity_id >=6
#tags = ids attack
```

3. Assign the tags in the `tags.conf `file.

```text
[eventtype=ossec_attack]
   attack = enabled
   ids = enabled
```

## Step 4: Verify tags

1. Verify that your Splunk platform applies the tags correctly. In the Searching and Reporting app, search for the source type as follows:

`sourcetype="ossec" `

2. Review the entries to find the tag statements under the log message.

## Step 5: Normalize fields

1. Create the field extractions that populate the fields according to the Common Information Model. First, review the Common Information Model and the Dashboard requirements matrix for Splunk Enterprise Security in Administer Splunk Enterprise Security to determine that the OSSEC add-on needs to include the following fields in order to populate the Intrusion Center and Intrusion Search dashboards in Splunk Enterprise Security:

| Domain | Field Name | Data Type |
| --- | --- | --- |
| Intrusion Detection | signature | string |
| Intrusion Detection | category | string |
| Intrusion Detection | severity | string |
| Intrusion Detection | src | string |
| Intrusion Detection | dest | string |
| Intrusion Detection | ids_type Note: ids_type of ` host ` is necessary to include this in the host root model | string |

You can also populate additional CIM fields, if they are available in your data.

2. Create extractions. OSSEC data is in a proprietary format that does not use key-value pairs or any kind of standard delimiter between the fields. Therefore, you have to write a regular expression to parse the individual fields. The following outlines a log message highlighting the relevant fields.

The severity field includes an integer, while the Common Information Model requires a string. Therefore, extract this into a different field, `severity_id `, then perform the necessary conversion later to produce the severity field.

3. Extract the Location, Message, severity_id, signature and src_ip fields. To do so, edit the `default/transforms.conf `file to add a stanza that extracts the fields you need to the following:

```text
[force_sourcetype_for_ossec]
   DEST_KEY = MetaData:Sourcetype
   REGEX = ossec\:
   FORMAT = sourcetype::ossec

   [kv_for_ossec]
   REGEX = Alert Level\:\s+([^;]+)\;\s+Rule\:\s+([^\s]+)\s+-
   \s+([^\.]+)\.{0,1}\;\s+Location\:\s+([^;]+)\;\s*(srcip\:\s+(\d{1,3}
   \.\d{1,3}\.\d{1,3}\.\d{1,3})\;){0,1}\s*(user\:\s+([^;]+)\;){0,1}\s*(.*)
   FORMAT = severity_id::"$1" signature_id::"$2" signature::"$3"
   Location::"$4" src_ip::"$6" user::"$8" Message::"$9"
```

4. Enable the statement in the `default/props.conf `file in your add-on folder.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

5. Extract the `dest `field. Some of the fields need additional field extraction to fully match the Common Information Model. The `Location `field includes several separate fields within a single field value. Create the following stanza in the `default/props.conf `file to extract the destination DNS name, destination IP address, and original source address.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec

   [kv_for_ossec]
   REGEX = Alert Level\:\s+([^;]+)\;\s+Rule\:\s+([^\s]+)\s+-
   \s+([^\.]+)\.{0,1}\;\s+Location\:\s+([^;]+)\;\s*(srcip\:\s+(\d{1,3
   }\.\d{1,3}\.\d{1,3}\.\d{1,3})\;){0,1}\s*(user\:\s+([^;]+)\;){0,1}\s*(.*)
   FORMAT = severity_id::"$1" signature_id::"$2" signature::"$3"
   Location::"$4" src_ip::"$6" user::"$8" Message::"$9"

   [Location_kv_for_ossec]
   SOURCE_KEY = Location
   REGEX = (\(([^\)]+)\))*\s*(.*?)(->)(.*)
   FORMAT = dest_dns::"$2" dest_ip::"$3" orig_source::"$5"
```

6. Enable the statement in the `default/props.conf `file in the add-on folder:

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec, Location_kv_for_ossec

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

7. The " `Location_kv_for_ossec `" stanza creates two fields that represent the destination (either by the DNS name or destination IP address). You need a single field named " `dest `" that represents the destination. To handle this, add stanzas to `default/transforms.conf `that populate the destination field if the `dest_ip `or `dest_dns `is not empty. Note that the regular expressions below work only if the string has at least one character. This ensures that the destination is not an empty string.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec

   [kv_for_ossec]
   REGEX = Alert Level\:\s+([^;]+)\;\s+Rule\:\s+([^\s]+)\s+-
   \s+([^\.]+)\.{0,1}\;\s+Location\:\s+([^;]+)\;\s*(srcip\:\s+(\d{1,3}\.\d{1,3
   }\.\d{1,3}\.\d{1,3})\;){0,1}\s*(user\:\s+([^;]+)\;){0,1}\s*(.*)
   FORMAT = severity_id::"$1" signature_id::"$2" signature::"$3"
   Location::"$4" src_ip::"$6" user::"$8" Message::"$9"

   [Location_kv_for_ossec]
   SOURCE_KEY = Location
   REGEX = (\(([^\)]+)\))*\s*(.*?)(->)(.*)
   FORMAT = dest_dns::"$2" dest_ip::"$3" orig_source::"$5"

   [dest_ip_as_dest]
   SOURCE_KEY = dest_ip
   REGEX = (.+)
   FORMAT = dest::"$1"

   [dest_dns_as_dest]
   SOURCE_KEY = dest_dns
   REGEX = (.+)
   FORMAT = dest::"$1"
```

8. Enable the field extractions you created in the `default/transforms.conf `file by adding them to the `default/props.conf `file. Set up your field extractions to ensure that you get the DNS name instead of the IP address if both are available. To do so, place the " `dest_dns_as_dest `" transform first; the Splunk platform processes field extractions in order, stopping on the first one that matches.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec, Location_kv_for_ossec
   REPORT-dest_for_ossec = dest_dns_as_dest,dest_ip_as_dest

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

9. Extract the `src `field. You populated the source IP into the field " `src_ip `", but the CIM requires a separate " `src `" field as well. To create the separate field, add a field alias in the `default/props.conf `file that populates the " `src `" field with the value in " `src_ip `".

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec, Location_kv_for_ossec
   REPORT-dest_for_ossec = dest_dns_as_dest,dest_ip_as_dest
   FIELDALIAS-src_for_ossec = src_ip as src

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

10. Normalize the severity field. The OSSEC data includes a field that contains an integer value for the severity. However, the Common Information Model requires a string value for the severity. Therefore, you need to convert the input value to a value that matches the Common Information Model. Do this using a lookup table. Map the " `severity_id `" values to the corresponding severity string, then create a CSV file in `lookups/ossec_severities.csv `.

```text
severity_id,severity
   0,informational
   1,informational
   2,informational
   3,informational
   4,error
   5,error
   6,low
   7,low
   8,low
   9,medium
  10,medium
  11,medium
  12,high
  13,high
  14,high
  15,critical
```

11. Add the lookup file definition to the `default/transforms.conf `file.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec

   [kv_for_ossec]
   REGEX = Alert Level\:\s+([^;]+)\;\s+Rule\:\s+([^\s]+)\s+-
   \s+([^\.]+)\.{0,1}\;\s+Location\:\s+([^;]+)\;\s*(srcip\:\s+(\d{1,3
   }\.\d{1,3}\.\d{1,3}\.\d{1,3})\;){0,1}\s*(user\:\s+([^;]+)\;){0,1}\s*(.*)
   FORMAT = severity_id::"$1" signature_id::"$2" signature::"$3"
   Location::"$4" src_ip::"$6" user::"$8" Message::"$9"

   [Location_kv_for_ossec]
   SOURCE_KEY = Location
   REGEX = (\(([^\)]+)\))*\s*(.*?)(->)(.*)
   FORMAT = dest_dns::"$2" dest_ip::"$3" orig_source::"$5"

   [dest_ip_as_dest]
   SOURCE_KEY = dest_ip
   REGEX = (.+)
   FORMAT = dest::"$1"

   [dest_dns_as_dest]
   SOURCE_KEY = dest_dns
   REGEX = (.+)
   FORMAT = dest::"$1"

   [ossec_severities_lookup]
   filename = ossec_severities.csv
```

12. Add the lookup to `default/props.conf `:

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec, Location_kv_for_ossec
   REPORT-dest_for_ossec = dest_dns_as_dest,dest_ip_as_dest
   FIELDALIAS-src_for_ossec = src_ip as src
   LOOKUP-severity_for_ossec = ossec_severities_lookup severity_id OUTPUT severity

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec
```

13. Define the vendor and product fields. The last fields to populate are the vendor and product fields. To populate these, add stanzas to the `default/transforms.conf `file to statically define them:

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false

   [source::udp:514]
   TRANSFORMS-force_sourcetype_for_ossec_syslog = force_sourcetype_for_ossec

   [kv_for_ossec]
   REGEX = Alert Level\:\s+([^;]+)\;\s+Rule\:\s+([^\s]+)\s+-
   \s+([^\.]+)\.{0,1}\;\s+Location\:\s+([^;]+)\;\s*(srcip\:\s+(\d{1,3}\.\d{1,3}\.\d{1,3
   }\.\d{1,3})\;){0,1}\s*(user\:\s+([^;]+)\;){0,1}\s*(.*)
   FORMAT = severity_id::"$1" signature_id::"$2" signature::"$3"
   Location::"$4" src_ip::"$6" user::"$8" Message::"$9"

   [Location_kv_for_ossec]
   SOURCE_KEY = Location
   REGEX = (\(([^\)]+)\))*\s*(.*?)(->)(.*)
   FORMAT = dest_dns::"$2" dest_ip::"$3" orig_source::"$5"

   [dest_ip_as_dest]
   SOURCE_KEY = dest_ip
   REGEX = (.+)
   FORMAT = dest::"$1"

   [dest_dns_as_dest]
   SOURCE_KEY = dest_dns
   REGEX = (.+)
   FORMAT = dest::"$1"

   [ossec_severities_lookup]
    filename = ossec_severities.csv

   [product_static_hids]
   REGEX = (.)
   FORMAT = product::"HIDS"

   [vendor_static_open_source_security]
   REGEX = (.)
   FORMAT = vendor::"Open Source Security"
```

14. Enable the stanzas in the `default/props.conf `file.

```text
[source::....ossec]
   sourcetype=ossec

   [ossec]
   SHOULD_LINEMERGE = false
   REPORT-0kv_for_ossec = kv_for_ossec, Location_kv_for_ossec
   REPORT-dest_for_ossec = dest_dns_as_dest,dest_ip_as_dest
   FIELDALIAS-src_for_ossec = src_ip as src
   LOOKUP-severity_for_ossec = ossec_severities_lookup severity_id OUTPUT severity
   REPORT-product_for_ossec = product_static_hids
   REPORT-vendor_for_ossec = vendor_static_open_source_security
```

## Step 6: Validate your CIM compliance

1. Verify that your field extractions function correctly. First, restart the Splunk platform so that it recognizes the lookups you created.

2. In the Searching and Reporting app, search for the source type.

`sourcetype="ossec" `

3. From the search results, select Pick Fields to choose the fields that the Splunk platform ought to populate. Hover over the field name to display the values (see example below).

Optional You can further validate using one of the following methods:

- Use Pivot. See Validate using Pivot for details.
- Use the `datamodel `command. See Validate using the `datamodel `command for details.
- Use the Splunk Enterprise Security dashboard in which you expect the data to appear. In this example, the OSSEC data ought to display in the Intrusion Center dashboard. The OSSEC data is not immediately available in the dashboard because Splunk Enterprise Security uses summary indexing. Therefore, the data may not be available on the dashboard for up to an hour after you have completed the add-on.

## Step 7: (Optional) Document and package your configurations as an add-on

1. Create a README file. In the file, include information necessary for others to use the add-on. Create the following `README.txt `file under the root add-on directory.

```text
===OSSEC add-on===

   Author: John Doe
   Version/Date: 1.3 September 2013

   Supported product(s):
   This add-on supports Open Source Security (OSSEC) IDS 2.5

   Source type(s): This add-on will process data that is source typed
   as "ossec".

   Input requirements: Syslog data sent to port UDP\514

   ===Using this add-on===

   Configuration: Automatic
   Syslog data sent to port UDP\514 will automatically be detected as OSSEC
   data and processed accordingly.

   To process data that is sent to another
   port, configure the data input with a source type of "ossec".
```

2. Package the OSSEC add-on by converting it into a zip archive named `Splunk_TA-ossec.zip `.

3. To share your add-on, go to https://splunkbase.splunk.com/develop/ , then click Submit your app .
