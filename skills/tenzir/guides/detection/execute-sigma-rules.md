---
title: "Execute Sigma rules"
description: "Run Sigma rules on parsed and OCSF events, generate findings, and implement unsupported features and correlations in TQL"
canonical: https://tenzir.com/docs/guides/detection/execute-sigma-rules
source: https://tenzir.com/docs/guides/detection/execute-sigma-rules.md
section: "Docs"
---

# Execute Sigma rules

> Run Sigma rules on parsed and OCSF events, generate findings, and implement unsupported features and correlations in TQL

This guide shows you how to run [Sigma rules](https://github.com/SigmaHQ/sigma) on parsed security telemetry with the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) operator. Sigma is a bring-your-own-content integration: rule sets you already have, whether from the public SigmaHQ repository, a content vendor, or your own detection team, run directly in the pipeline. For detections you write from scratch, native TQL predicates are the more expressive tool, as the guide on [matching events with TQL](match-events-with-tql.md) shows.

The `sigma` operator transpiles rule YAML into a TQL expression. Semantically, you can think of it as applying [`where`](https://tenzir.com/docs/reference/operators/where.md) to the input: non-matching events are discarded, and matching events become `tenzir.sigma` records that include the original event and the matched rule.

The examples progress from running one rule to refreshing a rule set, aligning rule fields with event schemas, and generating OCSF findings. The final sections translate unsupported rule features and correlations into native TQL.

## Match events with Sigma

Start with one rule, then scale the same execution pattern to a rule set that refreshes without restarting the pipeline.

### Run a single rule

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

### Run and refresh a rule set

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

## Align rules with your event schema

Field names

The `sigma` operator does not normalize Sigma field names automatically. A rule key such as `EventData.CommandLine` or `process.cmd_line` must match the field path in the input event. Either write rules for your Tenzir field paths or map incoming records to the field names used by your rule set before running [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md).

### Map events to existing rule fields

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
    id: "7f01f6b8-9f1e-48f5-bab9-2d1f7040c6a1",
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
id: 7f01f6b8-9f1e-48f5-bab9-2d1f7040c6a1
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

### Write rules against OCSF fields

Because the `sigma` operator takes rule keys verbatim, nested dotted paths resolve directly into OCSF records. That turns Sigma into a syntax over your normalized schema: instead of renaming OCSF events back into Windows-style selectors, write the rule against OCSF field paths in the first place.

The following rule reimplements the upstream `Sensitive File Dump Via Print.EXE` detection against OCSF Process Activity events. The `selection_*` groups and the `all of selection_*` condition carry over unchanged from upstream Sigma conventions; only the field paths differ. The `windash` modifier of the original rule has no supported equivalent, so this version omits the `/D` flag check, which the [TQL translation of this rule](execute-sigma-rules.md#translate-unsupported-rules-to-tql) expresses precisely:

rules/ocsf/print-dump-ocsf.yml

```yaml
title: Sensitive File Dump Via Print.EXE
id: 2fcda7e2-8c57-4904-86ac-37fc3157e09d
status: test
logsource:
  product: ocsf
detection:
  selection_class:
    class_uid: 1007
    activity_id: 1
  selection_img:
    - process.path|endswith: '\print.exe'
    - process.file.internal_name: 'Print.EXE'
  selection_cli:
    process.cmd_line|contains:
      - '\config\SAM'
      - '\config\SECURITY'
      - '\config\SYSTEM'
      - '\windows\ntds\ntds.dit'
  condition: all of selection_*
level: high
```

Run it on OCSF events like any other rule. The example data contains one matching credential-store dump and one benign `print.exe` launch:

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
sigma "rules/ocsf/print-dump-ocsf.yml"
```

```tql
{
  event: {
    time: 2026-04-28T10:01:00Z,
    class_uid: 1007,
    activity_id: 1,
    device: {
      hostname: "WORKSTATION-17",
    },
    actor: {
      user: {
        name: "alice",
      },
    },
    process: {
      name: "print.exe",
      path: "C:\\Windows\\System32\\print.exe",
      file: {
        internal_name: "Print.EXE",
      },
      cmd_line: "print.exe /D:C:\\Windows\\System32\\config\\SAM C:\\Temp\\sam.bak",
    },
  },
  rule: {
    title: "Sensitive File Dump Via Print.EXE",
    id: "2fcda7e2-8c57-4904-86ac-37fc3157e09d",
    status: "test",
    logsource: {
      product: "ocsf",
    },
    detection: {
      selection_class: {
        class_uid: 1007,
        activity_id: 1,
      },
      selection_img: [
        {
          "process.path|endswith": "\\print.exe",
          "process.file.internal_name": null,
        },
        {
          "process.path|endswith": null,
          "process.file.internal_name": "Print.EXE",
        },
      ],
      selection_cli: {
        "process.cmd_line|contains": [
          "\\config\\SAM",
          "\\config\\SECURITY",
          "\\config\\SYSTEM",
          "\\windows\\ntds\\ntds.dit",
        ],
      },
      condition: "all of selection_*",
    },
    level: "high",
  },
}
```

Only the credential-store dump matches; the benign launch passes through the operator silently. Keeping rules in OCSF terms means one rule serves every data source you normalize, and the rule reads in the same vocabulary as the rest of your detection stack.

## Generate OCSF Detection Findings

The `{event, rule}` wrapper is operator output, not a finding. Reshape it into an OCSF [Detection Finding](https://schema.ocsf.io/classes/detection_finding) (`class_uid: 2004`) so Sigma matches flow through the same downstream processing as every other detection. Give every rule a stable `id` before this step because it identifies both the analytic and the resulting finding:

```tql
let $finding_time = 2026-04-28T10:01:05Z


from {
  time: 2026-04-28T10:01:00Z,
  metadata: {uid: "process-activity-52517", version: "1.8.0"},
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
}
sigma "rules/ocsf/print-dump-ocsf.yml"
// Reshape the {event, rule} wrapper into a Detection Finding.
this = {
  time: $finding_time, // use now() in a live pipeline
  metadata: {
    product: {name: "Tenzir", vendor_name: "Tenzir"},
    uid: f"finding-create-sigma-{rule.id}-{event.metadata.uid}",
    version: "1.9.0",
  },
  class_uid: 2004,
  category_uid: 2,
  activity_id: 1,
  severity_id: 4,
  status_id: 1,
  is_alert: true,
  finding_info: {
    uid: f"sigma-{rule.id}-{event.metadata.uid}",
    title: rule.title,
    analytic: {
      name: rule.title,
      uid: rule.id,
      type_id: 1,
    },
  },
  device: event.device,
  evidences: [{
    uid: event.metadata.uid,
    actor: event.actor,
    process: event.process,
  }],
}
type_uid = class_uid * 100 + activity_id
```

```tql
{
  time: 2026-04-28T10:01:05Z,
  metadata: {
    product: {
      name: "Tenzir",
      vendor_name: "Tenzir",
    },
    uid: "finding-create-sigma-2fcda7e2-8c57-4904-86ac-37fc3157e09d-process-activity-52517",
    version: "1.9.0",
  },
  class_uid: 2004,
  category_uid: 2,
  activity_id: 1,
  severity_id: 4,
  status_id: 1,
  is_alert: true,
  finding_info: {
    uid: "sigma-2fcda7e2-8c57-4904-86ac-37fc3157e09d-process-activity-52517",
    title: "Sensitive File Dump Via Print.EXE",
    analytic: {
      name: "Sensitive File Dump Via Print.EXE",
      uid: "2fcda7e2-8c57-4904-86ac-37fc3157e09d",
      type_id: 1,
    },
  },
  device: {
    hostname: "WORKSTATION-17",
  },
  evidences: [
    {
      uid: "process-activity-52517",
      actor: {
        user: {
          name: "alice",
        },
      },
      process: {
        name: "print.exe",
        path: "C:\\Windows\\System32\\print.exe",
        file: {
          internal_name: "Print.EXE",
        },
        cmd_line: "print.exe /D:C:\\Windows\\System32\\config\\SAM C:\\Temp\\sam.bak",
      },
    },
  ],
  type_uid: 200401,
}
```

The rule’s identity maps onto `finding_info.analytic`: its title becomes the analytic name, its Sigma rule ID the analytic `uid`, and `type_id: 1` labels it as a rule-based detection. The matched event travels in `evidences`, so analysts pivot from the finding to the triggering process without a lookup. Build `finding_info.uid` from the rule identity plus the event identity. This example uses `event.metadata.uid`, so the same rule matching two source events yields two distinct findings even when their host and timestamp coincide.

## Translate unsupported rules to TQL

Unsupported modifiers are skipped silently

The operator skips [value modifiers](../../reference/operators/sigma.md#description) it does not implement instead of rejecting the rule, so a rule relying on one matches as if the modifier were absent. Before importing a rule set, grep it for the unsupported modifiers listed in the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) reference, currently including `windash`, `cased`, `i`/`ignorecase`, `exists`, `fieldref`, `neq`, and the UTF-16 family. Express affected predicates in native TQL instead, where `ignore_case=true` and `match_regex(r"(?i)...")` cover the common cases.

When a rule needs unsupported modifiers or sharper predicates than the format offers, translate it to native TQL. The translation is mechanical: map the rule’s field names to your schema and its modifiers to TQL functions. The result often expresses the intent more faithfully than the rule format allows, because TQL has no unsupported-modifier gaps.

The upstream original of the credential-store rule from the previous sections shows why: `proc_creation_win_print_dump_sensitive_files.yml` (`Sensitive File Dump Via Print.EXE`, April 28, 2026) detects `print.exe` abuse for copying sensitive Windows credential stores, and its `/D` flag selector relies on the unsupported `windash` modifier:

proc\_creation\_win\_print\_dump\_sensitive\_files.yml

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

When your source emits OCSF Process Activity events, translate the selectors to OCSF fields:

| Sigma selector         | OCSF Process Activity field             |
| ---------------------- | --------------------------------------- |
| `Image`                | `process.path` or `process.name`        |
| `OriginalFileName`     | `process.file.internal_name`            |
| `CommandLine`          | `process.cmd_line`                      |
| Host and user grouping | `device.hostname` and `actor.user.name` |

The `windash` modifier, which matches both `/D` and `-D` parameter spellings, has a direct regex equivalent: `[/-]d`. The `process.file` object is optional in OCSF, so the predicate reads it with `?` access and a trailing `== true`, following the optional-field guidance in the section on [filtering by event type and fields](match-events-with-tql.md#filter-by-event-type-and-fields). The following example data contains two matching process launches and one benign `print.exe` launch. The pipeline keeps the rule’s single-event semantics and emits one detection per matching event:

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


// class_name: "Process Activity", activity_name: "Launch"
where class_uid == 1007 and activity_id == 1


where process.path.ends_with("\\print.exe", ignore_case=true) \
  or process.name.equals("print.exe", ignore_case=true) \
  or process.file?.internal_name?.equals("print.exe", ignore_case=true) == true


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

The predicate vocabulary behind this translation, and how to package the result as a reusable operator, is the subject of the guide on [matching events with TQL](match-events-with-tql.md).

## Implement Sigma correlation rules in TQL

Sigma also defines [correlation rules](https://github.com/SigmaHQ/sigma-specification/blob/main/specification/sigma-correlation-rules-specification.md): a `correlation:` block that counts or sequences the sightings of one or more detection rules.

### Map correlation types to TQL

The `sigma` operator runs single detection rules only and does not execute correlation rules, but each correlation type maps directly onto [`window`](https://tenzir.com/docs/reference/operators/window.md) and [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md):

| Correlation type   | The question it asks                     | TQL building blocks                                              |
| ------------------ | ---------------------------------------- | ---------------------------------------------------------------- |
| `event_count`      | ≥ N sightings per group in a window      | `window` + `summarize count=count()` + `where`                   |
| `value_count`      | ≥ N distinct values of a field per group | `window` + `summarize count_distinct(field)` + `where`           |
| `temporal`         | several rules fire together, any order   | `window` + `summarize distinct(rule)` + `where`                  |
| `temporal_ordered` | several rules fire in a defined order    | `window` + `sort` + `summarize collect(rule)` + subsequence scan |

### Express count correlations

The two count types threshold sightings of a single rule with the same event-time windows used for native TQL detections. The example data sets are simplified sightings carrying `time`, `host`, `user`, and `rule`; in production these values come from Detection Finding fields such as `device.hostname` and `finding_info.analytic.uid`. The examples use fixed, epoch-aligned time bins; use a hopping window for a sliding interpretation. They also share one event-time clock across hosts and omit `tolerance`. In production, keep [`window`](https://tenzir.com/docs/reference/operators/window.md) on the outside so it bounds keyed state, put [`group`](https://tenzir.com/docs/reference/operators/group.md) inside it when the correlation needs a full keyed subpipeline, and size `tolerance` for ingestion skew.

An `event_count` correlation fires when the same rule matches repeatedly for a group within a window:

```tql
from {time: 2026-07-01T10:00:00Z, host: "ws-17", rule: "print-dump"},
     {time: 2026-07-01T10:02:00Z, host: "ws-17", rule: "print-dump"},
     {time: 2026-07-01T10:04:00Z, host: "ws-17", rule: "print-dump"},
     {time: 2026-07-01T10:05:00Z, host: "ws-9", rule: "print-dump"}
window size=10min, on=time {
  summarize host, rule, matches=count()
  where matches >= 3
  start = $window.start
  end = $window.end
}
```

```tql
{
  host: "ws-17",
  rule: "print-dump",
  matches: 3,
  start: 2026-07-01T10:00:00Z,
  end: 2026-07-01T10:10:00Z,
}
```

A `value_count` correlation counts distinct values of a field instead, for example flagging a host where at least three different users trip the same rule within five minutes:

```tql
from {time: 2026-07-01T10:00:00Z, host: "ws-17", user: "alice", rule: "print-dump"},
     {time: 2026-07-01T10:01:00Z, host: "ws-17", user: "bob", rule: "print-dump"},
     {time: 2026-07-01T10:03:00Z, host: "ws-17", user: "carol", rule: "print-dump"},
     {time: 2026-07-01T10:04:00Z, host: "ws-9", user: "alice", rule: "print-dump"}
window size=5min, on=time {
  summarize host, rule, users=count_distinct(user)
  where users >= 3
}
```

```tql
{
  host: "ws-17",
  rule: "print-dump",
  users: 3,
}
```

The two temporal types combine sightings of different rules into a composite verdict; the guide on [creating multi-stage detectors](create-multi-stage-detectors.md) builds them out together with cross-stage state and suppression.

## See Also

* [Detections](../../explanations/detections.md)
* [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md)
* [`where`](https://tenzir.com/docs/reference/operators/where.md)
* [`window`](https://tenzir.com/docs/reference/operators/window.md)
* [`group`](https://tenzir.com/docs/reference/operators/group.md)
* [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md)
* [`parse_winlog`](https://tenzir.com/docs/reference/functions/parse_winlog.md)
* [`count_distinct`](https://tenzir.com/docs/reference/functions/count_distinct.md)
* [Match events with TQL](match-events-with-tql.md)
* [Model detections in OCSF](model-detections-in-ocsf.md)
* [Detect over time windows](detect-over-time-windows.md)
* [Create multi-stage detectors](create-multi-stage-detectors.md)
* [Map to OCSF](../normalization/map-to-ocsf.md)
* [Microsoft Windows Event Logs](../../integrations/microsoft/windows-event-logs.md)
