# save_kafka


Saves a byte stream to a Apache Kafka topic.

```tql
save_kafka topic:string, [key=string, timestamp=time, options=record,
           aws_iam=record, aws_region=string]
```

## Description

Deprecated

The `save_kafka` operator does not respect event boundaries and can combine multiple events into a single message, causing issues for consumers. Consider using [`to_kafka`](/reference/operators/to_kafka.md) instead.

The `save_kafka` operator saves bytes to a Kafka topic.

The implementation uses the official [librdkafka](https://github.com/confluentinc/librdkafka) from Confluent and supports all [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md). You can specify them via `options` parameter as `{key: value, ...}`.

The operator injects the following default librdkafka configuration values in case no configuration file is present, or when the configuration does not include them:

* `bootstrap.servers`: `localhost`
* `client.id`: `tenzir`
* `group.id`: `tenzir`

### `topic: string`

The Kafka topic to use.

### `key = string (optional)`

Sets a fixed key for all messages.

### `timestamp = time (optional)`

Sets a fixed timestamp for all messages.

### `options = record (optional)`

A record of key-value configuration options for [librdkafka](https://github.com/confluentinc/librdkafka), e.g., `{"auto.offset.reset" : "earliest", "enable.partition.eof": true}`.

The `save_kafka` operator passes the key-value pairs directly to [librdkafka](https://github.com/confluentinc/librdkafka). Consult the list of available [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md) to configure Kafka according to your needs.

We recommend factoring these options into the plugin-specific `kafka.yaml` so that they are independent of the `save_kafka` arguments.

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

## Examples

### Write the Tenzir version to topic `tenzir` with timestamp from the past

```tql
version
write_json
save_kafka "tenzir", timestamp=1984-01-01
```

### Follow a CSV file and publish it to topic `data`

```tql
load_file "/tmp/data.csv"
read_csv
write_json
save_kafka "data"
```

## See Also

* [`from_kafka`](/reference/operators/from_kafka.md)
* [`to_kafka`](/reference/operators/to_kafka.md)
* [Kafka](../../integrations/kafka.md)