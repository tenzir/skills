# OCSF changelog: [v1.6.0] - Aug 1st, 2025

### Added
* #### Event Classes
  1. Added `IAM Analysis Finding` event class to the Findings category. [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
* #### Dictionary Attributes
  1. Added `from_list`, `from_mailboxes`,`reply_to_list`, `return_path`, `sender` and `sender_mailbox`. [#1454](https://github.com/ocsf/ocsf-schema/pull/1454)
  1. Added `access_level`, `programmatic_credentials`, `last_authentication_time`, `access_analysis_result`, `last_used_time`, `accessors`, `granted_privileges`, `identity_activity_metrics`, `password_last_used_time`, `access_type`, `permission_analysis_results`, `additional_restrictions`, `unused_privileges_count`, `condition_keys`, `applications`, `role`, `role_id`. [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
  1. Added `reg_binary_data`, `reg_integer_data`, `reg_string_data`, `reg_string_list_data` to Windows extension. [#1468](https://github.com/ocsf/ocsf-schema/pull/1468)
  1. Added `is_src_dst_assignment_known` as a boolean. [#1464](https://github.com/ocsf/ocsf-schema/pull/1464)
  1. Added `network_scope`, `network_scope_id`, `observation_point` and `observation_point_id`. [#1481](https://github.com/ocsf/ocsf-schema/pull/1481)

* #### Objects
  1. Added  `access_analysis_result`, `additional_restriction`, `identity_activity_metrics`, `permission_analysis_result`, `programmatic_credential`. [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
  1. Added `port_info` object. [#1466](https://github.com/ocsf/ocsf-schema/pull/1466)

### Improved
* #### Event Classes
  1. Added `Disconnect` and `Reconnect` activities in the `RDP Activity` class. [#1415](https://github.com/ocsf/ocsf-schema/pull/1415)
  1. Added `user` as an attribute to the `RDP Activity` class. [#1419](https://github.com/ocsf/ocsf-schema/pull/1419)
  1. Added `raw_data_hash` as an attribute to `base_event`. [#1420](https://github.com/ocsf/ocsf-schema/pull/1420)
  1. Added `Add Subgroup`, and `Remove Subgroup` activities in the `Group Management` class. [#1447](https://github.com/ocsf/ocsf-schema/pull/1447)
  1. Added `MTA Relay` activity and `to`/`from` attributes to the `Email Activity` class. [#1454](https://github.com/ocsf/ocsf-schema/pull/1454)
  1. Added `http_request` and `http_response` objects to the `File Hosting Activity` Class [#1458](https://github.com/ocsf/ocsf-schema/pull/1458)
  1. Added `Account Switch` activity_id to the `Authentication` class. Added `account_switch_type` and `account_switch_type_id` attributes to the `Authentication` class. [#1460](https://github.com/ocsf/ocsf-schema/pull/1460)
  1. Added `is_src_dst_assignment_known` attribute to `Network Activity` class. [#1464](https://github.com/ocsf/ocsf-schema/pull/1464)
  1. Added `observation_point` and `observation_point_id` to the base `Network` event. [#1481](https://github.com/ocsf/ocsf-schema/pull/1481)

* #### Objects
  1. Added more `algorithm_id` values and references to the `fingerprint` object. [#1412](https://github.com/ocsf/ocsf-schema/pull/1412)
  1. Added xxHash H3's 64-bit and 128-bit variants to `algorithm_id` on the `fingerprint` object. [#1420](https://github.com/ocsf/ocsf-schema/pull/1412)
  1. Added `Service` to `user` `type_id` enum. [#1428](https://github.com/ocsf/ocsf-schema/pull/1428)
  1. Added `Deleted` to `finding` `status_id` enum. [#1437](https://github.com/ocsf/ocsf-schema/pull/1437)
  1. Added `status` to `related_event` object. [#1434](https://github.com/ocsf/ocsf-schema/pull/1434)
  1. Added `attack_graph` to `finding_info`. [#1436](https://github.com/ocsf/ocsf-schema/pull/1436)
  1. Added `Executable File` to `file` `type_id` enum. Added `is_readonly` as an optional attribute. [#1438](https://github.com/ocsf/ocsf-schema/pull/1438)
  1. Added `ptid` (type `long_t`) to `process` and deprecated `tid` (type `integer_t`) [#1450](https://github.com/ocsf/ocsf-schema/pull/1450)
  1. Added `state_id` and `state` to `analytic`. [#1448](https://github.com/ocsf/ocsf-schema/pull/1448)
  1. Added `from_list`, `from_mailboxes`,`reply_to_list`, `return_path`, `sender` and `sender_mailbox` attributes to `email` object. [#1454](https://github.com/ocsf/ocsf-schema/pull/1454)
  1. Added `role`, `role_id` to `resource_details` object, `type` to `policy` object,  [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
  1. Added `is_truncated` and `untruncated_size` to `metadata`, `logger` objects. [#1461](https://github.com/ocsf/ocsf-schema/pull/1461)
  1. Added `open_ports` to the `network_interface` object. [#1466](https://github.com/ocsf/ocsf-schema/pull/1466)
  1. Added `reg_binary_data`, `reg_integer_data`, `reg_string_data`, `reg_string_list_data` to `reg_value` object in Windows extension. [#1468](https://github.com/ocsf/ocsf-schema/pull/1468)
  1. Added `network_scope` and `network_scope_id` to the `network_endpoint` object. [#1481](https://github.com/ocsf/ocsf-schema/pull/1481)


### Misc
  1. Fixed spelling errors throughout the project and added spell checking to the CI linter workflow. [#1411](https://github.com/ocsf/ocsf-schema/pull/1411)
  1. Improved description of the `Application Error` class. [#1424](https://github.com/ocsf/ocsf-schema/pull/1424)
  1. Fixed links to ocsf-docs repo [#1453](https://github.com/ocsf/ocsf-schema/pull/1453)
  1. Set `device.uid` as an Observable type - type_id: 47 [#1446](https://github.com/ocsf/ocsf-schema/pull/1446)
  1. Improved descriptions of `src_endpoint` and `dst_endpoint` attributes in `Network Activity` class. [#1464](https://github.com/ocsf/ocsf-schema/pull/1464)
  1. Improved the description of the `bytestring_t` data type. [#1468](https://github.com/ocsf/ocsf-schema/pull/1468)

### Deprecated
  1. Deprecated usage of `group` attribute in favor of `groups` in the `databucket` object. [#1344](https://github.com/ocsf/ocsf-schema/pull/1344)
  1. Deprecated usage of `credential_uid` attribute in favor of `programmatic_credentials` in the `user` object. [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
  1. Deprecated usage of items `3` and `4` in the `type_id` enum in `account` object, in favor of the `type_id` enum in the `user` object. [#1389](https://github.com/ocsf/ocsf-schema/pull/1389)
  1. Deprecated item `9` (`REG_QWORD_LITTLE_ENDIAN`) in the `type_id` enum in the `reg_value` object. Its presence was an error. [#1468](https://github.com/ocsf/ocsf-schema/pull/1468)
