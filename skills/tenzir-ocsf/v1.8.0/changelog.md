# OCSF changelog: [v1.8.0] - Mar 16th, 2026

### Added
* #### Categories
* #### Event Classes
* #### Profiles
  1. Added `ai_operation` profile with essential attributes for AI operation event mapping. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `macos/macos_users` profile with `egid` and `euid` attributes. This profile is used by the `process` object. [#1538](https://github.com/ocsf/ocsf-schema/pull/1538)
* #### Objects
  1. Added `ai_model` object with core fields (`name`, `ai_provider`, `version`) for AI operation events. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `message_context` object for AI system interactions with role-based identification and token usage metrics (`prompt_tokens`, `completion_tokens`, `total_tokens`). [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `token` object for API tokens, client tokens, and API keys used in API activity events. [#1429](https://github.com/ocsf/ocsf-schema/pull/1429)
  1. Added `gpu_info` object for GPU's (array name `gpu_info_list`). [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `privilege_info` object for describing specific privileges, actions, or permissions with usage status and `type_id` enum (Read, Write, Execute). [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `privilege_attack_info` object for grouping privileges by potential MITRE ATT&CK techniques. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `service_privilege_analysis` object for privilege analysis results per cloud service or namespace. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `packet` object for network packets (array name `packet_list`). [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
* #### Observables
* #### Platform Extensions
  1. Added `macos` extension (`uid` 3). This extension adds the `macos/macos_users` profile and patches the `process` object to add this profile. [#1538](https://github.com/ocsf/ocsf-schema/pull/1538)
* #### Dictionary Attributes
  1. Added `ai_provider` attribute for AI model identification. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `ai_role_id`, `ai_role` attributes for AI communication context with proper sibling relationship. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `prompt_tokens`, `completion_tokens`, `total_tokens` attributes for AI token usage metrics. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `embedding_model` attribute for AI retrieval systems. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `imported_symbols` attribute for reporting an executable file's imports.  [#1553](https://github.com/ocsf/ocsf-schema/pull/1553)
  1. Added `Imphash (18)` enum to the `algorithm_id` attribute of the `fingerprint` object. [#1553](https://github.com/ocsf/ocsf-schema/pull/1553)
  1. Added `token` as a `token` object. [#1429](https://github.com/ocsf/ocsf-schema/pull/1429)
  1. Added `bus_type`	Derived from `bus_type_id`. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `bus_type_id` Identifier for the bus/interface standard. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `cores` Number of cores. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `vram_size` Installed VRAM. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `vram_mode` Derived from `vram_type_id`. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `vram_mode_id` Identifier for VRAM type. [#1527](https://github.com/ocsf/ocsf-schema/pull/1527)
  1. Added `total_queued_duration` to track how long an event spent in a queue. [#1536](https://github.com/ocsf/ocsf-schema/pull/1536)
  1. Added `department` and `is_on_premises_sync_enabled` for ldap and Entra ID support. [#1584](https://github.com/ocsf/ocsf-schema/pull/1584)
  1. Added `is_disabled` and `is_locked` as type `boolean_t` with a "See specific usage" description. [#1583](https://github.com/ocsf/ocsf-schema/pull/1583)
  1. Added `all_privileges_unused` boolean attribute indicating whether all privileges in a group are unused. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `analyzed_privileges_count` integer attribute for the total count of analyzed privileges. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `attack` singular attribute for MITRE ATT&CK details (complements existing `attacks` array). [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `is_unused` boolean attribute indicating whether an item is unused. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `privilege_attack_info`, `privilege_attack_info_list` attributes for privilege-to-attack mappings. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `privilege_info`, `privilege_info_list` attributes for specific privilege information. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `service_privilege_analysis`, `service_privilege_analysis_list` attributes for service-level privilege analysis. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `total_potential_attacks_count` integer attribute for count of privileges mapping to attack techniques. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `read_count`, `write_count`, and `execute_count` integer attributes. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `pool` attribute of type `group`. [#1521](https://github.com/ocsf/ocsf-schema/pull/1521)
  1. Added `mac_vendor` as `string_t`. [#1575](https://github.com/ocsf/ocsf-schema/pull/1575)
  1. Added `network_observation_point` as type `network_endpoint`. [#1571](https://github.com/ocsf/ocsf-schema/pull/1571)
  1. Added `packet` as a `packet` object. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `packet_list` as an array of `packet` objects. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `encoding`, `encoding_id` attributes for data encoding representation. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `format`, `format_id` attributes for data format identification. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `source_id` normalized identifier for the source. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `sequence_number` attribute for ordering within a sequence. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `start_offset` attribute for the starting offset. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
  1. Added `end_offset` attribute for the ending offset. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
### Improved
* #### Categories
* #### Event Classes
  1. Add `app_protocol_name` to `Network Activity` class with clarified description for deep packet inspection. [#1557](https://github.com/ocsf/ocsf-schema/pull/1557)
  1. Enhanced `app_name` description in `Network Activity` class to clarify network application identification by tools such as NBAR. [#1557](https://github.com/ocsf/ocsf-schema/pull/1557)
  1. Added `ai_operation` profile to `process_activity` event class. [#1578](https://github.com/ocsf/ocsf-schema/pull/1578)
  1. Added `network_observation_point` attribute to the base `Network` event. [#1571](https://github.com/ocsf/ocsf-schema/pull/1571)
  1. Added `packet_list` to `network` event class. [#1569](https://github.com/ocsf/ocsf-schema/pull/1569)
* #### Profiles
* #### Objects
  1. Extended `database` object with AI-specific database types (`Vector (7)`, `Knowledge Graph (8)`) and `embedding_model` field for AI retrieval systems. [#1488](https://github.com/ocsf/ocsf-schema/pull/1488)
  1. Added `signatures` to the `file` object. [#1546](https://github.com/ocsf/ocsf-schema/pull/1546)
  1. Expanded on `created_time` attribute description within the `related_event` object. [1552](https://github.com/ocsf/ocsf-schema/pull/1552)
  1. Added `imported_symbols` attribute to the `file` object.  [#1553](https://github.com/ocsf/ocsf-schema/pull/1553)
  1. Updated `fingerprint` object description. Updated the descriptions of `algorithm`, `algorithm_id`, and `value` attributes in the `fingerprint` object. [#1560](https://github.com/ocsf/ocsf-schema/pull/1560)
  1. Added `fingerprints` attribute to the `network_endpoint` object. [#1560](https://github.com/ocsf/ocsf-schema/pull/1560)
  1. Added `mac_vendor` to the `endpoint` object. [#1575](https://github.com/ocsf/ocsf-schema/pull/1575)
  1. Added `token` as an attribute to the `api` object. [#1429](https://github.com/ocsf/ocsf-schema/pull/1429)
  1. Added `created_time` attribute back to the `authentication_token` object with improved description. [#1429](https://github.com/ocsf/ocsf-schema/pull/1429)
  1. Added `provider` to the `resource_details` object via `cloud` profile. [#1566](https://github.com/ocsf/ocsf-schema/pull/1566)
  1. Added `resource` attribute to the `check` object to describe details about the resource that the check evaluated. [#1574](https://github.com/ocsf/ocsf-schema/pull/1574)
  1. Added `total_queued_duration` to the `metadata` object. [#1536](https://github.com/ocsf/ocsf-schema/pull/1536)
  1. Added `is_on_premises_sync_enabled` to `Account`. Added `department` to `ldap_person`. Added `ActiveDirectory Account` to `Account.type`. [#1584](https://github.com/ocsf/ocsf-schema/pull/1584)
  1. Added `is_disabled` and `is_locked` attributes to the `account` object. [#1583](https://github.com/ocsf/ocsf-schema/pull/1583)
  1. Added `analyzed_privileges_count`, `service_privilege_analysis_list`, and `total_potential_attacks_count` attributes to the `permission_analysis_result` object for detailed privilege analysis. [#1581](https://github.com/ocsf/ocsf-schema/pull/1581)
  1. Added `macos/macos_users` profile to the `process` object via `macos` extension patch. [#1538](https://github.com/ocsf/ocsf-schema/pull/1538)
  1. Added `pool` attribute to the `endpoint` object. [#1521](https://github.com/ocsf/ocsf-schema/pull/1521)
  1. Added `uid_alt` attribute to the `group` object. [#1521](https://github.com/ocsf/ocsf-schema/pull/1521)

* #### Observables
* #### Platform Extensions
* #### Dictionary Attributes
  1. Moved all dictionary attributes previously defined in the `linux` extension to the base schema: the `auid`, `egid`, and `euid` dictionary attributes. This was done so the `egid` and `euid` attributes can be used by both the `linux` and `macos` extensions. This changes the internal names of these items in the compiled schema, removing the `linux/` prefix. This should _not_ cause a problem for tooling since compiled classes and objects include processed and enriched versions of these attributes. There is no need to lookup class and object attributes in the dictionary, and indeed doing can yield incomplete and inaccurate information. [#1538](https://github.com/ocsf/ocsf-schema/pull/1538)
* #### Dictionary Types
  1. The regular expression constraint in dictionary type `file_hash_t` has been removed to use as a general fingerprint with an arbitrary string. **Warning:** This can create a breaking change for some kinds of tooling that process OCSF events. [1564](https://github.com/ocsf/ocsf-schema/pull/1564)

### Bugfixes
* #### Event Classes
  1. Removed erroneous `at_least_one` constraint in `Live Evidence Info` class [#1357](https://github.com/ocsf/ocsf-schema/pull/1537)

### Deprecated
1. Deprecated the `signature` attribute of the file object in favour of the `signatures` attribute. [#1546](https://github.com/ocsf/ocsf-schema/pull/1546)

### Breaking changes
  1. The regular expression constraint in dictionary type `file_hash_t` has been removed. This can create a breaking change for some kinds of tooling that process OCSF events. (Repeated item from Dictionary Types section above.) [1564](https://github.com/ocsf/ocsf-schema/pull/1564)

### Misc
1. New Extension registration for Synqly [#1579](https://github.com/ocsf/ocsf-schema/pull/1579).
1. Added GitHub Actions workflow for automated schema description review using Claude to suggest LLM comprehension improvements on PRs. [#1587](https://github.com/ocsf/ocsf-schema/pull/1587) [#1588](https://github.com/ocsf/ocsf-schema/pull/1588)
1. Corrected caption for `type` attribute in `group` object: was `Account Type`, now `Group Type`. Also corrected description, which erroneously included 'or account'. [#1590](https://github.com/ocsf/ocsf-schema/pull/1590)
