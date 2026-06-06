---
title: Databases
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/databases
last_modified: 2026-04-01T20:48:25.715Z
version: 8.5
---

# Databases

The fields and tags in the Databases data model describe events that pertain to structured and semi-structured data storage.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Databases event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Databases | database |

| \|____ Database_Instance | instance |

| \|____ Instance_Stats | stats |

| \|____ Session_Info | session |

| \|____ Lock_Info | lock |

| \|____ Database_Query | query |

| \|____ Tablespace | tablespace |

| \|____ Query_Stats | stats |

## Fields for Databases event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| All_Databases | ` dest ` | string | The destination of the database event. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . |  |

| All_Databases | ` dest_bunit ` | string | The business unit of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` dest_category ` | string | The category of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` dest_priority ` | string | The priority of the destination, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Databases | ` duration ` | number | The amount of time for the completion of the database event, in seconds. |  |
| All_Databases | ` object ` | string | The name of the database object. |  |
| All_Databases | ` response_time ` | number | The amount of time it took to receive a response in the database event, in seconds. |  |
| All_Databases | ` src ` | string | The source of the database event. You can alias this from more specific fields, such as ` src_host ` , ` src_ip ` , or ` src_name ` . |  |

| All_Databases | ` src_bunit ` | string | The business unit of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` src_category ` | string | The category of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` src_priority ` | string | The priority of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Databases | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
| All_Databases | ` user ` | string | Name of the database process user. |  |

| All_Databases | ` user_bunit ` | string | The business unit of the user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` user_category ` | string | The category associated with the user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Databases | ` user_priority ` | string | The priority of the user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Databases | ` vendor_product ` | string | The vendor and product name of the database system. This field can be automatically populated by ` vendor ` and ` product ` fields in your data. |  |
| Database_Instance | ` instance_name ` | string | The name of the database instance. |  |
| Database_Instance | ` instance_version ` | string | The version of the database instance. |  |
| Database_Instance | ` process_limit ` | number | The maximum number of processes that the database instance can handle. |  |
| Database_Instance | ` session_limit ` | number | The maximum number of sessions that the database instance can handle. |  |

| Instance_Stats | ` availability ` | string | The status of the database server. | prescribed values: ` Available ` , ` Not Available ` |
| Instance_Stats | ` avg_executions ` | number | The average number of executions for the database instance. |  |
| Instance_Stats | ` dump_area_used ` | string | The amount of the database dump area that has been used. |  |
| Instance_Stats | ` instance_reads ` | number | The total number of reads for the database instance. |  |
| Instance_Stats | ` instance_writes ` | number | The total number of writes for the database instance. |  |
| Instance_Stats | ` number_of_users ` | number | The total number of users for the database instance. |  |
| Instance_Stats | ` processes ` | number | The number of processes currently running for the database instance. |  |
| Instance_Stats | ` sessions ` | number | The total number of sessions currently in use for the database instance. |  |
| Instance_Stats | ` sga_buffer_cache_size ` | number | The total size of the buffer cache for the database instance, in bytes. |  |
| Instance_Stats | ` sga_buffer_hit_limit ` | number | The maximum number of number of buffers that can be hit in the database instance without finding a free buffer. |  |
| Instance_Stats | ` sga_data_dict_hit_ratio ` | number | The hit-to-miss ratio for the database instance's data dictionary. |  |
| Instance_Stats | ` sga_fixed_area_size ` | number | The size of the fixed area (also referred to as the fixed SGA) for the database instance, in bytes. |  |
| Instance_Stats | ` sga_free_memory ` | number | The total amount of free memory in the database instance SGA, in bytes. |  |
| Instance_Stats | ` sga_library_cache_size ` | number | The total library cache size for the database instance, in bytes. |  |
| Instance_Stats | ` sga_redo_log_buffer_size ` | number | The total size of the redo log buffer for the database instance, in bytes. |  |
| Instance_Stats | ` sga_shared_pool_size ` | number | The total size of the shared pool for this database instance, in bytes. |  |
| Instance_Stats | ` sga_sql_area_size ` | number | The total size of the SQL area for this database instance, in bytes. |  |
| Instance_Stats | ` start_time ` | time | The total amount of uptime for the database instance. |  |
| Instance_Stats | ` tablespace_used ` | string | The total amount of tablespace used for the database instance, in bytes. |  |
| Session_Info | ` buffer_cache_hit_ratio ` | number | The percentage of logical reads from the buffer during the session (1-physical reads/session logical reads*100). |  |
| Session_Info | ` commits ` | number | The number of commits per second performed by the user associated with the session. |  |
| Session_Info | ` cpu_used ` | number | The number of CPU centiseconds used by the session. Divide this value by 100 to get the CPU seconds. |  |
| Session_Info | ` cursor ` | number | The number of the cursor currently in use by the session. |  |
| Session_Info | ` elapsed_time ` | number | The total amount of time elapsed since the user started the session by logging into the database server, in seconds. |  |
| Session_Info | ` logical_reads ` | number | The total number of consistent gets and database block gets performed during the session. |  |
| Session_Info | ` machine ` | string | The name of the logical host associated with the database instance. |  |
| Session_Info | ` memory_sorts ` | number | The total number of memory sorts performed during the session. |  |
| Session_Info | ` physical_reads ` | number | The total number of physical reads performed during the session. |  |
| Session_Info | ` seconds_in_wait ` | number | The description of ` seconds_in_wait ` depends on the value of ` wait_time ` . If ` wait_time = 0 ` , ` seconds_in_wait ` is the number of seconds spent in the current wait condition. If ` wait_time ` has a nonzero value, ` seconds_in_wait ` is the number of seconds that have elapsed since the start of the last wait. You can get the active seconds that have elapsed since the last wait ended by calculating ` seconds_in_wait - wait_time / 100 ` . |  |
| Session_Info | ` session_id ` | string | The unique id that identifies the session. |  |

