---
title: "isMalicious integration"
description: "Load STIX threat intelligence over TAXII into a local lookup table and enrich OCSF events in the stream."
canonical: https://tenzir.com/integrations/ismalicious
source: https://tenzir.com/integrations/ismalicious.md
section: "Integrations"
---

# isMalicious integration

> Load STIX threat intelligence over TAXII into a local lookup table and enrich OCSF events in the stream.

The European threat intelligence provider [isMalicious](https://ismalicious.com) publishes reputation with risk, evidence, and provenance for IP addresses, domains, URLs, and file hashes. Its feeds are STIX 2.1 Indicators served over TAXII 2.1, so you can load them with open standards end to end.

The isMalicious package builds on our generic STIX package: it fetches TAXII collections, maps each STIX Indicator to OCSF [OSINT Inventory Info](https://schema.ocsf.io/classes/osint_inventory_info), and loads the result into a local lookup table. Tenzir then enriches OCSF network and DNS events in the stream without an API call per event.

## What you can do

* Load isMalicious TAXII collections into a local lookup table on a schedule.
* Keep the upstream sources, risk score, validity, and, when supplied, confidence of every indicator in OCSF.
* Remove revoked and expired indicators from the lookup table.
* Enrich OCSF network and DNS events while they are still moving.
* Route high-score matches to the alert path and keep the full stream for investigation.
* Look up a single indicator on demand during an investigation.

## Prerequisites

To use this integration, you need:

* An isMalicious Pro or Enterprise plan, which includes TAXII access. You can [create your isMalicious account](https://ismalicious.com/auth/register).
* An isMalicious API key and secret. Store the Base64 encoding of `apiKey:apiSecret` as the [secret](../explanations/secrets.md) `ISMALICIOUS_API_CREDENTIAL`.
* The `ismalicious`, `stix`, and `tenzir` packages from the [Tenzir Library](https://app.tenzir.com/library).

## Load the feeds into a lookup table

The isMalicious TAXII server offers twelve collections, including `malicious-domains`, `malicious-ips`, `malicious-urls`, `malicious-file-hashes`, `c2-indicators`, `phishing-indicators`, and `ransomware-iocs`. Start with the domain and IP collections, and validate the indicator types and mappings of other collections before you add them.

Keep the lookup table current with two pipelines. The first walks both collections daily and reloads the active indicators:

```tql
// Runs at 07:00 in the node's local time zone. The provider reload starts at
// 02:00 UTC, so check this time against when the reload actually completes.
cron "0 0 7 * * *" {
  from {collection: "malicious-domains"}, {collection: "malicious-ips"}
  // Walk one collection at a time to stay within the API rate limit.
  each parallel=1 {
    ismalicious::feed $this.collection,
      api_credential=secret("ISMALICIOUS_API_CREDENTIAL"),
      params={min_score: 60}
  }
  ismalicious::ocsf::normalize
  tenzir::osint::update_context max_age=30d
}
```

The second polls between walks with `added_after`, which delivers new indicators and revocations. Only polls with `added_after` deliver revocations, and isMalicious keeps them for 30 days. Each poll looks back a full day, so a few failed polls lose nothing:

```tql
cron "0 0 1,13,19 * * *" {
  from {collection: "malicious-domains"}, {collection: "malicious-ips"}
  each parallel=1 {
    ismalicious::feed $this.collection,
      api_credential=secret("ISMALICIOUS_API_CREDENTIAL"),
      added_after=now() - 1d,
      params={min_score: 60}
  }
  ismalicious::ocsf::normalize
  tenzir::osint::update_context max_age=30d
}
```

The collections hold millions of indicators, and the operator pages at your plan’s per-minute burst limit. TAXII collection pulls do not consume your monthly reputation-check quota. The `min_score` parameter keeps indicators with a risk score of at least the given value, but the server applies it after scanning the whole collection, and so does `added_after`. In a walk on 9 October 2026, `min_score: 70` loaded 39,879 domains and 619 IPs in 77 minutes on a Pro plan.

Choose the threshold deliberately. Most indicators score between 20 and 39, and only a small tier scores high. A lower threshold loads more context for investigations, while a higher one keeps the table focused on indicators you want to alert on. The threshold filters by risk, not by confidence.

## Keep evidence and provenance

The mapping keeps the evidence behind each indicator in standard OCSF fields instead of collapsing it into a single verdict:

| STIX Indicator              | OCSF `osint`                    |
| --------------------------- | ------------------------------- |
| Single-comparison `pattern` | `value`, `type_id`              |
| `external_references`       | `references`                    |
| `x_opencti_score`           | `risk_score`                    |
| `confidence`                | `confidence_id`                 |
| `valid_until`               | `expiration_time`               |
| `created`, `modified`       | `created_time`, `modified_time` |
| `id`                        | `external_uid`                  |

When isMalicious revokes an indicator, the mapped event carries the status `Removed`, and `tenzir::osint::update_context` erases the entry from the lookup table. Updates apply page by page, so an interrupted walk leaves the pages it already applied. Tenzir also honors expiry: an indicator whose `expiration_time` has passed no longer matches and leaves the table on the next update. Independently, each entry expires from the lookup table after `max_age`, 30 days by default.

## Enrich events in the stream

With the lookup table in place, add enrichment after your pipeline maps events to OCSF and before it sends them to downstream tools:

```tql
tenzir::osint::enrich
```

The operator matches source and destination IP addresses of network events and the queried hostname of DNS Activity events, and appends every match to the `osint` array. An event without an `osint` match is unknown to the feed, not safe.

## Route by risk score

In your alert path, keep events with at least one high-score match:

```tql
where osint?.map(x => x.risk_score >= 70).any()
```

Keep an unfiltered copy of the full enriched stream, including low-score matches, in a lake for investigations and retrospective hunts.

Tune the threshold in a proof of value. Count how many events each tier routes and how many of the alerted matches analysts confirm.

## Look up a single indicator

During an investigation, query the isMalicious API for one indicator:

```tql
ismalicious::check query="198.51.100.7",
  api_credential=secret("ISMALICIOUS_API_CREDENTIAL")
```

Read `evidence.verdict` together with `evidence.reasons` and `evidence.contradictorySignals`. A response with `malicious: false` does not prove that an indicator is safe: unknown hashes and context-only sources yield the verdict `unknown`. Each individual API lookup counts against your monthly reputation-check quota, so use the lookup table for high-volume streams.

## Use other TAXII sources

The `stix` package works with other TAXII servers too. Point `stix::taxii::fetch` at a collection, keep the `indicator` objects, and normalize them to the same OCSF shape after validating their indicator types and mappings:

```tql
every 1d {
  stix::taxii::fetch "https://taxii.example.com/api-root/collections/indicators/objects/",
    headers={Authorization: f"Basic {secret("TAXII_CREDENTIAL")}"}
  where type == "indicator"
  stix::ocsf::normalize
  tenzir::osint::update_context max_age=30d
}
```

Indicators from different providers then share one lookup table and one enrichment pipeline.

## See also

* [Enrich with threat intel](../guides/enrich/enrich-with-threat-intel.md)
* [Install a package](../guides/packages/install-a-package.md)
* [Enrichment](../explanations/enrichment.md)
* [Secrets](../explanations/secrets.md)
