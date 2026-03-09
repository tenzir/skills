# Brand

> Tenzir brand and style guidelines for frontend development. Includes design tokens, component specifications, and official logo assets to ensure consistent UI styling across Tenzir products.


Tenzir brand and style guidelines for frontend development. Includes design tokens, component specifications, and official logo assets to ensure consistent UI styling across Tenzir products.

## Features

* 🎨 **Design Tokens** - Colors, typography, spacing, and shadows as CSS custom properties and Tailwind config
* 🧩 **Component Specs** - 17 UI components (buttons, inputs, tags, toasts, and more) with all states documented
* ⚡ **Tailwind Ready** - Configuration snippets for immediate integration
* 🏷️ **Logo Assets** - Official SVG logos and logomarks in standard and white variants

## Installation

* Interactive

  Use the plugin manager UI in Claude Code.

  1. Run `/plugin` in Claude Code `Enter`
  2. Go to **Marketplaces** `Tab`
  3. Select **+ Add Marketplace** `Enter`
  4. Type `tenzir/claude-plugins` `Enter`
  5. Install **brand** from the plugin list

* Shell

  Add the marketplace (once), then install the plugin with your preferred scope.

  ```bash
  # Add the Tenzir marketplace (only needed once)
  claude plugin marketplace add tenzir/claude-plugins


  # Install to user scope (default)
  claude plugin install brand@tenzir


  # Install to project scope (shared with team)
  claude plugin install brand@tenzir --scope project


  # Install to local scope (gitignored)
  claude plugin install brand@tenzir --scope local
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
      "brand@tenzir": true
    }
  }
  ```

## Capabilities

| Type  | Name                | Description                                                                                                                                                                                                                                              |
| ----- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill | `styling-tenzir-ui` | Provides Tenzir design system tokens and component specifications. Use when building UI components, styling with CSS/Tailwind, choosing colors, typography, spacing, or implementing buttons, inputs, tags/badges, toasts, and other Tenzir UI elements. |

## Usage

The `brand:styling-tenzir-ui` skill activates automatically when you work on Tenzir frontend code. It provides design tokens, component specs, and CSS snippets for consistent UI styling.

[ Changelog ](../../changelog/claude-plugins/brand.md)

[View the release history and recent changes.](../../changelog/claude-plugins/brand.md)

[ View on GitHub ](https://github.com/tenzir/claude-plugins/tree/main/plugins/brand)

[Browse the plugin source code and documentation.](https://github.com/tenzir/claude-plugins/tree/main/plugins/brand)