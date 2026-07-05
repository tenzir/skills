This release streamlines the shared Tenzir Skills collection by renaming the bundled documentation skill to tenzir and removing the opinionated shared review workflow. It also keeps scheduled ASIM updates stable when upstream branch movement does not change the copied source content.

## 💥 Breaking changes

### Review changes skill removal

The shared Tenzir Skills collection no longer includes `tenzir-review-changes` because its structured code review workflow is too opinionated to fit every contributor's pull request process.

Teams that need an agent-assisted code review workflow should keep that guidance in their own team-specific or personal skill collection.

*By @mavam and @codex in #30.*

### The tenzir-docs skill is now the tenzir skill

The `tenzir-docs` skill is now called `tenzir`. The skill remains the bundled Tenzir documentation—TQL, operators, functions, integrations, and deployment—and its `SKILL.md` now adds a "Beyond the docs" section with live entry points to the changelog, blog, solutions, and the full site index at `https://tenzir.com/llms.txt`, reflecting that tenzir.com and the documentation now live in one place.

Reinstall the skill under its new name:

Before:

```sh
npx skills add tenzir/skills@tenzir-docs
```

After:

```sh
npx skills remove tenzir-docs
npx skills add tenzir/skills@tenzir
```

Skills that declared a dependency on `tenzir-docs` (such as `tenzir-manage-packages`) now require `tenzir` instead.

*By @mavam and @claude in #27.*

## 🐞 Bug fixes

### Stable ASIM sync provenance

Scheduled updates of the `tenzir-asim` skill no longer create release churn when the Microsoft Defender Docs `public` branch moves but the copied ASIM source content has not changed.

The generated provenance page still links to Microsoft's upstream files and keeps local raw Markdown copies for audit, but branch movement alone no longer rewrites every upstream link.

*By @mavam and @codex in #29.*
