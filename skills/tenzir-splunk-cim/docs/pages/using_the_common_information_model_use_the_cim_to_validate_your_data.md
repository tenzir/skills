---
title: Use the CIM to validate your data
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/use-the-cim-to-validate-your-data
last_modified: 2026-04-01T20:48:22.568Z
version: 8.5
---

# Use the CIM to validate your data

The Common Information Model offers several built-in validation tools.

## Use the ` datamodelsimple ` command

To determine the available fields for a data model, you can run the custom command `datamodelsimple `. Use or automate this command to recursively retrieve available fields for a given dataset of a data model.

You can use `datamodelsimple `in scenarios such as exploring the structure of data models or using the output of the command to create custom dashboards. This is helpful for technology add-on developers and dashboard content writers.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

The following format is expected by the command.

CODE Copy | datamodelsimple type=<models|objects|attributes> datamodel=<model name> object=<dataset name> nodename=<dataset lineage>

```text
`| datamodelsimple type=<models|objects|attributes> datamodel=<model name> object=<dataset name> nodename=<dataset lineage>`
```

### Syntax for datamodelsimple

`datamodelsimple [datamodelsimple-options] `

### Parameters for datamodelsimple

The following parameters are optional unless otherwise specified.

[datamodelsimple-options]

Optional parameters for datamodelsimple command.

syntax: `type=<datamodelsimple-option-type> <datamodelsimple-option-datamodel> <datamodelsimple-option-object> <datamodelsimple-option-nodename> `

[datamodelsimple-option-type]

The list that will be returned.

syntax: `models|objects|attributes `

examples:

- models = returns a list of model names, such as `Authentication `
- objects = returns a list of object names, such as `Authentication.Failed_Authentication `
- attributes = returns a list of attribute names, such as `host, authentication_method, dest_bunit, reason `

[datamodelsimple-option-datamodel]

The datamodel name. Required for `type=objects `and `type=attributes `.

syntax: `datamodel=<string> `

[datamodelsimple-option-object]

The datamodel object name. Required for `type=attributes `.

syntax: `object=<string> `

[datamodelsimple-option-nodename]

The datamodel object name including lineage. Required for `type=attributes `in lieu of object.

syntax: `nodename=<string> `

### Examples for datamodelsimple

You can use the datamodelsimple command in Splunk Web UI searches.

- List all the data models in the environment.

`| datamodelsimple type=models `

- List the objects in the Authentication data model.

`| datamodelsimple type=objects datamodel=Authentication `

- List attributes for the Failed_Authentication object in the Authentication data model.

`| datamodelsimple type=attributes datamodel=Authentication nodename=Authentication.Failed_Authentication `

## Use the CIM Validation (S.o.S.) datamodel

Version 4.2.0 of the Common Information Model moves the CIM Validation datasets into their own data model. Previously, the validation datasets were located within each relevant model.

Note: Accelerating the CIM Validation (S.o.S.) data model might cause potential issues.

Access the CIM Validation (S.o.S.) model in Pivot. From there, you can select a top-level dataset, a Missing Extractions search, or an Untagged Events search for a particular category of data. See Introduction to Pivot in the Splunk Enterprise Pivot Manual .

From the Splunk Enterprise menu bar, access the model from the following steps:

- Select Settings > Data models
- Locate the CIM Validation (S.o.S.) data model and in the Actions column, click Pivot.
- Click one of the following to create the Pivot:

- Top level dataset
- Missing extractions
- Untagged events
- Click Save As... to save your changes as a report or a dashboard panel.

### Top level datasets

Top level datasets such as Authentication tell you what is feeding the model. Pivot allows you to validate that you are getting what you expect from your available source types. For best results, split rows by source type and add a column to the table to show counts for how many events in that source type are missing extractions. The following screenshot shows an example of how that looks using Authentication as an example.

If you see values in the missing extractions column, and the data model is accelerated, you can go to the Datamodel Audit Dashboard in Splunk Enterprise Security. See Datamodel Audit Dashboard for more information. Alternatively, you can access the appropriate Missing Extractions dataset in Pivot to drill further into the attributes.

### Missing extractions

Missing extractions run searches that return all missing field extractions. There are certain field extractions that are expected in order to fully populate that dataset of the data model, and the names display here if the data is missing. In other words, Splunk Enterprise finds tagged events for this dataset in this model, but there are field extractions for this event type that Splunk Enterprise expects, but they are not present. If you get results, split rows by source type to find which data source is contributing events for this model but is not fully mapping to the CIM.

### Untagged events

Untagged events runs a search for events that have a strong potential for CIM compliance but are not tagged with the appropriate tag or tags. For example, the Untagged Authentication search is:

`(login OR "log in" OR authenticated) sourcetype!=stash NOT tag=authentication `

For best results, split by source type. Click the results to drill into the untagged events.
