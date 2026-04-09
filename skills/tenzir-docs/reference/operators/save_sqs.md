# save_sqs


Saves bytes to [Amazon SQS](https://docs.aws.amazon.com/sqs/) queues.

```tql
save_sqs queue:str, [poll_time=duration, aws_iam=record]
```

## Description

[Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/sqs/) is a fully managed message queuing service to decouple and scale microservices, distributed systems, and serverless applications. The `save_sqs` operator writes bytes as messages into an SQS queue.

The `poll_time` parameter configures request timeouts for the underlying AWS SDK client.

The operator requires the following AWS permissions:

* `sqs:GetQueueUrl`
* `sqs:SendMessage`

### `queue: str`

The name of the queue to use.

### `poll_time = duration (optional)`

The request timeout for AWS SDK operations.

The value must be between 1 and 20 seconds.

Defaults to `3s`.

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

Write JSON messages from a source feed to the SQS queue `tenzir`:

```tql
subscribe "to-sqs"
write_json
save_sqs "tenzir"
```

Send messages using explicit credentials:

```tql
from {alert: "security event detected"}
write_json
save_sqs "alerts-queue", aws_iam={
  region: "us-east-1",
  access_key_id: secret("aws-key"),
  secret_access_key: secret("aws-secret")
}
```

Send messages by assuming an IAM role:

```tql
subscribe "events"
write_json
save_sqs "my-queue", aws_iam={
  region: "eu-west-1",
  assume_role: "arn:aws:iam::123456789012:role/my-sqs-role"
}
```

## See Also

* [`load_sqs`](/reference/operators/load_sqs.md)
* [SQS](../../integrations/amazon/sqs.md)