# Dev

> Developer utilities including documentation, changelogs, code review, plan review, git workflows, auto-formatting, and releases. Provides documentation workflows with the Diataxis framework, technical writing guidance based on Google's style guide, changelog management with tenzir-ship, parallel code review with specialized reviewers and automated fix execution, plan review with external AI tools, git commit/PR workflows, and automatic file formatting after edits.


Developer utilities including documentation, changelogs, code review, plan review, git workflows, auto-formatting, and releases. Provides documentation workflows with the Diataxis framework, technical writing guidance based on Google’s style guide, changelog management with tenzir-ship, parallel code review with specialized reviewers and automated fix execution, plan review with external AI tools, git commit/PR workflows, and automatic file formatting after edits.

## Features

* 📚 **Docs Authoring Skill**: Guidance on the Diataxis framework, section selection, and Tenzir docs conventions
* ✍️ **Technical Writing Skill**: Style guidelines for clear technical documentation following Google’s developer documentation style guide
* 📝 **Changelog Adder Agent**: Creates changelog entries for PR changes, suitable for CI automation
* 🔍 **Code Review Command**: Spawns specialized reviewers in parallel, triages findings, creates fix tasks, and executes fixes with GitHub thread resolution
* 🚀 **Release Command**: Guides through releasing a project with tenzir-ship
* 🔬 **Plan Reviewer Agent**: Reviews implementation plans using external AI models (Codex, Gemini, Opus) with structured evaluation methodology
* 📦 **Committer Agent**: Stages and commits changes with cohesion analysis and automatic splitting of unrelated changes
* 🔀 **PR Maker Agent**: Creates GitHub pull requests with proper branching and commit workflows
* 🤖 **Fixer Agent**: Opus-powered agent that fixes findings. In PR mode, commits, pushes, and resolves GitHub threads. In batch mode, applies fixes without individual commits
* 🎯 **Triager Agent**: Filters low-confidence findings, groups related issues, and deduplicates cross-reviewer overlap for focused review
* 📋 **Planner Agent**: Creates ordered fix tasks with file-level dependencies to prevent merge conflicts
* 🚢 **Shipping Skill**: Ships code and docs — commit, PR, changelog, and documentation updates orchestrated end-to-end
* 🔧 **Auto-Formatting Hook**: Automatically formats files after every Write or Edit operation using language-specific formatters

## Installation

* Interactive

  Use the plugin manager UI in Claude Code.

  1. Run `/plugin` in Claude Code `Enter`
  2. Go to **Marketplaces** `Tab`
  3. Select **+ Add Marketplace** `Enter`
  4. Type `tenzir/claude-plugins` `Enter`
  5. Install **dev** from the plugin list

* Shell

  Add the marketplace (once), then install the plugin with your preferred scope.

  ```bash
  # Add the Tenzir marketplace (only needed once)
  claude plugin marketplace add tenzir/claude-plugins


  # Install to user scope (default)
  claude plugin install dev@tenzir


  # Install to project scope (shared with team)
  claude plugin install dev@tenzir --scope project


  # Install to local scope (gitignored)
  claude plugin install dev@tenzir --scope local
  ```

* Settings

  Add the marketplace and plugin to your settings file.

  .claude/settings.json

  ```json
  {
    "extraKnownMarketplaces": {
      "tenzir": {
        "source": {
          "source": "github",
          "repo": "tenzir/claude-plugins"
        }
      }
    },
    "enabledPlugins": {
      "dev@tenzir": true
    }
  }
  ```

## Capabilities

| Type    | Name                      | Description                                                                                                                                                                                              |
| ------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill   | `addressing-reviews`      | Address GitHub PR review feedback. Use when responding to reviewers, resolving threads, or handling review comments.                                                                                     |
| Skill   | `docs-authoring`          | Author documentation for Tenzir projects. Use when creating or updating tutorials, guides, explanations, reference, or integrations.                                                                     |
| Skill   | `docs-editing`            | Edit Tenzir documentation. Use when writing, updating, or validating docs in .docs/.                                                                                                                     |
| Skill   | `reviewing-changes`       | Review methodology for code changes with confidence scoring. Use when spawning reviewer agents, rating issue severity (P1-P4), or scoring review confidence.                                             |
| Skill   | `reviewing-plans`         | Review methodology for implementation plans. Use when evaluating plan quality, completeness, or risk.                                                                                                    |
| Skill   | `shipping-changes`        | >-                                                                                                                                                                                                       |
| Skill   | `technical-writing`       | Write clear technical documentation following Google’s style guide. Use when writing docs, README files, API documentation, code comments, user guides, or asking about documentation style.             |
| Skill   | `writing-commit-messages` | Write git commit messages for Tenzir repositories. Use when committing changes, running git commit, drafting commit messages, detecting staged changes, or asking about commit format and subject lines. |
| Command | `/dev:release`            | Guide through releasing a project via remote workflow or local tenzir-ship (detect, stage, commit, publish, verify).                                                                                     |
| Command | `/dev:review`             | Run parallel code review on changes. Use when reviewing a PR, checking code quality, or auditing changes.                                                                                                |
| Agent   | `dev:changelog-adder`     | Create a changelog entry for PR changes. Use when adding changelog entries, running tenzir-ship, or automating CI workflows.                                                                             |
| Agent   | `dev:committer`           | Commit changes autonomously for automated workflows. Use when staging files, creating commits, or automating git workflows.                                                                              |
| Agent   | `dev:docs-editor`         | Edit Tenzir documentation. Use when writing docs, updating guides, or syncing docs with code without creating a PR.                                                                                      |
| Agent   | `dev:fixer`               | Fix review findings with commits. Use when addressing findings from /dev:review.                                                                                                                         |
| Agent   | `dev:planner`             | Plan fixes for review findings. Use when creating fix tasks from triaged findings.                                                                                                                       |
| Agent   | `dev:pr-maker`            | Create a pull request on GitHub for current changes. Use when opening a PR, pushing a topic branch, or submitting changes for review.                                                                    |
| Agent   | `dev:triager`             | Triage review findings. Use when filtering false positives, grouping related findings, or deduplicating reviewer overlap.                                                                                |
| Hook    | `SessionStart`            | Triggers on \*                                                                                                                                                                                           |
| Hook    | `PostToolUse`             | Triggers on Write, Edit                                                                                                                                                                                  |

## Usage

### Creating changelog entries

Spawn the changelog adder agent to create a changelog entry for your changes:

```plaintext
Create a changelog entry @dev:changelog-adder
```

The agent analyzes your changes and creates an appropriate changelog entry using tenzir-ship.

 Changelog 

View the release history and recent changes.

[ View on GitHub ](https://github.com/tenzir/claude-plugins/tree/main/plugins/dev)

[Browse the plugin source code and documentation.](https://github.com/tenzir/claude-plugins/tree/main/plugins/dev)