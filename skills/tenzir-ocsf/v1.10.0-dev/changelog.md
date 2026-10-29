# OCSF changelog: [Unreleased]

### Added
* #### Categories
* #### Event Classes
  1. Added `dns_zone_transfer_activity` (`DNS Zone Transfer Activity`) class to capture DNS zone transfers (AXFR/IXFR) and NOTIFY. [#1675](https://github.com/ocsf/ocsf-schema/pull/1675)
* #### Profiles
  1. Added optional `ai_capability` attribute to the `ai_operation` profile, recording the invoked AI capability (tool, resource, or prompt). [#1729](https://github.com/ocsf/ocsf-schema/pull/1729)
* #### Objects
  1. Added `firewall_rule_evaluation` (Security Control Rule Evaluation), extending `firewall_rule` with optional normalized action and disposition attributes. [#1786](https://github.com/ocsf/ocsf-schema/pull/1786)
  1. Added `ai_capability` object describing an invoked AI capability — its primitive kind, provenance (serving system and transport), declared behavior hints, and input/output schema, description, and baseline fingerprints. [#1729](https://github.com/ocsf/ocsf-schema/pull/1729)
  1. Added the `ai_status` object for per-operation outcome scalars contributed by the `ai_operation` profile, with `stop_reason` / `stop_reason_id` (enum: Unknown (0), End of Turn (1), Token Limit (2), Tool Use (3), Session Stop (4), Content Filter (5), Other (99)) and `permission_result` / `permission_result_id` (enum: Unknown (0), Allowed (1), Denied (2), Other (99)). Additional outcome attributes may be added in later versions. [#1704](https://github.com/ocsf/ocsf-schema/pull/1704)
  1. Added the `wifi` object describing IEEE 802.11 network identity, radio and security attributes. [#1721](https://github.com/ocsf/ocsf-schema/pull/1721)
  1. Added `dns_soa` object to represent the RFC 1035 SOA (Start of Authority) record RDATA, used to carry zone serials and timers in DNS zone transfers. [#1675](https://github.com/ocsf/ocsf-schema/pull/1675)
* #### Observables
* #### Platform Extensions
* #### Dictionary Attributes
  1. Added `additional_firewall_rules` as an array of `firewall_rule_evaluation` objects. [#1786](https://github.com/ocsf/ocsf-schema/pull/1786)
  1. Added `likelihood` as a `string_t`, normalized to the caption of `likelihood_id`. [#1715](https://github.com/ocsf/ocsf-schema/pull/1715)
  1. Added `likelihood_id` as an `integer_t` enum with values Unknown (0), Very Low (1), Low (2), Moderate (3), High (4), Very High (5), Other (99). [#1715](https://github.com/ocsf/ocsf-schema/pull/1715)
  1. Added `likelihood_score` as an `integer_t`, complementing `confidence_score`, `impact_score`, and `risk_score`. [#1715](https://github.com/ocsf/ocsf-schema/pull/1715)
  1. Added `ai_capability`, `transport`/`transport_id`, `is_destructive`, `is_idempotent`, `is_open_world`, `input_schema_fingerprint`, `output_schema_fingerprint`, `desc_fingerprint`, `baseline_fingerprint`, `cache_scope`/`cache_scope_id`, `cache_ttl`, and `task_uid` attributes for the `ai_capability` object. [#1729](https://github.com/ocsf/ocsf-schema/pull/1729)
  1. Added `is_declared_incident` and `resolved_time`. [#1740](https://github.com/ocsf/ocsf-schema/pull/1740)
  1. Added `progress_current`, `progress_total`, `progress_unit`, `progress_unit_id`, `bytes_processed`, `bytes_written`, `throughput` and `queue_name` attributes. [#1722](https://github.com/ocsf/ocsf-schema/pull/1722)
  1. Added `log_facility` and `log_facility_id` attributes. [#1720](https://github.com/ocsf/ocsf-schema/pull/1720)
  1. Added `icmp_type`, `icmp_code` and `icmp_uid` attributes. [#1719](https://github.com/ocsf/ocsf-schema/pull/1719)
  1. Added `audience` as a `string_t`, with `source` set to the `aud` claim and a reference to RFC 7519. [#1705](https://github.com/ocsf/ocsf-schema/pull/1705)
  1. Added `ai_status`, `permission_result`, `permission_result_id`, `stop_reason`, and `stop_reason_id` attributes. [#1704](https://github.com/ocsf/ocsf-schema/pull/1704)
  1. Added `access_point_status`, `access_point_status_id`, `band`, `band_id`, `bssid`, `channel_number`, `data_rate`, `is_access_point_on_wired_network`, `noise_floor`, `security_protocol`, `security_protocol_id`, `signal_noise_ratio`, `signal_strength`, `ssid`, `standard` and `wifi` attributes. [#1721](https://github.com/ocsf/ocsf-schema/pull/1721)
  1. Added `dns_zone`, `dns_additional`, `soa`, `updated_soa`, `num_records`, `transfer_type`, `transfer_type_id`, and the SOA sub-fields `primary_server`, `responsible_party`, `sequence_number`, `refresh_interval`, `retry_interval`, `expire_interval`, and `minimum_ttl` for DNS zone transfers. [#1675](https://github.com/ocsf/ocsf-schema/pull/1675)
  1. Added `data_bytes`, `data_bytes_in` and `data_bytes_out` attributes. [#1775](https://github.com/ocsf/ocsf-schema/pull/1775)

### Improved
* #### Categories
* #### Event Classes
  1. Added `likelihood`, `likelihood_id`, and `likelihood_score` as optional attributes in the `context` group on `Detection Finding` (class 2004). [#1715](https://github.com/ocsf/ocsf-schema/pull/1715)
  1. Added `is_declared_incident` to finding.json and incident_finding.json. Added `resolved_time` to `finding.json` and `incident_finding.json`. [#1740](https://github.com/ocsf/ocsf-schema/pull/1740)
  1. Overrode the `ai_operation` profile's `ai_agent` description on `Application Lifecycle` (class 6002) to clarify that it represents the affected application when that application is itself an AI agent. [#1751](https://github.com/ocsf/ocsf-schema/pull/1751)
  1. Clarified `ai_agent` description in `role_management` to identify the agent that `iam_role` is provisioned for or bound to, rather than the actor-oriented wording inherited from the `ai_operation` profile. Noted in the class description that `role_management` covers roles bound to AI agents. [#1726](https://github.com/ocsf/ocsf-schema/pull/1726)
* #### Profiles
  1. Added optional `additional_firewall_rules` to the `security_control` profile for other reported security control rule evaluations and their individual actions and dispositions. Clarified the profile's event-level action and disposition, attribution through `firewall_rule`, and distinction from additional rule evaluations. [#1786](https://github.com/ocsf/ocsf-schema/pull/1786)
  1. Added `ai_status` (optional) to the `ai_operation` profile in the `context` group, grouping per-operation outcome scalars (stop reason and permission check result) so they do not proliferate at the event root. [#1704](https://github.com/ocsf/ocsf-schema/pull/1704)
  1. Added `is_declared_incident` to incident.json. [#1740](https://github.com/ocsf/ocsf-schema/pull/1740)
* #### Objects
  1. Added `labels` to the `node` object for grouping nodes into named subgraphs. [#1715](https://github.com/ocsf/ocsf-schema/pull/1715)
  1. Broadened the `firewall_rule` caption and descriptions to Security Control Rule, covering rules evaluated by firewalls and other security controls. [#1786](https://github.com/ocsf/ocsf-schema/pull/1786)
  1. Added `progress_current`, `progress_total`, `progress_unit`, `progress_unit_id`, `bytes_processed`, `bytes_written`, `throughput` and `queue_name` to the `job` object so a running job can report its progress and throughput. [#1722](https://github.com/ocsf/ocsf-schema/pull/1722)
  1. Added `created_time`, `first_seen_time`, `last_seen_time`, `modified_time`, `src_url`, and `criticality_id` attributes to the `application` object. [#1683](https://github.com/ocsf/ocsf-schema/pull/1683)
  1. Added `is_declared_incident`, `resolved_time` to `finding.json` and `incident_finding.json`. [#1740](https://github.com/ocsf/ocsf-schema/pull/1740)
  1. Added `query_info` to the `finding_info` object  for the search behind the `related_events` in the finding. [#1744](https://github.com/ocsf/ocsf-schema/pull/1744)
  1. Added `finding_info` to the `related_events` object for cases where the related event is a finding. [#1744](https://github.com/ocsf/ocsf-schema/pull/1744)
  1. Added `raw_data` to the `related_events` object to optionally carry the full event as a string. [#1744](https://github.com/ocsf/ocsf-schema/pull/1744)
  1. Added `risk_details`, `risk_level_id`, `risk_level`, `risk_score` to `related_events` to carry any risk values when the related event is a finding. [#1744](https://github.com/ocsf/ocsf-schema/pull/1744)
  1. Added `type_id`, `type` to `related_events` to distinguish activities, alerts, or findings as the type of the related event. [#1744](https://github.com/ocsf/ocsf-schema/pull/1744)
  1. Added `log_facility` and `log_facility_id` to the `metadata` and `logger` objects. [#1720](https://github.com/ocsf/ocsf-schema/pull/1720)
  1. Added `icmp_type`, `icmp_code` and `icmp_uid` to the `network_connection_info` object. [#1719](https://github.com/ocsf/ocsf-schema/pull/1719)
  1. Added `data_bytes`, `data_bytes_in` and `data_bytes_out` to the `network_traffic` object, counting the data carried by the Layer 4 (Transport Layer) protocol, excluding the IP and transport headers, and clarified that its `bytes`, `bytes_in`, `bytes_out` and `bytes_missed` count bytes in Layer 3 (Network Layer) packets, including IP header and payload. [#1775](https://github.com/ocsf/ocsf-schema/pull/1775)
  1. Added per-node authority attributes `scopes`, `audience`, and `expiration_time` to the `delegation` object, so each hop in the chain of authority records what was granted, for whom, and until when. [#1705](https://github.com/ocsf/ocsf-schema/pull/1705)
  1. Added `wifi` to the `network_endpoint` and `network_interface` objects. Resolves #1463. [#1721](https://github.com/ocsf/ocsf-schema/pull/1721)
  1. Added `value` to the `digital_signature` object so an event can carry the signature bytes themselves, not only a description of them — the raw signature output of `algorithm_id`, encoded as standard Base64 (RFC 4648 §4). [#1709](https://github.com/ocsf/ocsf-schema/pull/1709)
* #### Observables
* #### Platform Extensions
* #### Dictionary Attributes
  1. Added `Sub-Agent Stop (6)` to the `stop_reason_id` enum, for a completion that ended because the sub-agent performing it was stopped. [#1780](https://github.com/ocsf/ocsf-schema/pull/1780)
  1. Broadened the `firewall_rule` caption and description to Security Control Rule while preserving its attribution to the event-level action or disposition. [#1786](https://github.com/ocsf/ocsf-schema/pull/1786)

### Bugfixes
1. Changed the `account` requirement in the `user` object from optional to recommended to align with its participation in the `at_least_one` constraint. [#1766](https://github.com/ocsf/ocsf-schema/pull/1766)
1. Changed optional attributes that participate in an `at_least_one` or `just_one` constraint to `recommended`, and replaced the undefined `log_file` constraint member on `event_log_activity` with `file`. [#1767](https://github.com/ocsf/ocsf-schema/pull/1767)
1. Escaped the dots between IPv4 octets in the `ip_t` regex (IPv4 and IPv4-embedded IPv6 forms), which matched any character, so `192x168x1x1` validated as an IP address. Raised `ip_t` `max_len` from 40 to 45 so the longest form the regex accepts (`0000:0000:0000:0000:0000:ffff:192.168.100.200`) fits. [#1769](https://github.com/ocsf/ocsf-schema/pull/1769)
1. Moved the literal `-` to the end of the `email_t` local-part character class. As `+-/` it formed a range that also admitted a comma, so `a,b@example.com` validated. [#1769](https://github.com/ocsf/ocsf-schema/pull/1769)
1. Widened the `datetime_t` regex to accept a space between the date and the time, as RFC 3339 section 5.6 permits and as the type's own `2024-09-10 23:20:50.520789Z` example uses. [#1769](https://github.com/ocsf/ocsf-schema/pull/1769)
1. Corrected the `uuid_t` description example, which had 11 hex digits in its last group and failed its own regex. Fixed the `file_hast_t` typo in `file_hash_t` and a repeated "For example:" in `file_path_t`. [#1768](https://github.com/ocsf/ocsf-schema/pull/1768)
1. Corrected the `type_uid` example in the `observable` object: Network Activity is class_uid 4001 (type_uid 400101), not 3001. [#1768](https://github.com/ocsf/ocsf-schema/pull/1768)

### Deprecated

### Breaking changes

### Misc
  1. Compare compatibility CI with the `1.9.0` tag, align GitHub Action versions, and require a `Signed-off-by` trailer on pull request commits. Spellcheck stays a warning.
  1. Read the text block from the description-review response. `claude-sonnet-5-5` returns a thinking block first, and the reviewer crashed on `content[0].text`.
  1. Added the `@recursive` attribute annotation to the metaschema, letting an attribute declare that expanding it reenters a type already on the path, with an optional nesting `limit` and, for indirect recursion, the `path` that closes the cycle. No schema definitions are annotated yet. [#1762](https://github.com/ocsf/ocsf-schema/pull/1762)
  1. New Extension registration for Yandex Cloud. [#1759](https://github.com/ocsf/ocsf-schema/pull/1759)
  1. New Extension registration for WithSecure. [#1773](https://github.com/ocsf/ocsf-schema/pull/1773)
  1. New Extension registration for ZeroSOC. [#1785](https://github.com/ocsf/ocsf-schema/pull/1785)
