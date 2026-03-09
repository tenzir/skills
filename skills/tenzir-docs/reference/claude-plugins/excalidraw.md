# Excalidraw

> Generate valid `.excalidraw` JSON files that render correctly in excalidraw.com or VS Code extensions.


Generate valid `.excalidraw` JSON files that render correctly in excalidraw\.com or VS Code extensions.

## Features

* 📐 **All element types**: Shapes, text, arrows, lines, freedraw, images, frames, and custom polygons
* 🔗 **Proper bindings**: Text labels inside shapes, arrows connected to shapes
* 🎨 **Accurate properties**: Values and constants derived from Excalidraw source code

## Installation

* Interactive

  Use the plugin manager UI in Claude Code.

  1. Run `/plugin` in Claude Code `Enter`
  2. Go to **Marketplaces** `Tab`
  3. Select **+ Add Marketplace** `Enter`
  4. Type `tenzir/claude-plugins` `Enter`
  5. Install **excalidraw** from the plugin list

* Shell

  Add the marketplace (once), then install the plugin with your preferred scope.

  ```bash
  # Add the Tenzir marketplace (only needed once)
  claude plugin marketplace add tenzir/claude-plugins


  # Install to user scope (default)
  claude plugin install excalidraw@tenzir


  # Install to project scope (shared with team)
  claude plugin install excalidraw@tenzir --scope project


  # Install to local scope (gitignored)
  claude plugin install excalidraw@tenzir --scope local
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
      "excalidraw@tenzir": true
    }
  }
  ```

## Capabilities

| Type  | Name          | Description                                                                                                                           |
| ----- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Skill | `diagramming` | Generate Excalidraw diagrams. Use when creating flowcharts, ER diagrams, sequence diagrams, block diagrams, or any .excalidraw files. |

## Usage

### `excalidraw:diagramming` skill

Activates when creating or editing `.excalidraw` files. Provides the file format structure and progressively loads element and styling references as needed.

**When it activates:**

* Creating diagrams or `.excalidraw` files
* Asking about Excalidraw element structure or properties

**Example prompts:**

```plaintext
Create a diagram with three boxes connected by arrows
```

```plaintext
Draw a state machine with Start, Processing, and Done states
```

```plaintext
Make a simple org chart with a root node and three children
```

[ Changelog ](../../changelog/claude-plugins/excalidraw.md)

[View the release history and recent changes.](../../changelog/claude-plugins/excalidraw.md)

[ View on GitHub ](https://github.com/tenzir/claude-plugins/tree/main/plugins/excalidraw)

[Browse the plugin source code and documentation.](https://github.com/tenzir/claude-plugins/tree/main/plugins/excalidraw)