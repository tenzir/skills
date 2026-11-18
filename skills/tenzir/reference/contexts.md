---
title: "Contexts"
canonical: https://tenzir.com/docs/reference/contexts
source: https://tenzir.com/docs/reference/contexts.md
section: "Docs"
---

# Contexts

> A deployment declares its contexts in its configuration, one YAML file per context. This page lists what a context file may contain and what a deploy does with it. Our explanation of what a deployment runs describes the model behind it.

A deployment declares its [contexts](../explanations/enrichment.md) in its configuration, one YAML file per context. This page lists what a context file may contain and what a deploy does with it. Our explanation of [what a deployment runs](../explanations/deployment.md#what-a-deployment-runs) describes the model behind it.

## Files

Every file in the configuration’s `contexts/` folder declares one context. A file must sit directly in `contexts/` and end in `.yaml`. The deployment refuses the configuration for a file anywhere below `contexts/` that breaks this rule, such as `contexts/feeds/threats.yaml` or `contexts/threats.yml`, rather than ignoring it.

A file holds a YAML mapping with these keys:

| Key    | Type   | Default       | Description                                                        |
| ------ | ------ | ------------- | ------------------------------------------------------------------ |
| `type` | string | required      | The type of context: `lookup-table`, `bloom-filter`, or `geoip`.   |
| `name` | string | the file stem | The name pipelines use to refer to the context. Must not be empty. |

The other keys depend on the type and are listed under [context types](contexts.md#context-types). A key that the type doesn’t know is an error, because it would say something about the context that the deployment would silently ignore. Context files have no `description`.

Names may contain spaces. Set `name` when the name you want doesn’t make a good file name:

contexts/known-threats.yaml

```yaml
name: known threats
type: lookup-table
```

Two files that declare the same name refuse the configuration.

### Values

Durations are strings that hold a positive duration, such as `30s`, `5min`, `1h`, or `7d`. A bare number is not a duration. The files take plain YAML only: the deployment refuses tags such as `!!int`, aliases, and a key that appears twice in one mapping.

## Context types

The `type` key selects one of three types of context, each with its own settings.

### Lookup table

A lookup table, `type: lookup-table`, maps keys to values. A key of type `subnet` also matches the IP addresses within it, and where subnet keys overlap, the [longest prefix wins](../explanations/enrichment.md#1-longest-prefix-subnet-match-for-subnet-keys). Its settings are all optional:

| Key                | Type     | Default | Description                                                                                   |
| ------------------ | -------- | ------- | --------------------------------------------------------------------------------------------- |
| `persist-interval` | duration | none    | How often the table is persisted once it changed. Without it, the table lives in memory only. |
| `create-timeout`   | duration | none    | How long an entry lives after its key was first stored.                                       |
| `write-timeout`    | duration | none    | How long an entry lives after its key was last stored.                                        |
| `read-timeout`     | duration | none    | How long an entry lives after its key was last stored or used for enrichment.                 |

Without a timeout, an entry lives until the context is removed or starts over. The timeouts apply to every entry, and one that is up suffices to expire an entry. A changed timeout applies to the entries the table holds already, except that an entry that expired stays expired. A `read-timeout` that was unset before counts from the deploy that sets it. Our explanation of [per-key expiration](../explanations/enrichment.md#2-per-key-createwriteread-expiration) shows how the three timeouts combine.

contexts/active-indicators.yaml

```yaml
type: lookup-table
persist-interval: 5min
create-timeout: 30d
write-timeout: 7d
```

A lookup table takes any change to its settings in place and keeps its content.

### Bloom filter

A Bloom filter, `type: bloom-filter`, holds a set of keys in fixed space and may report a key it doesn’t hold. Our explanation of [Bloom filters](../explanations/enrichment.md#bloom-filter) shows how the two sizing settings trade space for accuracy.

| Key                | Type     | Default  | Description                                                                                                                                     |
| ------------------ | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `capacity`         | integer  | required | How many keys the filter is sized for. Must be positive.                                                                                        |
| `fp-probability`   | number   | required | How often enrichment may report a key that was never stored, while the filter holds at most `capacity` keys. Must lie strictly between 0 and 1. |
| `persist-interval` | duration | none     | How often the filter is persisted once it changed. Without it, the filter lives in memory only.                                                 |

contexts/malware-hashes.yaml

```yaml
type: bloom-filter
capacity: 10000000
fp-probability: 0.001
persist-interval: 1h
```

A filter takes its full size in memory as soon as the deploy creates it, no matter how many keys it holds: about 1.2 MB per million keys of `capacity` at an `fp-probability` of 0.01, and 1.8 MB at 0.001. The example above takes about 18 MB. A persisting filter writes the same amount to the object store.

A filter takes a change of its `persist-interval` in place. A change of `capacity` or `fp-probability` replaces it with an empty filter, because a filter cannot be resized. A filter holds its keys forever.

### GeoIP database

A GeoIP context, `type: geoip`, finds what a [MaxMind database](https://maxmind.github.io/MaxMind-DB/) says about an IP address. It loads the database from its source and takes no updates from pipelines. Our explanation of [GeoIP databases](../explanations/enrichment.md#geoip-database) describes the format and a typical use.

| Key               | Type     | Default  | Description                                                                                                                    |
| ----------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `url`             | string   | required | Where to download the database from: any URL that curl can fetch, such as one with `https://` or `file://`. Must not be empty. |
| `reload-interval` | duration | none     | How often to check the source for a newer database after the first load. Without it, the context loads the database once.      |
| `persist`         | boolean  | `false`  | Whether to keep a persisted copy of the database, so that a restart doesn’t have to download it again.                         |

contexts/geo.yaml

```yaml
type: geoip
url: https://example.com/GeoLite2-City.mmdb
reload-interval: 1d
persist: true
```

The context loads the database right after the deploy. Enrichment waits for that first load and adds `null` if it failed. A later load that fails keeps the database the context holds. A GeoIP context has no `persist-interval`: with `persist`, it persists after each load that changed the database.

A GeoIP context takes a change of `reload-interval` or `persist` in place. A change of `url` replaces it, so that it loads from the new source right away.

## Deploying

When you deploy a configuration, the deployment matches its contexts to the running ones by name:

| The configuration…                                 | The context…                                  |
| -------------------------------------------------- | --------------------------------------------- |
| declares a name that no running context has        | starts empty.                                 |
| keeps a name, with settings the context can take   | keeps its content and takes the new settings. |
| keeps a name, with settings the context can’t take | starts over empty.                            |
| changes the `type`                                 | starts over empty.                            |
| no longer declares the name                        | is removed, together with what it persisted.  |

Renaming a context removes the old one and creates an empty one under the new name. An invalid context file refuses the whole configuration and leaves the running contexts as they are.

## Persistence

A context comes back with its content after a restart only if it persists:

* A lookup table or Bloom filter persists with a `persist-interval`.
* A GeoIP context persists with `persist: true`.

Any other context starts empty, and a GeoIP context without `persist` downloads its database again. A persisting context writes to the deployment’s object store when it changed, and once more when the deployment stops. A context comes back only if what it persisted was written with settings it can take, as on a deploy; otherwise it starts over and the deployment drops the old state.

## Pipelines

Pipelines refer to a context by its name:

* [`context_update`](operators/context_update.md) stores keys and values in a lookup table, or keys in a Bloom filter.
* [`context_enrich`](operators/context_enrich.md) enriches events from any type of context.

A pipeline that refers to a name the configuration doesn’t declare fails. A pipeline that uses a context keeps running when a deploy replaces the context with an empty one of the same type, and continues with the new context. It fails when a deploy changes the type or removes the context.
