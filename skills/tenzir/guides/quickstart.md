---
title: "Quickstart"
description: "See live security events flow through Tenzir within minutes, from your AI agent, the app, or a terminal."
canonical: https://tenzir.com/docs/guides/quickstart
source: https://tenzir.com/docs/guides/quickstart.md
section: "Docs"
---

# Quickstart

> See live security events flow through Tenzir within minutes, from your AI agent, the app, or a terminal.

The fastest way to understand Tenzir is to watch it work on real data. In a few steps, you get a deployment, feed it a live stream of Zeek and Suricata events from our [`demo` package](https://tenzir.com/product/library/demo.md), look at them, and keep a pipeline running. Each step offers three ways to do it: ask your AI agent via MCP, click through the app, or use a terminal. Pick one, and every step follows it.

1. Create an account at [platform.tenzir.com](https://platform.tenzir.com) and connect the way you want to work.

   * MCP

     Add the platform’s MCP server to your agent, such as Claude Code:

     ```sh
     claude mcp add --transport http tenzir https://platform.tenzir.com/mcp
     ```

     Start Claude Code and run `/mcp`, which opens your browser to sign in.

   * App

     Sign in. The app needs no further setup.

   * CLI

     [Install the `tenzir` command](installation.md) with the package manager of your system, then sign in:

     ```sh
     tenzir auth login
     ```

2. Get a deployment to run your pipelines.

   * MCP

     ```prompt
     Create a Tenzir-hosted deployment named quickstart. If my organization can't have one, install the tenzir command with uv, sign me in with tenzir auth login, select my workspace with tenzir use, and run tenzir up quickstart -d.
     ```

   * App

     Open **Deployments**, select **New deployment**, then **Tenzir-hosted**, name it `quickstart`, and select **Start deployment**. On the Community edition, select **Self-hosted** instead and follow the install dialog.

   * CLI

     Select your workspace and run a deployment on your machine in the background:

     ```sh
     tenzir use <org>/<workspace>
     tenzir up quickstart -d
     tenzir use quickstart
     ```

3. Add the demo package, which generates live security events.

   * MCP

     ```prompt
     Add the demo package to my configuration, commit it, and deploy it to quickstart.
     ```

   * App

     Open **Packages**, select **Demo**, and select **Add**. Then commit the draft from the top bar.

   * CLI

     ```sh
     tenzir config clone
     cd tenzir-workspace
     test -f package.yaml || echo 'dependencies: {}' > package.yaml
     tenzir package add demo
     tenzir config apply -m 'Add the demo package'
     ```

4. Look at live data.

   * MCP

     ```prompt
     Run demo::zeek | head 10 on quickstart and explain what the events show.
     ```

   * App

     Open **Explorer**, select the `quickstart` deployment, enter `demo::zeek | head 10`, and select **Run**.

   * CLI

     ```sh
     tenzir run -r 'demo::zeek | head 10'
     ```

5. Keep a pipeline running that publishes the Suricata events to a topic:

   pipelines/suricata.tql

   ```tql
   demo::suricata
   publish "suricata"
   ```

   * MCP

     ```prompt
     Add a pipeline pipelines/suricata.tql to my configuration that publishes demo::suricata to the topic "suricata", commit it, and deploy it to quickstart.
     ```

   * App

     Open **Files**, select **Create file**, name it `pipelines/suricata.tql`, enter the pipeline, and commit the draft from the top bar.

   * CLI

     Save the pipeline as `pipelines/suricata.tql` in your clone, then commit and push it:

     ```sh
     tenzir config apply -m 'Publish the Suricata demo feed'
     ```

6. Watch the alerts flow through it.

   * MCP

     ```prompt
     Show me five alerts from the topic "suricata" on quickstart.
     ```

   * App

     Run this in the **Explorer**:

     ```tql
     subscribe "suricata"
     where @name == "suricata.alert"
     head 5
     ```

   * CLI

     ```sh
     tenzir run -r 'subscribe "suricata" | where @name == "suricata.alert" | head 5'
     ```

You’re in business: a deployment runs a pipeline continuously, and you can look at any data it sees.

What just happened

* The [deployment](../explanations/deployment.md) connected to the platform and follows the `main` branch of your configuration. Every commit there reaches it automatically, which is how the package and the pipeline arrived without a separate deploy step.
* Looking at `demo::zeek` ran an **ad-hoc pipeline**: it ran once, showed you its events, and is gone.
* The pipeline in `pipelines/suricata.tql` is a **deployed pipeline**: it keeps running, also after a restart, and feeds the topic `suricata` that other pipelines subscribe to.

Our explanation of [where pipelines run](../explanations/pipeline.md#where-pipelines-run) compares both kinds.

## Next steps

* [Connect to Tenzir](connect-to-tenzir.md)
* [Onboard a data source](../tutorials/onboard-a-data-source.md)
* [Change configurations](change-configurations.md)
* [Configuration](../explanations/configuration.md)
