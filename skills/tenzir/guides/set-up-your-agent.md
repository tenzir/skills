---
title: "Set up your agent"
description: "Give an AI agent what it needs to operate your deployments, write and test pipelines on your machine, and map events to security schemas."
canonical: https://tenzir.com/docs/guides/set-up-your-agent
source: https://tenzir.com/docs/guides/set-up-your-agent.md
section: "Docs"
---

# Set up your agent

> Give an AI agent what it needs to operate your deployments, write and test pipelines on your machine, and map events to security schemas.

An AI agent can do real work with Tenzir: operate your deployments, write and test pipelines on your machine, and map events to security schemas. Three building blocks make that work. The platform’s MCP server lets the agent act on your deployments, the `tenzir` skill gives it our documentation, and the `tenzir` command lets it run pipelines locally and check its own work.

What you need

* **Operate deployments and work with live data:** connect the platform via MCP.
* **Write and test pipelines and packages on your machine:** install the `tenzir` command and the `tenzir` skill.
* **Map events to OCSF, ASIM, CIM, ECS, UDM, or EDM, or produce CEF or LEEF:** use the schema skills, which the MCP server serves, or install them locally.

## Connect via MCP

An agent connected via MCP operates your deployments on your behalf: it starts and stops pipelines, runs ad-hoc pipelines on live data, and changes and deploys configurations. It also reads our documentation and schema references for the Tenzir release of your deployment through the server, so it needs no skills installed.

For Claude Code, add the server, then start Claude Code and run `/mcp` to sign in:

```sh
claude mcp add --transport http tenzir https://platform.tenzir.com/mcp
```

Our guide on [connecting to Tenzir](connect-to-tenzir.md) sets up Codex and other clients.

## Give your agent the docs

The `tenzir` skill is our entire documentation, packaged for agents with progressive disclosure: the agent reads a map first and loads individual pages only when it needs them. Install it when your agent works without MCP, such as on your machine or offline.

### Use the tenzir skill

Install the skill into the current project:

* gh skill

  ```bash
  gh skill install tenzir/skills tenzir
  ```

* uvx skeel

  ```bash
  uvx skeel add tenzir/skills tenzir
  ```

* npx skills

  ```bash
  npx skills add tenzir/skills@tenzir
  ```

Your agent loads the skill when a request is about Tenzir. To make sure that it does, name the skill in your prompt:

```prompt
Use the tenzir skill to explain the difference between the summarize and top operators.
```

For the `tenzir` command itself, an agent needs no skill: `tenzir help` and `tenzir help <command>` describe every command and flag.

## Let your agent run pipelines

With the `tenzir` command installed, your agent runs TQL on your machine, without a deployment or an account. It can iterate on a pipeline against sample data until the output is what you want, then hand you the result or add it to your configuration.

Install the command as our guide on [installing Tenzir](installation.md) shows. In a sandbox without a package manager, the agent can also run it ad hoc with [uv](https://docs.astral.sh/uv/):

```sh
uvx tenzir run 'from {x: 42}'
```

The agent runs a pipeline on a file, on standard input, or from a file that holds the pipeline:

```sh
tenzir run 'from_file "events.json" { read_json } | where severity > 3'
cat input.yaml | tenzir run 'read_yaml | select x | write_csv'
tenzir run -f pipeline.tql
```

In a configuration or package directory, the agent can call the operators of its packages once `tenzir package fetch` downloaded them, and test them with `tenzir-test`, as our guide on [writing tests](write-tests.md) shows.

Ask for a result that the agent can check by running it:

```prompt
Write a pipeline that parses these firewall logs into OCSF Network Activity, run it with tenzir run on sample.log until the output validates, then show me the pipeline.
```

The same engine runs in your deployments, so a pipeline that works on your machine runs there too. Our CLI reference lists how [`tenzir run`](../reference/cli.md#tenzir-run) completes a pipeline with standard input and output.

## Add the schema skills

The schema skills document the security schemas and formats that pipelines map events to. The MCP server serves them too; install them locally for agents without MCP. To install all of our skills at once:

```bash
npx skills add tenzir/skills
```

### Use the ASIM skill

Microsoft Sentinel ASIM schemas, normalized fields, aliases, and roles, for mapping events and entities to ASIM.

```bash
npx skills add tenzir/skills@tenzir-asim
```

### Use the CEF skill

ArcSight CEF headers, escaping rules, the predefined extension keys, and the ESM event schema behind them.

```bash
npx skills add tenzir/skills@tenzir-cef
```

### Use the CIM skill

Splunk CIM data models, datasets, fields, tags, constraints, and lookups.

```bash
npx skills add tenzir/skills@tenzir-cim
```

### Use the ECS skill

Elastic Common Schema fields, fieldsets, categorization values, and custom fields, and how ECS aligns with OpenTelemetry.

```bash
npx skills add tenzir/skills@tenzir-ecs
```

### Use the EDM skill

The FortiSIEM Event Data Model: data models, event attributes, their types, and their names.

```bash
npx skills add tenzir/skills@tenzir-edm
```

### Use the LEEF skill

IBM QRadar LEEF 1.0 and 2.0 headers, delimiters, predefined event attributes, and timestamps.

```bash
npx skills add tenzir/skills@tenzir-leef
```

### Use the OCSF skill

OCSF event classes, objects, attributes, profiles, and extensions, across OCSF versions.

```bash
npx skills add tenzir/skills@tenzir-ocsf
```

### Use the UDM skill

Google SecOps UDM fields, event types, and entities, for ingestion payloads and for detection logic such as YARA-L.

```bash
npx skills add tenzir/skills@tenzir-udm
```
