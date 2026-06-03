# Hardware

Hardware specification details for a resource, including both physical and virtual hardware.

- **Full name**: `google.backstory.Hardware`
- **Fields**: `9`

## Fields

### `serial_number`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `serialNumber`

Hardware serial number.

### `manufacturer`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `manufacturer`

Hardware manufacturer.

### `model`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `model`

Hardware model.

### `cpu_platform`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `cpuPlatform`

Platform of the hardware CPU (e.g. "Intel Broadwell").

### `cpu_model`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `cpuModel`

Model description of the hardware CPU (e.g. "2.8 GHz Quad-Core Intel Core i5").

### `cpu_clock_speed`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `cpuClockSpeed`

Clock speed of the hardware CPU in MHz.

### `cpu_max_clock_speed`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `cpuMaxClockSpeed`

Maximum possible clock speed of the hardware CPU in MHz.

### `cpu_number_cores`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `cpuNumberCores`

Number of CPU cores.

### `ram`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `ram`

Amount of the hardware ramdom access memory (RAM) in Mb.
