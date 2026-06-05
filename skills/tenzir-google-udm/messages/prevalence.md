# Prevalence

The prevalence of a resource within the customer's environment. This measures how common it is for assets to access the resource.

## Fields

### `rolling_max` / `rollingMax`

- Type: `int32` (singular)

The maximum number of assets per day accessing the resource over the trailing day_count days.

### `day_count` / `dayCount`

- Type: `int32` (singular)

The number of days over which rolling_max is calculated.

### `rolling_max_sub_domains` / `rollingMaxSubDomains`

- Type: `int32` (singular)

The maximum number of assets per day accessing the domain along with sub-domains over the trailing day_count days. This field is only valid for domains.

### `day_max` / `dayMax`

- Type: `int32` (singular)

The max prevalence score in a day interval window.

### `day_max_sub_domains` / `dayMaxSubDomains`

- Type: `int32` (singular)

The max prevalence score in a day interval window across sub-domains. This field is only valid for domains.
