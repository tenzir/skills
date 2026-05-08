# to_sqs


Sends messages to an [Amazon SQS](https://docs.aws.amazon.com/sqs/) queue.

```tql
to_sqs queue:str, [message=str|blob, aws_region=str, aws_iam=record]
```

## Description

[Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/sqs/) is a fully managed message queueing service for decoupling distributed systems. The `to_sqs` operator sends one SQS message per input event.

By default, `to_sqs` serializes each input event as NDJSON. Use the `message` option to send a specific string or blob expression instead. If the expression evaluates to `null` or another type, the operator skips that event and emits a warning.

The operator requires the following AWS permissions:

* `sqs:GetQueueUrl` (only when passing a queue name; not required for URLs)
* `sqs:SendMessage`

### `queue: str`

The name of the queue to send messages to. You can optionally prefix the queue name with `sqs://`.

You can also pass a full queue URL (`https://...` or `http://...`) instead of a name. When a URL is given, the operator skips the `GetQueueUrl` lookup and talks to the URL’s host directly. Set `aws_region` when the queue is in a non-default AWS region so SigV4 signing matches.

### `message = str | blob (optional)`

The expression that produces the SQS message body.

Defaults to `this.print_ndjson()`.

### `aws_region = str (optional)`

The AWS region for resolving the queue URL and sending messages.

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

### Send events to a queue

```tql
subscribe "to-sqs"
to_sqs "sqs://tenzir"
```

### Send a specific field as the message body

```tql
from {payload: "security event detected"}
to_sqs "alerts-queue", message=payload
```

### Use an explicit region

```tql
from {alert: "security event detected"}
to_sqs "alerts-queue", aws_region="us-east-1"
```

### Pass a queue URL directly

```tql
from {alert: "security event detected"}
to_sqs "https://sqs.eu-west-1.amazonaws.com/123456789012/alerts-queue",
  aws_region="eu-west-1"
```

### Use explicit credentials

```tql
from {alert: "security event detected"}
to_sqs "alerts-queue", aws_iam={
  region: "us-east-1",
  access_key_id: secret("aws-key"),
  secret_access_key: secret("aws-secret")
}
```

### Assume an IAM role

```tql
subscribe "events"
to_sqs "my-queue", aws_iam={
  region: "eu-west-1",
  assume_role: "arn:aws:iam::123456789012:role/my-sqs-role"
}
```

## See Also

* [`from_sqs`](/reference/operators/from_sqs.md)
* [Send to destinations](../../guides/routing/send-to-destinations.md)
* [SQS](../../integrations/amazon/sqs.md)