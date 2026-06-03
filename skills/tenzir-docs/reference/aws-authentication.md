# AWS Authentication


Tenzir’s AWS operators authenticate with AWS using the AWS SDK’s default credential chain, an OIDC web identity token, or static credentials. This page describes the shared `aws_iam` option used by [`from_s3`](/reference/operators/from_s3.md), [`to_s3`](/reference/operators/to_s3.md), [`from_sqs`](/reference/operators/from_sqs), [`to_sqs`](/reference/operators/to_sqs), [`from_amazon_cloudwatch`](/reference/operators/from_amazon_cloudwatch.md), [`to_amazon_cloudwatch`](/reference/operators/to_amazon_cloudwatch.md), [`from_kafka`](/reference/operators/from_kafka.md), and [`to_kafka`](/reference/operators/to_kafka.md).

## Local usage with the AWS CLI

When you run `tenzir` locally, the simplest way to authenticate is to reuse the AWS CLI’s configuration. After installing the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), configure your default profile:

```bash
aws configure
```

This writes credentials to `~/.aws/credentials` and settings to `~/.aws/config`. Verify the configuration by calling any AWS API, for example:

```bash
aws sts get-caller-identity
```

Tenzir picks up the same files through the default credential chain, so no further configuration is required:

```tql
from_s3 "s3://my-bucket/data.json"
```

### Named profiles

To use a profile other than `default`, set the `AWS_PROFILE` environment variable before starting `tenzir` or `tenzir-node`:

```bash
export AWS_PROFILE=my-profile
tenzir 'from_s3 "s3://my-bucket/data.json"'
```

Profiles defined in `~/.aws/config` can chain into other profiles, assume roles with MFA, or use SSO. Tenzir transparently follows these mechanisms through the AWS SDK.

### Configuring credentials for the service user

The AWS CLI writes its configuration files under `~/.aws`, which only the owning user can read. Configure credentials for the same user account that runs `tenzir` and `tenzir-node`.

The `tenzir-node` systemd unit by default creates a `tenzir` user and runs as that user, so AWS credentials must be configured for that user and `~/.aws` must be readable by it.

## Ambient credentials

If you omit the `aws_iam` parameter, operators use the AWS SDK’s [default credential provider chain](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/credentials.html), which searches in this order:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, optionally `AWS_SESSION_TOKEN`).
2. Shared credentials and config files (`~/.aws/credentials`, `~/.aws/config`).
3. IAM role for Amazon EC2 or ECS task role.
4. Instance metadata service.

This is the recommended approach on AWS itself: attach an instance profile or task role to the workload and Tenzir picks it up automatically.

## Web identity authentication

For cross-cloud authentication, exchange an OIDC token from an external identity provider (Azure, Google Cloud, a Kubernetes service account, or any custom OIDC issuer) for temporary AWS credentials with `AssumeRoleWithWebIdentity`:

```tql
from_s3 "s3://my-bucket/data.json", aws_iam={
  region: "us-east-1",
  assume_role: "arn:aws:iam::123456789012:role/CrossCloudRole",
  web_identity: {
    token_file: "/var/run/secrets/tokens/aws-token",
  },
}
```

When you set `web_identity`, you must also set `assume_role` to the ARN of the IAM role configured to trust your identity provider.

Exactly one of the following token sources must be specified in `web_identity`:

* **`token_file`**: Path to a file containing the JWT token. This is standard for Kubernetes workload identity (EKS, AKS, GKE) where the platform mounts a service account token into the pod.

* **`token_endpoint`**: Configuration for fetching tokens from an HTTP endpoint. Use this for Azure IMDS or similar metadata services. The nested record contains:

  * `url` (required): The HTTP endpoint URL that returns a token.
  * `headers`: HTTP headers to include in the token request. For Azure IMDS, you typically need `{Metadata: "true"}`.
  * `path`: JSON path to extract the token from the endpoint response. Defaults to `.access_token`. Set to `null` for endpoints that return the token as plain text.

* **`token`**: Direct token value, useful for testing or when the token comes from another source.

Tenzir refreshes credentials automatically before expiration, with exponential backoff retry for transient failures, making this suitable for long-running pipelines.

## Static credentials

Pass an access key and secret directly. The `access_key_id` and `secret_access_key` options must be specified together. Wrap secrets with [`secret`](/reference/functions/secret.md) to keep them out of pipeline definitions:

```tql
from_s3 "s3://my-bucket/data.json", aws_iam={
  region: "us-east-1",
  access_key_id: secret("aws-access-key-id"),
  secret_access_key: secret("aws-secret-access-key"),
}
```

Use `assume_role` with any of the above mechanisms to call `sts:AssumeRole` and adopt a different role for the request:

```tql
from_s3 "s3://my-bucket/data.json", aws_iam={
  region: "us-east-1",
  assume_role: "arn:aws:iam::123456789012:role/MyRole",
  session_name: "tenzir-session",
}
```

The role’s trust policy must allow your active principal (for example an EC2 instance role or a local SSO role) to assume it.

## See Also

* [`from_amazon_cloudwatch`](/reference/operators/from_amazon_cloudwatch.md)
* [`from_kafka`](/reference/operators/from_kafka.md)
* [`from_s3`](/reference/operators/from_s3.md)
* [`from_sqs`](/reference/operators/from_sqs)
* [`to_amazon_cloudwatch`](/reference/operators/to_amazon_cloudwatch.md)
* [`to_amazon_security_lake`](/reference/operators/to_amazon_security_lake.md)
* [`to_kafka`](/reference/operators/to_kafka.md)
* [`to_s3`](/reference/operators/to_s3.md)
* [`to_sqs`](/reference/operators/to_sqs)
* [CloudWatch](../integrations/amazon/cloudwatch.md)
* [MSK](../integrations/amazon/msk.md)
* [S3](../integrations/amazon/s3.md)
* [Security Lake](../integrations/amazon/security-lake.md)
* [SQS](../integrations/amazon/sqs.md)