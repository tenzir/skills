# load_sqs


Loads bytes from [Amazon SQS](https://docs.aws.amazon.com/sqs/) queues.

```tql
load_sqs queue:str, [poll_time=duration, aws_iam=record]
```

## Description

[Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/sqs/) is a fully managed message queuing service to decouple and scale microservices, distributed systems, and serverless applications. The `load_sqs` operator reads bytes from messages of an SQS queue.

The `load_sqs` operator uses long polling, which helps reduce your cost of using SQS by reducing the number of empty responses when there are no messages available to return in reply to a message request. Use the `poll_time` option to adjust the timeout.

The operator requires the following AWS permissions:

* `sqs:GetQueueUrl`
* `sqs:ReceiveMessage`
* `sqs:DeleteMessage`

### `queue: str`

The name of the queue to use.

### `poll_time = duration (optional)`

The long polling timeout per request.

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

Read JSON messages from the SQS queue `tenzir`:

```tql
load_sqs "tenzir"
```

Read JSON messages with a 20-second long poll timeout:

```tql
load_sqs "tenzir", poll_time=20s
```

Read messages using explicit credentials:

```tql
load_sqs "my-queue", aws_iam={
  region: "us-east-1",
  access_key_id: secret("aws-key"),
  secret_access_key: secret("aws-secret")
}
```

Read messages by assuming an IAM role:

```tql
load_sqs "my-queue", aws_iam={
  region: "eu-west-1",
  assume_role: "arn:aws:iam::123456789012:role/my-sqs-role",
  session_name: "tenzir-session"
}
```

## See Also

* [`save_sqs`](save_sqs.md)
* [SQS](../../integrations/amazon/sqs.md)