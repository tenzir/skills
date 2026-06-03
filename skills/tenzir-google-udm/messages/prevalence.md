# Prevalence

The prevalence of a resource within the customer's environment. This measures how common it is for assets to access the resource.

- **Full name**: `google.backstory.Prevalence`
- **Fields**: `5`

## Fields

### `rolling_max`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `rollingMax`

The maximum number of assets per day accessing the resource over the trailing day_count days.

### `day_count`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `dayCount`

The number of days over which rolling_max is calculated.

### `rolling_max_sub_domains`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `rollingMaxSubDomains`

The maximum number of assets per day accessing the domain along with sub-domains over the trailing day_count days. This field is only valid for domains.

### `day_max`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `dayMax`

The max prevalence score in a day interval window.

### `day_max_sub_domains`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `dayMaxSubDomains`

The max prevalence score in a day interval window across sub-domains. This field is only valid for domains.
