# Operating System Patch State (patch_state)

Operating System Patch State reports the installation of an OS patch to a device and any associated knowledgebase articles.

- **UID**: `4`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

An addressable device, computer system or host.

### `kb_article_list`

- **Type**: `kb_article`
- **Requirement**: recommended
- **Group**: primary

A list of KB articles or patches related to an endpoint. A KB Article contains metadata that describes the patch or an update.
