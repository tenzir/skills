---
title: "Use lookup tables"
description: "Store reference data in lookup tables and apply it to OCSF events"
canonical: https://tenzir.com/docs/guides/enrich/use-lookup-tables
source: https://tenzir.com/docs/guides/enrich/use-lookup-tables.md
section: "Docs"
---

# Use lookup tables

> Store reference data in lookup tables and apply it to OCSF events

This guide shows you how to use lookup tables in Tenzir to store reference data and apply it to OCSF events. Use lookup tables when you have data keyed by an event value, such as a user ID, hostname, IP address, subnet, file hash, or cloud resource ID.

A [lookup table](../../explanations/enrichment.md#lookup-table) is a Tenzir context that stores key-value mappings. Pipelines update the table, and other pipelines query it with [`context_enrich`](../../reference/operators/context_enrich.md). This guide covers the basic lookup table lifecycle first, then shows where enrichment results should land in OCSF events. Start with the standard `enrichments` array when the extra data is general context. When the enrichment result describes a specific OCSF object, enrich that object instead.

## Set up lookup tables

Declare each lookup table as a file in the `contexts/` folder of your deployment’s configuration:

contexts/user\_roles.yaml

```yaml
type: lookup-table
persist-interval: 5min
```

The file name becomes the table name, and the `persist-interval` keeps the table’s entries across restarts. Deploying the configuration creates the empty table. You can also select **Add context** in the platform, which writes the file for you. Our guide on [declaring contexts](declare-contexts.md) covers the lifecycle in detail.

Each example below uses its own table, such as `users` or `network_segments`. Declare a file for each table you use.

## Add entries

Use [`context_update`](../../reference/operators/context_update.md) to add or replace lookup-table entries. This example stores user role metadata keyed by the OCSF user UID:

```tql
from {
  user_uid: "S-1-5-21-1001",
  role: "SOC analyst",
  department: "Security Operations",
  privileges: ["investigate", "contain"],
}
context_update "user_roles", key=user_uid, value={
  role: role,
  department: department,
  privileges: privileges,
}
```

The value can be any structured TQL value. Prefer values that are already close to the OCSF shape you want to produce later. This reduces reshaping in high-volume enrichment pipelines.

## Apply lookup tables to OCSF events

OCSF gives you several places to put enrichment results. Choose the destination based on what the lookup-table value describes.

### Enrich into `enrichments`

The most general OCSF enrichment target is the base event’s `enrichments` array. Use it when the enrichment result adds useful context but doesn’t belong to a more specific OCSF object.

The following pipeline enriches an OCSF Authentication event with user role context:

```tql
from {
  time: 2024-08-22T09:12:34,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  user: {
    uid: "S-1-5-21-1001",
    name: "alice",
  },
  service: {
    name: "vpn",
  },
  enrichments: [],
}
context_enrich "user_roles",
  key=user.uid,
  into=enrichments,
  mode="append",
  format="ocsf"
```

```tql
{
  time: 2024-08-22T09:12:34,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  user: {
    uid: "S-1-5-21-1001",
    name: "alice",
  },
  service: {
    name: "vpn",
  },
  enrichments: [{
    created_time: 2024-08-22T09:12:35.069981,
    data: {
      role: "SOC analyst",
      department: "Security Operations",
      privileges: ["investigate", "contain"],
    },
    name: "user.uid",
    provider: "user_roles",
    value: "S-1-5-21-1001",
  }],
}
```

The `format="ocsf"` option wraps the enrichment result as an OCSF `enrichment` object with the enrichment result in `data` and the context name in `provider`. It does not infer an enrichment `type`. The `mode="append"` option appends the result to the existing `enrichments` list instead of overwriting it.

### Choose semantic OCSF fields

Use `enrichments` as the baseline, not as the only destination. If the enrichment result describes an OCSF object, write the result into that object’s semantic fields. This keeps the event easier to query and lets downstream tools use the standard schema.

For example, user inventory belongs in `user`. Create the lookup table in a separate setup pipeline before you populate it:

```tql
from {
  uid: "S-1-5-21-1001",
  name: "alice",
  display_name: "Alice Nguyen",
  email_addr: "alice@example.com",
  type_id: 2,
  type: "Admin",
  has_mfa: true,
}
context_update "users", key=uid
```

Enrich an Authentication event with the source user ID from `unmapped` and writing the result directly into the OCSF `user` object:

```tql
from {
  time: 2024-08-22T09:12:34,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  service: {
    name: "vpn",
  },
  unmapped: {
    user_uid: "S-1-5-21-1001",
  },
}
context_enrich "users", key=unmapped.user_uid, into=user
```

```tql
{
  time: 2024-08-22T09:12:34,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  service: {
    name: "vpn",
  },
  unmapped: {
    user_uid: "S-1-5-21-1001",
  },
  user: {
    uid: "S-1-5-21-1001",
    name: "alice",
    display_name: "Alice Nguyen",
    email_addr: "alice@example.com",
    type_id: 2,
    type: "Admin",
    has_mfa: true,
  },
}
```

This pattern is the foundation for the OCSF-specific enrichment guides:

* [Enrich with asset inventory](enrich-with-asset-inventory.md) shows how to enrich `src_endpoint`, `dst_endpoint`, `device`, and related asset fields.
* [Enrich with threat intel](enrich-with-threat-intel.md) shows how to enrich `enrichments`, `observables`, `osint`, and related reputation fields.

### Use subnet keys

Lookup tables support longest-prefix matching when the stored keys are `subnet` values and the enrichment key is an `ip` value. This is useful for asset inventory, network ownership, and routing context.

Populate a pre-created subnet table:

```tql
from {subnet: 10.0.0.0/22, zone: "corp", owner: {name: "platform"}},
     {subnet: 10.0.0.0/24, zone: "production", owner: {name: "web-platform"}},
     {subnet: 10.0.1.0/24, zone: "database", owner: {name: "data-platform"}}
context_update "network_segments", key=subnet, value={
  subnet_uid: subnet,
  zone: zone,
  owner: owner,
}
```

Enrich with endpoint IP addresses from `unmapped` and write the matched values directly into the OCSF endpoint objects:

```tql
from {
  time: 2024-08-22T09:13:01,
  category_uid: 4,
  class_uid: 4001,
  activity_id: 6,
  type_uid: 400106,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  unmapped: {
    src_ip: 10.0.0.15,
    dst_ip: 10.0.1.20,
  },
}
context_enrich "network_segments", key=unmapped.src_ip, into=src_endpoint
context_enrich "network_segments", key=unmapped.dst_ip, into=dst_endpoint
```

```tql
{
  time: 2024-08-22T09:13:01,
  category_uid: 4,
  class_uid: 4001,
  activity_id: 6,
  type_uid: 400106,
  severity_id: 1,
  metadata: {
    version: "1.9.0",
  },
  unmapped: {
    src_ip: 10.0.0.15,
    dst_ip: 10.0.1.20,
  },
  src_endpoint: {
    subnet_uid: 10.0.0.0/24,
    zone: "production",
    owner: {
      name: "web-platform",
    },
  },
  dst_endpoint: {
    subnet_uid: 10.0.1.0/24,
    zone: "database",
    owner: {
      name: "data-platform",
    },
  },
}
```

The IP address `10.0.0.15` matches `10.0.0.0/24` instead of `10.0.0.0/22` because `/24` is the more specific prefix.

## Use compound keys

Use record values as keys when an enrichment depends on more than one field. This example populates a pre-created access policy table keyed by a source zone and destination zone:

```tql
from {
  key: {
    src_zone: "internet",
    dst_zone: "dmz",
  },
  action: "allow",
  reason: "Public web tier",
},
{
  key: {
    src_zone: "internet",
    dst_zone: "database",
  },
  action: "deny",
  reason: "Database tier is not internet-facing",
}
context_update "access_policies", key=key, value={
  action: action,
  reason: reason,
}
```

Use the same record shape for enrichment:

```tql
from {
  src_endpoint: {
    zone: "internet",
  },
  dst_endpoint: {
    zone: "dmz",
  },
}
context_enrich "access_policies",
  key={
    src_zone: src_endpoint.zone,
    dst_zone: dst_endpoint.zone,
  },
  into=access_policy
```

```tql
{
  src_endpoint: {
    zone: "internet",
  },
  dst_endpoint: {
    zone: "dmz",
  },
  access_policy: {
    action: "allow",
    reason: "Public web tier",
  },
}
```

Compound keys keep the enrichment deterministic when a single event field isn’t selective enough.

## Expire stale entries

Set timeouts in the table’s context file when it contains data with a known lifetime, such as active sessions, short-lived indicators, or temporary allowlist entries:

contexts/active\_indicators.yaml

```yaml
type: lookup-table
create-timeout: 7d
write-timeout: 24h
```

Then update the table as usual:

```tql
from {
  indicator: "malicious.example",
  confidence: 90,
  source: "ThreatFeed",
}
context_update "active_indicators",
  key=indicator,
  value={
    confidence: confidence,
    source: source,
    updated_time: now(),
  }
```

The `create-timeout` setting removes an entry after a fixed lifetime, the `write-timeout` setting removes it if it isn’t refreshed, and the `read-timeout` setting removes it if no enrichment uses it. The timeouts apply to every entry of the table, and a changed timeout also applies to the entries the table holds already.

## See Also

* [Declare contexts](declare-contexts.md)
* [Enrich with asset inventory](enrich-with-asset-inventory.md)
* [Enrich with threat intel](enrich-with-threat-intel.md)
* [Enrich events with AI](enrich-events-with-ai.md)
* [Enrichment](../../explanations/enrichment.md)
