---
title: "Connect to Tenzir"
description: "Connect your AI agent via MCP, sign in with the tenzir command, or create an API key for your scripts."
canonical: https://tenzir.com/docs/guides/connect-to-tenzir
source: https://tenzir.com/docs/guides/connect-to-tenzir.md
section: "Docs"
---

# Connect to Tenzir

> Connect your AI agent via MCP, sign in with the tenzir command, or create an API key for your scripts.

You work with Tenzir through the [platform](../explanations/platform.md), and you can reach it four ways under the same permissions: the app in your browser, your AI agent via MCP, the `tenzir` command, and the API. The app, MCP, and the API offer the same operations. The `tenzir` command offers them too, and adds what only a terminal can do: running pipelines and deployments on your machine and editing a configuration as files. The app at [platform.tenzir.com](https://platform.tenzir.com) needs nothing beyond an account. This guide connects the other three, so that every later guide works with the interface you prefer.

## Connect your interface

* MCP

  Add the platform’s MCP server at `https://platform.tenzir.com/mcp` to your agent. Any agent that supports remote MCP servers with OAuth works:

  * **Claude Code:** run the following command, then start Claude Code and run `/mcp`, which opens your browser to sign in.

    ```sh
    claude mcp add --transport http tenzir https://platform.tenzir.com/mcp
    ```

  * **Codex:** run the following commands. The login command opens your browser to sign in.

    ```sh
    codex mcp add tenzir --url https://platform.tenzir.com/mcp
    codex mcp login tenzir
    ```

  * **Other clients:** add the server to the client’s MCP configuration. The client discovers how to sign in and opens your browser when it first connects.

    ```json
    {
      "mcpServers": {
        "tenzir": {
          "url": "https://platform.tenzir.com/mcp"
        }
      }
    }
    ```

  The app shows the same instructions under your account menu → **Connect MCP**. Once you signed in, the agent acts on your behalf with the permissions of your roles. Check the connection by asking:

  ```prompt
  Which Tenzir organizations, workspaces, and deployments do I have?
  ```

  The agent reads our documentation and schema references through the server, so it needs no [agent skills](set-up-your-agent.md).

* CLI

  Install the `tenzir` command with the package manager of your system, as our guide on [installing Tenzir](installation.md) shows.

  Sign in and select the workspace and deployment to work with:

  ```sh
  tenzir auth login
  tenzir use acme/prod/edge-1
  ```

  The login command prints a URL to sign in with in your browser, which also works when you’re connected to a remote machine. The `use` command takes an organization, a workspace, and a deployment, each by slug or id; a bare `tenzir use` lets you pick from a list. Check your sign-in and selection with:

  ```sh
  tenzir status
  ```

  The command also runs pipelines on your machine without any account, such as `tenzir run 'from {x: 42}'`.

* API

  Create an API key, which lets a script act on your behalf without a password or a browser:

  1. Open **Settings** → **API keys** in the app.
  2. Select **Create API key** and give the key a name, such as `ci`.
  3. Copy the secret that the dialog shows.

  The platform shows the secret only once, so store it where your script reads it, such as a secret of your CI system. With the CLI, `tenzir api-key create --name ci` does the same.

  Send the key in the `x-tenzir-api-key` header. Reading your account works with every key:

  ```sh
  curl -H "x-tenzir-api-key: $TENZIR_API_KEY" \
    https://platform.tenzir.com/api/account
  ```

  The platform documents every operation at `https://platform.tenzir.com/api/docs`, and as an OpenAPI document at `https://platform.tenzir.com/api/openapi.json` to generate a client from. The `tenzir` command takes the same key from the `TENZIR_API_KEY` environment variable, which suits shell scripts better than raw requests.

  A new key may only read its own account. Our guide on [controlling access](control-access.md#limit-what-a-script-may-do) gives it the permissions your script needs.

## Next steps

With your interface connected, add the deployments that run your pipelines, as our guide on [adding a deployment](add-a-deployment.md) shows.

* [Add a deployment](add-a-deployment.md)
* [Platform](../explanations/platform.md)
* [MCP](../reference/mcp.md)
* [CLI](../reference/cli.md)
* [API](../reference/api.md)
