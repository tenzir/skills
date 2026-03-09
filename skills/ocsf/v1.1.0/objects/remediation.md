# Remediation (remediation)

The Remediation object describes the recommended remediation steps to address identified issue(s).

- **Extends**: `object`

## Attributes

### `desc`

- **Type**: `string_t`
- **Requirement**: required

The description of the remediation strategy.

### `references`

- **Type**: `string_t`
- **Requirement**: optional

A list of supporting URL/s, references that help describe the remediation strategy.

### `kb_articles`

- **Type**: `string_t`
- **Requirement**: optional

The KB article/s related to the entity. A KB Article contains metadata that describes the patch or an update.

### `kb_article_list`

- **Type**: [`kb_article`](kb_article.md)
- **Requirement**: optional

A list of KB articles or patches related to an endpoint. A KB Article contains metadata that describes the patch or an update.
