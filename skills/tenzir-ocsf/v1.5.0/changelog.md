# OCSF changelog: [v1.5.0] - April 28th, 2025

### Added
* #### Event Classes
  1. Added `Application Security Posture Finding` event class to the Findings category. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `Live Evidence Info` event class to Discovery category. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
* #### Dictionary Attributes
  1. Added `boot_uid` as a `string_t`. [#1335](https://github.com/ocsf/ocsf-schema/pull/1335)
  1. Added `cpid` as a `uuid_t`. [#1246](https://github.com/ocsf/ocsf-schema/pull/1246)
  1. Added `raw_data_size` as a `long_t`. [#1347](https://github.com/ocsf/ocsf-schema/pull/1347)
  1. Added `assessments` as an array of `assessment` objects. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `meets_criteria` as a `boolean_t`. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `display_name` attribute as a `string_t`. [#1341](https://github.com/ocsf/ocsf-schema/pull/1341)
  1. Added `is_directed` as a `boolean_t`, `relation` as a `string_t`, `query_language` & `query_language_id` a sibling pair. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `resource_relationship` of type `graph`, `nodes` of type `node`, `edges` of type `edge`. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `fix_coverage` as `string_t` and `fix_coverage_id` as `int_t`. [#1350](https://github.com/ocsf/ocsf-schema/pull/1350)
  1. Added `eid`, `iccid`, and `meid` as `string_t`. [#1346](https://github.com/ocsf/ocsf-schema/pull/1346)
  1. Added `is_backed_up`, `is_mobile_account_active`, and `is_shared` as `boolean_t`. [#1346](https://github.com/ocsf/ocsf-schema/pull/1346)
  1. Added `detection_pattern_type` an `detection_pattern_type_id` as a `string_t` and `int_t` respectively. [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `external_id` as an `string_t`. [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `intrusion_sets` as an array `string_t`. [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `uploaded_time` as an `timestamp_t`. [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `isp_org` as `string_t`. [#1351](https://github.com/ocsf/ocsf-schema/pull/1351)
  1. Added `ldap` protocol to `auth_protocol_id` enum. [#1359](https://github.com/ocsf/ocsf-schema/pull/1359)
  1. Added `observation_parameter`, `observation_type`, `observed_pattern` as `string_t` and `occurrences` as an array of `occurrence_details`. [#1358](https://github.com/ocsf/ocsf-schema/pull/1358)
  1. Added `analysis_targets` as an array of type `analysis_target`. [#1371](https://github.com/ocsf/ocsf-schema/pull/1371)
  1. Added `num_volumes`, `num_infected` as `int_t`, `unique_malware_count`, `volume` as `string_t`. [#1373](https://github.com/ocsf/ocsf-schema/pull/1373)
  1. Added `end_column` and `start_column` as `integer_t`. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `dependency_chain`, `exploit_requirement`, and `exploit_type` as `string_t`. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `exploit_ref_url`, `license_url`, `package_manager_url`, and `uri` as `url_t`. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `transformation_info_list` [#1392](https://github.com/ocsf/ocsf-schema/pull/1392)
  1. Added `authentication_token` as `authentication_token`, `kerberos_flags` as `string_t` and `is_renewable` as `boolean_t`. [#1391](https://github.com/ocsf/ocsf-schema/pull/1391)
  1. Added `tickets` as an array of `ticket` objects. [#1402](https://github.com/ocsf/ocsf-schema/pull/1402)
  1. Added `is_read` as `boolean_t`. [#1406](https://github.com/ocsf/ocsf-schema/pull/1406)
  1. Added `query_type` and `query_type_id` as `string` and `integer_t` respectively. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
  1. Added `tcp_state_id` as `integer_t`. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
  1. Added `query_evidence` as type `query_evidence`. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
  1. Added `checks` as type `check`. [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
  1. Added 'is_readonly' as type `boolean_t` with a "See specific usage" description. [#1438](https://github.com/ocsf/ocsf-schema/pull/1438)
* #### Objects
  1. Added `assessment` object to capture evaluations/assessments of configurations/signals. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `node`, `edge`, `graph` objects. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `anomaly`, `anomaly_analysis`, `baseline`, `observation` objects. [#1358](https://github.com/ocsf/ocsf-schema/pull/1358)
  1. Added `trait` object. [#1363](https://github.com/ocsf/ocsf-schema/pull/1363)
  1. Added `mitigation` object. [#1348](https://github.com/ocsf/ocsf-schema/pull/1348)
  1. Added `analysis_target` object. [#1371](https://github.com/ocsf/ocsf-schema/pull/1371)
  1. Added `malware_scan_info` object. [#1373](https://github.com/ocsf/ocsf-schema/pull/1373)
  1. Added `application` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `campaign` object [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `threat_actor` object [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `transformation_info` [#1392](https://github.com/ocsf/ocsf-schema/pull/1392)
  1. Added `authentication_token` object. [#1391](https://github.com/ocsf/ocsf-schema/pull/1391)
  1. Added `query_evidence` object. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
  1. Added `check` object [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
* #### Observables
  1. Added `process_entity.uid` as an Observable type - `type_id: 39`. [#1380](https://github.com/ocsf/ocsf-schema/pull/1380)
  1. Added `email.subject` and `email.uid` as an Observable types - `type_id: 40` and `type_id: 41`. [#1380](https://github.com/ocsf/ocsf-schema/pull/1380)
  1. Added `message_uid` as Observable type - `type_id: 42`. [#1380](https://github.com/ocsf/ocsf-schema/pull/1380)
  1. Added `reg_value.name` as an Observable type - `type_id: 43`. [#1380](https://github.com/ocsf/ocsf-schema/pull/1380)
  1. Added `advisory.uid` as Observable type `type_id: 44`. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Updated `resource_details.uid`, `web_resource.uid`, and `win_resource.uid` to be observable `type_id: 10` [#1394](https://github.com/ocsf/ocsf-schema/pull/1394)
  1. Added `file_path_t` as an Observable type - `type_id: 45` and marked fields as this type [#1381](https://github.com/ocsf/ocsf-schema/pull/1381)
     - `lineage` dictionary attribute
     - `affected_package.path` object attribute
     - `file.path` object attribute
     - `image.path` object attribute
     - `kernel.path` object attribute
     - `malware.path` object attribute
     - `process_entity.path` object attribute
  1. Added `extensions/windows/reg_key_path_t` as an Observable type - `type_id: 46` and marked fields as this type [#1381](https://github.com/ocsf/ocsf-schema/pull/1381)
     - `reg_key.path` object attribute
     - `reg_value.path` object attribute


### Improved
* #### Event Classes
  1. Added `assessments` to `config_state`. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `raw_data_size` to `base_event`. [#1347](https://github.com/ocsf/ocsf-schema/pull/1347)
  1. Added `anomaly_analyses` to `detection_finding`. [#1358](https://github.com/ocsf/ocsf-schema/pull/1358)
  1. Added `Detect` value for `activity_id` in Remediation events. [#1362](https://github.com/ocsf/ocsf-schema/pull/1362)
  1. Added `resources` to `user_access`. [#1374](https://github.com/ocsf/ocsf-schema/pull/1374)
  1. Added `malware_scan_info`, `malware` to `detection_finding`. [#1373](https://github.com/ocsf/ocsf-schema/pull/1373)
  1. Added `authentication_token` to `authentication`. [#1391](https://github.com/ocsf/ocsf-schema/pull/1391)

* #### Objects
  1. Added `boot_uid` to `device` object. [#1335](https://github.com/ocsf/ocsf-schema/pull/1335)
  1. Relaxed constraint to provide `email_addr`, `phone_number`, or `security_questions` on `auth_factor`. [#1339](https://github.com/ocsf/ocsf-schema/pull/1339)
  1. Added `cpid` to `process_entity` object. [#1246](https://github.com/ocsf/ocsf-schema/pull/1246)
  1. Added `boot_uid` to `device` object. [#1335](https://github.com/ocsf/ocsf-schema/pull/1335)
  1. Added `meets_criteria` and `policy` to `assessment` object. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `assessments` to `compliance` object. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `data` to `policy` object. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `display_name` attribute to the `user` and `ldap_person` objects. [#1341](https://github.com/ocsf/ocsf-schema/pull/1341)
  1. Added `resource_relationship` to `resource_details` object. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Added `fix_coverage`, `fix_coverage_id` to `vulnerability` object. [#1350](https://github.com/ocsf/ocsf-schema/pull/1350)
  1. Added `eid`, `iccid`, `is_backed_up`, `is_mobile_account_active`, `is_shared`, and `meid` to `device`. [#1346](https://github.com/ocsf/ocsf-schema/pull/1346)
  1. Added `is_backed_up` to `resource_details`. [#1346](https://github.com/ocsf/ocsf-schema/pull/1346)
  1. Added `isp`, `isp_org` to `network_endpoint` & `whois` objects. [#1351](https://github.com/ocsf/ocsf-schema/pull/1351)
  1. Reduced requirement of `standards` to recommended in the `compliance` object. [#1352](https://github.com/ocsf/ocsf-schema/pull/1352)
  1. Updated MITRE `attack`, `tactic`, `technique`, `subtechnique` captions, descriptions, references to include MITRE ATLAS. Used standard requirements for `_entity` extended objects. [#1355](https://github.com/ocsf/ocsf-schema/pull/1355).
  1. Added `name`, `resources`, `uid`, `verdict`, and `verdict_id` to `evidences`. [#1337](https://github.com/ocsf/ocsf-schema/pull/1337)
  1. Added `algorithm` to `analytic` object. [#1358](https://github.com/ocsf/ocsf-schema/pull/1358)
  1. Added 'Network Zone' type to the `managed_entity` object enum list. [#1364](https://github.com/ocsf/ocsf-schema/pull/1364)
  1. Added 'count' `start_time` `end_time` to `timespan` object. [#1365](https://github.com/ocsf/ocsf-schema/pull/1365)
  1. Added `traits` to `related_event` object. [#1363](https://github.com/ocsf/ocsf-schema/pull/1363)
  1. Updated `timespan` to include a Time Window `type_id` and `start_time`, `end_time` to the `at_least_one` constraint. [#1372](https://github.com/ocsf/ocsf-schema/pull/1372)
  1. Added `mitigation` to `attack` object. [#1348](https://github.com/ocsf/ocsf-schema/pull/1348)
  1. Added `timespan` object to `observation` object. [#1371](https://github.com/ocsf/ocsf-schema/pull/1371)
  1. Added `end_column`, `rule`, and `start_column` to `affected_code` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `category` and `desc` to `compliance` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `uri` to the `file` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `license_url`, `package_manager`, `package_manager_url`, `src_url`, and `uid` to `package` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `type`, `type_id`, `uid`, and `version` to `sbom` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `category`, `dependency_chain`, `exploit_ref_url`, `exploit_requirement`, and `exploit_type` to `vulnerability` object. [#1357](https://github.com/ocsf/ocsf-schema/pull/1357)
  1. Added `status`, `status_id`, `status_details` to `ticket` object; `uid_alt`, `created_time` to `_resource` object; `traits` to `finding_info` object. [#1402](https://github.com/ocsf/ocsf-schema/pull/1402)
  1. Added `modified_time` to `_resource` object; `zone` to `resource_details` object. [#1403](https://github.com/ocsf/ocsf-schema/pull/1403)
  1. Added `countermeasures` to `mitigation` object. [#1348](https://github.com/ocsf/ocsf-schema/pull/1348)
  1. Added `is_read` to `email` object. [#1406](https://github.com/ocsf/ocsf-schema/pull/1406)
  1. Added `cis_controls` to `remediation` object [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
  1. Added `check` object to `compliance` object [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
  1. Added `Patch` as a value of `http_method` in the `http_request` object. [#1427](https://github.com/ocsf/ocsf-schema/pull/1427)

* #### Profiles
  1. Added `malware_scan_info` to `security_control` profile. [#1373](https://github.com/ocsf/ocsf-schema/pull/1373)
  1. Added `campaign`, `category`, `created_time`, `creator`, `desc`, `expiration_time`, `external_id`, `labels`, `malware`, `modified_time`, `name`, `detection_pattern`, `detection_pattern_type`, `detection_pattern_type_id`, `intrusion_sets`, `risk_score`, `references`, `uploaded_time`, `severity`, `uid` and `threat_actor` to `osint` object. [#1310](https://github.com/ocsf/ocsf-schema/pull/1310)
  1. Added `tickets` to `incident` profile. [#1402](https://github.com/ocsf/ocsf-schema/pull/1402)

### Deprecated
  1. Deprecated usage of `isp` attribute in the `location` object. [#1351](https://github.com/ocsf/ocsf-schema/pull/1351)
  1. Deprecated usage of `occurrence_details` in favor of `occurrences` in `discovery_details` object. [#1358](https://github.com/ocsf/ocsf-schema/pull/1358)
  1. Deprecated usage of `resource` in favor of `resources` in the `user_access` class. [#1374](https://github.com/ocsf/ocsf-schema/pull/1374)
  1. Deprecated usage of `ticket` in favor of `tickets` in `incident` profile and `incident_finding` event class. [#1402](https://github.com/ocsf/ocsf-schema/pull/1402)
  1. Deprecated `kernel_object_query`, `file_query`, `folder_query`, `admin_group_query`, `job_query`, `module_query`, `network_connection_query`, `networks_query`, `peripheral_device_query`, `process_query`, `service_query`, `user_session_query`, `user_query`, `startup_item_query`, `registry_key_query`, `registry_value_query`, and `prefetch_query` classes in favor of the `live_evidence_info` class. [#1382](https://github.com/ocsf/ocsf-schema/pull/1382)
  1. Deprecated `compliance_references` and `compliance_standards` in favor of the `check` object. [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
  1. Deprecated `cis_csc` in favor of `cis_control` object. [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
  1. Deprecated the `Device Config State` class in favor of the `Compliance Finding` class. [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)

### Misc
  1. Updated description of `config_state` to reflect the addition of the `assessments` object. [#1343](https://github.com/ocsf/ocsf-schema/pull/1343)
  1. Updated description of `hw_info.uuid` to clarify usage especially in presence of new `device.udid` field. [#1354](https://github.com/ocsf/ocsf-schema/pull/1354)
  1. Updated dictionary descriptions and references of MITRE `attacks`, `tactic`, `technique`, `subtechnique`. [#1355](https://github.com/ocsf/ocsf-schema/pull/1355)
  1. Added enhanced descriptions and references to `requirements`, `standards`, `control_parameters`, and `control` in the `compliance` object for clarity and usage. [#1369](https://github.com/ocsf/ocsf-schema/pull/1369)
