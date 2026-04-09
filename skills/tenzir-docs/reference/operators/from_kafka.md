# from_kafka


Receives events from an Apache Kafka topic.

```tql
from_kafka topic:string, [count=int, exit=bool, offset=int|string, options=record,
           aws_iam=record, aws_region=string, commit_batch_size=int]
```

## Description

The `from_kafka` operator consumes messages from a Kafka topic and produces events containing the message payload as a string field.

The implementation uses the official [librdkafka](https://github.com/confluentinc/librdkafka) from Confluent and supports all [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md). You can specify them via `options` parameter as `{key: value, ...}`.

The operator injects the following default librdkafka configuration values in case no configuration file is present, or when the configuration does not include them:

* `bootstrap.servers`: `localhost`
* `client.id`: `tenzir`
* `group.id`: `tenzir`
* `enable.auto.commit`: `false` (This option cannot be changed)

Each consumed message is produced as an event with the following schema:

```tql
{
  message: string
}
```

### `topic: string`

The Kafka topic to consume from.

### `count = int (optional)`

Exit successfully after having consumed `count` messages.

### `exit = bool (optional)`

Exit successfully after having received the last message from all partitions.

Without this option, the operator waits for new messages after consuming the last one.

### `offset = int|string (optional)`

The offset to start consuming from. Possible values are:

* `"beginning"`: first offset
* `"end"`: last offset
* `"stored"`: stored offset
* `<value>`: absolute offset
* `-<value>`: relative offset from end

The default is `"stored"`.

### `options = record (optional)`

A record of key-value configuration options for [librdkafka](https://github.com/confluentinc/librdkafka), e.g., `{"auto.offset.reset" : "earliest", "enable.partition.eof": true}`.

The `from_kafka` operator passes the key-value pairs directly to [librdkafka](https://github.com/confluentinc/librdkafka). Consult the list of available [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md) to configure Kafka according to your needs.

We recommend factoring these options into the plugin-specific `kafka.yaml` so that they are independent of the `from_kafka` arguments.

### `commit_batch_size = int (optional)`

The operator commits offsets after receiving `commit_batch_size` messages to improve throughput. If you need to ensure exactly-once semantics for your pipeline, set this option to `1` to commit every message individually.

Defaults to `1000`.

## Amazon MSK

The operator supports [Amazon MSK](../../integrations/amazon/msk.md) with IAM authentication.

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

### `aws_region = string (optional)`

The AWS region used to construct the MSK authentication URL. Required when connecting to MSK with IAM authentication.

### Consume from MSK using AWS IAM authentication

```tql
from_kafka "security-logs",
  options={"bootstrap.servers": "my-cluster.kafka.us-east-1.amazonaws.com:9098"},
  aws_iam={region: "us-east-1"}
```

## Examples

### Consume JSON messages and parse them

```tql
from_kafka "logs"
message = message.parse_json()
```

### Consume 100 messages starting from the beginning

```tql
from_kafka "events", count=100, offset="beginning"
```

### Consume messages and exit when caught up

```tql
from_kafka "alerts", exit=true
```

## See Also

* [`to_kafka`](/reference/operators/to_kafka.md)
* [Kafka](../../integrations/kafka.md)