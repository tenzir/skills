# OCSF

> Reference documentation for the Open Cybersecurity Schema Framework (OCSF).


This reference provides comprehensive documentation for the [Open Cybersecurity Schema Framework (OCSF)](https://ocsf.io), an open standard for normalizing security telemetry across tools and vendors.

## Resources

<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->

[ Introduction ](ocsf/introduction.md)

[Comprehensive guide to OCSF concepts](ocsf/introduction.md)

<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->

[ Schema ](ocsf/1-7-0.md)

[Classes, objects, profiles, and extensions](ocsf/1-7-0.md)

<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->

[ FAQs ](ocsf/faqs.md)

[Common questions about OCSF](ocsf/faqs.md)

<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->

[ Articles ](ocsf/articles.md)

[In-depth guides and best practices](ocsf/articles.md)

## Versions

We publish all OCSF schema versions with full cross-references between classes, objects, profiles, extensions, and types.

| Version                            | Classes | Objects | Profiles | Extensions | Types |
| ---------------------------------- | ------- | ------- | -------- | ---------- | ----- |
| [v1.7.0](ocsf/1-7-0.md) | 76      | 166     | 11       | 0          | 23    |
| [v1.6.0](ocsf/1-6-0.md) | 75      | 163     | 11       | 0          | 23    |
| [v1.5.0](ocsf/1-5-0.md) | 74      | 157     | 11       | 0          | 23    |
| [v1.4.0](ocsf/1-4-0.md) | 72      | 138     | 11       | 0          | 22    |
| [v1.3.0](ocsf/1-3-0.md) | 65      | 117     | 9        | 0          | 22    |
| [v1.2.0](ocsf/1-2-0.md) | 59      | 108     | 8        | 0          | 22    |
| [v1.1.0](ocsf/1-1-0.md) | 44      | 103     | 7        | 0          | 22    |
| [v1.0.0](ocsf/1-0-0.md) | 33      | 81      | 5        | 0          | 22    |

Note

This documentation is auto-generated from the official [OCSF schema](https://schema.ocsf.io) and [ocsf-docs](https://github.com/ocsf/ocsf-docs) repository. Download an AI-optimized snapshot at our [GitHub release page](https://github.com/tenzir/docs/releases/tag/latest).

## Using OCSF with Tenzir

Tenzir provides native support for OCSF through the `ocsf.*` operators: [`ocsf.apply`](operators/ocsf/apply.md), [`ocsf.cast`](operators/ocsf/cast.md), [`ocsf.derive`](operators/ocsf/derive.md), and [`ocsf.trim`](operators/ocsf/trim.md). You can normalize events to OCSF, validate schema compliance, and work with OCSF-formatted data throughout your pipelines.

Use [Tenzir’s Claude plugins](../guides/ai-workbench/use-claude-plugins.md) for guided OCSF mapping workflows.

## Contents

- [Introduction](ocsf/introduction.md)
- [Classes](ocsf/1-7-0/classes.md)
- [Objects](ocsf/1-7-0/objects.md)
- [Profiles](ocsf/1-7-0/profiles.md)
- [Extensions](ocsf/1-7-0/extensions.md)
- [Types](ocsf/1-7-0/types.md)
- [FAQs](ocsf/faqs.md)
- [Articles](ocsf/articles.md)