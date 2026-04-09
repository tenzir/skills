# load_s3


Loads from an Amazon S3 object.

```tql
load_s3 uri:str, [anonymous=bool, aws_iam=record]
```

## Description

The `load_s3` operator connects to an S3 bucket to acquire raw bytes from an S3 object.

The connector tries to retrieve the appropriate credentials using AWS’s [default credentials provider chain](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Note

Make sure to configure AWS credentials for the same user account that runs `tenzir` and `tenzir-node`. The AWS CLI creates configuration files for the current user under `~/.aws`, which can only be read by the same user account.

The `tenzir-node` systemd unit by default creates a `tenzir` user and runs as that user, meaning that the AWS credentials must also be configured for that user. The directory `~/.aws` must be readable for the `tenzir` user.

If a config file `<prefix>/etc/tenzir/plugin/s3.yaml` or `~/.config/tenzir/plugin/s3.yaml` exists, it is always preferred over the default AWS credentials. The configuration file must have the following format:

```yaml
access-key: your-access-key
secret-key: your-secret-key
session-token: your-session-token (optional)
```

### `uri: str`

The path to the S3 object.

The syntax is `s3://[<access-key>:<secret-key>@]<bucket-name>/<full-path-to-object>(?<options>)`.

Options can be appended to the path as query parameters, as per [Arrow](https://arrow.apache.org/docs/r/articles/fs.html#connecting-directly-with-a-uri):

> For S3, the options that can be included in the URI as query parameters are `region`, `scheme`, `endpoint_override`, `allow_bucket_creation`, and `allow_bucket_deletion`.

### `anonymous = bool (optional)`

Whether to ignore any predefined credentials and try to load with anonymous credentials.

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

Read CSV from an object `obj.csv` in the bucket `examplebucket`:

```tql
load_s3 "s3://examplebucket/obj.csv"
read_csv
```

Read JSON from an object `test.json` in the bucket `examplebucket`, but using a different, S3-compatible endpoint:

```tql
load_s3 "s3://examplebucket/test.json?endpoint_override=s3.us-west.mycloudservice.com"
read_json
```

## See Also

* [`save_s3`](/reference/operators/save_s3.md)
* [S3](../../integrations/amazon/s3.md)