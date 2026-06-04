This release consolidates Tenzir package development into the new tenzir-create-package skill, replacing the older parser and OCSF mapping workflows with one broader package creation workflow. It also adds a generated Google SecOps UDM skill for schema reference and normalization guidance.

## 💥 Breaking changes

### Consolidated Tenzir package creation skill

The package creation workflow is now centered on `tenzir-create-package`, a single skill for building library-quality Tenzir packages with UDOs, tests, examples, disabled-by-default pipelines, inputs, contexts, and optional OCSF mappings.

Before:

```sh
npx skills add tenzir/skills@tenzir-create-parser-package
npx skills add tenzir/skills@tenzir-create-ocsf-mapping
```

After:

```sh
npx skills add tenzir/skills@tenzir-create-package
```

Use the new skill for parser package work, OCSF mapping work, and broader package development.

*By @mavam and @codex.*

## 🚀 Features

### Add Google UDM skill

Added `tenzir-google-udm`, a generated Google SecOps UDM schema and normalization guidance skill derived from the canonical `googleapis/googleapis` UDM and Entity protocol buffers plus targeted Google SecOps usage guidance.

*By @mavam and @codex.*
