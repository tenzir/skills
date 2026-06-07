---
name: tenzir-ecs
description: Answer questions about Elastic Common Schema (ECS), Elastic field names, fieldsets, field types, categorization fields such as event.kind/event.category/event.type/event.outcome, ECS mapping decisions, custom fields, field reuse, and ECS/OpenTelemetry relations. Use whenever the user maps logs, events, security telemetry, network data, IAM activity, threat indicators, cloud/service context, or observability data into ECS, even if they only mention Elastic fields or event categorization.
---

# Elastic Common Schema

Elastic Common Schema (ECS) defines common fields for logs, metrics, security telemetry, and observability data so events from different sources can be queried and correlated consistently.

This skill is generated from the latest supported ECS release in this repository: `v9.4.0` / `9.4.0`.
Use the YAML files as the authoritative reference for exact field names, fieldsets, types, levels, allowed values, normalization hints, reuse metadata, and OpenTelemetry relations.
Use the Markdown docs only for conceptual guidance, mapping examples, and implementation conventions.
If a field, fieldset, allowed value, or relation is not present in the YAML data, say that it is not documented here.

## Data files

- Use [fields.yaml](fields.yaml) to find a dotted ECS field and then load the referenced `fields/<field>.yaml` file.
- Use [fieldsets.yaml](fieldsets.yaml) to choose a fieldset and then load the referenced `fieldsets/<fieldset>.yaml` file.
- Use [categorization.yaml](categorization.yaml) for `event.kind`, `event.category`, `event.type`, `event.outcome`, allowed values, and expected category/type combinations.
- Use [otel.yaml](otel.yaml) for ECS-to-OpenTelemetry relation records.
- Use [source.md](source.md) for release provenance, source artifacts, copied docs, and counts.

## Complementary docs

- Start with [Implementation patterns](docs/implementation-patterns.md), [Design principles](docs/design-principles.md), and [Conventions](docs/conventions.md) for general modeling questions.
- Use [Categorization fields](docs/categorization-fields.md) and [Using categorization fields](docs/categorization-usage.md) when assigning `event.*` categorization values.
- Use [Mapping network events](docs/mapping-network-events.md) for `source`/`destination` versus `client`/`server` decisions.
- Use [Custom fields](docs/custom-fields.md) when ECS has no suitable field.
- Use [ECS and OpenTelemetry](docs/opentelemetry.md) together with [otel.yaml](otel.yaml) for OTel alignment questions.
- Use focused usage docs for [cloud](docs/usage/cloud.md), [service](docs/usage/service.md), [threat](docs/usage/threat.md), and [user](docs/usage/user.md) mapping scenarios.

## Mapping rules

- Populate required fields first: `@timestamp` and `ecs.version`.
- Prefer documented ECS fields over custom fields when the field semantics match.
- Preserve source-specific detail in custom fields when ECS has no matching field; use `labels` for small keyword metadata when appropriate.
- For categorization, use only allowed values from [categorization.yaml](categorization.yaml); leave categorization fields empty when no allowed value fits.
- Treat `event.category` and `event.type` as arrays and use multiple values only when the event reasonably belongs to multiple categories or types.
- Use fieldset reuse metadata in [fieldsets.yaml](fieldsets.yaml) to distinguish role-specific locations such as `user.target`, `process.parent`, `cloud.origin`, and `service.target`.
- For network events, use `source`/`destination` for packet or flow direction and also populate `client`/`server` when the endpoint roles are known.
- Copy pivot values into `related.*` when the docs or field semantics call for cross-field searching.

## Question routing

- **What does field X mean?** Start with [fields.yaml](fields.yaml), then load the selected field YAML.
- **What fields exist under fieldset X?** Start with [fieldsets.yaml](fieldsets.yaml), then load the selected fieldset YAML.
- **Which `event.category` or `event.type` should I use?** Start with [categorization.yaml](categorization.yaml), then read [Using categorization fields](docs/categorization-usage.md) for examples.
- **How should I map a network event?** Read [Mapping network events](docs/mapping-network-events.md), then inspect the relevant fieldsets.
- **How do I model users, cloud resources, services, or threat indicators?** Read the matching usage doc under `docs/usage/`, then inspect the relevant fieldset YAML.
- **How does ECS relate to OpenTelemetry?** Use [otel.yaml](otel.yaml) for relation records and [ECS and OpenTelemetry](docs/opentelemetry.md) for conceptual guidance.
- **What if ECS has no matching field?** Read [Custom fields](docs/custom-fields.md).
- **What raw upstream source backs this skill?** Use [source.md](source.md).
