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
}
```

The `access_key_id` and `secret_access_key` must be specified together. If neither is specified, the operator uses the default AWS credential chain:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. Shared credentials file (`~/.aws/credentials`)
3. IAM role for Amazon EC2 or ECS task role
4. Instance metadata service

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

* [`load_sqs`](load_sqs.md)
* [SQS](../../integrations/amazon/sqs.md)