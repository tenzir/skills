# from_sqs


Receives messages from an [Amazon SQS](https://docs.aws.amazon.com/sqs/) queue.

```tql
from_sqs queue:str, [keep_messages=bool, batch_size=int, poll_time=duration,
                     visibility_timeout=duration, aws_region=str, aws_iam=record]
```

## Description

[Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/sqs/) is a fully managed message queueing service for decoupling distributed systems. The `from_sqs` operator reads messages from an SQS queue and emits one event per message.

The emitted events use the `tenzir.sqs` schema with these fields:

| Field                      | Type     | Description                               |
| -------------------------- | -------- | ----------------------------------------- |
| `message`                  | `string` | The SQS message body.                     |
| `message_id`               | `string` | The SQS message ID.                       |
| `sent_time`                | `time`   | The time when SQS sent the message.       |
| `first_receive_time`       | `time`   | The first time SQS delivered the message. |
| `receive_count`            | `int`    | The approximate receive count.            |
| `sender_id`                | `string` | The sender ID reported by SQS.            |
| `message_group_id`         | `string` | The FIFO message group ID.                |
| `message_deduplication_id` | `string` | The FIFO message deduplication ID.        |
| `sequence_number`          | `string` | The FIFO sequence number assigned by SQS. |

All fields except `message` and `message_id` are optional because SQS only returns them when they are present on the message.

The operator uses long polling, which reduces empty responses when there are no messages available. By default, after the operator emits a message, it deletes the message from the queue.

The operator requires the following AWS permissions:

* `sqs:GetQueueUrl` (only when passing a queue name; not required for URLs)
* `sqs:ReceiveMessage`
* `sqs:DeleteMessage` (unless `keep_messages=true`)

### `queue: str`

The name of the queue to receive messages from. You can optionally prefix the queue name with `sqs://`.

You can also pass a full queue URL (`https://...` or `http://...`) instead of a name. When a URL is given, the operator skips the `GetQueueUrl` lookup and talks to the URL’s host directly. Set `aws_region` when the queue is in a non-default AWS region so SigV4 signing matches.

### `poll_time = duration (optional)`

The long polling timeout per request.

The value must be between `1s` and `20s`.

Defaults to `3s`.

### `batch_size = int (optional)`

The maximum number of messages to receive per SQS request.

The value must be between `1` and `10`.

Defaults to `1`.

### `keep_messages = bool (optional)`

Whether to keep messages in the queue after receiving and emitting them.

Defaults to `false`.

Set this option to `true` to keep received messages in the queue:

```tql
from_sqs "my-queue", keep_messages=true
```

When `keep_messages=true`, SQS hides each received message until the queue’s visibility timeout expires, then makes the message visible again. This option only skips `DeleteMessage`; it doesn’t make downstream processing transactional.

### `visibility_timeout = duration (optional)`

The receive-level visibility timeout for messages returned by SQS.

The value must be between `0s` and `12h`. When omitted, SQS uses the queue’s configured visibility timeout.

Use this option with `keep_messages=true` to control when messages become available for redelivery:

```tql
from_sqs "my-queue", keep_messages=true, visibility_timeout=30s
```

### `aws_region = str (optional)`

The AWS region for resolving the queue URL and receiving messages.

If omitted, the operator uses the region from `aws_iam` when present. Otherwise, it uses the default AWS SDK region resolution.

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

### Receive messages from a queue

```tql
from_sqs "sqs://tenzir"
```

### Parse JSON messages

```tql
from_sqs "sqs://alerts", poll_time=5s, batch_size=10
this = message.parse_json()
```

### Receive messages without deleting them

```tql
from_sqs "sqs://alerts",
  keep_messages=true,
  poll_time=5s,
  batch_size=10,
  visibility_timeout=30s
this = message.parse_json()
```

### Use an explicit region

```tql
from_sqs "my-queue", aws_region="us-east-1"
```

### Pass a queue URL directly

```tql
from_sqs "https://sqs.eu-west-1.amazonaws.com/123456789012/my-queue",
  aws_region="eu-west-1"
```

### Use explicit credentials

```tql
from_sqs "my-queue", aws_iam={
  region: "us-east-1",
  access_key_id: secret("aws-key"),
  secret_access_key: secret("aws-secret")
}
```

### Assume an IAM role

```tql
from_sqs "my-queue", aws_iam={
  region: "eu-west-1",
  assume_role: "arn:aws:iam::123456789012:role/my-sqs-role",
  session_name: "tenzir-session"
}
```

## See Also

* [`to_sqs`](/reference/operators/to_sqs.md)
* [Read from message brokers](../../guides/collecting/read-from-message-brokers.md)
* [SQS](../../integrations/amazon/sqs.md)