---
title: Use the CIM to normalize data at search time
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/use-the-cim-to-normalize-data-at-search-time
last_modified: 2026-04-01T20:48:22.344Z
version: 8.5
---

# Use the CIM to normalize data at search time

If you are working with a new data source, you can manipulate your already-indexed data at search time so that it conforms to the common standard used by other Splunk applications and their dashboards. Your goal might be to create a new application or add-on specific to this data source for use with Splunk Enterprise Security or other existing applications, or you might just want to normalize the data for your own dashboards.

This topic guides you through the steps to normalize your data to the Common Information Model, following established best practices.

To see these steps applied in a real use case, see Use the CIM to normalize CPU performance metrics .

Before you start, keep in mind that someone else may have already built an add-on to normalize the data you have in mind. Check Splunkbase for CIM-compatible apps and add-ons that match your requirements.

## 1. Get your data in

If you have not already done so, get your data in to the Splunk platform.

Do not be concerned about making your data conform to the CIM in the parsing or indexing phase. You normalize your data to be CIM compliant at search time. See Getting Data In if you need more direction for capturing and indexing your data.

## 2. Examine your data in the context of the CIM

Determine which data models are relevant for the data source you are working with.

Use the CIM reference tables to find fields that are relevant to your domain and your data. You might need to normalize data from a single event or source of events against more than one data model. Some events may be logs tracking create, read, update, delete (CRUD) changes to a system, others may log the login/logout activities for that system. For each different kind of event, look for data models that match the context of your data. For example, CRUD events map to the Change data model. Login events map to the Authentication data model.

You might see the `app `field in the Authentication, Network Traffic, or Web data models. Consider the source and purpose of the events. If the primary purpose is login activities, then Authentication is the data model to match against, even though the `app `field exists in multiple data models. Do not force-fit based solely on field name.

Refer to How to use these reference tables for a description of how to compare the information in the reference tables with the data models in the Data Model Editor page in Splunk Web. Keep both the documentation and the Data Model Editor open for reference, because you need to refer to them in the following steps.

## 3. Configure CIM-compliant event tags

Apply tags to categorize your event data according to type.

Categorizing your data allows you to specify the dashboards in which the data should appear, something that cannot necessarily be determined just by field names and sources. Many of the CIM data models have the same field names, so the tags act as constraints to filter the data to just the relevant events for that model. Also, many different sources may produce events relevant to a particular data model. For example, web applications, VPN servers, and email servers all have authentication events, yet the source and structure of these authentication events are considerably different for each type of device. Tagging all of the authentication related events appropriately makes it possible for your dashboards to pull data from the correct events automatically.

To apply the CIM-compliant tags to your data, follow these steps.

- Determine which tags are necessary for your data. Refer to the data models that use similar domain data to choose the tags from the Common Information Model that are needed. Remember to look for inherited tags from parent datasets. See How to use these reference tables for more information.
- Create the appropriate event types in Splunk Web by selecting Settings > Event types .
- Click New and create a new event type.
- Add or edit tags for the event type. Separate tags with spaces or commas.
- Click Save to save the new event type and tags.

If an event type already exists, add tags to the event type.

- In Splunk Web, click Settings > Event types .
- Locate the event type that you want to tag and click its name.
- On the detail page for the event type, add or edit tags in the Tags field. Separate tags with spaces or commas.
- Click Save .

Repeat this process for each of the tags needed to map your events to the correct datasets in the data models.

If you have access to the file system, you can add an event type by editing the local version of the `eventtypes.conf `file directly. You can also add tags for an event type using the file system. Edit the local version of the `tags.conf `file. For example:

```text
[eventtype=nessus] vulnerability = enabled report = enabled
```

The event type and tag modifications that you make are saved in `$SPLUNK_HOME/etc/users/$USERNAME$/$APPNAME$/local/eventtypes.conf `and `$SPLUNK_HOME/etc/users/$USERNAME$/$APPNAME$/local/tags.conf `.

For more information about event typing, see the Data Classification: Event types and transactions section in the Splunk Enterprise Knowledge Manager Manual . For more information about managing tags in Splunk Web, see Data normalization: tags and aliases in the Splunk Enterprise Knowledge Manager Manual .

## 4. Verify tags

To verify that the data is tagged correctly, display the event type tags and review the events.

- Search for the source type.
- Use the field picker to display the field `tag::eventtype `at the bottom of each event.
- Look at your events to verify that they are tagged correctly.
- If you created more than one event type, also check that each event type is finding the events you intended.

## 5. Make your fields CIM-compliant

Examine the fields available in the data model, and look for the equivalent fields in your indexed data. Some of the fields might already be present with the correct field names and value types that match the expectations of the Common Information Model. If you are not certain that your values match what is expected by the model, check the description of that field in the data model reference tables in this documentation.

Fields from different sources can use different names for similar events. You can map the names to CIM-compliant fields. For example, the following diagram shows login events from two different sources as mapped to CIM-compliant fields.

