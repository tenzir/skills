This release consolidates Tenzir package development into the new tenzir-manage-packages skill, replacing the older parser and OCSF mapping workflows with one broader package management workflow. It also adds a generated Google SecOps UDM skill for schema reference and normalization guidance.

## 💥 Breaking changes

### Consolidated Tenzir package management skill

The package management workflow is now centered on `tenzir-manage-packages`, a single skill for adding, inspecting, updating, extending, refactoring, deprecating, and removing library-quality Tenzir package capabilities with UDOs, tests, examples, disabled-by-default pipelines, inputs, contexts, and optional OCSF mappings.

Before:

```sh
npx skills add tenzir/skills@tenzir-create-parser-package
npx skills add tenzir/skills@tenzir-create-ocsf-mapping
```

After:

```sh
npx skills add tenzir/skills@tenzir-manage-packages
```

Use the new skill for parser package work, OCSF mapping work, and broader package lifecycle management.

*By @mavam and @codex.*

## 🚀 Features

### Add Google UDM skill

Added `tenzir-google-udm`, a generated Google SecOps UDM schema and normalization guidance skill derived from the canonical `googleapis/googleapis` UDM and Entity protocol buffers plus targeted Google SecOps usage guidance.

*By @mavam and @codex.*
