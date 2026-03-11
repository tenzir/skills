# save_s3


Saves bytes to an Amazon S3 object.

```tql
save_s3 uri:str, [anonymous=bool, aws_iam=record]
```

## Description

The `save_s3` operator writes bytes to an S3 object in an S3 bucket.

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

Whether to ignore any predefined credentials and try to save with anonymous credentials.

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
}
```

The `access_key_id` and `secret_access_key` must be specified together. If neither is specified, the operator uses the default AWS credential chain:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. Shared credentials file (`~/.aws/credentials`)
3. IAM role for Amazon EC2 or ECS task role
4. Instance metadata service

## Examples

Read CSV from an object `obj.csv` in the bucket `examplebucket` and save it as YAML to another bucket `examplebucket2`:

```tql
load_s3 "s3://examplebucket/obj.csv"
read_csv
write_yaml
save_s3 "s3://examplebucket2/obj.yaml"
```

## See Also

* [`load_s3`](/reference/operators/load_s3.md)
* [`to_amazon_security_lake`](/reference/operators/to_amazon_security_lake.md)
* [S3](../../integrations/amazon/s3.md)