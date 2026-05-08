# to_s3


Writes events to one or multiple objects in Amazon S3.

```tql
to_s3 url:string, [anonymous=bool, aws_iam=record, max_size=int,
      timeout=duration, partition_by=list<field>] { … }
```

## Description

The `to_s3` operator writes events to Amazon S3, automatically opening new objects when a rotation condition triggers. It supports hive-style partitioning through a `**` placeholder in the URL and per-partition unique object keys through a `{uuid}` placeholder.

By default, authentication is handled by AWS’s default credentials provider chain, which may read from multiple environment variables and credential files:

* `~/.aws/credentials` and `~/.aws/config`
* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
* `AWS_SESSION_TOKEN`
* EC2 instance metadata service
* ECS container credentials

### `url: string`

URL identifying the S3 location where data should be written.

Supported URI format: `s3://[<access-key>:<secret-key>@]<bucket-name>/<full-path-to-object>(?<options>)`

Options can be appended to the path as query parameters:

* `region`: AWS region (e.g., `us-east-1`)
* `scheme`: Connection scheme (`http` or `https`)
* `endpoint_override`: Custom S3-compatible endpoint
* `allow_bucket_creation`: Allow creating buckets if they don’t exist
* `allow_bucket_deletion`: Allow deleting buckets

The path portion may contain two placeholders:

* `**` marks the location where hive partition segments are inserted. When present, `partition_by` must also be set, and vice versa.
* `{uuid}` expands to a fresh UUIDv7 for every object. This is required when partitioning or when rotation can produce multiple objects, so that rotated or per-partition objects do not overwrite each other.

### `anonymous = bool (optional)`

Use anonymous credentials instead of any configured authentication.

Defaults to `false`.

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

### `max_size = int (optional)`

Rotates to a new file after the current file exceeds this size in bytes. Because rotation only fires after the threshold is crossed, individual files may be slightly larger than `max_size`.

Defaults to `100M`.

### `timeout = duration (optional)`

Rotates to a new file after the current file has been open for this duration. Rotation is measured from the time the file was first opened.

Defaults to `5min`.

### `partition_by = list<field> (optional)`

A list of fields used to partition events into separate files. For every distinct combination of partition-field values, a separate file (or group of rotated files) is written. The URL must contain a `**` placeholder, which is replaced by the hive-style path `field1=value1/field2=value2/…`.

Unlike [`to_hive`](/reference/operators/to_hive.md), the partitioning fields are **not** stripped from the written events — they remain in each record.

### `{ … }`

Pipeline that transforms the incoming events into the byte stream that is written to each file. The pipeline must return bytes, so it must end with a writer such as `write_ndjson`, `write_parquet`, or `write_csv`, optionally followed by a compressor such as `compress_gzip`.

The subpipeline runs once per output file. When rotation or partitioning produces a new file, a new instance of the subpipeline is spawned for it.

## Examples

### Write a single NDJSON object to S3

```tql
to_s3 "s3://my-bucket/events/out_{uuid}.json" {
  write_ndjson
}
```

### Partition events by date into Parquet objects

```tql
to_s3 "s3://my-bucket/events/**/data_{uuid}.parquet",
  partition_by=[year, month, day] {
  write_parquet
}
// Produces objects under:
//   s3://my-bucket/events/year=<year>/month=<month>/day=<day>/data_<uuid>.parquet
```

### Write with explicit credentials

```tql
to_s3 "s3://my-bucket/data/out_{uuid}.json",
  aws_iam={
    access_key_id: "AKIAIOSFODNN7EXAMPLE",
    secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  } {
  write_ndjson
}
```

### Write to an S3-compatible endpoint

```tql
to_s3 "s3://my-bucket/data/out_{uuid}.json?endpoint_override=minio.example.com:9000&scheme=http" {
  write_ndjson
}
```

### Rotate to a new object every 10 MB

```tql
to_s3 "s3://my-bucket/logs/events_{uuid}.json.gz", max_size=10M {
  write_ndjson
  compress_gzip
}
```

## See Also

* [`from_s3`](/reference/operators/from_s3.md)
* [`to_s3`](/reference/operators/to_s3.md)
* [`to_file`](/reference/operators/to_file.md)
* [`to_hive`](/reference/operators/to_hive.md)
* [S3](../../integrations/amazon/s3.md)