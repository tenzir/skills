# Tenzir

> Build TQL pipelines and OCSF mappings with expert guidance. Provides workflow skills for creating parser packages and OCSF mappings, plus subagents for documentation lookup and OCSF schema navigation.


Build TQL pipelines and OCSF mappings with expert guidance. Provides workflow skills for creating parser packages and OCSF mappings, plus subagents for documentation lookup and OCSF schema navigation.

## Features

* **Documentation Access**: Complete Tenzir documentation available as a skill, auto-synced from the latest release
* **Parser Creation**: Guided workflow for building parsing pipelines from raw log data with iterative testing
* **OCSF Mapping**: Transform parsed events into OCSF-compliant format with validation
* **Documentation Guide**: Fast answers to Tenzir questions via the `tenzir:guide` subagent
* **OCSF Schema Navigation**: Fast answers to OCSF schema questions via the `tenzir:ocsf` subagent

## Installation

* Interactive

  Use the plugin manager UI in Claude Code.

  1. Run `/plugin` in Claude Code `Enter`
  2. Go to **Marketplaces** `Tab`
  3. Select **+ Add Marketplace** `Enter`
  4. Type `tenzir/claude-plugins` `Enter`
  5. Install **tenzir** from the plugin list

* Shell

  Add the marketplace (once), then install the plugin with your preferred scope.

  ```bash
  # Add the Tenzir marketplace (only needed once)
  claude plugin marketplace add tenzir/claude-plugins


  # Install to user scope (default)
  claude plugin install tenzir@tenzir


  # Install to project scope (shared with team)
  claude plugin install tenzir@tenzir --scope project


  # Install to local scope (gitignored)
  claude plugin install tenzir@tenzir --scope local
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
      "tenzir@tenzir": true
    }
  }
  ```

## Capabilities

| Type  | Name                       | Description                                                                                                                                                               |
| ----- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill | `orchestrating-workflows`  | Orchestrate Tenzir workflows. Use when executing Tenzir workflows.                                                                                                        |
| Agent | `tenzir:guide`             | Answer questions about Tenzir. Use when the user asks about TQL pipelines, operators, functions, node configuration, platform setup, or integrations.                     |
| Agent | `tenzir:ocsf`              | Answer questions about the OCSF (Open Cyber Security Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, or event normalization. |
| Agent | `tenzir:workflow-executor` | Execute Tenzir workflow steps. Use when running a specific phase of a Tenzir workflow.                                                                                    |
| Hook  | `SessionStart`             | Triggers on \*                                                                                                                                                            |
| Hook  | `PreToolUse`               | Triggers on Skill                                                                                                                                                         |

## Usage

### `tenzir:docs` skill

Provides the complete Tenzir documentation as context. The documentation is automatically downloaded from the latest GitHub release and cached locally. Syncs every 24 hours to stay current.

The skill covers deployment, configuration, TQL (Tenzir Query Language), operators, functions, formats, connectors, integrations, and the Tenzir Platform.

 Changelog 

View the release history and recent changes.

[ View on GitHub ](https://github.com/tenzir/claude-plugins/tree/main/plugins/tenzir)

[Browse the plugin source code and documentation.](https://github.com/tenzir/claude-plugins/tree/main/plugins/tenzir)