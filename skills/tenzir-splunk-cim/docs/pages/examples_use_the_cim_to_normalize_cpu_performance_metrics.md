---
title: Use the CIM to normalize CPU performance metrics
url: https://help.splunk.com/en/data-management/common-information-model/8.5/examples/use-the-cim-to-normalize-cpu-performance-metrics
last_modified: 2026-04-01T20:48:22.484Z
version: 8.5
---

# Use the CIM to normalize CPU performance metrics

This example illustrates how to normalize data for CIM-compliance for an IT Service Intelligence use case. This example provides two variations: one using Splunk Web, and another using configuration files from the command line.

## Normalize data for CIM-compliance using Splunk Web

### Step 1. Get your data in

For the purposes of this example, assume that you have already added data to your Splunk platform deployment. For instructions on adding data, see Getting Data In .

### Step 2. Examine your data in context of the CIM

Make sure that the data that you want to extract has a dataset specified in the CIM. For example, if you want to build a KPI search based on a specific CPU performance metric, such as `cpu_load_percent `, review the Performance data model to make sure that the data model lists `CPU `as a dataset.

If the CIM does not contain the specific data that you want to extract for your KPI searches, you can use a Splunk add-on or apply the Common Information Model to your own data. See Design data models in the Splunk Enterprise Knowledge Manager Manual .

### Step 3. Configure CIM-compliant event types

- From Splunk Web, select Settings > Data Models .
- Find the data model dataset that you want to map your data to, then identify its associated tags.

For example, the `CPU `dataset in the `Performance `data model has the following tags associated with it:

CODE Copy tag = performance tag = cpu

```text
`tag = performance tag = cpu`
```

- Create an event type.

- Select Settings > Event types .
- Click New.
- In the Add new dialog, type the following values for the following fields.

| Destination App: | ITSI |
| --- | --- |
| Name: | Type the name of the event type. For example, ` cpu_metrics ` . |
| Search String: | Type a search string for the event type. For example, ` sourcetype=test_cpu_log ` . |
| Tag(s): | Type the tags associated with the data model dataset you are mapping to. For example, ` performance ` , ` cpu ` . |
| Color | Select a color for the event type. Priority determines which event type color displays for an event. For more information, see About event type priorities . |
| Priority | Select a priority from 1 to 10, with 1 being the highest and 10 being the lowest. For more information, see About event type priorities . |

- Click Save .

For more information, see Configure event types in Splunk Web in the Splunk Enterprise Knowledge Manager Manual .

### Step 4. Verify your tags

See Use the CIM to normalize data at search time for details.

### Step 5. Make fields CIM-compliant

Create field aliases to make fields CIM-compliant.

Note : Field aliases do not support multi-value fields. For more information, see Create aliases for fields .

- From Splunk Web, select Settings > Fields > Field Aliases .
- Click New .
- In the Add New window, type the following:

- For Destination App: , select ITSI.
- For Name: , type a name for your field alias.
- For Apply to: , select Sourcetype .
- For named: , type the name of the source type. For example, `test_cpu_log `.
- Restart the Splunk platform for your changes to take effect.
- Create search-time field extractions.

If your event data contains fields that are not found in existing data models or search-time field extractions, you can add those fields using the Field Extractions page in Splunk Web. See Use the Field extractions page in the Knowledge Manager Manual .
- Write lookups to add fields and normalize field values.
- Verify fields and values.

### Step 6. Validate normalized data against the data model

Now that you have mapped your data to the CIM, you can validate that your data is CIM-compliant. See 6. Validate your data against the data model .

## Normalize data for CIM-compliance using configuration files

This section demonstrates how to normalize data for CIM-compliance at search-time using Splunk configuration files.

### Step 1. Get your data in

For the purposes of this example, assume that you have already added data to your Splunk platform deployment. For instructions on adding data, see Getting Data In .

### Step 2. Examine your data in context of the CIM

Make sure that the data that you want to extract has a dataset specified in the CIM. For example, if you want to build a KPI search based on a specific CPU performance metric, such as `cpu_load_percent `, review the Performance data model to make sure that the data model lists `CPU `as a dataset.

If the CIM does not contain the specific data that you want to extract for your KPI searches, you can use a Splunk add-on or apply the Common Information Model to your own data. See Design data models in the Splunk Enterprise Knowledge Manager Manual .

### Step 3. Configure CIM-compliant event tags

- Determine which tags are associated with the data model dataset. In Splunk Web, select Settings > Data Models .
- Find the data model dataset that you want to map your data to, then identify its associated tags.

For example, the `cpu_load_percent `attribute in the `CPU `dataset in the `Performance `data model has the following tags associated with it:

CODE Copy tag = performance tag = cpu

```text
`tag = performance tag = cpu`
```

- On the search head, edit or create an `$SPLUNK_HOME/etc/apps/$APPNAME$/local/eventtypes.conf `file, then manually add the event type.

For example:

CODE Copy [cpu_metrics] search = sourcetype=test_cpu_log

```text
`[cpu_metrics]
search = sourcetype=test_cpu_log`
```

- On the search head, edit or create a `$SPLUNK_HOME/etc/apps/$APPNAME$/local/tags.conf `file, then manually add the appropriate tags for the data model dataset. For example:

CODE Copy [eventtype=cpu_metrics] performance = enabled cpu = enabled

```text
`[eventtype=cpu_metrics]
performance = enabled
cpu = enabled`
```

- Restart the Splunk platform.

For more information, see Configure event types in eventtypes.conf .

### Step 4. Verify your tags

See Use the CIM to normalize data at search time .

### Step 5. Make fields CIM-compliant

Create field aliases to make fields CIM-compliant, then add search-time field extractions for additional fields as needed.

- Create field aliases in `props.conf `. You can create multiple field aliases in a single stanza. Create your field alias by adding the following line to a stanza in the `$SPLUNK_HOME/etc/apps/$APPNAME$/local/props.conf `file.

CODE Copy FIELDALIAS-<class> = <orig_field_name> AS <new_field_name>

```text
`FIELDALIAS-<class> = <orig_field_name> AS <new_field_name>`
```

For example:

CODE Copy [test_cpu_log] FIELDALIAS-cpu_percent = cpu_percent AS cpu_load_percent

```text
`[test_cpu_log]
FIELDALIAS-cpu_percent = cpu_percent AS cpu_load_percent`
```

- Restart the Splunk platform for your changes to take effect.
- Create basic search-time field extractions in `props.conf `by adding an EXTRACT stanza to `$SPLUNK_HOME/etc/apps/$APPNAME$/local/props.conf `:

CODE Copy EXTRACT-<class> = [<regular_expression>|<regular_expression> in <source_field>]

```text
`EXTRACT-<class> = [<regular_expression>|<regular_expression> in <source_field>]`
```

For more information about field aliases, see Create aliases for fields in the Knowledge Manager Manual .

For more information about search-time field extractions, see Create basic search-time field extractions with props.conf edits .

### Step 6. Validate normalized data against the data model

Now that you have mapped your data to the CIM, you can validate that your data is CIM-compliant. See 6. Validate your data against the data model .
