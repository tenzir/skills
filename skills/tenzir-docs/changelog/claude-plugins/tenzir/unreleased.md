# Tenzir Plugin Unreleased


## 🔧 Changes

### Generalized workflow orchestration system

Feb 5, 2026 · [@mavam](https://github.com/mavam), [@claude](https://github.com/claude) · #15

Consolidate workflow skills into a generalized orchestration system.

The Tenzir plugin now uses a two-tier workflow system: the `tenzir:orchestrating-workflows` skill guides you through multi-step workflows by breaking them into trackable tasks, while the `tenzir:workflow-executor` agent handles execution of individual steps. This replaces the previous granular skills for managing packages and mapping to OCSF, which are now read from the `tenzir:docs` skill and orchestrated dynamically. The new system makes it easier to add new workflows without creating additional skills.