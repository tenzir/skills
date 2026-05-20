# to_amazon_cloudwatch


Sends events to Amazon CloudWatch Logs.

```tql
to_amazon_cloudwatch group:string, stream=string, [method=string,
  payload=string|blob, timestamp=time, batch_timeout=duration, batch_size=int,
  parallel=int, token=secret, endpoint=string, aws_region=string,
  aws_iam=record]
```

## Description

The `to_amazon_cloudwatch` operator writes events to an existing CloudWatch log group and stream. By default, it uses the AWS `PutLogEvents` API. Set `method` to use a CloudWatch Logs HTTP ingestion endpoint instead.

### `group: string`

Name of the CloudWatch log group.

The operator expects the log group to already exist.

### `stream = string`

Name of the CloudWatch log stream.

The operator expects the log stream to already exist.

### `method = string (optional)`

CloudWatch write method.

Defaults to `put`.

Supported values:

* `put`: Use the AWS `PutLogEvents` API. This method uses AWS IAM.
* `hlc`: Use the CloudWatch HTTP Log Collector endpoint.
* `ndjson`: Use the CloudWatch NDJSON endpoint.
* `json`: Use the CloudWatch structured JSON endpoint.

The `otlp` endpoint is not supported by this operator.

### `payload = string|blob (optional)`

Expression that computes the log message for each event.

Defaults to the incoming event serialized as NDJSON.

### `timestamp = time (optional)`

Expression that computes the CloudWatch event timestamp.

Defaults to a `timestamp` field when present. Otherwise, the operator uses the processing time.

### `batch_timeout = duration (optional)`

Maximum time to keep events in a batch before flushing them.

Defaults to `1s`.

### `batch_size = int (optional)`

Maximum number of events per batch.

Defaults to `1000`.

### `parallel = int (optional)`

Maximum number of in-flight write requests.

Defaults to `1`.

CloudWatch no longer requires sequence tokens for `PutLogEvents`, so you can raise this value for higher throughput to the same stream.

### `endpoint = string (optional)`

CloudWatch Logs endpoint override.

Use this option for tests or compatible deployments that need an explicit endpoint. For HTTP ingestion methods, the operator appends the method-specific path to this endpoint.

### `token = secret (optional)`

Bearer token for HTTP ingestion methods.

Do not use `token` with `method="put"`. When omitted for an HTTP ingestion method, the operator signs requests with AWS IAM.

Bearer-token HTTP ingestion requires a CloudWatch log group that is configured for bearer-token authentication. The log group and stream must already exist. The IAM user behind the bearer token needs `logs:CallWithBearerToken` and `logs:PutLogEvents`. AWS currently supports bearer-token authentication for CloudWatch HTTP ingestion only in `us-east-1`, `us-east-2`, `us-west-1`, and `us-west-2`.

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

## Batching

The operator sorts each batch by timestamp and enforces CloudWatch limits before sending:

* At most 10,000 events per request.
* At most 1 MiB per request, counted as UTF-8 message bytes plus 26 bytes per event.
* A maximum timestamp span of 24 hours within one request.
* No events more than 2 hours in the future or older than 14 days.

Events that exceed CloudWatch event size or timestamp limits are skipped with a warning.

For HTTP ingestion methods, the operator skips individual events larger than 256 KiB and batches accepted events into one HTTP request until the request reaches the 1 MiB limit.

## Examples

### Write events to a log stream

```tql
from {message: "hello"}
to_amazon_cloudwatch "/tenzir/events",
  stream="default",
  payload=message
```

### Use an event timestamp field

```tql
from {ts: 2026-05-14T00:00:00Z, message: "hello"}
to_amazon_cloudwatch "/tenzir/events",
  stream="default",
  payload=message,
  timestamp=ts
```

### Send through the HTTP Log Collector

```tql
from {message: "hello"}
to_amazon_cloudwatch "/tenzir/events",
  stream="default",
  method="hlc",
  payload=message,
  token=secret("cloudwatch-hlc-token")
```

### Assume an IAM role

```tql
from {message: "hello"}
to_amazon_cloudwatch "/tenzir/events",
  stream="default",
  payload=message,
  aws_iam={
    region: "us-east-1",
    assume_role: "arn:aws:iam::123456789012:role/cloudwatch-writer"
  }
```

## See Also

* [`from_amazon_cloudwatch`](/reference/operators/from_amazon_cloudwatch.md)
* [CloudWatch](../../integrations/amazon/cloudwatch.md)