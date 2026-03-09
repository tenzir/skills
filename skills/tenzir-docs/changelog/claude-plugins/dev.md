# Dev Plugin

> Developer utilities for Tenzir projects.


Developer utilities for Tenzir projects.

## Releases

* [Unreleased](dev/unreleased.md)
* [v4.2.0 Feb 13, 2026](dev/v4-2-0.md)

  [This release adds remote release workflow detection to `/dev:release`, letting you trigger GitHub Actions workflows instead of running local release steps. It also modularizes the documentation editing architecture and improves issue identifier guidance in the PR maker agent.](dev/v4-2-0.md)
* [v4.1.0 Jan 30, 2026](dev/v4-1-0.md)

  [This release improves workflow automation for changelog creation and code review. The changelog-adder agent now auto-detects changed files and provides clearer guidance for writing user-focused entries. The review command streamlines decision points, reducing prompts while maintaining control ove...](dev/v4-1-0.md)
* [v4.0.0 Jan 28, 2026](dev/v4-0-0.md)

  [This release introduces a unified code review and fix workflow that consolidates the review, triage, planning, and execution phases into a single `/dev:review` command. The workflow spawns specialized reviewers in parallel, filters findings by confidence, plans fixes with proper dependencies, and...](dev/v4-0-0.md)
* [v3.0.0 Jan 22, 2026](dev/v3-0-0.md)

  [This release consolidates developer utilities into a unified plugin. The docs, prose, and ship plugins have merged into dev, providing changelog management, code review, and documentation workflows in one place. The new `/dev:review` command spawns seven specialized reviewers in parallel to anal...](dev/v3-0-0.md)
* [v2.2.2 Jan 15, 2026](dev/v2-2-2.md)

  [This release updates the docs plugin command scripts to use bun instead of pnpm, aligning with the Tenzir documentation site's package manager migration.](dev/v2-2-2.md)
* [v2.2.1 Jan 8, 2026](dev/v2-2-1.md)

  [This release fixes two bugs in the documentation reader subagent. The reader now reports all examples from operator and function pages instead of only the first one, and only reports verbatim examples from the documentation instead of synthesizing potentially incorrect code.](dev/v2-2-1.md)
* [v2.2.0 Jan 4, 2026](dev/v2-2-0.md)

  [This release restores the `/docs:pr` command with enhanced cross-referencing capabilities that automatically link documentation PRs with parent project PRs. It also improves the synchronization workflow by automatically cloning the documentation repository when needed, eliminating manual setup st...](dev/v2-2-0.md)
* [v2.1.0 Dec 28, 2025](dev/v2-1-0.md)

  [This release adds a documentation reader subagent that answers questions about Tenzir by navigating the live documentation at docs.tenzir.com. It also makes the docs:writer subagent fully autonomous by handling PR creation directly from within the .docs/ repository.](dev/v2-1-0.md)
* [v2.0.0 Dec 28, 2025](dev/v2-0-0.md)

  [This major release renames the `docs:writing` skill to `docs:authoring` to better reflect its comprehensive scope beyond prose writing. It also introduces an intelligent documentation sync hook that automatically keeps the `.docs/` repository synchronized while preventing conflicts.](dev/v2-0-0.md)
* [v1.1.1 Dec 22, 2025](dev/v1-1-1.md)

  [This release ensures the `/docs:write` command works with up-to-date documentation by synchronizing the `.docs/` clone with the latest changes from `main` before writing.](dev/v1-1-1.md)
* [v1.1.0 Dec 19, 2025](dev/v1-1-0.md)

  [This release introduces autonomous documentation workflows with the new `/docs:review` command and `docs:writer` subagent. The plugin now uses `.docs` as the unconditional documentation root and streamlines command naming by renaming `/docs:write-docs` to `/docs:write`.](dev/v1-1-0.md)
* [v1.0.0 Dec 15, 2025](dev/v1-0-0.md)

  [This is the first stable release of the docs plugin. It introduces a streamlined workflow with dedicated commands for documentation management, replacing the previous agent-based approach. The plugin now features intelligent path detection, SSH-based repository cloning, and a simplified directory...](dev/v1-0-0.md)
* [v0.1.0 Dec 9, 2025](dev/v0-1-0.md)

  [Initial release of the docs plugin.](dev/v0-1-0.md)