| Session_Info | ` session_status ` | string | The current status of the session. | prescribed values: ` Online ` , ` Offline ` . |
| Session_Info | ` table_scans ` | number | Number of table scans performed during the session. |  |

| Session_Info | ` wait_state ` | string | Provides the current wait state for the session. Can indicate that the session is currently waiting or provide information about the session's last wait. | prescribed values: ` WAITING ` (the session is currently waiting), ` WAITED UNKNOWN ` (the duration of the last session wait is unknown), ` WAITED SHORT TIME ` (the last session wait was < 1/100th of a second), ` WAITED KNOWN TIME ` (the ` wait_time ` is the duration of the last session wait). |
| Session_Info | ` wait_time ` | number | When ` wait_time = 0 ` , the session is waiting. When ` wait_time ` has a nonzero value, it is displaying the last wait time for the session. |  |
| Lock_Info | ` last_call_minute ` | number | Represents the amount of time elapsed since the ` session_status ` changed to its current status. The definition of this field depends on the ` session_status ` value. If ` session_status = ONLINE ` , the ` last_call_minute ` value represents the time elapsed since the session became active. If ` session_status = OFFLINE ` , the ` last_call_minute ` value represents the time elapsed since the session became inactive. |  |
| Lock_Info | ` lock_mode ` | string | The mode of the lock on the object. |  |
| Lock_Info | ` lock_session_id ` | string | The session identifier of the locked object. |  |
| Lock_Info | ` logon_time ` | number | The database logon time for the session. |  |
| Lock_Info | ` obj_name ` | string | The name of the locked object. |  |
| Lock_Info | ` os_pid ` | string | The process identifier for the operating system. |  |
| Lock_Info | ` serial_num ` | string | The serial number of the object. |  |
| Database_Query | ` query ` | string | The full database query. |  |
| Database_Query | ` query_id ` | string | The identifier for the database query. |  |
| Database_Query | ` query_time ` | time | The time the system initiated the database query. |  |
| Database_Query | ` records_affected ` | number | The number of records affected by the database query. |  |
| Tablespace | ` free_bytes ` | number | The total amount of free space in the tablespace, in bytes. |  |
| Tablespace | ` tablespace_name ` | string | The name of the tablespace. |  |
| Tablespace | ` tablespace_reads ` | number | The number of tablespace reads carried out by the query. |  |

| Tablespace | ` tablespace_status ` | string | The status of the tablespace. | prescribed values: ` Offline ` , ` Online ` , ` Read Only ` |
| Tablespace | ` tablespace_writes ` | number | The number of tablespace writes carried out by the query. |  |
| Query_Stats | ` indexes_hit ` | string | The names of the indexes hit by the database query. |  |
| Query_Stats | ` query_plan_hit ` | string | The name of the query plan hit by the query. |  |
| Query_Stats | ` stored_procedures_called ` | string | The names of the stored procedures called by the query. |  |
| Query_Stats | ` tables_hit ` | string | The names of the tables hit by the query. |  |
