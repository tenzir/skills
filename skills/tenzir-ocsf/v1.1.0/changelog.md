# OCSF changelog: [v1.1.0] - January 25th, 2024

### Added
* #### Categories
    `n/a`
* #### Event Classes
    1. Added `User Inventory Info` event class. [#667](https://github.com/ocsf/ocsf-schema/pull/667)
    2. Added `Vulnerability Finding` event class. [#698](https://github.com/ocsf/ocsf-schema/pull/698)
    3. Added `NTP Activity` event class [#705](https://github.com/ocsf/ocsf-schema/pull/705)
    4. Added `OS Patch State` event class. [#746](https://github.com/ocsf/ocsf-schema/pull/746)
    5. Added `Datastore Activity` event class 6005. [#874](https://github.com/ocsf/ocsf-schema/pull/874)
    6. Added `Detection Finding` event class. [#877](https://github.com/ocsf/ocsf-schema/pull/877)
    7. Added `Incident Finding` event class. [#903](https://github.com/ocsf/ocsf-schema/pull/903)
    8. Added `Device Config Sate Change` event class. [#914](https://github.com/ocsf/ocsf-schema/pull/914)
    9. Added `Scan Activity` event class. [#915](https://github.com/ocsf/ocsf-schema/pull/915)
    10. Added `File Hosting Activity` event class. [#917](https://github.com/ocsf/ocsf-schema/pull/917)

* #### Profiles
	1. Added `Network Proxy` Profile for the `Network Activity` and `Application Activity` classes. [#705](https://github.com/ocsf/ocsf-schema/pull/705)
    2. Added `Load Balancer` Profile for the Network Activity classes. [#897](https://github.com/ocsf/ocsf-schema/pull/897)

* #### Objects
    1. Added new `cwe` object to `cve` and `vulnerability` objects. [#678](https://github.com/ocsf/ocsf-schema/pull/678)
    2. Added Firewall Rule object. [#685](https://github.com/ocsf/ocsf-schema/pull/685)
    3. Added new `kb_article` object to house Knowledgebase Article info. [#709](https://github.com/ocsf/ocsf-schema/pull/709) [#862](https://github.com/ocsf/ocsf-schema/pull/862) [#924](https://github.com/ocsf/ocsf-schema/pull/924)
    4. Added new `epss` object to the `cve` object. [#741](https://github.com/ocsf/ocsf-schema/pull/741)

### Improved
* #### Categories
    1. Improved Findings Category, with new and domain specific event classes (Vulnerability Finding, Compliance Finding, Detection Finding, Incident Finding), description updates across the board. [#895](https://github.com/ocsf/ocsf-schema/pull/895) [#907](https://github.com/ocsf/ocsf-schema/pull/907) [#903](https://github.com/ocsf/ocsf-schema/pull/903) [#698](https://github.com/ocsf/ocsf-schema/pull/698) [#718](https://github.com/ocsf/ocsf-schema/pull/718)

* #### Event Classes
    1. Added `MFA Enable` and `Disable` to `activity_id` to the Account Change event class. [#724](https://github.com/ocsf/ocsf-schema/pull/724)
    2. Added `Service Ticket Renew` to `activity_id` of the Authentication event class. [#765](https://github.com/ocsf/ocsf-schema/pull/765)
    3. Added `url` attribute to Network Activity event class. [#857](https://github.com/ocsf/ocsf-schema/pull/857)
    4. Added `http_request`, `http_response`, `tls` attributes, `network_proxy` profile to Web Resources Activity event class. [#895](https://github.com/ocsf/ocsf-schema/pull/895)
    5. Adjusted requirement of `dst_endpoint` from `required` to `recommended` in the DNS Activity event class. [#901](https://github.com/ocsf/ocsf-schema/pull/901)
    6. Added `Create` and `Delete` to `activity_id` of the Group Management event class. [#929](https://github.com/ocsf/ocsf-schema/pull/929)

* #### Profiles
    1. Improved `security_control` profile to include access control semantics, firewall properties. [#851](https://github.com/ocsf/ocsf-schema/pull/851) [#888](https://github.com/ocsf/ocsf-schema/pull/888) [#889](https://github.com/ocsf/ocsf-schema/pull/889) [#906](https://github.com/ocsf/ocsf-schema/pull/906)

* #### Objects
    1. Added `url_string` attribute to the `product` and the `web_resource` objects. [#675](https://github.com/ocsf/ocsf-schema/pull/675)
    2. Added `type` and `type_id` attributes to the `endpoint` object. [#690](https://github.com/ocsf/ocsf-schema/pull/690)
    3. Added `cwe`, `desc`, `references` and `title` to `cve` object. [#698](https://github.com/ocsf/ocsf-schema/pull/698)
    4. Added `affected_package` object and`affected_packages` attribute to `vulnerability` object. [#698](https://github.com/ocsf/ocsf-schema/pull/698)
    5. Added `purl` to `package` object. [#698](https://github.com/ocsf/ocsf-schema/pull/698)
    6. Added `cpe_name` attribute to the `product` and os objects. [#713](https://github.com/ocsf/ocsf-schema/pull/713) [#731](https://github.com/ocsf/ocsf-schema/pull/731)
    7. Added `container` and `data` to `response` and `request` objects. [#738](https://github.com/ocsf/ocsf-schema/pull/738)
    8. Added `group` to the `api` object. [#738](https://github.com/ocsf/ocsf-schema/pull/738)
    9. Added `namespace` to the `resource_details` object. [#738](https://github.com/ocsf/ocsf-schema/pull/738)
    10. Added `log_level` to the `metadata` object. [#738](https://github.com/ocsf/ocsf-schema/pull/738)
    11. Added `length` to the `http_request` object. [#768](https://github.com/ocsf/ocsf-schema/pull/768)
    12. Added `is_exploit_available` to the `vulnerability` object. [#777](https://github.com/ocsf/ocsf-schema/pull/777)
    13. Added `domain` attribute to the `group` object. [#871](https://github.com/ocsf/ocsf-schema/pull/871)
    14. Adjusted attribute requirements in `dns_query`, `dns_answer` objects. [#879](https://github.com/ocsf/ocsf-schema/pull/879)
    15. Added firewall, router, switch, hub to endpoint `type_id` enum. [#921](https://github.com/ocsf/ocsf-schema/pull/921)
    16. Added `is_vpn` to the `session` object. [#922](https://github.com/ocsf/ocsf-schema/pull/922)
    17. Added `state` to `network_connection_info` object. [#932](https://github.com/ocsf/ocsf-schema/pull/932)
    18. Added `community_uid` to `network_connection_info` object. [#1202](https://github.com/ocsf/ocsf-schema/pull/1202)

### Bugfixes
`n/a`

### Deprecated
1. Deprecated `cwe_uid` and `cwe_url` attributes and removed from `cve` object. [#678](https://github.com/ocsf/ocsf-schema/pull/678)
2. Deprecated `http_status` attribute from `HTTP Activity` event to be replaced by `http_response.code`. [#767](https://github.com/ocsf/ocsf-schema/pull/767)
3. Deprecated `finding` object in favor of `finding_info` object. [#769](https://github.com/ocsf/ocsf-schema/pull/769)
4. Deprecated `proxy` attribute from the dictionary, in favor of `Network Proxy` profile. [#856](https://github.com/ocsf/ocsf-schema/pull/856)
5. Deprecated `group_name` attribute. [#873](https://github.com/ocsf/ocsf-schema/pull/873)
6. Deprecated `Security Finding` class to be replaced by the new specific classes according to the use-case: `Vulnerability Finding`, `Compliance Finding`, `Detection Finding`, `Incident Finding`. [#877](https://github.com/ocsf/ocsf-schema/pull/877)
7. Deprecated `Web Resources Access Activity` event class. [#890](https://github.com/ocsf/ocsf-schema/pull/890)
8. Deprecated `Network File Activity` event class in favor of `File Hosting Activity `[#917](https://github.com/ocsf/ocsf-schema/pull/917)
9. Deprecated `extension_list` in TLS object in favor of `tls_extension_list`. [#936](https://github.com/ocsf/ocsf-schema/pull/936)

### Breaking changes
`n/a`

### Misc
1. New Extension registration for SentinelOne. [#706](https://github.com/ocsf/ocsf-schema/pull/706)
2. Added json-schema based metaschema validation to ensure correctness, consistency of the JSON definitions. [#736](https://github.com/ocsf/ocsf-schema/pull/736) [#830](https://github.com/ocsf/ocsf-schema/pull/830) [#867](https://github.com/ocsf/ocsf-schema/pull/867) [#892](https://github.com/ocsf/ocsf-schema/pull/892)
3. Increased `max_len` for `subnet_t` type from `40` to `42`. [#745](https://github.com/ocsf/ocsf-schema/pull/745)
4. Improved the regex for `ip_t` type. [#745](https://github.com/ocsf/ocsf-schema/pull/745)
5. Updated the `datetime_t` validation regex to enable validation of timestamps, and to ensure that timestamps not matching `RFC-3339` are not considered valid. [#753](https://github.com/ocsf/ocsf-schema/pull/753)
6. Added version information to the native extensions. [#881](https://github.com/ocsf/ocsf-schema/pull/881)
7. Updated caption and description of Observable type - `File Hash` to read `Hash`. [#900](https://github.com/ocsf/ocsf-schema/pull/900)
8. New Extension registration for DataBee. [#912](https://github.com/ocsf/ocsf-schema/pull/912)
9. Changed data-type of `type_uid` to `long_t` from `int_t`. [#928](https://github.com/ocsf/ocsf-schema/pull/928)
