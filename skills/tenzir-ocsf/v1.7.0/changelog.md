# OCSF changelog: [v1.7.0] - Nov 14th, 2025

### Added
* #### Categories
* #### Event Classes
  1. Added `Peripheral Activity` event class to the System category. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
* #### Profiles
* #### Objects
  1. Added `reporter` object. [#1476](https://github.com/ocsf/ocsf-schema/pull/1476)
  1. Added Windows extension to the `process` object.
  1. Added the `function_invocation` and `parameter` objects. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
* #### Observables
  1. Set `network_endpoint.uid` as an Observable type - `type_id: 48`. [#1502](https://github.com/ocsf/ocsf-schema/pull/1502)
* #### Platform Extensions
* #### Dictionary Attributes
  1. Added `vendor_id_list` as a `string_t` array. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
  1. Added `post_value`, `pre_value` and `return_value` as `string_t`. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Added `launch_type_id` enum and `launch_type` sibling. [#1517](https://github.com/ocsf/ocsf-schema/pull/1517)
  1. Added `log_source` `log_source_uid` `log_format` as `string_t`. [#1483](https://github.com/ocsf/ocsf-schema/pull/1483)

### Improved
* #### Categories
* #### Event Classes
  1. Added `auth_factors` as an attribute to the `Account Change` class and updated related activity names. [#1455](https://github.com/ocsf/ocsf-schema/pull/1455)
  1. Added `Invoke` as an `activity_id` value for the `Module Activity` class. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Added `launch_type_id` and `launch_type` as attributes to the `Process Activity` event class. [#1517](https://github.com/ocsf/ocsf-schema/pull/1517)
  1. Added descriptions to values of `activity_id` enum in `Process Activity` event class. [#1517](https://github.com/ocsf/ocsf-schema/pull/1517)
  1. Added missing context classification to `windows_service_activity.win_service`. [#1531](https://github.com/ocsf/ocsf-schema/pull/1531)
  1. Added missing requirement to `process_activity.launch_type`. [#1531](https://github.com/ocsf/ocsf-schema/pull/1531)
  1. Added `cumulative_traffic` attribute to the base `Network` event. Updated `traffic` description. [#1529](https://github.com/ocsf/ocsf-schema/pull/1529)
* #### Profiles
* #### Objects
  1. Added `type`, `type_uid`, and `vendor_id_list` to the `peripheral_device` object. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
  1. Relaxed the `class` attribute requirement to `optional` in the `peripheral_device` object. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
  1. Set the `vendor_name` requirement to `recommended` in the `peripheral_device` object. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
  1. Added `reporter` to the `metadata` object. [#1476](https://github.com/ocsf/ocsf-schema/pull/1476)
  1. Added `event_uid` and `type_uid` to the `observable` object. [#1503](https://github.com/ocsf/ocsf-schema/pull/1503)
  1. Set `load_type_id` requirement to `recommended` in the `module` object. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Added `at_least_one` constraint on `load_type_id` and `function_name` in the `module` object. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Modified descriptions in the `module` object to accommodate `Module Activity: Invoke` event. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Added `function_invocation` to the `module` object. [#1497](https://github.com/ocsf/ocsf-schema/pull/1497)
  1. Relaxed the `file` attribute requirement to `optional` in the `job` object. [#1509](https://github.com/ocsf/ocsf-schema/pull/1509)
  1. Relaxed the `name` and `uid` requirement to `recommended` with `at_least_one` constraint in the `extension` object. [#1511](https://github.com/ocsf/ocsf-schema/pull/1511)
  1. Added `hosting_process`, `service_file` and `service_dll_file` to the `win_service` object.
  1. Added `hosted_services`, array to the `process` object.
  1. Added `source`, `type`, `log_source`, `original_event_uid`,`log_format`, `transmit_time` to `metadata`. `log_format` to `logger`[#1483](https://github.com/ocsf/ocsf-schema/pull/1483)
  1. Added `start_time`, `end_time` and `timespan` to the `network_traffic` object. Updated `network_traffic` description. [#1529](https://github.com/ocsf/ocsf-schema/pull/1529)
* #### Observables
* #### Platform Extensions
* #### Dictionary Attributes
  1. Added `Local (4)` enum to the `direction_id` attribute. [#1475](https://github.com/ocsf/ocsf-schema/pull/1475)
  1. Added `Atom (38)` enum as an available `type_id` for `win_resource` object. [#1477](https://github.com/ocsf/ocsf-schema/pull/1477)
  1. Updated reference descriptions/urls for win_resource types, including `Directory (1)`, `Event (2)`, `Timer (3)`, `Device (4)`, `Mutant (5)`, `File (7)`, `Token (8)`, `Thread (9)`, `Section (10)`, `WindowStation (11)`, `Driver (15)`, `IoCompletion (16)`, `Controller (17)`, `SymbolicLink (18)`, `WmiGuid (19)`, `Process (20)`, `Profile (21)`, `Desktop (22)`, `KeyedEvent (23)`, `Adapter (24)`, `Callback (27)`, `Semaphore (28)`, `Job (29)`, `ALPC Port (32)`, `SAM_ALIAS (33)`, `SAM_GROUP (34)`, `SAM_USER (35)`, `SAM_DOMAIN (36)`, `SAM_SERVER (37)`, and `Atom (38)`. [#1477](https://github.com/ocsf/ocsf-schema/pull/1477)
  1. Added `hosted_services` to the Windows extension to the `process` object.
  1. Added multiple values to the `state_id` enum attribute for the `digital_signature` object. [#1520](https://github.com/ocsf/ocsf-schema/pull/1520)
  1. Added `WFP Filter (39)`, `WFP Callout (40)`, `WFP Layer (41)`, `WFP Sub-layer (42)`, `WFP Provider (43)` and `WFP Provider Context (44)` WindowsFilteringPlatform-related enums as an available `type_ids` for `win_resource` object. [#1530](https://github.com/ocsf/ocsf-schema/pull/1530)
  1. Added `cumulative_traffic` of `network_traffic` type. [#1529](https://github.com/ocsf/ocsf-schema/pull/1529)

### Bugfixes

### Deprecated

### Breaking changes

### Misc
  1. Updated description for the `peripheral_device` object and the `vendor_name` attribute within it. [#1471](https://github.com/ocsf/ocsf-schema/pull/1471)
  1. Corrected the deprecation note for the `Web Resource Access Activity` event class. [#1492](https://github.com/ocsf/ocsf-schema/pull/1492)
