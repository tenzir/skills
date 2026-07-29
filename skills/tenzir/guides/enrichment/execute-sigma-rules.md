---
title: "Execute Sigma rules"
description: "Run Sigma detection rules on parsed Windows Event Logs and OCSF process events"
canonical: https://tenzir.com/docs/guides/enrichment/execute-sigma-rules
source: https://tenzir.com/docs/guides/enrichment/execute-sigma-rules.md
section: "Docs"
---

# Execute Sigma rules

> Run Sigma detection rules on parsed Windows Event Logs and OCSF process events

This guide shows you how to run [Sigma rules](https://github.com/SigmaHQ/sigma) on parsed security telemetry with the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) operator. Use this pattern to turn Windows Event Logs and other normalized records into Sigma sightings without leaving the Tenzir pipeline.

The `sigma` operator transpiles rule YAML into a TQL expression. Semantically, you can think of it as applying [`where`](https://tenzir.com/docs/reference/operators/where.md) to the input: non-matching events are discarded, and matching events become `tenzir.sigma` records that include the original event and the matched rule.

At a high level, the translation process looks as follows:

Field names

The `sigma` operator does not normalize Sigma field names automatically. A rule key such as `EventData.CommandLine` or `process.cmd_line` must match the field path in the input event. Either write rules for your Tenzir field paths or map incoming records to the field names used by your rule set before running [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md).

## Detect encoded PowerShell in Windows Event Logs

Windows process creation events are a good fit for Sigma because many detections are field-level predicates over Event ID 4688. Start with a rule that matches PowerShell launched with an encoded command:

rules/windows/encoded-powershell.yml

```yaml
title: Encoded PowerShell Command
id: 7f01f6b8-9f1e-48f5-bab9-2d1f7040c6a1
status: experimental
description: Detects Windows process creation events where PowerShell runs an encoded command.
logsource:
  product: windows
  service: security
detection:
  selection:
    System.EventID: 4688
    EventData.NewProcessName|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
    EventData.CommandLine|contains:
      - ' -enc '
      - ' -EncodedCommand '
      - ' -encodedcommand '
  condition: selection
fields:
  - System.Computer
  - EventData.SubjectUserName
  - EventData.NewProcessName
  - EventData.CommandLine
level: high
```

If your collector sends native Windows Event Log XML, parse each event with [`parse_winlog`](https://tenzir.com/docs/reference/functions/parse_winlog.md) and then run the rule:

```tql
from_file "windows-security.xml" {
  read_delimited "</Event>\n", include_separator=true
}
this = data.parse_winlog()
sigma "rules/windows/encoded-powershell.yml"
```

```tql
{
  event: {
    System: {
      Provider: {
        Name: "Microsoft-Windows-Security-Auditing",
      },
      EventID: 4688,
      TimeCreated: {
        SystemTime: 2026-06-07T10:00:00Z,
      },
      Channel: "Security",
      Computer: "WORKSTATION-17",
    },
    EventData: {
      NewProcessName: "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
      CommandLine: "powershell.exe -NoP -EncodedCommand SQBFAFgA",
      ParentProcessName: "C:\\Windows\\explorer.exe",
      SubjectUserName: "alice",
    },
  },
  rule: {
    title: "Encoded PowerShell Command",
    id: "7f01f6b8-9f1e-48f5-bab9-2d1f7040c6a1",
    status: "experimental",
    description: "Detects Windows process creation events where PowerShell runs an encoded command.",
    logsource: {
      product: "windows",
      service: "security",
    },
    detection: {
      selection: {
        "System.EventID": 4688,
        "EventData.NewProcessName|endswith": [
          "\\powershell.exe",
          "\\pwsh.exe",
        ],
        "EventData.CommandLine|contains": [
          " -enc ",
          " -EncodedCommand ",
          " -encodedcommand ",
        ],
      },
      condition: "selection",
    },
    fields: [
      "System.Computer",
      "EventData.SubjectUserName",
      "EventData.NewProcessName",
      "EventData.CommandLine",
    ],
    level: "high",
  },
}
```

For a live Windows Event Collector stream, keep the same parse-and-detect shape and change only the source:

```tql
accept_tcp "0.0.0.0:1514" {
  read_delimited "</Event>\n", include_separator=true
}
this = data.parse_winlog()
sigma "/etc/tenzir/sigma/windows/", refresh_interval=30s
publish "detections.sigma"
```

The directory form lets you add or update rules without restarting the pipeline. Every 30 seconds, Tenzir reloads the files in `/etc/tenzir/sigma/windows/` and uses the refreshed rule set for subsequent events.

See [Microsoft Windows Event Logs](../../integrations/microsoft/windows-event-logs.md) for collection patterns that deliver Windows Event Log XML to Tenzir.

## Map parsed events to existing rule fields

Many public Sigma rules use generic Windows field names such as `EventID`, `Image`, `CommandLine`, `ParentImage`, and `User`. You can either edit the rule to use `System.*` and `EventData.*` paths, or map the parsed Windows event to those field names before [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md):

```tql
from_file "windows-security.xml" {
  read_delimited "</Event>\n", include_separator=true
}
this = data.parse_winlog()


EventID = System.EventID
Image = EventData.NewProcessName
CommandLine = EventData.CommandLine
ParentImage = EventData.ParentProcessName
User = EventData.SubjectUserName


sigma "rules/windows/encoded-powershell-standard-fields.yml"
```

```tql
{
  event: {
    System: {
      Provider: {
        Name: "Microsoft-Windows-Security-Auditing",
      },
      EventID: 4688,
      TimeCreated: {
        SystemTime: 2026-06-07T10:00:00Z,
      },
      Channel: "Security",
      Computer: "WORKSTATION-17",
    },
    EventData: {
      NewProcessName: "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
      CommandLine: "powershell.exe -NoP -EncodedCommand SQBFAFgA",
      ParentProcessName: "C:\\Windows\\explorer.exe",
      SubjectUserName: "alice",
    },
    EventID: 4688,
    Image: "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    CommandLine: "powershell.exe -NoP -EncodedCommand SQBFAFgA",
    ParentImage: "C:\\Windows\\explorer.exe",
    User: "alice",
  },
  rule: {
    title: "Encoded PowerShell Command",
    logsource: {
      product: "windows",
      category: "process_creation",
    },
    detection: {
      selection: {
        EventID: 4688,
        "Image|endswith": [
          "\\powershell.exe",
          "\\pwsh.exe",
        ],
        "CommandLine|contains": [
          " -enc ",
          " -EncodedCommand ",
          " -encodedcommand ",
        ],
      },
      condition: "selection",
    },
    level: "high",
  },
}
```

With that mapping, the corresponding rule can use the common field names:

rules/windows/encoded-powershell-standard-fields.yml

```yaml
title: Encoded PowerShell Command
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    EventID: 4688
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
    CommandLine|contains:
      - ' -enc '
      - ' -EncodedCommand '
      - ' -encodedcommand '
  condition: selection
level: high
```

This approach is useful when you import a rule set that already follows a field taxonomy. The original Windows structure remains on the event, so analysts can still inspect `System` and `EventData` after a match.

## Transpile a process rule to OCSF TQL

You can also implement a Sigma detection in TQL directly, without going through the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) operator. This keeps your events in their canonical shape - useful when you’ve normalized to a schema such as OCSF and don’t want to rename fields back to Sigma’s Windows-style selectors only to satisfy a rule.

A recent upstream Sigma process-creation rule, `proc_creation_win_print_dump_sensitive_files.yml` (`Sensitive File Dump Via Print.EXE`, April 28, 2026), detects `print.exe` abuse for copying sensitive Windows credential stores such as `SAM`, `SECURITY`, `SYSTEM`, and `ntds.dit`.

The relevant source YAML is:

/tmp/sigma/rules/windows/process\_creation/proc\_creation\_win\_print\_dump\_sensitive\_files.yml

```yaml
title: Sensitive File Dump Via Print.EXE
id: 2fcda7e2-8c57-4904-86ac-37fc3157e09d
status: test
date: 2026-04-28
logsource:
  category: process_creation
  product: windows
detection:
  selection_img:
    - Image|endswith: '\print.exe'
    - OriginalFileName: 'Print.EXE'
  selection_cli:
    CommandLine|contains|windash: '/D'
    CommandLine|contains:
      - '\config\SAM'
      - '\config\SECURITY'
      - '\config\SYSTEM'
      - '\windows\ntds\ntds.dit'
  condition: all of selection_*
falsepositives:
  - Unlikely
level: high
```

When your source already emits OCSF Process Activity events, translate the selectors to OCSF fields:

| Sigma selector         | OCSF Process Activity field             |
| ---------------------- | --------------------------------------- |
| `Image`                | `process.path` or `process.name`        |
| `OriginalFileName`     | `process.file.internal_name`            |
| `CommandLine`          | `process.cmd_line`                      |
| Host and user grouping | `device.hostname` and `actor.user.name` |

The following fixture contains two matching process launches and one benign `print.exe` launch. The pipeline keeps the Sigma rule’s single-event semantics and emits one detection per matching process event:

```tql
from {
  time: 2026-04-28T10:01:00Z,
  class_uid: 1007,
  activity_id: 1,
  device: {hostname: "WORKSTATION-17"},
  actor: {user: {name: "alice"}},
  process: {
    name: "print.exe",
    path: "C:\\Windows\\System32\\print.exe",
    file: {internal_name: "Print.EXE"},
    cmd_line: "print.exe /D:C:\\Windows\\System32\\config\\SAM C:\\Temp\\sam.bak",
  },
}, {
  time: 2026-04-28T10:02:00Z,
  class_uid: 1007,
  activity_id: 1,
  device: {hostname: "WORKSTATION-17"},
  actor: {user: {name: "alice"}},
  process: {
    name: "print.exe",
    path: "C:\\Windows\\System32\\print.exe",
    file: {internal_name: "Print.EXE"},
    cmd_line: "print.exe /D:C:\\Windows\\System32\\config\\SYSTEM C:\\Temp\\system.bak",
  },
}, {
  time: 2026-04-28T10:02:30Z,
  class_uid: 1007,
  activity_id: 1,
  device: {hostname: "WORKSTATION-17"},
  actor: {user: {name: "alice"}},
  process: {
    name: "print.exe",
    path: "C:\\Windows\\System32\\print.exe",
    file: {internal_name: "Print.EXE"},
    cmd_line: "print.exe C:\\Users\\alice\\report.txt",
  },
}


where class_uid == 1007 and activity_id == 1


where process.path.ends_with("\\print.exe", ignore_case=true) \
  or process.name.equals("print.exe", ignore_case=true) \
  or process.file.internal_name.equals("print.exe", ignore_case=true)


where process.cmd_line.match_regex(r"(?i)[/-]d") and process.cmd_line.match_regex(
  r"(?i)\\config\\(sam|security|system)|\\windows\\ntds\\ntds\.dit"
)


select time,
  host=device.hostname,
  user=actor.user.name,
  command=process.cmd_line,
  rule="Sensitive File Dump Via Print.EXE",
  level="high"
```

```tql
{
  time: 2026-04-28T10:01:00Z,
  host: "WORKSTATION-17",
  user: "alice",
  command: "print.exe /D:C:\\Windows\\System32\\config\\SAM C:\\Temp\\sam.bak",
  rule: "Sensitive File Dump Via Print.EXE",
  level: "high",
}
{
  time: 2026-04-28T10:02:00Z,
  host: "WORKSTATION-17",
  user: "alice",
  command: "print.exe /D:C:\\Windows\\System32\\config\\SYSTEM C:\\Temp\\system.bak",
  rule: "Sensitive File Dump Via Print.EXE",
  level: "high",
}
```

If you package this predicate as `operators/detections/print_sensitive_dump.tql` in a package named `windows_threats`, callers can use the operator `windows_threats::detections::print_sensitive_dump` and add correlation separately. For example, use `window` after the UDO when you want one alert for repeated matches on the same host and user:

```tql
from_file "ocsf-process-events.json" {
  read_ndjson
}
windows_threats::detections::print_sensitive_dump
window size=5min, on=time {
  summarize host,
    user,
    rule,
    level,
    match_count=count(),
    commands=distinct(command)
  where match_count > 1
  window_start = $window.start
  window_end = $window.end
}
```

For the two detection records from the earlier fixture, the windowed pipeline emits one correlated result:

```tql
{
  host: "WORKSTATION-17",
  user: "alice",
  rule: "Sensitive File Dump Via Print.EXE",
  level: "high",
  match_count: 2,
  commands: [
    "print.exe /D:C:\\Windows\\System32\\config\\SAM C:\\Temp\\sam.bak",
    "print.exe /D:C:\\Windows\\System32\\config\\SYSTEM C:\\Temp\\system.bak",
  ],
  window_start: 2026-04-28T10:00:00Z,
  window_end: 2026-04-28T10:05:00Z,
}
```

## Express correlation rules in TQL

Sigma also defines [correlation rules](https://github.com/SigmaHQ/sigma-specification/blob/main/specification/sigma-correlation-rules-specification.md): a `correlation:` block that counts or sequences the sightings of one or more detection rules. The `sigma` operator runs single detection rules only and does not execute correlation rules, but each correlation type maps directly onto [`window`](https://tenzir.com/docs/reference/operators/window.md) and [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), as the windowed example above already shows for counting. Assume a stream of detection sightings that each carry a `rule` name and a `time`.

These examples use fixed, epoch-aligned time bins. For a sliding “within N minutes of each other” interpretation, use a hopping window instead, as shown in [`window`](https://tenzir.com/docs/reference/operators/window.md#detect-brute-force-logins-with-a-hopping-window).

| Correlation type   | The question it asks                     | TQL building blocks                                     |
| ------------------ | ---------------------------------------- | ------------------------------------------------------- |
| `event_count`      | ≥ N sightings per group in a window      | `window` + `summarize count=count()` + `where`          |
| `value_count`      | ≥ N distinct values of a field per group | `window` + `summarize count_distinct(field)` + `where`  |
| `temporal`         | several rules fire together, any order   | `window` + `summarize distinct(rule)` + `where`         |
| `temporal_ordered` | several rules fire in a defined order    | `sort` + `window` + `summarize collect(rule)` + `where` |

The windowed pipeline above is an `event_count` correlation: `count()` with a `where` threshold. A `value_count` correlation counts distinct values of a field instead, for example flagging a host where at least three different users trip the rule within five minutes:

```tql
window size=5min, on=time {
  summarize host, users=count_distinct(user)
  where users >= 3
}
```

A `temporal` correlation fires when several different rules match for the same group within a window, in any order:

```tql
window size=10min, on=time {
  summarize host, rules=distinct(rule)
  where rules.contains("recon") and rules.contains("exploit") and rules.contains("exfil")
}
```

A `temporal_ordered` correlation adds sequence. Sort by time so the window sees events in order, collect the rule names with [`collect`](https://tenzir.com/docs/reference/functions/collect.md) (which keeps order, unlike [`distinct`](https://tenzir.com/docs/reference/functions/distinct.md)), drop unrelated rules, and compare the remaining sequence as a string, because TQL has no list-to-list equality yet:

```tql
sort time
window size=10min, on=time {
  summarize host, sequence=collect(rule)
  where sequence.where(r => r == "recon" or r == "exploit" or r == "exfil").join(",") == "recon,exploit,exfil"
}
```

## See Also

* [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md)
* [`select`](https://tenzir.com/docs/reference/operators/select.md)
* [`where`](https://tenzir.com/docs/reference/operators/where.md)
* [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md)
* [`window`](https://tenzir.com/docs/reference/operators/window.md)
* [`distinct`](https://tenzir.com/docs/reference/functions/distinct.md)
* [`collect`](https://tenzir.com/docs/reference/functions/collect.md)
* [`count_distinct`](https://tenzir.com/docs/reference/functions/count_distinct.md)
* [`parse_winlog`](https://tenzir.com/docs/reference/functions/parse_winlog.md)
* [Add operators](../packages/add-operators.md)
* [Microsoft Windows Event Logs](../../integrations/microsoft/windows-event-logs.md)
