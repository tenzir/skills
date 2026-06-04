# Prevalence

The prevalence of a resource within the customer's environment. This measures how common it is for assets to access the resource.

- **Full name**: `google.backstory.Prevalence`
- **Fields**: `5`

## Fields

### `rollingMax`

- Type: `int32` (singular)

The maximum number of assets per day accessing the resource over the trailing dayCount days.

### `dayCount`

- Type: `int32` (singular)

The number of days over which rollingMax is calculated.

### `rollingMaxSubDomains`

- Type: `int32` (singular)

The maximum number of assets per day accessing the domain along with sub-domains over the trailing dayCount days. This field is only valid for domains.

### `dayMax`

- Type: `int32` (singular)

The max prevalence score in a day interval window.

### `dayMaxSubDomains`

- Type: `int32` (singular)

The max prevalence score in a day interval window across sub-domains. This field is only valid for domains.
