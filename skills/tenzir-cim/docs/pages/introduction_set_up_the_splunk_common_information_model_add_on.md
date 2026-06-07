---
title: Set up the Splunk Common Information Model Add-on
url: https://help.splunk.com/en/data-management/common-information-model/8.5/introduction/set-up-the-splunk-common-information-model-add-on
last_modified: 2026-04-01T20:48:27.035Z
version: 8.5
---

# Set up the Splunk Common Information Model Add-on

Perform optional configurations on the Splunk Common Information Model Add-on Setup page.

- Constrain the indexes that each data model searches in order to improve performance.
- Configure the tag allowlist that each data model searches.
- Enable or adjust the acceleration of each data model.

Access the setup page by selecting Apps > Manage Apps and then clicking Set up in the row for Splunk Common Information Model. You can only use the setup page on Splunk platform version 6.4.x or later. With Splunk_SA_CIM version 4.11.0 and lower, you need to have the admin_all_objects capability. With Splunk_SA_CIM version 4.12.0 and higher, you need to have the accelerate_datamodel capability. If you do not see a link to set up the app, you can access the setup page directly by going to `https://<URL of your Splunk deployment>/en-US/app/search/cim_setup `.

## Set index constraints

Improve performance by constraining the indexes that each data model searches. By default, each data model searches all indexes.

- In Splunk Web, access the CIM Setup page:

- Select Apps > Manage Apps and then click Set up in the row for Splunk Common Information Model.
- Access the setup page directly by going to `https://<URL of your Splunk deployment>/en-US/app/search/cim_setup `.
- Select the data model that you want to modify.
- In Indexes allowlist , type the index that the data model should search. You can type the names of indexes that are defined only on indexers.
- Click Save .

If you constrain a data model to selected indexes and then later add another index to your environment that is also relevant to the data model, return to this page and add the new index to the data model constraints.

## Accelerating CIM data models

Enable acceleration for data models to return results faster for searches, reports, and dashboard panels that reference the data model.

The summary range settings of a data model affect the size of the data models on disk and also affect the processing load on the indexers due to the load of creating accelerated data alongside the index buckets. See Enable data model acceleration in the Knowledge Manager Manual for Splunk Enterprise.

All data models included in the CIM add-on have data model acceleration turned off by default.

If you have Splunk Enterprise Security or the Splunk App for PCI Compliance installed, configuration settings automatically accelerate some of the data models in the CIM. If you use these apps, do not make changes to acceleration settings on the CIM setup page because your changes do not persist. Instead, make changes in the Data Model Acceleration Enforcement modular input on your search head. The modular input overrides the acceleration status that you set on the CIM setup page to make sure that the apps continue to work.

If you use the CIM without these apps installed, you can choose to accelerate one or more of the data models manually.

### Enable data model acceleration

Configure the acceleration parameters of the CIM data models in the CIM Setup view.

- In Splunk Web, access the CIM Setup page:

- Select Apps > Manage Apps and then click Set up in the row for Splunk Common Information Model.
- Access the setup page directly by going to `https://<URL of your Splunk deployment>/en-US/app/search/cim_setup `.
- Select a data model that you want to accelerate.
- Select the check box next to Accelerate to accelerate the model.
- (Optional) Configure the advanced acceleration settings.

| Parameter | Description | More information |
| --- | --- | --- |
| Backfill range | How far back in time the Splunk platform creates its column stores, specified as a relative time string. Only set this parameter if you want to backfill less data than the retention period set by Earliest time. Refer to ` datamodels.conf.spec ` for warnings and limitations. | See ` datamodels.conf.spec ` and Advanced configurations for persistently accelerated data models in the Knowledge Manager Manual in the Splunk Enterprise documentation. |
| Summary range | How far back in time the Splunk platform keeps these column stores, specified as a relative time string. Backfill Range should be more recent than Summary Range. |
| Max summarization search time | The maximum amount of time that the column store creation search is allowed to run, in seconds. |
| Accelerate until maximum time | When selected, runs the acceleration search until the maximum time is reached. |
| Max concurrent summarization searches | The maximum number of concurrent acceleration instances for this data model that the scheduler is allowed to run. |
| Manual rebuilds | When selected, prevents the ` summarize ` command from rebuilding outdated summaries. Admins can manually rebuild a data model in Settings. Select Settings > Data Models and locate the row for the data model. Click Rebuild to rebuild the data model. |

-
-
-

| Schedule priority | Raises the scheduling priority of a summary search, as follows: default: No scheduling priority increase. higher: Scheduling priority is higher than other data model searches. highest: Scheduling priority is higher than other searches regardless of scheduling tier, except real-time-scheduled searches with priority = highest always have priority over all other searches. This field is only available in Splunk platform 6.5.x or later. |
| Indexes allow list | Restricts the index attribute of the data model to specified index values to improve performance. | Expected format: comma delimited index names. For example: indexA, indexB, indexC |

