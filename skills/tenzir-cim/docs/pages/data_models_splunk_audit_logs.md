---
title: Splunk Audit Logs
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/splunk-audit-logs
last_modified: 2026-04-01T20:48:24.341Z
version: 8.5
---

# Splunk Audit Logs

The fields in the Splunk Audit Logs data model describe audit information for systems producing event logs.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with the Audit event datasets

The following tags act as constraints to identify your events as being relevant to the Modular_Actions dataset in this data model. For more information, see How to use these reference tables .

Although it is not part of the data model shipped in the CIM add-on, the common information model expects the tag `modaction_result `for events produced by custom alert actions.

| Dataset name | Tag name |
| --- | --- |
| Modular_Actions | modaction |
| \|____ Modular Action Invocations | invocation |

## Fields for the event dataset and the search datasets

The following table lists the extracted and calculated fields for the event dataset and search datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| View_Activity | ` app ` | string | The app name which contains the view. |  |
| View_Activity | ` spent ` | number | The amount of time spent loading the view (in milliseconds). |  |
| View_Activity | ` uri ` | string | The uniform resource identifier of the view activity. |  |
| View_Activity | ` user ` | string | The username of the user who accessed the view. |  |
| View_Activity | ` view ` | string | The name of the view. |  |
| Datamodel_Acceleration | ` access_count ` | number | The number of times the data model summary has been accessed since it was created. |  |
| Datamodel_Acceleration | ` access_time ` | time | The timestamp of the most recent access of the data model summary. |  |
| Datamodel_Acceleration | ` app ` | string | The application context in which the data model summary was accessed. |  |
| Datamodel_Acceleration | ` buckets ` | number | The number of index buckets spanned by the data model acceleration summary. |  |
| Datamodel_Acceleration | ` buckets_size ` | number | The total size of the bucket(s) spanned by the data model acceleration summary. |  |
| Datamodel_Acceleration | ` complete ` | number | The percentage of the data model summary that is currently complete. | other: ` 0-100 ` |
| Datamodel_Acceleration | ` cron ` | string | The cron expression used to accelerate the data model. |  |
| Datamodel_Acceleration | ` datamodel ` | string | The name of the data model accelerated. |  |
| Datamodel_Acceleration | ` digest ` | string | A hash of the current data model constraints. |  |
| Datamodel_Acceleration | ` earliest ` | time | The earliest time that the data model summary was accessed. |  |
| Datamodel_Acceleration | ` is_inprogress ` | boolean | Indicates whether the data model acceleration is currently in progress. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |
| Datamodel_Acceleration | ` last_error ` | string | The text of the last error reported during the data model acceleration. |  |
| Datamodel_Acceleration | ` last_sid ` | string | The search id of the last acceleration attempt. |  |
| Datamodel_Acceleration | ` latest ` | time | The most recent acceleration timestamp of the data model. |  |
| Datamodel_Acceleration | ` mod_time ` | time | The timestamp of the most recent modification to the data model acceleration. |  |
| Datamodel_Acceleration | ` retention ` | number | The length of time that data model accelerations are retained, in seconds. |  |
| Datamodel_Acceleration | ` size ` | number | The amount of storage space the data model's acceleration summary takes up, in bytes. |  |
| Datamodel_Acceleration | ` summary_id ` | string | The unique id of the data model acceleration summary. |  |
| Search_Activity | ` host ` | string | The host on which the search occurred. |  |
| Search_Activity | ` info ` | string | The action of the search (granted, completed, cancelled, failed). |  |
| Search_Activity | ` search ` | string | The search string. |  |
| Search_Activity | ` search_et ` | string | The earliest time of the search. |  |
| Search_Activity | ` search_lt ` | string | The latest time of the search. |  |
| Search_Activity | ` search_type ` | string | The type of search. |  |
| Search_Activity | ` source ` | string | The source associated with the search. |  |
| Search_Activity | ` sourcetype ` | string | The source types included in the search. |  |
| Search_Activity | ` user ` | string | The name of the user who ran the search. |  |
| Search_Activity | ` user_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| Search_Activity | ` user_category ` | string |
| Search_Activity | ` user_priority ` | string |
| Scheduler_Activity | ` app ` | string | The app context in which the scheduled search was run. |  |
| Scheduler_Activity | ` host ` | string | The host on which the scheduled search was run. |  |
| Scheduler_Activity | ` savedsearch_name ` | string | The name of the saved search. |  |
| Scheduler_Activity | ` sid ` | string | The search id. |  |
| Scheduler_Activity | ` source ` | string | The source associated with the scheduled search. |  |
| Scheduler_Activity | ` sourcetype ` | string | The source type associated with the scheduled search. |  |
| Scheduler_Activity | ` splunk_server ` | string | The Splunk Server on which the scheduled search runs. |  |
| Scheduler_Activity | ` status ` | string | The status of the scheduled search. |  |
| Scheduler_Activity | ` user ` | string | The user who scheduled the search. |  |
| Web_Service_Errors | ` host ` | string | The host on which the web service error occurred. |  |
| Web_Service_Errors | ` source ` | string | The source where the web service error occurred. |  |
| Web_Service_Errors | ` sourcetype ` | string | The source type associated with the web service error. |  |
| Web_Service_Errors | ` event_id ` | string | The unique event_id for the web service error event. |  |
| Modular_Actions | ` action_mode ` | string | Specifies whether the action was executed as an ad hoc action or from a saved search, based on whether a ` search_name ` exists. | prescribed values: ` saved ` , ` adhoc ` |
| Modular_Actions | ` action_status ` | string | The status of the action. For example, "success", "failure", or "pending". |  |
| Modular_Actions | ` app ` | string | The app ID of the app or add-on that owns the action. |  |
| Modular_Actions | ` duration ` | number | How long the action took to complete, in milliseconds. |  |
| Modular_Actions | ` component ` | string | The component of the modular action script involved in the event. Often used in conjunction with duration. |  |
| Modular_Actions | ` orig_rid ` | string | The ` rid ` value of a source action result, automatically added to an event if it is the product of a previously executed action. |  |
| Modular_Actions | ` orig_sid ` | string | The original ` sid ` value of a source action, automatically added to an event if it is the product of a previously executed action. |  |
| Modular_Actions | ` rid ` | string | The id associated with the result of a specific ` sid ` . By default, this is the row number of the search, starting with 0. |  |
| Modular_Actions | ` search_name ` | string | The name of the correlation search that triggered the action. Blank for ad hoc actions. |  |
| Modular_Actions | ` action_name ` | string | The name of the action. |  |
| Modular_Actions | ` signature ` | string | The logging string associated with alert action introspection events. |  |
| Modular_Actions | ` sid ` | string | The search id, automatically assigned by splunkd. |  |
| Modular_Actions | ` user ` | string | The user who triggered an ad hoc alert. Not relevant for actions triggered by searches. |  |
