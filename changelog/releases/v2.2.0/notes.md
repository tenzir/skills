This release adds generated reference skills for major security schema and event formats, including Microsoft Sentinel ASIM, Splunk CIM, Elastic ECS, ArcSight CEF, IBM QRadar LEEF, FortiSIEM EDM, and Google SecOps UDM. It also expands the Tenzir design system skill with machine-readable tokens and per-tool styling guidance.

## 🚀 Features

### ArcSight CEF skill

Added `tenzir-cef`, a generated ArcSight CEF (Common Event Format) reference skill for generating, parsing, and mapping CEF events, bundled with the ArcSight ESM event schema behind the format.

The skill exposes all 174 predefined extension keys from the OpenText extension dictionary as YAML — exact key spelling, expanded full name, data type, length, producer/consumer audience, and the CEF specification version that introduced each key — alongside the full ESM event schema: 479 data fields across 18 groups with labels, script aliases, types, and turbo levels. Extension keys whose full name resolves to an ESM script alias are crosswalked to their schema groups. Markdown guidance covers the CEF header, severity, character escaping, special mappings, user-defined extensions, and date formats. Upstream quirks, such as the duplicated `dmac` row and mid-word line-wrap artifacts in key names, are normalized and documented in the source notes.

*By @mavam and @claude in #23.*

### Elastic Common Schema skill

Added `tenzir-ecs`, a generated Elastic Common Schema reference skill for mapping logs and security telemetry into ECS.

The skill exposes ECS fields, fieldsets, categorization values, field reuse metadata, and ECS/OpenTelemetry relations as YAML, with curated upstream Markdown guidance for categorization, network mapping, custom fields, cloud and service context, threat indicators, and user modeling.

*By @mavam and @codex.*

### FortiSIEM Event Data Model skill

Added `tenzir-edm`, a generated FortiSIEM Event Data Model reference skill for mapping events into Fortinet's normalized event attributes.

The skill covers all 21 data models of the FortiSIEM 7.5.0 Event Data Model documentation, exposing event attributes with types, display names, descriptions, and cross-model usage as YAML, plus Markdown copies of the upstream Fortinet pages for audit.

*By @mavam and @claude in #21.*

### IBM QRadar LEEF skill

Added `tenzir-leef`, a generated IBM QRadar LEEF (Log Event Extended Format) reference skill for generating, parsing, and mapping LEEF 2.0 events.

The skill exposes all 45 predefined event attributes as YAML — exact key spelling, value type, normalization behavior, attribute limits, and reserved status — plus Markdown guidance for the syslog and LEEF headers, delimiter rules, custom event keys, and `devTime`/`devTimeFormat` timestamp patterns. Spec quirks published by IBM, such as the `identSecondlp` typo, are preserved verbatim and annotated.

*By @mavam and @claude in #20.*

### Microsoft Sentinel ASIM skill

Added `tenzir-asim`, a Microsoft Sentinel ASIM reference skill for mapping security telemetry to ASIM.

The generated reference currently covers 12 event schemas, 1 entity schema, 539 distinct fields, 1,426 schema field records, and 73 alias records from Microsoft Defender Docs. It now emits agent-native YAML catalogs, schema files, field files, alias data, and guidance data so agents can choose target ASIM schemas and map source telemetry with less context-window overhead.

*By @mavam and @codex in #11 and #17.*

### Splunk CIM skill

Added `tenzir-cim`, a generated Splunk Common Information Model reference skill for mapping security telemetry to CIM.

The generator takes an unpacked `Splunk_SA_CIM` app directory as input and emits agent-native YAML catalogs for CIM data models, datasets, effective fields, constraints, calculated fields, and lookup-backed values, translations, and enrichments. The generated skill also bundles core Splunk CIM 8.5 documentation as reference-only prose while keeping the app-derived YAML authoritative.

*By @mavam and @codex in #15.*

## 🔧 Changes

### Google UDM entity ingestion guidance

The Google UDM skill now clarifies that Entity Type Guidance values such as `USER` or `ASSET` belong to the Entity object's `metadata.entity_type` / `metadata.entityType`, while `entities.import` uses a separate `inlineSource.logType` for the context source, such as `AZURE_AD_CONTEXT`.

*By @mavam and @codex in #14.*

### Google UDM record YAML reference

The Google UDM skill now exposes record definitions as YAML leaves rather than Markdown message pages. Record YAML uses data-centric type shapes such as `list<T>`, `optional<T>`, `map<K, V>`, `variant`, and field `union`s, making event and entity fields easier for agents to scan when mapping logs into UDM.

*By @mavam and @codex in #16.*

### Multi-tool design system skill with machine-readable tokens

The `tenzir-design-system` skill is now the canonical home of the Tenzir design system and supports many consumers beyond Platform CSS: plain CSS, Tailwind, Quarto documents, slide decks, and Mermaid/Graphviz diagrams.

Token values now live in machine-readable YAML: `data/brand.yml` follows Quarto's brand.yml schema and can be consumed directly via `brand: data/brand.yml`, while `data/tokens.yml` carries the extended tokens (spacing, radius, type scale, shadows, motion, z-index, breakpoints, and a dark-mode mapping). Markdown references explain how to choose tokens; per-tool guides under `references/tools/` provide ready-to-use CSS custom properties, Tailwind v4/v3 configuration, a shadcn/ui theme, and diagram/slide styling.

*By @mavam and @claude in #22.*

### Tenzir UDM skill name

The Google UDM skill is now installed and referenced as `tenzir-udm`.

Use the new skill name when installing it directly:

```sh
npx skills add tenzir/skills@tenzir-udm
```

*By @mavam and @codex in #18.*