### a. Use the following search results to help prioritize field mapping

Use the following search results to help prioritize which fields to map when normalizing. The "recommended=true" fields are both commonly available in data sources of the intended type, and highly useful for security monitoring and investigations. Make a concerted effort to map appropriate fields from your source to these "recommended=true" data model fields. Without tagging for the recommended fields, an event may not be as useful.

`| rest splunk_server=local count=0 /services/data/models | rename title as model,eai:data as data | spath input=data output=objects path=objects{} | mvexpand objects | spath input=objects output=object_name path=objectName | spath input=objects output=fields path=fields{} | appendpipe [| spath input=objects output=fields path=calculations{}.outputFields{}] | mvexpand fields | spath input=fields output=field_name path=fieldName | spath input=fields output=recommended path=comment.recommended | table model,object_name,field_name,recommended | sort model,object_name,field_name `

You can also narrow down the search results by changing `/services/data/models `to one model, such as `/services/data/models/Alerts `.

Make note of all fields in the data model that do not correspond exactly to your event data. Some might not exist in your data, have different field names, or have the correct field names but have values that do not match the expected type of the model. Normalize your data for each of these fields using a combination of field aliases, field extractions, and lookups.

### b. Create field aliases to normalize field names

First, look for opportunities to add aliases to fields. Determine whether any existing fields in your data have different names than the names expected by the data models. For example, the Web data model has a field called `http_referrer `. This field may be misspelled as `http_referer `in your source data. Define field aliases to capture the differently-named field in your original data and map it to the field name that the CIM expects.

Also check your existing fields for field names that match the CIM field names but do not match the expected values as described in the data model reference tables. Your event may have an extracted field such as `id `that refers to the name of a completely different entity than the description of the field `id `in the CIM data model. Define a field alias to copy the `id `field from your indexed data to a different field name, such as `vendor_id `. The field alias is only part of the solution for preventing that data from appearing in reports and dashboards that expect the CIM `id `field. To capture the correct `id `field that you need for CIM compliance, you can either extract the field from elsewhere in your event, or write a lookup file to add that field from a CSV file.

See Add aliases to fields in the Splunk Enterprise documentation for more information about adding aliases to fields.

### c. Create field extractions to extract new fields

After you have added aliases to all the fields that you can, add missing fields. When the values that you need for the CIM data model exist in the event data, extract the necessary fields using the field extraction capabilities of the Splunk platform. Name the fields to exactly match the field names in the CIM data models.

See Build field extractions with the field extractor and Create and maintain search-time field extractions through configuration files in the Splunk Enterprise documentation.

### d. Write lookups to add fields and normalize field values

After you have aliased or extracted all the fields that you can in your indexed data, you might have to create lookup files to finish normalizing your data.

There are two reasons to create lookup files:

- Add fields that cannot be extracted from the event data. For example, your events might not contain the name of the `vendor `, `product `, or `app `of the system logging the event, but the data model you are mapping the data to expects all three of these fields. In this case, populate a CSV file with the source types generating the events and map each to the appropriate vendor name, product name, and application name.
- Normalize field values to make them compliant with the CIM. For example, the Network Traffic data model includes a `rule `field that expects string values that define the action taken in the network event. If your network traffic data contains a numeric value for the field `rule `, create a field alias for that field to something like `rule_id `so that it does not conflict with the `rule `field expected by the data model, which must be a string. Then, add a lookup to map the `rule_id `values to a new `rule `field with their corresponding string values.

See About lookups in the Knowledge Manager Manual .

### e. Verify fields and values

After you finish normalizing your fields and values, validate that the fields appear in your events as you intended.

- Search for the source type containing the data you are working to map to the CIM.
- Use the field picker to select all the fields you just aliased, extracted, or looked up in your data.
- Scan your events and verify that each field is populated correctly.
- If one of the normalized fields has an incorrect value, edit the extraction, update the field alias, or correct your lookup file to correct the value.

## 6. Validate your data against the data model

After you have added your event tags and normalized your data by extracting fields, adding field aliases, and writing lookups, the data from your source type should map to the CIM data models that you targeted. You can validate that your data is fully CIM compliant by using the data model itself, using Pivot or Datasets, or by searching the data model directly.

Validate your data with specific goals in mind. For each field that you normalized within each unique event type, think of a useful metric that you can build with Pivot or Datasets to assess whether your data appears as you expect. Whether you use Pivot or Datasets depends on the apps installed in your deployment.

- If you use a version of Splunk Enterprise prior to 6.5.0, or do not have the Splunk Datasets Add-on installed, use Pivot to validate that your data is CIM compliant.
- If you use Splunk Cloud Platform or version 6.5.0 or later of Splunk Enterprise and have the Splunk Datasets Add-on installed, use Datasets to validate that your data is CIM compliant.

### a. Validate using Datasets

