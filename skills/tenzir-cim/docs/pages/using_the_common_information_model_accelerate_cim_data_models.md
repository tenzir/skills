---
title: Accelerate CIM data models
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/accelerate-cim-data-models
last_modified: 2026-04-01T20:48:39.694Z
version: 8.5
---

# Accelerate CIM data models

You can accelerate a data model to speed up the data set represented by that data model for reporting purposes. After you accelerate a data model, your reports and dashboard panels that reference the accelerated data model will return results faster. A data model's summary range setting impacts the size of the data models on disk, and the processing load of creating accelerated data alongside the index buckets. For more information about accelerating data models, see Enable data model acceleration in the Knowledge Manager Manual for Splunk Enterprise.

On the Splunk Cloud Platform, running accelerated data models might impact the performance of the search head since these heavy searches that collect the data for the data acceleration model can cause the search head to run out of processing power.

Additionally, when a time summary range of over 3 months is selected, it might cause searches to run on a loop. This implies that even though the search head is unable to finish the first search and build a data model, it repeats the same search that creates incomplete data models since accelerated data models are searches that run in the background to build a data model. For more information on how to change the summary time range, see Change the summary time range for data model accelerations .

## Enable data model acceleration

By default, the data model acceleration for all models included in the Splunk Common Information Model Add-on are disabled.

Configure the acceleration parameters of the CIM data models in the CIM Setup view.

- In Splunk Web, go to Apps > Manage Apps .
- Click on Set up in the row for Splunk Common Information Model.
- Click on the Settings tab.
- Select a data model that you want to accelerate.
- Click the box next to acceleration.enabled to accelerate the model.
- (Optional) Configure the advanced acceleration settings.

| Parameter | Description |
| --- | --- |
| acceleration.backfill_time | How far back in time the Splunk platform should create its column stores, specified as a relative time string. Only set this parameter if you want to backfill less data than the retention period set by 'acceleration.earliest_time'. Refer to ` datamodels.conf.spec ` for warnings and limitations. |
| acceleration.earliest_time | How far back in time the Splunk software should keep these column stores, specified as a relative time string. |
| acceleration.max_time | The maximum amount of time that the column store creation search is allowed to run, in seconds. |
| acceleration.max_concurrent | The maximum number of concurrent acceleration instances for this data model that the scheduler is allowed to run. |
| acceleration.manual_rebuilds | When checked, this setting prevents outdated summaries from being rebuilt by the 'summarize' command. Admins can manually rebuild a data model through the Data Model Manager page by expanding the row for the affected data model and clicking Rebuild . |

For more detailed reference information on these fields, see Advanced configurations for persistently accelerated data models in the Knowledge Manager Manual in the Splunk Enterprise documentation.
- Click Save .

For more information about accelerated data models and data model acceleration jobs, see Use the data model audit dashboard in this topic.

## Disable acceleration for a data model

If you have Splunk Enterprise Security or the Splunk App for PCI Compliance installed, some of the data models in the CIM are automatically accelerated by configuration settings in these apps. If you want to change which data models are accelerated by these apps, access the Data Model Acceleration Enforcement modular input on your search head and make your changes there. If you attempt to unaccelerate a data model using any other method, including using the Settings tab in the CIM Setup page, your changes will not persist because the the app acceleration enforcement re-accelerates the data models automatically.

If you do not have an app installed that enforces any CIM data models to be accelerated, you can edit the acceleration settings on the CIM Setup page.

- In Splunk Web, go to Apps > Manage Apps
- Click on Set up in the row for Splunk Common Information Model.
- Click on the Settings tab.
- Select the data model for which you want to disable acceleration.
- Uncheck the box next to acceleration.enabled to stop accelerating this data model.
- Click Save .

## Change the summary range for data model accelerations

A data model's summary range setting impacts the size of the data models on disk, and the processing load of creating accelerated data alongside the index buckets.

- In Splunk Web, go to Apps > Manage Apps .
- Find the Splunk Common Information Model add-on.
- Click Set up to open the CIM Setup page.
- Click the Settings tab.
- Select the data model you want to change.
- Set a summary range:

- Review the acceleration.enabled setting. A summary range only applies to accelerated data models.
- Review the acceleration.earliest_time setting to determine the current summary range.
- Change the acceleration.earliest_time setting. Examples: -1y, -3mon, -1mon, -1w, -1d, or 0 for "All Time".
- Select Save .

The CIM Setup page will only display CIM data models. A custom data model will not be displayed and cannot have its settings changed from the CIM Setup page. To change the summary range or other settings on a custom data model, manually edit the `datamodels.conf `provided with the app or add-on. For more information, see the datamodels.conf spec file in the Splunk Enterprise Admin Manual .

## Use the Data Model Audit dashboard

Use the Data Model Audit dashboard to display information about the state of data model accelerations in your environment. Alternatively, use the ``cim_datamodelinfo` `macro to search the data model statuses from the search bar.

To access the dashboard:

- Go to the Search and Reporting app.
- In the menu bar, click Dashboards .
- Select the Data Model Audit dashboard.

### Check the status of data model accelerations

| Panel | Description |
| --- | --- |
| Top Accelerations By Size | Displays the accelerated data models sorted in descending order by MB on disk |
| Top Accelerations By Run Duration | Displays the accelerated data models sorted in descending order by the time spent on running acceleration tasks. |
| Acceleration Details | Displays a table of the accelerated data models with additional information. |
