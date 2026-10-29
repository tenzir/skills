# OCSF changelog: [v1.2.0] - April 23rd, 2024

### Added
* #### Categories
    n/a
* #### Event Classes
    1. Added `Data Security Finding` event class. [#953](https://github.com/ocsf/ocsf-schema/pull/953)
    2. Added `File Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    3. Added `Folder Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    4. Added `Group Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    5. Added `Job Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    6. Added `Kernel Object Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    7. Added `Module Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    8. Added `Network Connection Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    9. Added `Networks Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    10. Added `Peripheral Device Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    11. Added `Prefetch Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    12. Added `Process Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    13. Added `Registry Key Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    14. Added `Registry Value Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    15. Added `Service Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    16. Added `Session Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    17. Added `User Query` event class. [#967](https://github.com/ocsf/ocsf-schema/pull/967)
    18. Added `Tunnel Activity` event class. [#1012](https://github.com/ocsf/ocsf-schema/pull/1012)

* #### Profiles
    1. Added `data_classification` profile. [#998](https://github.com/ocsf/ocsf-schema/pull/998)

* #### Objects
    1. Added `auth_factor` object. [#949](https://github.com/ocsf/ocsf-schema/pull/949)
    2. Added `data_security` object. [#953](https://github.com/ocsf/ocsf-schema/pull/953)
    3. Added `autonomous_system` object. [#978](https://github.com/ocsf/ocsf-schema/pull/978)
    4. Added `agent` object. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    5. Added `data_classification` object. [#998](https://github.com/ocsf/ocsf-schema/pull/998)

* #### Observables
    1. Added `port_t` `subnet_t` `cmd_line` `country` `pid` `cwe.uid` `cve.uid` `user_agent` enum items. [#1035](https://github.com/ocsf/ocsf-schema/pull/1035)

* #### Platform Extensions
    n/a

### Improved
* #### Categories
* #### Event Classes
    1. Added `auth_factors` array to Authentication event class. [#949](https://github.com/ocsf/ocsf-schema/pull/949)
    2. Modified all classes such that primary attributes are at least recommended. [#974](https://github.com/ocsf/ocsf-schema/pull/974)
    3. Added `src_endpoint`, `http_request` attributes to all IAM category classes. [#976](https://github.com/ocsf/ocsf-schema/pull/976)
    4. Added `autonomous_system` to `network_endpoint` objects. [#978](https://github.com/ocsf/ocsf-schema/pull/978)
    5. Added `List`, `Encrypt` and `Decrypt` activities to `datastore` event class. [#989](https://github.com/ocsf/ocsf-schema/pull/989)
    6. Added `file` attribute to `http`, `rdp`, `ssh`, and `ftp` event classes. [#985](https://github.com/ocsf/ocsf-schema/pull/985)
    7. Added a `Preauth` `activity_id` to the `Authentication` class. [#1018](https://github.com/ocsf/ocsf-schema/pull/1018)
    8. Added the `Security Control` profile to the `Datastore Activity` class. [#1030](https://github.com/ocsf/ocsf-schema/pull/1030)
    9. Added `risk_details` to Detection Finding. [#1032](https://github.com/ocsf/ocsf-schema/pull/1032)

* #### Profiles
    n/a
* #### Objects
    1. Expanded `type_id` enum in `analytic` object to account for more use-cases: [#953](https://github.com/ocsf/ocsf-schema/pull/953)
        - `5 - Fingerprinting`
        - `6 - Tagging`
        - `7 - Keyword Match`
        - `8 - Regular Expressions`
        - `9 - Exact Data Match`
        - `10 - Partial Data Match`
        - `11 - Indexed Data Match`
    2. Added `lat`, `long`, `geohash` attributes to `location` object. [#971](https://github.com/ocsf/ocsf-schema/pull/971).
    3. Added `risk_score`, `risk_level_id`, `risk_level` to `user` object. Issue [#972](https://github.com/ocsf/ocsf-schema/pull/972).
    4. Added `app_name`, `app_uid` to `actor` object.  Issue [#966](https://github.com/ocsf/ocsf-schema/pull/966), PR [#979](https://github.com/ocsf/ocsf-schema/pull/979).
    5. Added `container`, `database`, `databucket` to the `evidences` object. [#984](https://github.com/ocsf/ocsf-schema/pull/984)
    6. Added `owner` to `endpoint` object. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    7. Added `is_applied` Boolean attribute to `policy` object. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    8. Added `agent_list` as an array of `agent` objects. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    9. Added `policies` object as an array of `policy` objects. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    10. Added `agent_list` to `endpoint` object. [#987](https://github.com/ocsf/ocsf-schema/pull/987)
    11. Added `labels` to the `Account` object. [#1028](https://github.com/ocsf/ocsf-schema/pull/1028)
    12. Added `data_classification` profile to `database`, `databucket`, `email`, `file`, `metadata`, `product`, `resource_details` and `web_resource` objects. [#998](https://github.com/ocsf/ocsf-schema/pull/998)

* #### Platform Extensions
    n/a

### Bugfixes
1. Changed datatype of `priority` attribute, from `integer_t` to `string_t` [#959](https://github.com/ocsf/ocsf-schema/pull/959)
2. Extended `email_t` regexp to allow characters from RFC5322 before @.
3. Updated `logon_type_id` enum to include `0` as `Unknown`. Added enum item `1` as `System`. [#1055](https://github.com/ocsf/ocsf-schema/pull/1055)

### Deprecated
1. Deprecated `coordinates` attribute in favor of specific `lat`, `long` attributes. [#971](https://github.com/ocsf/ocsf-schema/pull/971)
2. Deprecated `invoked_by` attribute in the `Actor` object in favor of `app_name`. [#979](https://github.com/ocsf/ocsf-schema/pull/979).

### Breaking changes
n/a

### Misc
1. New Extension registration for Sedara. [#951](https://github.com/ocsf/ocsf-schema/pull/951)
2. Corrected punctuation for the `transmit_time` attribute. [#1001](https://github.com/ocsf/ocsf-schema/pull/1001)
3. New ways to define observables in the metaschema. [#982](https://github.com/ocsf/ocsf-schema/pull/982) and [#993](https://github.com/ocsf/ocsf-schema/pull/993)
    * (Current) Dictionary types using `observable` property in dictionary types. This allows defining all occurrences of attributes of this type as an observable.
    * (Current) Objects using top-level `observable` property. This allows defining all occurrences attributes whose type is this object as an observable.
    * _**(New)**_ Dictionary attributes using `observable` property in attribute. This allows defining all occurrences of this attribute as an observable.
    * _**(New)**_ Object-specific attributes using `observable` property class's attributes. This allows defining object attributes as observables _only_ within instances of this specific object.
    * _**(New)**_ Event class-specific attributes using `observable` property class's attributes. This allows defining class attributes as observables _only_ within instances of this specific class.
    * _**(New)**_ Event class-specific attribute _paths_ using top-level `observables` property. The `observables` property holds an object mapping from an dotted attribute path to an observable `type_id`. This allows defining an observables _only_ within instances of this specific class, and only for the attributes at these paths, even for attributes that are within nested objects and arrays. This can also be used for top-level class attributes, which can be more convenient that defining a class attribute observable for classes that extend another, but don't otherwise change a attribute definition.
4. Metaschema improvements. [#993](https://github.com/ocsf/ocsf-schema/pull/993)
    * Detect unexpected top-level properties in object and event class definitions. This was added at this point to detect invalid observable definitions: invalid `observable` property in event classes, and invalid `observables` property in objects.
    * Remove hard-coded list of categories from `metaschema/categories.schema.json`, leaving this to the `ocsf-validator`. This change makes testing with alternate schemas that may add extra categories easier, as well as making it possible to validate private extensions that contain new categories.
5. Metaschema error reporting [#1027](https://github.com/ocsf/ocsf-schema/pull/1027)
    * Updated the definition of `object` and `event` so that metaschema errors reported by the validator with nested properties correctly attribute the error to the property with the error, rather than the top-level class.
