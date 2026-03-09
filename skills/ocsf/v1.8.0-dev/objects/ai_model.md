# AI Model (ai_model)

The AI Model object describes the characteristics of an AI/ML model. Examples include language models like GPT-4, embedding models like text-embedding-ada-002, and computer vision models like CLIP.

- **Extends**: `_entity`

## Attributes

### `name`

- **Type**: `string_t`
- **Requirement**: required

Human-readable model name. For example: `gpt-4o`, `claude-3-sonnet`, or `text-embedding-ada-002`.

### `ai_provider`

- **Type**: `string_t`
- **Requirement**: required

AI service provider or organization name. For example: `OpenAI`, `Anthropic`, `Google`, or `Internal`.

### `version`

- **Type**: `string_t`
- **Requirement**: recommended

Model version identifier. For example: `2024-05-13`, `v2.1.0`, or `beta`.

### `uid`

- **Type**: `string_t`

The unique identifier of the AI model.
