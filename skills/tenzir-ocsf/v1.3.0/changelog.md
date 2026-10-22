# OCSF changelog: [v1.3.0] - August 1st, 2024

### Added
* #### Categories
    1. Added `Remediation` category. [#1066](https://github.com/ocsf/ocsf-schema/pull/1066)
* #### Event Classes
    1. Added `Event Log Activity` event class to the System Activity category. [#1014](https://github.com/ocsf/ocsf-schema/pull/1014)
    2. Added `Remediation Activity`, `File Remediation Activity`, `Process Remediation Activity`, `Network Remediation Activity` event classes to the Remediation category. [#1066](https://github.com/ocsf/ocsf-schema/pull/1066)
    3. Added `Windows Service Activity` event class to the System Activity category via Windows extension. [#1103](https://github.com/ocsf/ocsf-schema/pull/1103)
    4. Added `Software Inventory Info` event class to the Discovery category. [#1134](https://github.com/ocsf/ocsf-schema/pull/1134)
* #### Profiles
    1. Added `osint` Profile based on the `osint` object. [#992](https://github.com/ocsf/ocsf-schema/pull/992)
* #### Objects
    1. Added `d3fend`, `d3f_tactic`, `d3f_technique` MITRE objects. [#1066](https://github.com/ocsf/ocsf-schema/pull/1066)
    2. Added `ja4_fingerprint` object. [#834](https://github.com/ocsf/ocsf-schema/pull/834)
    3. Added `ja4_fingerprint_list` as a list of `ja4_fingerprint` objects.  [#834](https://github.com/ocsf/ocsf-schema/pull/834)
    4. Added `ticket` object. [#1068](https://github.com/ocsf/ocsf-schema/pull/1068)
    5. Added `osint` object. [#992](https://github.com/ocsf/ocsf-schema/pull/992)
    6. Added `signatures` object, an array of `signature` objects. [#992](https://github.com/ocsf/ocsf-schema/pull/992)
    7. Added `whois` object. [#992](https://github.com/ocsf/ocsf-schema/pull/992)
    8. Added `domain_contact` and array-typed `domain_contacts` object for use with `whois` object. [#992](https://github.com/ocsf/ocsf-schema/pull/992)
    9. Added `Windows Service` object to the Windows extension. [#1103](https://github.com/ocsf/ocsf-schema/pull/1103)
    10. Added `timespan` object. [#1125](https://github.com/ocsf/ocsf-schema/pull/1125)

### Improved
* #### Categories
    n/a
* #### Event Classes
    1. Added `file_result` to File Hosting Activity. [#1045](https://github.com/ocsf/ocsf-schema/pull/1045)
    2. Added entries to `injection_type_id` enum (`Process Activity`) and `activity_id` enum (`Memory Activity`). [#1060](https://github.com/ocsf/ocsf-schema/pull/1060)
    3. Added a `Restart`, `Enable`, `Disable`, and `Update` `activity_id` to the `Application Lifecycle` class. [#1064](https://github.com/ocsf/ocsf-schema/pull/1064)
    4. Added `ja4_fingerprint_list` to base network event class. [#834](https://github.com/ocsf/ocsf-schema/pull/834)
    5. Added `ticket` to `Incident Finding` event class. [#1068](https://github.com/ocsf/ocsf-schema/pull/1068)
    6. Added new activities `Enroll`, `Activate`, `Deactivate`, `Suspend`, and `Resume` to the `Entity Management` class. [#1095](https://github.com/ocsf/ocsf-schema/pull/1095)
    7. Added new activity `Listen` to `Network Activity` and relax requirement of `src_endpoint`. [#1147](https://github.com/ocsf/ocsf-schema/pull/1147)
    8. Added `state`, `state_id` to `Device Config State Change`. [#1143](https://github.com/ocsf/ocsf-schema/pull/1143)
    9. Added `resources` attribute to `Vulnerability Finding` and `Compliance Finding`. [#1150](https://github.com/ocsf/ocsf-schema/pull/1150)
* #### Profiles
    n/a
* #### Objects
    1. Added `ext` to `File` object. [#1046](https://github.com/ocsf/ocsf-schema/pull/1046)
    2. Added `account`, `device`, `email`, `url`, `user` to `evidences` in detection finding. [#1000](https://github.com/ocsf/ocsf-schema/pull/1000)
    3. Added `state_id`, `state` to `Digital Signature` object. [#1069](https://github.com/ocsf/ocsf-schema/pull/1069)
    4. Added `domain` to `Uniform Resource Locator` object. [#1096](https://github.com/ocsf/ocsf-schema/pull/1096)
    5. Added `reg_key` and `reg_value` to `Evidence Artifacts` object. [#1078](https://github.com/ocsf/ocsf-schema/pull/1078)
    6. Added `type_id` and associated entity objects to `Managed Entity`. [#1094](https://github.com/ocsf/ocsf-schema/pull/1094)
    7. Added `vendor_name`, `type`, `type_id` to object `package`. [#1093](https://github.com/ocsf/ocsf-schema/pull/1093)
    8. Added `router`, `ids`, and `ips` entries to `type_id` enum in the `Endpoint` object. [#1121](https://github.com/ocsf/ocsf-schema/pull/1121)
    9. Added `job` to `Evidence Artifacts` object. [#1130](https://github.com/ocsf/ocsf-schema/pull/1130)
    10. Added `ip` to object `load_balancer`. [#1138](https://github.com/ocsf/ocsf-schema/pull/1138)
    11. Added `cpe_name` and `hash` to `Software Package` object. [#1142](https://github.com/ocsf/ocsf-schema/pull/1142)
    12. Added `avg_timespan` to the `kb_article` object. [#1125](https://github.com/ocsf/ocsf-schema/pull/1125)
    13. Added `created_time`,`desc`, `short_desc`, `reputation`, `src_url` to `enrichment` object. [#1149](https://github.com/ocsf/ocsf-schema/pull/1149)
    14. Added `compliance_references`, `compliance_standards` to the `compliance` object. [#1110](https://github.com/ocsf/ocsf-schema/pull/1110)

### Bugfixes
1. Fixed the host profile construction in `patch_state` event class. [#1087](https://github.com/ocsf/ocsf-schema/pull/1087)
2. Removed the optional requirement overrides for `name` and `uid` in `_resource` as they are part of a constraint. [#1087](https://github.com/ocsf/ocsf-schema/pull/1087)
3. Fixed declarations of `data_lifecycle_state_id`, `integrity`, `opcode_id`, `risk_level`, and `analytic.type_id`. [#1111](https://github.com/ocsf/ocsf-schema/pull/1111)

### Deprecated
1. Deprecated `resource` in `Vulnerability Finding` and `Compliance Finding` event classes in favor of `resources`. [#1150](https://github.com/ocsf/ocsf-schema/pull/1150)

### Breaking changes
n/a
### Misc
1. Colorized validator output [#1048](https://github.com/ocsf/ocsf-schema/pull/1048)
    * Updated the GitHub workflow for the `ocsf-validator` to print colorized output.
2. Clarify how to reference profiles in metadata [#1056](https://github.com/ocsf/ocsf-schema/pull/1056)
    * Updated the description of `metadata.profiles` to clarify the correct way to reference a profile in that list.
3. Added a `gitignore` file. [#1071](https://github.com/ocsf/ocsf-schema/pull/1071)
4. New Extension registration for Cisco [#1074](https://github.com/ocsf/ocsf-schema/pull/1074)
5. Cleaned up MITRE trademarks and registrations for captions and descriptions.
6. Declared enums in dictionary.json have sane "0" (Unknown) and "99" (Other) declarations and descriptions where appropriate [#1111](https://github.com/ocsf/ocsf-schema/pull/1111)
7. Adds support for `suppress_checks` controls in attributes to allow tools to automatically validate conventions [#1063](https://github.com/ocsf/ocsf-schema/pull/1063)
    * Updated several attributes that do not follow conventions to disable linting for them
8. Added `credential_uid` as an Observable type - `type_id: 19`. [#1137](https://github.com/ocsf/ocsf-schema/pull/1137)
9. New Extension registration for US Gov [#1140](https://github.com/ocsf/ocsf-schema/pull/1140)
10. Enum definitions are now refactored such that generic enum descriptions have "See specific usage" in the description [#1146](https://github.com/ocsf/ocsf-schema/pull/1146)
