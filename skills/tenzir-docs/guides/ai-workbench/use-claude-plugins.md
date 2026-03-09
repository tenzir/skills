# Use Claude plugins

> Install the Tenzir plugin to write TQL pipelines and navigate OCSF schemas


This guide shows you how to install and use the `tenzir` plugin for Claude Code. The plugin provides documentation for writing TQL pipelines and the `tenzir:ocsf` subagent for OCSF schema questions.

## Install the plugin

* Interactive

  1. Run `/plugins` in Claude Code
  2. Go to **Marketplaces**
  3. Select **Add Marketplace**
  4. Enter `tenzir/claude-plugins`
  5. Install **tenzir** from the plugin list

* Shell

  ```bash
  # Add the Tenzir marketplace (once)
  claude plugins marketplace add tenzir/claude-plugins


  # Install the plugin
  claude plugins install tenzir@tenzir
  ```

## Write TQL pipelines

The plugin loads TQL language fundamentals, operator references, and idiomatic patterns on demand. Ask it to write pipelines and it will consult the documentation to produce correct code.

* Prompt

  ```plaintext
  Write a TQL pipeline that reads Zeek TSV logs from a TCP socket, extracts the
  connection 4-tuple, log ID, inbound/outbound bytes, and sends to Kafka.
  ```

* Response

  ```tql
  from "tcp://0.0.0.0:9999" {
    read_zeek_tsv
  }
  select \
    uid,
    src_ip=id.orig_h,
    src_port=id.orig_p,
    dst_ip=id.resp_h,
    dst_port=id.resp_p,
    orig_bytes,
    resp_bytes,
  to_kafka "flows"
  ```

  | Operator                    | Purpose                                                              |
  | --------------------------- | -------------------------------------------------------------------- |
  | `from "tcp://0.0.0.0:9999"` | Listens on TCP port 9999 for incoming connections                    |
  | `{ read_zeek_tsv }`         | Per-connection pipeline that parses Zeek’s tab-separated format      |
  | `select`                    | Extracts only the requested fields, renaming the 4-tuple for clarity |
  | `to_kafka "flows"`          | Publishes each event as JSON to the Kafka topic “flows”              |

## Navigate OCSF schemas

The `tenzir:ocsf` subagent answers questions about the [Open Cybersecurity Schema Framework](https://schema.ocsf.io)—event classes, objects, attributes, and profiles across multiple versions.

* Prompt

  ```plaintext
  @tenzir:ocsf What OCSF class should I use for firewall blocks?
  ```

* Response

  Use **Network Activity** (`class_uid`: **4001**).

  Key attributes for firewall events:

  * `action_id`: The action taken (allow, block, deny)
  * `disposition_id`: The outcome (allowed, blocked)
  * `firewall_rule`: The rule that triggered the action
  * `src_endpoint` / `dst_endpoint`: Network endpoints
  * `connection_info`: Protocol, ports, etc.

## Next steps

* Browse the [Claude Marketplace](https://github.com/tenzir/claude-plugins) for all available plugins