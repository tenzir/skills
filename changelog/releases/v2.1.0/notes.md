This release improves agent guidance for package lifecycle management and Google SecOps UDM workflows. It helps agents choose the right package surfaces while making UDM field name differences explicit for mapping and detection use cases.

## 🚀 Features

### UDM field name forms for mapping and YARA-L

The `tenzir-google-udm` skill now shows both UDM field spellings when they differ, so mapping and detection workflows can use the same reference.

For example, generated field headings now show `event_type` / `eventType` and `security_result` / `securityResult`. Use the right side when mapping logs into UDM event or entity objects for Google SecOps UDM API ingestion; use the left side in YARA-L, Detect Engine, CBN, and other dotted field-path contexts.

*By @mavam and @codex in #12.*

## 🔧 Changes

### Package lifecycle management focus

The `tenzir-manage-packages` skill now focuses on package lifecycle management instead of package content development.

It routes agents through package surfaces such as manifests, UDO files, pipelines, examples, tests, changelog entries, and publishing while leaving operator implementation details to the relevant docs or specialized skills.

*By @mavam and @codex in #13.*
