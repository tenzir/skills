---
title: "Add enrichment contexts"
canonical: https://tenzir.com/docs/tutorials/add-enrichment-contexts
source: https://tenzir.com/docs/tutorials/add-enrichment-contexts.md
section: "Docs"
---

# Add enrichment contexts

> A context is state, not code. Tenzir holds it, pipelines enrich events with it, and somebody has to keep it current. A package therefore carries no contexts: your deployment’s configuration declares them, next to the packages and pipelines that use them. This tutorial adds a GeoIP context next to the Amazon package from the earlier Development tutorials and enriches the OCSF Network Activity events from Onboard a data source with country and ASN data.

A context is state, not code. Tenzir holds it, pipelines enrich events with it, and somebody has to keep it current. A package therefore carries no contexts: your deployment’s configuration declares them, next to the packages and pipelines that use them. This tutorial adds a GeoIP context next to the Amazon package from the earlier Development tutorials and enriches the OCSF Network Activity events from [Onboard a data source](onboard-a-data-source.md) with country and ASN data.

Geo Open publishes free country and ASN data from [CIRCL](https://www.circl.lu/), the Computer Incident Response Center Luxembourg, as a new snapshot every few weeks. The two jobs stay apart. The Amazon package turns a VPC Flow Log line into OCSF, the context owns the database and its refresh, and neither one has to know about the other.

## Declare the context

Add one file to the `contexts/` folder of your configuration:

contexts/geo-open.yaml

```yaml
type: geoip
url: https://cra.circl.lu/opendata/geo-open/mmdb-country-asn/latest.mmdb
reload-interval: 1d
persist: true
```

The file name makes the context `geo-open`. Each setting does one job:

* The `url` says where the database comes from. The context downloads it right after the deploy, and enrichment waits for that first download.
* The `reload-interval` checks the source once a day and replaces the database when CIRCL has published a newer one. A failed download keeps the database the context already holds, so enrichment never stalls on the network.
* The `persist` setting keeps a copy of the database, so that a restart doesn’t download it again.

The reference for [context files](../reference/contexts.md#geoip-database) lists every GeoIP setting.

Geo Open distributes a precompiled MMDB file, which the GeoIP context stores as it is. The file already encodes IP networks, country fields, and ASN fields, so it *is* the context value, and the GeoIP context needs the file itself to match longest prefixes. Decoding it into one event per network and rebuilding a lookup table would be slower and less accurate. That is also why a GeoIP context takes no updates from pipelines.

Other context types work the other way around. A `lookup-table` context has no precompiled file, so a pipeline shapes each entry and hands a stable key to `context_update`:

pipelines/update-assets.tql

```tql
every 1h {
  from_http "https://inventory.example.net/assets.json" {
    read_json
  }
}
asset = {
  uid: move id,
  owner: move team,
  environment: move environment,
}
context_update "assets", key=ip, value=asset
```

That pipeline needs its own context file, `contexts/assets.yaml` with `type: lookup-table`.

## Choose the source

The URL lives in the context file, where whoever runs the deployment reads it and changes it with one line. Point it at a pinned snapshot for reproducible results, or at an internal mirror when the deployment can’t reach the internet. A `file://` URL loads a database from the deployment’s own disk:

contexts/geo-open.yaml

```yaml
type: geoip
url: https://cra.circl.lu/opendata/geo-open/mmdb-country-asn/2025-12-03-GeoOpen-Country-ASN.mmdb
persist: true
```

A pinned snapshot never changes, so this version drops the `reload-interval`. Changing the `url` replaces the context on the next deploy, which then loads the database from the new source right away.

## Enrich events

Apply the context to both endpoints of an OCSF Network Activity event, after the Amazon package has mapped it:

pipelines/enrich-ocsf-geo.tql

```tql
subscribe "ocsf"
where category_uid == 4
context_enrich "geo-open", key=src_endpoint?.ip, into=src_endpoint.geo
context_enrich "geo-open", key=dst_endpoint?.ip, into=dst_endpoint.geo
publish "ocsf-geo"
```

A miss writes `null` into the target field. The `?` on the key keeps that silent when an event has only one endpoint IP, which happens often enough that a warning per event would drown out real ones.

## Deploy and verify

Your configuration now holds the package, the context, and the pipeline:

* contexts/

  * geo-open.yaml

* packages/

  * amazon/

    * …

* pipelines/

  * enrich-ocsf-geo.tql

Deploy it, then run a pipeline that enriches an address you know:

```tql
from {ip: 1.1.1.1}
context_enrich "geo-open", key=ip, into=geo
where geo? != null
```

The pipeline returns the event once the database has loaded. An empty result means that the download failed, and the deployment’s logs say why.

## See it end to end

With the configuration deployed, one pipeline takes a raw VPC Flow Log line to a geolocated OCSF event. Start from the line, which describes a host talking to a public DNS resolver:

```text
2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 8.8.8.8 51514 53 17 2 148 1767225600 1767225660 ACCEPT OK
```

The Amazon package turns it into OCSF, and the context adds data to both endpoints:

```tql
from {
  message: "2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 8.8.8.8 51514 53 17 2 148 1767225600 1767225660 ACCEPT OK",
}
amazon::vpc_flow::ocsf::normalize message
context_enrich "geo-open", key=src_endpoint?.ip, into=src_endpoint.geo
context_enrich "geo-open", key=dst_endpoint?.ip, into=dst_endpoint.geo
```

The result carries the mapped event plus the two enrichments, highlighted below:

```tql
{
  metadata: {version: "1.9.0", product: {name: "Amazon VPC", vendor_name: "AWS"}},
  time: 2026-01-01T00:00:00Z,
  category_uid: 4,
  class_uid: 4001,
  activity_id: 6,
  src_endpoint: {
    ip: 10.0.1.10,
    port: 51514,
    geo: null,
  },
  dst_endpoint: {
    ip: 8.8.8.8,
    port: 53,
    geo: {
      country: {
        iso_code: "US",
        AutonomousSystemNumber: "15169",
        AutonomousSystemOrganization: "GOOGLE",
      },
    },
  },
  traffic: {bytes: 148, packets: 2},
  raw_data: "2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 8.8.8.8 …",
}
```

Everything else came from the Amazon package. The private source address shows the miss case: Geo Open has no entry for `10.0.1.10`, so that enrichment adds `null` and the pipeline continues.

The shape under `geo` comes from the MMDB rather than from OCSF, which is why it sits under a field of its own. Mapping it into `src_endpoint.location` and `src_endpoint.autonomous_system`, for which OCSF has attributes, is a separate decision that belongs to whoever consumes the events.

A package and a context file now cover the path from an opaque line to a geolocated OCSF event, and either one can change without touching the other. Return to [Onboard a data source](onboard-a-data-source.md) for the parsing, mapping, and packaging contracts that produced those events.
