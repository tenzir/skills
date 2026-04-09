# from_s3


Reads one or multiple files from Amazon S3.

```tql
from_s3 url:string, [anonymous=bool, aws_iam=record, watch=bool,
  remove=bool, rename=string->string, path_field=field, max_age=duration] { … }
```

## Description

The `from_s3` operator reads files from Amazon S3, with support for glob patterns, automatic format detection, and file monitoring.

By default, authentication is handled by AWS’s default credentials provider chain, which may read from multiple environment variables and credential files:

* `~/.aws/credentials` and `~/.aws/config`
* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
* `AWS_SESSION_TOKEN`
* EC2 instance metadata service
* ECS container credentials

### `url: string`

URL identifying the S3 location where data should be read from.

The characters `*` and `**` have a special meaning. `*` matches everything except `/`. `**` matches everything including `/`. The sequence `/**/` can also match nothing. For example, `bucket/**/data` matches `bucket/data`.

Supported URI format: `s3://[<access-key>:<secret-key>@]<bucket-name>/<full-path-to-object>(?<options>)`

Options can be appended to the path as query parameters:

* `region`: AWS region (e.g., `us-east-1`)
* `scheme`: Connection scheme (`http` or `https`)
* `endpoint_override`: Custom S3-compatible endpoint
* `allow_bucket_creation`: Allow creating buckets if they don’t exist
* `allow_bucket_deletion`: Allow deleting buckets

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

### `watch = bool (optional)`

In addition to processing all existing files, this option keeps the operator running, watching for new files that also match the given URL. Currently, this scans the filesystem up to every 10s.

Defaults to `false`.

### `remove = bool (optional)`

Deletes files after they have been read completely.

This also cleans up directory marker objects (zero-byte objects with keys ending in \`/\`) encountered while globbing. These markers are artifacts from some tools and can accumulate over time, increasing API costs. Removing them does not affect other files.

Defaults to `false`.

### `rename = string -> string (optional)`

Renames files after they have been read completely. The lambda function receives the original path as an argument and must return the new path.

If the target path already exists, the operator will overwrite the file.

The operator automatically creates any intermediate directories required for the target path. If the target path ends with a trailing slash (`/`), the original filename will be automatically appended to create the final path.

### `path_field = field (optional)`

This makes the operator insert the path to the file where an event originated from before emitting it.

By default, paths will not be inserted into the outgoing events.

### `max_age = duration (optional)`

Only process files that were modified within the specified duration from the current time. Files older than this duration will be skipped.

### `{ … } (optional)`

Pipeline to use for parsing the file. By default, this pipeline is derived from the path of the file, and will not only handle parsing but also decompression if applicable.

## Examples

### Read every JSON file from a bucket

```tql
from_s3 "s3://my-bucket/data/**.json"
```

### Read CSV files using explicit credentials

```tql
from_s3 "s3://my-bucket/data.csv", aws_iam={
  access_key_id: "AKIAIOSFODNN7EXAMPLE",
  secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}
```

### Read from S3-compatible service with custom endpoint

```tql
from_s3 "s3://my-bucket/data/**.json?endpoint_override=minio.example.com:9000&scheme=http"
```

### Read files continuously and assume IAM role

```tql
from_s3 "s3://logs/application/**.json", watch=true, aws_iam={
  assume_role: "arn:aws:iam::123456789012:role/LogReaderRole"
}
```

### Process files and move them to an archive bucket

```tql
from_s3 "s3://input-bucket/**.json",
  rename=(path => "archive/" + path)
```

### Add source path to events

```tql
from_s3 "s3://data-bucket/**.json", path_field=source_file
```

### Read Zeek logs with anonymous access

```tql
from_s3 "s3://public-bucket/zeek/**.log", anonymous=true {
  read_zeek_tsv
}
```

## See Also

* [`from_file`](/reference/operators/from_file.md)
* [`load_s3`](/reference/operators/load_s3.md)
* [`save_s3`](/reference/operators/save_s3.md)
* [S3](../../integrations/amazon/s3.md)