If you have the Splunk Datasets Add-on installed, you can use Datasets to check whether your own login activity appears in your authentication data.

- In the Search and Reporting app, click Datasets .
- Select the data model and dataset in the model that you want to visualize with Pivot. For this example, locate Authentication > Authentication > Successful Authentication and click Explore > Visualize with Pivot .
- Set the time range to an appropriate range to speed up the search. For this example, select Last 15 minutes if you recently logged in to a system.
- Apply a filter to match your source type.
- Split rows and columns by other relevant attributes in the model. For example, you might split the rows by `user `to see a list of usernames that have logged in during the past 15 minutes.

### b. Validate using Pivot

If you do not have the Splunk Datasets Add-on installed and are not a Splunk Cloud Platform customer, use Pivot. In this example, check whether your own login activity appears in your authentication data.

- In the Search and Reporting app, click Pivot .
- Select the data model against which you want to validate your data, then click into a relevant dataset in the model. For this example, select Authentication , then Successful Authentication .
- Set the time range to an appropriate time range to speed up the search. For this example, set it to Last 15 minutes if you recently logged in to a system.
- Apply a filter to match your source type.
- Split rows and columns by other relevant attributes in the model. For example, you might split the rows by `user `to see a list of usernames that have logged in during the past 15 minutes.

### c. Validate by searching the data model

You can search the data model using the `datamodel `command or the `| from datamodel `search syntax.

- Open the Search and Reporting app.
- Construct a search referencing the data model, including a filter for your source type, the `table `command, and the `field summary `command.

For example, format a search using the `datamodel `command as follows:

`| datamodel <Data_Model> <Data_Model_Dataset> search | search sourcetype=<your:sourcetype> | table * | fields - <List any statistics columns that you do not want to display> | fieldsummary `

To use the `| from datamodel `syntax, format your search as follows:

`| from datamodel:<Data_Model>.<Data_Model_Dataset> | search sourcetype=<your:sourcetype> | table * | fields - <List any statistics columns that you do not want to display> | fieldsummary `
- Observe the results of the search. To identify problems with your field normalizations, scan this table to look for empty values, incorrect values, or statistics that do not match your expectations.

The `datamodel `command performs a search against the data model and returns a list of all fields in the model, some statistics about them, and sample output from your data in the values column. You can remove statistics columns by specifying them after the `| fields - `portion of the search string.

The `from `command does the same search, but flattens the results, so the field names are not prefaced with the name of the data model.

You can use these example searches to check for problems with your source type and field normalizations.

| Normalization | Description |
| --- | --- |

| Source Type | You can use this example search to check for problems with your source type normalizations. For example, where your source type is a Cisco device, you can search for the following: ` \| datamodel Network_Traffic All_Traffic search \| search sourcetype=cisco:* \| stats count by sourcetype ` If you don't see all the ` sourcetype ` results that you expect, then you may need to revisit the corresponding add-on details. See Supported Add-ons . |

| Field | You can use this example search to check for problems with your field normalizations. For example, where your source type is a Linux Secure device, you can use this example search to check that Linux Secure data maps as expected to the Authentication data model for successful login activities. ` \| datamodel Authentication Successful_Authentication search \| search sourcetype=linux_secure \| table * \| fields - date_* host index punct _raw time* splunk_server sourcetype source eventtype linecount \| fieldsummary ` Here is the result using the example search string above. |

For more information about the datamodel command, see the datamodel in the Search Reference manual.

## 7. (Optional) Extend the CIM definition with custom fields

If some of the fields that you want to use are not defined in the data model by default, you can add fields to a dataset. As a precaution, consider keeping a record of your modifications, so that they can be reapplied if models are updated or restored in the future. You can do this by selecting download from the datamodel editor page, after you have made your modifications.

Add new fields as follows:

- From the Splunk ES menu bar, click Search > Datasets .
- Find the name of the Data Model and click Manage > Edit Data Model .
- From the Add Field drop-down, select a method for adding the field, such as Auto-Extracted .

- If you see the field name, check the check box for it, enter a display name, and select a type.
- If you don't see the field name, click Add by Name , enter the field name, enter a display name, and select a type.

Then you can search the dataset again:

- From the Splunk ES menu bar, click Search > Datasets .
- Find the name of the Data Model and click Explore > Investigate in Search .
- The search displays in the search bar:

`| from datamodel:"Web.Web" `and the new field displays in the results.

Note: It is not considered a best practice to clone the data model and to keep the original for record keeping purposes. Cloning would create an entirely new model that wouldn't be referenced in any downstream searches.

## 8. (Optional) Package your configurations as an add-on

Now that you have tested your field extractions, lookups, and tags, you can choose to package the search-time configurations as an add-on and publish it to the community. Using your add-on, other Splunk platform users with the same data source can map their data to the CIM without having to repeat the steps you completed above.

See Package and publish a Splunk app on the Splunk Developer Portal.