| Tags allow list | Restricts the ` tag ` attribute of the data model to specified tag values to improve performance. By default, the allow lists for each CIM data model contain the tags used as constraints for the child datasets as well as the tags used in any searches within the model. Do not remove these tags, or data model searches that rely on these tags will fail. You can add additional tags to this allow list to accommodate how you have applied tags to your data. Add additional tags that you need to use to search and filter within searches for a data model. | The tags_allowlist setting is only available in Splunk Enterprise 6.6.0 and above. For organizations running Splunk Enterprise 6.6.4 and above, there is a UI component to manage the tags_allowlist setting via the Splunk Web UI. For organizations running Splunk Enterprise 6.6.0 - 6.6.3, the tags_allowlist setting must be managed manually via conf file access. See ` datamodels.conf.spec ` and Set a tag allowlist for better data model search performance in the Knowledge Manager Manual in the Splunk Enterprise documentation. |

- Click Save .

For more information about accelerated data models and data model acceleration jobs, see Check the status of data model accelerations in this topic.

### Turn off acceleration for a data model

If you have Splunk Enterprise Security or the Splunk App for PCI Compliance installed, some of the data models in the CIM are automatically accelerated by configuration settings in these apps. If you want to change which data models are accelerated by these apps, access the Data Model Acceleration Enforcement modular input on your search head and make your changes there. If you attempt to de-accelerate a data model using any other method, including using the Settings tab in the CIM Setup page, your changes will not persist because the the app acceleration enforcement re-accelerates the data models automatically.

If you do not have an app installed that enforces the acceleration of any CIM data models, you can edit the acceleration settings on the CIM Setup page.

- In Splunk Web, access the CIM Setup page:

- Select Apps > Manage Apps and then click Set up in the row for Splunk Common Information Model.
- Access the setup page directly by going to `https://<URL of your Splunk deployment>/en-US/app/search/cim_setup `.
- Select the data model for which you want to turn off acceleration.
- Deselect the check box next to Enable acceleration to stop accelerating the data model.
- Click Save .

### Change the summary range for data model accelerations

A data model's summary range setting affects the size of the data models on disk, and the processing load of creating accelerated data alongside the index buckets.

- In Splunk Web, access the CIM Setup page:

- Select Apps > Manage Apps and then click Set up in the row for Splunk Common Information Model.
- Access the setup page directly by going to `https://<URL of your Splunk deployment>/en-US/app/search/cim_setup `.
- Select the data model you want to change.
- Set a summary range:

- Make sure that Enable acceleration is checked. A summary range only applies to accelerated data models.
- Review the Earliest time setting to determine the current summary range.
- Change the Earliest time setting.

For example, -1y, -3mon, -1mon, -1w, -1d, or 0 for "All Time".
- Click Save .

The CIM Setup page only displays CIM data models. You cannot change the settings of a custom data model on the CIM Setup page. To change the summary range or other settings on a custom data model, manually edit the `datamodels.conf `provided with the app or add-on. For more information, see the datamodels.conf spec file in the Splunk Enterprise Admin Manual .

### Check the status of data model accelerations

Use the Data Model Audit dashboard to display information about the state of data model accelerations in your environment. Alternatively, use the ``cim_datamodelinfo` `macro to search the data model statuses from the search bar.

To access the dashboard:

- Open the Search and Reporting app.
- In the menu bar, click Dashboards .
- Select the Data Model Audit dashboard.

| Panel | Description |
| --- | --- |
| Top Accelerations By Size | Displays the accelerated data models sorted in descending order by MB on disk |
| Top Accelerations By Run Duration | Displays the accelerated data models sorted in descending order by the time spent on running acceleration tasks. |
| Acceleration Details | Displays a table of the accelerated data models with additional information. |

Data model acceleration can be in progress and 100% complete at the same time. The process running and the status completing are not directly tied together.

### Use the CIM with Splunk platform field filters

If your organization uses the CIM and field filters on the Splunk platform to protect sensitive fields, you must understand the following downstream impact of field filters on data model acceleration (DMA).

-

As the first operation in the search-time operation sequence, field filters protect confidential information in indexes that data model summary generation searches pull from. As a result of this protection, DMA searches using fields calculated based on sensitive data might produce different results than searches without field filters.
-

If certain highly privileged roles need access to protected data during data model summary generation, you can exempt roles from field filters. Use caution when exempting roles from field filters because of the risk that users with access to the data model summary have increased visibility into sensitive data through the summary.

For more information about the impact of field filters on DMA, see Plan for field filters in your organization .
