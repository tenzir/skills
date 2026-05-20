# from_amazon_cloudwatch


Reads events from Amazon CloudWatch.

```tql
from_amazon_cloudwatch group:string|list<string>, [mode=string,
  stream=string|list<string>, stream_prefix=string, filter=string,
  start=time, end=time, count=int, from_start=bool, unmask=bool,
  aws_region=string, aws_iam=record]
```

## Description

The `from_amazon_cloudwatch` operator reads CloudWatch events and emits one event per log entry.

The emitted events use the `tenzir.cloudwatch` schema:

| Field            | Type     | Description                           |
| ---------------- | -------- | ------------------------------------- |
| `timestamp`      | `time`   | The CloudWatch event timestamp.       |
| `ingestion_time` | `time`   | The CloudWatch ingestion timestamp.   |
| `log_group`      | `string` | The log group that contains the log.  |
| `log_stream`     | `string` | The log stream that contains the log. |
| `message`        | `string` | The log message.                      |
| `event_id`       | `string` | The CloudWatch event ID, if present.  |

### `group: string|list<string>`

Log group name or identifier to read from.

Use log group ARNs with `mode="live"`. Live mode accepts at most 10 log groups. Use a list only with `mode="live"`; historical modes require exactly one log group.

### `mode = string (optional)`

Read mode.

Supported values:

* `live`: Subscribe with CloudWatch Live Tail for continuous processing of new events. This mode doesn’t read historical events.
* `search`: Search historical events in one log group with `FilterLogEvents`. Use this mode for investigations, bounded backfills, and exports across one or more streams in the group.
* `replay`: Replay one known log stream with `GetLogEvents`. This mode requires exactly one `stream`.

Defaults to `live`. For detailed mode selection guidance, see [CloudWatch](../../integrations/amazon/cloudwatch.md).

### `stream = string|list<string> (optional)`

Log stream name or names to read.

In `mode="replay"`, this option is required and must name exactly one stream. In `mode="live"` and `mode="search"`, this option narrows the read to one or more streams. In live mode, `stream` requires exactly one `group`. Live and search modes accept at most 100 streams.

This option is mutually exclusive with `stream_prefix`.

### `stream_prefix = string (optional)`

Non-empty prefix for selecting log streams in `mode="live"` or `mode="search"`.

This option is mutually exclusive with `stream`. In live mode, `stream_prefix` requires exactly one `group`.

### `filter = string (optional)`

CloudWatch filter pattern.

This option isn’t valid with `mode="replay"`.

### `start = time (optional)`

Earliest event timestamp to read in `mode="search"` or `mode="replay"`.

### `end = time (optional)`

Latest event timestamp to read in `mode="search"` or `mode="replay"`.

### `count = int (optional)`

Maximum number of events to read in `mode="search"` or `mode="replay"`.

The maximum value is `2147483647`.

### `from_start = bool (optional)`

Whether `mode="replay"` should read from the start of the log stream.

### `unmask = bool (optional)`

Whether to unmask protected log data when the AWS principal has permission.

This option is valid for `mode="search"` and `mode="replay"`.

### `aws_region = string (optional)`

AWS region for CloudWatch requests.

If omitted, the operator uses the region from `aws_iam` when present. Otherwise, it uses the AWS SDK’s default region resolution.

### `aws_iam = record (optional)`

Configures explicit AWS credentials or IAM role assumption. If not specified, the operator uses the default AWS credential chain.

```tql
{
  region: string,        // AWS region for API requests.
  access_key_id: string, // AWS access key ID.
  secret_access_key: string, // AWS secret access key.
  session_token: string, // session token for temporary credentials.
  assume_role: string,   // ARN of IAM role to assume.
  session_name: string,  // session name for role assumption.
  external_id: string,   // external ID for role assumption.
  web_identity: record,  // OIDC web identity token configuration.
}
```

The `access_key_id` and `secret_access_key` must be specified together. If neither is specified, the operator uses the default AWS credential chain:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. Shared credentials file (`~/.aws/credentials`)
3. IAM role for Amazon EC2 or ECS task role
4. Instance metadata service

#### Web identity authentication

The `web_identity` option enables OIDC-based authentication using the AWS `AssumeRoleWithWebIdentity` API. This lets you authenticate with AWS resources using OpenID Connect tokens from external identity providers like Azure, Google Cloud, or custom OIDC endpoints.

When `web_identity` is specified, you must also provide `assume_role` with the ARN of the IAM role configured to trust your identity provider.

The `web_identity` record accepts the following fields:

```tql
{
  token_file: string,       // path to file containing the JWT token.
  token_endpoint: {         // HTTP endpoint configuration.
    url: string,            // endpoint URL to fetch tokens from.
    headers: record,        // HTTP headers for the request.
    path: string,           // JSON path to extract token from response.
  },
  token: string,            // direct token value.
}
```

Exactly one of `token_file`, `token_endpoint`, or `token` must be specified:

* `token_file`: Path to a file containing the JWT token. This is the standard approach for Kubernetes workload identity (EKS, AKS, GKE) where the platform mounts a token file into the pod.

* `token_endpoint`: Configuration for fetching tokens from an HTTP endpoint. Use this for Azure IMDS or similar metadata services. The nested record contains:

  * `url` (required): The HTTP endpoint URL that returns a token, such as `http://169.254.169.254/metadata/identity/oauth2/token?...` for Azure IMDS.

  * `headers`: HTTP headers to include in the token request. For Azure IMDS, you typically need `{Metadata: "true"}`.

  * `path`: JSON path to extract the token from the endpoint response. Defaults to `.access_token`. Set to `null` for endpoints that return the token as plain text.

* `token`: Direct token value as a string. Useful for testing or when the token is available from another source.

Credentials are automatically refreshed before expiration, with exponential backoff retry logic for transient failures.

## Examples

### Live tail a log group

```tql
from_amazon_cloudwatch \
  "arn:aws:logs:us-east-1:123456789012:log-group:/aws/vpc/flowlogs"
```

### Live tail multiple log groups

```tql
from_amazon_cloudwatch [
  "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/api",
  "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/worker",
],
  filter="ERROR"
```

### Search historical events

```tql
from_amazon_cloudwatch "/aws/lambda/api",
  mode="search",
  filter="ERROR",
  start=2026-05-14T00:00:00Z,
  end=2026-05-14T01:00:00Z
```

### Replay one log stream

```tql
from_amazon_cloudwatch "/aws/lambda/api",
  mode="replay",
  stream="2026/05/14/[$LATEST]abcdef",
  from_start=true
```

### Assume an IAM role

```tql
from_amazon_cloudwatch "/aws/lambda/api",
  mode="search",
  aws_iam={
    region: "us-east-1",
    assume_role: "arn:aws:iam::123456789012:role/cloudwatch-reader"
  }
```

## See Also

* [`to_amazon_cloudwatch`](/reference/operators/to_amazon_cloudwatch.md)
* [CloudWatch](../../integrations/amazon/cloudwatch.md)