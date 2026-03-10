# Python

> Python coding conventions and workflows for Tenzir projects. Covers uv-based tooling, Ruff formatting, strict Mypy type checking, and naming conventions.


Python coding conventions and workflows for Tenzir projects. Covers uv-based tooling, Ruff formatting, strict Mypy type checking, and naming conventions.

## Features

* 🐍 **Coding Conventions**: uv-based tooling, Ruff formatting, strict Mypy, naming conventions
* 🔍 **Pyright LSP Integration**: Pre-configured language server for enhanced type checking and IDE support

## Installation

* Interactive

  Use the plugin manager UI in Claude Code.

  1. Run `/plugin` in Claude Code `Enter`
  2. Go to **Marketplaces** `Tab`
  3. Select **+ Add Marketplace** `Enter`
  4. Type `tenzir/claude-plugins` `Enter`
  5. Install **python** from the plugin list

* Shell

  Add the marketplace (once), then install the plugin with your preferred scope.

  ```bash
  # Add the Tenzir marketplace (only needed once)
  claude plugin marketplace add tenzir/claude-plugins


  # Install to user scope (default)
  claude plugin install python@tenzir


  # Install to project scope (shared with team)
  claude plugin install python@tenzir --scope project


  # Install to local scope (gitignored)
  claude plugin install python@tenzir --scope local
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
      "python@tenzir": true
    }
  }
  ```

## Capabilities

| Type  | Name                    | Description                                                                                                                                                                        |
| ----- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill | `following-conventions` | Tenzir Python coding standards and tooling setup. Use when writing python code, running ruff/mypy/pytest, encountering pyproject.toml/uv.lock, or setting up a new Python project. |

## Usage

### Skill: `python:following-conventions`

The skill activates automatically when editing `.py` files, running Ruff/Mypy/pytest, or working with `pyproject.toml`. It provides guidance on:

**Type Annotations** - Strict Mypy settings require explicit types:

```python
# Before: Mypy rejects implicit Any and untyped definitions
def process(data, config=None):
    return data.get("value")


# After: Explicit types, no implicit optional
def process(data: dict[str, str], config: Config | None = None) -> str:
    return data.get("value", "")
```

**Naming and Style** - Enforces `snake_case` functions, `PascalCase` classes, `CONSTANT_CASE` constants. Uses Click for CLIs with kebab-case flags (`--output-file`).

**Quality Gates** - Run before committing:

```sh
uv run ruff check && uv run ruff format --check && uv run mypy && uv run pytest
```

**Project Setup** - For new projects, the skill provides ready-to-use `pyproject.toml` templates with Tenzir metadata, Hatchling build config, and standard tool configurations.

 Changelog 

View the release history and recent changes.

[ View on GitHub ](https://github.com/tenzir/claude-plugins/tree/main/plugins/python)

[Browse the plugin source code and documentation.](https://github.com/tenzir/claude-plugins/tree/main/plugins/python)