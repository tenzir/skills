---
title: CIM fields per associated data model
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/cim-fields-per-associated-data-model
last_modified: 2026-04-01T20:48:24.139Z
version: 8.5
---

# CIM fields per associated data model

Single page view of all the CIM fields and the associated models. See where the overlapping models use the same fields and how to join across different datasets.

| Field name | Data model |
| --- | --- |
| access_count | Splunk Audit Logs |
| access_time | Splunk Audit Logs |
| action | Authentication , Change , Data Access , Data Loss Prevention , Email , Endpoint , Intrusion Detection , Malware , Network Sessions , Network Traffic , Performance , Web |
| action_mode | Splunk Audit Logs |
| action_name | Splunk Audit Logs |
| action_status | Splunk Audit Logs |
| additional_answer_count | Network Resolution (DNS) |
| affect_dest | TicketManagement |
| answer | Network Resolution (DNS) |
| answer_count | Network Resolution (DNS) |
| app | Alerts , Authentication , Data Access , Data Loss Prevention , Network Traffic , Splunk Audit Logs , Web |
| app_id | Data Access |
| array | Inventory , Performance |
| authentication_method | Authentication |
| authentication_service | Authentication |
| authority_answer_count | Network Resolution (DNS) |
| availability | Databases |
| avg_executions | Databases |
| blocksize | Inventory , Performance |
| body | Alerts Deprecated in favor of ` description ` . |
| buckets | Splunk Audit Logs |
| buckets_size | Splunk Audit Logs |
| buffer_cache_hit_ratio | Databases |
| bugtraq | Vulnerabilities |
| bytes | Network Traffic , Web |
| bytes_in | Network Traffic , Web |
| bytes_out | Network Traffic , Web |
| cached | Web |
| category | Data Loss Prevention , Intrusion Detection , Malware , Vulnerabilities , Web |
| cert | Vulnerabilities |
| change | TicketManagement |
| change_type | Change |
| channel | Network Traffic |
| cluster | Inventory , Performance |
| cm_enabled | Java Virtual Machines (JVM) |
| cm_supported | Java Virtual Machines (JVM) |
| command | Change |
| comments | TicketManagement |
| commits | Databases |
| committed_memory | Java Virtual Machines (JVM) |
| compilation_time | Java Virtual Machines (JVM) |
| complete | Splunk Audit Logs |
| component | Splunk Audit Logs |
| cookie | Web |
| cpu_cores | Inventory |
| cpu_count | Inventory |
| cpu_load_mhz | Performance |
| cpu_load_percent | Endpoint , Performance |
| cpu_mhz | Inventory |
| cpu_time | Java Virtual Machines (JVM) , Performance |
| cpu_time_enabled | Java Virtual Machines (JVM) |
| cpu_time_supported | Java Virtual Machines (JVM) |
| cpu_used | Databases |
| cpu_user_percent | Performance |
| creation_time | Endpoint |
| cron | Splunk Audit Logs |
| current_cpu_time | Java Virtual Machines (JVM) |
| current_loaded | Java Virtual Machines (JVM) |
| current_user_time | Java Virtual Machines (JVM) |
| cursor | Databases |
| cve | Vulnerabilities |
| cvss | Vulnerabilities |
| daemon_thread_count | Java Virtual Machines (JVM) |
| datamodel | Splunk Audit Logs |
| date | Malware |
| delay | Email |
| description | Alerts , Endpoint , Inventory , TicketManagement |
| dest | Alerts , Authentication , Certificates , Change , Data Access , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Interprocess Messaging , Intrusion Detection , Inventory , Malware , Network Resolution (DNS) , Network Traffic , Performance , TicketManagement , Updates , Vulnerabilities , Web |
| dest_bunit | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Interprocess Messaging , Intrusion Detection , Inventory , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Performance , TicketManagement , Updates , Vulnerabilities , Web |
| dest_category | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Interprocess Messaging , Intrusion Detection , Inventory , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Performance , TicketManagement , Updates , Vulnerabilities , Web |
| dest_dns | Network Sessions |
| dest_interface | Network Traffic |
| dest_ip | Inventory , Network Sessions , Network Traffic |
| dest_ip_range | Change |
| dest_is_expected | Endpoint |
| dest_mac | Network Sessions , Network Traffic |
| dest_name | Data Access |
| dest_nt_domain | Authentication , Change , Malware |
| dest_nt_host | Network Sessions |
| dest_port | Certificates , Endpoint , Intrusion Detection , Network Resolution (DNS) , Network Traffic , Web |
| dest_port_range | Change |
| dest_priority | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Interprocess Messaging , Intrusion Detection , Inventory , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Performance , TicketManagement , Updates , Vulnerabilities , Web |
| dest_requires_av | Endpoint , Malware |
| dest_should_timesync | Endpoint , Performance |
| dest_should_update | Endpoint , Performance , Updates |
| dest_translated_ip | Network Traffic |
| dest_translated_port | Network Traffic |
| dest_type | Alerts |
| dest_url | Data Access |
| dest_zone | Data Loss Prevention , Network Traffic |
| digest | Splunk Audit Logs |
| direction | Change , Network Traffic |
| dlp_type | Data Loss Prevention |
| dns | Inventory |
| dump_area_used | Databases |
| duration | Authentication , Certificates , Databases , Email , Interprocess Messaging , Network Resolution (DNS) , Network Sessions , Network Traffic , Splunk Audit Logs , Web |
| dvc | Change , Data Access , Data Loss Prevention , Intrusion Detection , Network Traffic , Updates , Vulnerabilities |
| dvc_bunit | Data Loss Prevention , Intrusion Detection , Network Traffic , Vulnerabilities |
| dvc_category | Data Loss Prevention , Intrusion Detection , Network Traffic , Vulnerabilities |
| dvc_ip | Network Traffic |
| dvc_mac | Network Traffic |
| dvc_priority | Data Loss Prevention , Intrusion Detection , Network Traffic , Vulnerabilities |
| dvc_zone | Data Loss Prevention , Network Traffic |
| earliest | Splunk Audit Logs |
| elapsed_time | Databases |
| email | Data Access |
| enabled | Inventory |
| endpoint | Interprocess Messaging |
| endpoint_version | Interprocess Messaging |
| error_code | Web |
| event_id | Splunk Audit Logs |
| family | Inventory |
| fan_speed | Performance |
| fd_max | Inventory , Performance |
| fd_used | Performance |
| file_access_time | Endpoint |
| file_acl | Endpoint |
| file_create_time | Endpoint |
| file_hash | Email , Endpoint , Intrusion Detection , Malware , Updates |
| file_modify_time | Endpoint |
| file_name | Email , Endpoint , Intrusion Detection , Malware , Updates |
| file_path | Endpoint , Intrusion Detection , Malware |
| file_size | Email , Endpoint |
| filter_action | Email |
| filter_score | Email |
| flow_id | Network Traffic |
| free_bytes | Databases |
| free_physical_memory | Java Virtual Machines (JVM) |
| free_swap | Java Virtual Machines (JVM) |
| heap_committed | Java Virtual Machines (JVM) |
| heap_initial | Java Virtual Machines (JVM) |
| heap_max | Java Virtual Machines (JVM) |
| heap_used | Java Virtual Machines (JVM) |
| host | Splunk Audit Logs |
| http_content_type | Web |
| http_method | Web |
| http_referrer | Web |
| http_referrer_domain | Web |
| http_user_agent | Web |
| http_user_agent_length | Web |
| hypervisor | Inventory |
| hypervisor_id | Inventory , Performance |
| icmp_code | Network Traffic |
| icmp_type | Network Traffic |
| id | Alerts |
| ids_type | Intrusion Detection |
| image_id | Change |
| incident | TicketManagement |
| indexes_hit | Databases |
| info | Splunk Audit Logs |
| inline_nat | Inventory |
| instance_name | Databases |
| instance_reads | Databases |
| instance_type | Change |
| instance_version | Databases |
| instance_writes | Databases |
| interactive | Inventory |
| interface | Inventory |
| internal_message_id | Email |
| ip | Inventory |
| is_inprogress | Splunk Audit Logs |
| jvm_description | Java Virtual Machines (JVM) |
| last_call_minute | Databases |
| last_error | Splunk Audit Logs |
| last_sid | Splunk Audit Logs |
| latency | Inventory , Performance |
| latest | Splunk Audit Logs |
| lb_method | Inventory |
| lease_duration | Network Sessions |
| lease_scope | Network Sessions |
| lock_mode | Databases |
| lock_session_id | Databases |
| logical_reads | Databases |
| logon_time | Databases |
| mac | Inventory |
| machine | Databases |
| max_file_descriptors | Java Virtual Machines (JVM) |
| mem | Inventory , Performance |
| mem_committed | Performance |
| mem_free | Performance |
| mem_used | Endpoint , Performance |
| memory_sorts | Databases |
| message | Interprocess Messaging |
| message_consumed_time | Interprocess Messaging |
| message_correlation_id | Interprocess Messaging |
| message_delivered_time | Interprocess Messaging |
| message_delivery_mode | Interprocess Messaging |
| message_expiration_time | Interprocess Messaging |
| message_id | Email , Interprocess Messaging |
| message_info | Email |
| message_priority | Interprocess Messaging |
| message_properties | Interprocess Messaging |
| message_received_time | Interprocess Messaging |
| message_redelivered | Interprocess Messaging |
| message_reply_dest | Interprocess Messaging |
| message_type | Interprocess Messaging , Network Resolution (DNS) |
| mitre_technique_id | Alerts |
| mod_time | Splunk Audit Logs |
| mount | Inventory , Performance |
| msft | Vulnerabilities |
| mskb | Vulnerabilities |
| name | Inventory , Network Resolution (DNS) |
| node | Inventory |
| node_port | Inventory |
| non_heap_committed | Java Virtual Machines (JVM) |
| non_heap_initial | Java Virtual Machines (JVM) |
| non_heap_max | Java Virtual Machines (JVM) |
| non_heap_used | Java Virtual Machines (JVM) |
| number_of_users | Databases |
| obj_name | Databases |
| object | Change , Data Access , Data Loss Prevention , Databases |
| object_attrs | Change |
| object_category | Change , Data Access , Data Loss Prevention |
| object_id | Change , Data Access |
| object_path | Change , Data Access , Data Loss Prevention |
| object_size | Data Access |
| objects_pending | Java Virtual Machines (JVM) |
| omu_supported | Java Virtual Machines (JVM) |
| open_file_descriptors | Java Virtual Machines (JVM) |
| operation | Web |
| orig_dest | Email |
| orig_recipient | Email |
| orig_rid | Splunk Audit Logs |
| orig_sid | Splunk Audit Logs |
| orig_src | Email |
| original_file_name | Endpoint |
| os | Endpoint , Inventory , Java Virtual Machines (JVM) |
| os_architecture | Java Virtual Machines (JVM) |
| os_pid | Databases |
| os_version | Java Virtual Machines (JVM) |
| owner | Data Access |
| owner_email | Data Access |
| owner_id | Data Access |
| packets | Network Traffic |
| packets_in | Network Traffic |
| packets_out | Network Traffic |
| parameters | Interprocess Messaging |
| parent | Inventory , Performance |
| parent_object | Data Access |
| parent_object_category | Data Access |
| parent_object_id | Data Access |
| parent_process | Endpoint |
| parent_process_exec | Endpoint |
| parent_process_guid | Endpoint |
| parent_process_id | Endpoint |
| parent_process_name | Endpoint |
| parent_process_path | Endpoint |
| password | Inventory |
| payload | Interprocess Messaging |
| payload_type | Interprocess Messaging |
| peak_thread_count | Java Virtual Machines (JVM) |
| physical_memory | Java Virtual Machines (JVM) |
| physical_reads | Databases |
| power | Performance |
| priority | TicketManagement |
| problem | TicketManagement |
| process | Email , Endpoint |
| process_current_directory | Endpoint |
| process_exec | Endpoint |
| process_guid | Endpoint |
| process_hash | Endpoint |
| process_id | Email , Endpoint , Network Traffic |
| process_integrity_level | Endpoint |
| process_limit | Databases |
| process_name | Endpoint , Java Virtual Machines (JVM) |
| process_path | Endpoint |
| processes | Databases |
| product_version | Malware |
| protocol | Change , Email , Network Traffic |
| protocol_version | Network Traffic |
| query | Databases , Network Resolution (DNS) |
| query_count | Network Resolution (DNS) |
| query_id | Databases |
| query_plan_hit | Databases |
| query_time | Databases |
| query_type | Network Resolution (DNS) |
| read_blocks | Inventory , Performance |
| read_latency | Inventory , Performance |
| read_ops | Inventory , Performance |
| reason | Authentication |
| recipient | Email |
| recipient_count | Email |
| recipient_domain | Email |
| recipient_status | Email |
| record_type | Network Resolution (DNS) |
| records_affected | Databases |
| registry_hive | Endpoint |
| registry_key_name | Endpoint |
| registry_path | Endpoint |
| registry_value_data | Endpoint |
| registry_value_name | Endpoint |
| registry_value_text | Endpoint |
| registry_value_type | Endpoint |
| reply_code | Network Resolution (DNS) |
| reply_code_id | Network Resolution (DNS) |
| request_payload | Interprocess Messaging |
| request_payload_type | Interprocess Messaging |
| request_sent_time | Interprocess Messaging |
| resource_type | Performance |
| response_code | Interprocess Messaging |
| response_payload_type | Interprocess Messaging |
| response_received_time | Interprocess Messaging |
| response_time | Authentication , Certificates , Databases , Email , Interprocess Messaging , Network Resolution (DNS) , Network Sessions , Network Traffic , Web |
| result | Change |
| result_id | Change |
| retention | Splunk Audit Logs |
| retries | Email |
| return_addr | Email |
| return_message | Interprocess Messaging |
| rid | Splunk Audit Logs |
| rpc_protocol | Interprocess Messaging |
| rule | Network Traffic |
| rule_action | Change |
| savedsearch_name | Splunk Audit Logs |
| search | Splunk Audit Logs |
| search_et | Splunk Audit Logs |
| search_lt | Splunk Audit Logs |
| search_name | Splunk Audit Logs |
| search_type | Splunk Audit Logs |
| seconds_in_wait | Databases |
| sender | Malware |
| serial | Inventory |
| serial_num | Databases |
| service | Endpoint |
| service_dll | Endpoint |
| service_dll_hash | Endpoint |
| service_dll_path | Endpoint |
| service_dll_signature_exists | Endpoint |
| service_dll_signature_verified | Endpoint |
| service_exec | Endpoint |
| service_hash | Endpoint |
| service_id | Endpoint |
| service_name | Endpoint |
| service_path | Endpoint |
| service_signature_exists | Endpoint |
| service_signature_verified | Endpoint |
| session_id | Databases , Network Traffic |
| session_limit | Databases |
| session_status | Databases |
| sessions | Databases |
| severity | Alerts , Data Loss Prevention , Intrusion Detection , TicketManagement , Updates , Vulnerabilities |
| severity_id | Alerts , Data Loss Prevention , Intrusion Detection , Malware , TicketManagement , Updates , Vulnerabilities |
| sga_buffer_cache_size | Databases |
| sga_buffer_hit_limit | Databases |
| sga_data_dict_hit_ratio | Databases |
| sga_fixed_area_size | Databases |
| sga_free_memory | Databases |
| sga_library_cache_size | Databases |
| sga_redo_log_buffer_size | Databases |
| sga_shared_pool_size | Databases |
| sga_sql_area_size | Databases |
| shell | Inventory |
| sid | Splunk Audit Logs , Splunk Audit Logs |
| signature | Alerts , Authentication , Data Loss Prevention , Email , Event Signatures , Intrusion Detection , Malware , Network Sessions , Performance , Splunk Audit Logs , Updates , Vulnerabilities |
| signature_extra | Email |
| signature_id | Alerts , Authentication , Email , Event Signatures , Data Loss Prevention , Intrusion Detection , Malware , Network Sessions , Performance , Updates , Vulnerabilities |
| signature_version | Malware |
| site | Web |
| size | Email , Inventory , Splunk Audit Logs |
| snapshot | Inventory |
| source | Splunk Audit Logs |
| sourcetype | Splunk Audit Logs |
| spent | Splunk Audit Logs |
| splunk_id | TicketManagement |
| splunk_realm | TicketManagement |
| splunk_server | Splunk Audit Logs |
| src | Alerts , Authentication , Certificates , Change , Data Access , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Malware , Network Resolution (DNS) , Network Traffic , Web |
| src_bunit | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Intrusion Detection , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Web |
| src_category | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Web |
| src_dns | Network Sessions |
| src_interface | Network Traffic |
| src_ip | Inventory , Network Sessions , Network Traffic |
| src_ip_range | Change |
| src_mac | Network Sessions , Network Traffic |
| src_nt_domain | Authentication , Change |
| src_nt_host | Network Sessions |
| src_port | Certificates , Endpoint , Network Resolution (DNS) , Network Traffic |
| src_port_range | Change |
| src_priority | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Web |
| src_requires_av | Endpoint |
| src_should_timesync | Endpoint |
| src_should_update | Endpoint |
| src_translated_ip | Network Traffic |
| src_translated_port | Network Traffic |
| src_type | Alerts |
| src_user | Authentication , Change , Data Loss Prevention , Email , TicketManagement |
| src_user_bunit | Authentication , Change , Data Loss Prevention , Email , TicketManagement |
| src_user_category | Authentication , Change , Data Loss Prevention , Email , TicketManagement |
| src_user_domain | Email |
| src_user_id | Authentication |
| src_user_name | Change |
| src_user_priority | Authentication , Change , Data Loss Prevention , Email , TicketManagement |
| src_user_role | Authentication |
| src_user_type | Authentication , Change |
| src_zone | Data Loss Prevention , Network Traffic |
| ssid | Network Traffic |
| ssl_end_time | Certificates |
| ssl_engine | Certificates |
| ssl_hash | Certificates |
| ssl_is_valid | Certificates |
| ssl_issuer | Certificates |
| ssl_issuer_common_name | Certificates |
| ssl_issuer_email | Certificates |
| ssl_issuer_email_domain | Certificates |
| ssl_issuer_locality | Certificates |
| ssl_issuer_organization | Certificates |
| ssl_issuer_state | Certificates |
| ssl_issuer_street | Certificates |
| ssl_issuer_unit | Certificates |
| ssl_name | Certificates |
| ssl_policies | Certificates |
| ssl_publickey | Certificates |
| ssl_publickey_algorithm | Certificates |
| ssl_serial | Certificates |
| ssl_session_id | Certificates |
| ssl_signature_algorithm | Certificates |
| ssl_start_time | Certificates |
| ssl_subject | Certificates |
| ssl_subject_common_name | Certificates |
| ssl_subject_email | Certificates |
| ssl_subject_email_domain | Certificates |
| ssl_subject_locality | Certificates |
| ssl_subject_organization | Certificates |
| ssl_subject_state | Certificates |
| ssl_subject_street | Certificates |
| ssl_subject_unit | Certificates |
| ssl_validity_window | Certificates |
| ssl_version | Certificates |
| start_mode | Endpoint |
| start_time | Databases , Java Virtual Machines (JVM) |
| state | Endpoint |
| status | Change , Endpoint , Interprocess Messaging , Inventory , Splunk Audit Logs , TicketManagement , Updates , Web |
| status_code | Email |
| storage | Inventory , Performance |
| storage_free | Performance |
| storage_free_percent | Performance |
| storage_name | Web |
| storage_used | Performance |
| storage_used_percent | Performance |
| stored_procedures_called | Databases |
| subject | Alerts Deprecated in favor of ` signature ` , Email |
| summary_id | Splunk Audit Logs |
| swap | Performance |
| swap_free | Performance |
| swap_space | Java Virtual Machines (JVM) |
| swap_used | Performance |
| synch_supported | Java Virtual Machines (JVM) |
| system_load | Java Virtual Machines (JVM) |
| table_scans | Databases |
| tables_hit | Databases |
| tablespace_name | Databases |
| tablespace_reads | Databases |
| tablespace_status | Databases |
| tablespace_used | Databases |
| tablespace_writes | Databases |
| tag | Alerts , Authentication , Certificates , Change , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Interprocess Messaging , Intrusion Detection , Inventory , Java Virtual Machines (JVM) , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Performance , TicketManagement , Updates , Vulnerabilities , Web |
| tcp_flag | Network Traffic |
| temperature | Performance |
| thread_count | Java Virtual Machines (JVM) |
| threads_started | Java Virtual Machines (JVM) |
| thruput | Performance |
| thruput_max | Performance |
| ticket_id | TicketManagement |
| time | Inventory |
| time_submitted | TicketManagement |
| tos | Network Traffic |
| total_loaded | Java Virtual Machines (JVM) |
| total_processors | Java Virtual Machines (JVM) |
| total_unloaded | Java Virtual Machines (JVM) |
| transaction_id | Network Resolution (DNS) |
| transport | Certificates , Endpoint , Intrusion Detection , Network Resolution (DNS) , Network Traffic |
| transport_dest_port | Endpoint |
| ttl | Network Resolution (DNS) , Network Traffic |
| type | Alerts |
| uptime | Java Virtual Machines (JVM) , Performance |
| uri | Splunk Audit Logs |
| uri_path | Web |
| uri_query | Web |
| url | Email , Malware , Vulnerabilities , Web |
| url_domain | Web |
| url_length | Web |
| user | Alerts , Authentication , Change , Data Access , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Inventory , Malware , Network Sessions , Network Traffic , Splunk Audit Logs , TicketManagement , Vulnerabilities , Web |
| user_agent | Authentication , Change , Data Access |
| user_bunit | Alerts , Authentication , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Inventory , Malware , Network Sessions , Network Traffic , Splunk Audit Logs , TicketManagement , Vulnerabilities , Web |
| user_category | Alerts , Authentication , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Inventory , Malware , Network Sessions , Network Traffic , Splunk Audit Logs , TicketManagement , Vulnerabilities , Web |
| user_group | Data Access |
| user_id | Authentication , Endpoint , Inventory |
| user_name | Alerts , Change |
| user_priority | Alerts , Authentication , Data Loss Prevention , Databases , Email , Endpoint , Intrusion Detection , Inventory , Malware , Network Sessions , Network Traffic , Splunk Audit Logs , TicketManagement , Vulnerabilities , Web |
| user_role | Authentication , Data Access |
| user_type | Authentication , Change |
| vendor_account | Alerts , Authentication , Change , Data Access , Network Traffic |
| vendor_product | Authentication , Change , Data Access , Data Loss Prevention , Databases , Email , Endpoint , Event Signatures , Intrusion Detection , Inventory , Java Virtual Machines (JVM) , Malware , Network Resolution (DNS) , Network Sessions , Network Traffic , Updates , Vulnerabilities , Web |
| vendor_product_id | Alerts , Change |
| vendor_region | Alerts , Change |
| version | Inventory , Java Virtual Machines (JVM) |
| view | Splunk Audit Logs |
| vip_port | Inventory |
| vlan | Network Traffic |
| wait_state | Databases |
| wait_time | Databases |
| wifi | Network Traffic |
| write_blocks | Inventory , Performance |
| write_latency | Inventory , Performance |
| write_ops | Inventory , Performance |
| xdelay | Email |
| xref | Email |
| xref | Vulnerabilities |
