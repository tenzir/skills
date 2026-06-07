---
title: Use the CIM to create reports and dashboards
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/use-the-cim-to-create-reports-and-dashboards
last_modified: 2026-04-01T20:48:22.654Z
version: 8.5
---

# Use the CIM to create reports and dashboards

If you are working with data that has already been normalized to the Common Information Model, you can use the CIM data models to generate visualizations, reports, and dashboards the same way you would use any other data model in the Splunk platform.

Your data is normalized if you or someone else in your organization have completed the normalizing steps described in Use the CIM to normalize data at search time , or you are using an add-on that normalizes data to the CIM data models.

## Example: Create a report to analyze authorization events using CIM data models

For example, you want to create a report to monitor authorization events on your systems. Both the Authentication and Change data models contain authorization-relevant fields. You can create reports using search or using Pivot. This example uses Pivot.

Start by opening the Change data model in Pivot. You can open a data model in Pivot two different ways, depending on if you use the Splunk Datasets Add-on or not.

- If you use Splunk Cloud Platform or you have the Splunk Datasets Add-on, open a data model in Pivot with the following steps:

- In the Search and Reporting App, click Datasets .
- Locate the Change > All Changes > Account Management data model and datasets.
- Click > to review the fields available in the dataset of the data model.
- Click Explore > Visualize with Pivot to open Pivot to explore the data model and dataset.
- If you do not have the Splunk Datasets Add-on, or do not use Splunk Cloud Platform, you can open a data model in Pivot with the following steps:

- In the Search and Reporting App, click Pivot .
- Select the Change data model. Observe that it has a child dataset called Account Management.
- Click > next to the Account Management dataset and its child datasets to browse the available events and fields contained in the model.

Then, create a report in Pivot. This report uses the Account Management dataset of the Change data model.

For example, to see the number of account lockouts over the past hour, create a report as follows.

- In Pivot, select the Area Chart option.
- Set the time range to Last 60 minutes .
- If the `dest_category `field is in use, you can filter based on the destination category to review account lockouts only on specifically-categorized machines. Otherwise, leave the filter blank.
- Leave the X-axis as the default of time.
- Select a field of `is_Account_Lockouts `for the Y-axis.
- (Optional) Modify additional settings.
- Select Save As > Report to save the chart as a report.

After creating the report, you can add the report to a dashboard and adjust the permissions so that others can view it.

## Resources for using Pivot with data models

To learn more about using Pivot with data models, use the following resources.

- See About Data Models in the Splunk Enterprise Knowledge Manager Manual .
- See the Introduction to Pivot in the Splunk Enterprise documentation.

## Use the Data Model Audit dashboard and Machine Learning ToolKit

You can use the dashboard included with the Common Information Model to monitor your data model accelerations and searches. The Common Information Model includes the Data Model Audit dashboard to help you analyze the performance of your data model accelerations.

Access these dashboard by going to the Search and Reporting app. From there, click Dashboards to view your list of dashboards. When the Splunk Common Information Model Add-on is installed, the dashboard appear in the list.

For more detail on the data model audit dashboard, see Check the status of data model accelerations in this manual.

You can also use MLTK to find different varieties of anomalous events in your data. See Machine Learning Toolkit Overview in Splunk Enterprise Security in the Splunk Enterprise Security Administer Splunk Enterprise Security manual.
