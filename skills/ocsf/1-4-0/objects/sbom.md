# Software Bill of Materials (sbom)

The Software Bill of Materials object describes characteristics of a generated SBOM.

- **Extends**: `object`

## Attributes

### `created_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended

The time when the SBOM was created.

### `package`

- **Type**: `package`
- **Requirement**: required

The device software that is being discovered by an inventory process.

### `product`

- **Type**: `product`
- **Requirement**: recommended

The product that generated the SBOM e.g. cdxgen or Syft.

### `software_components`

- **Type**: `software_component`
- **Requirement**: required

The list of software components used in the software package.
