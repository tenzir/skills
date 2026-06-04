# Hardware

Hardware specification details for a resource, including both physical and virtual hardware.

## Fields

### `serial_number` / `serialNumber`

- Type: `string` (singular)

Hardware serial number.

### `manufacturer`

- Type: `string` (singular)

Hardware manufacturer.

### `model`

- Type: `string` (singular)

Hardware model.

### `cpu_platform` / `cpuPlatform`

- Type: `string` (singular)

Platform of the hardware CPU (e.g. "Intel Broadwell").

### `cpu_model` / `cpuModel`

- Type: `string` (singular)

Model description of the hardware CPU (e.g. "2.8 GHz Quad-Core Intel Core i5").

### `cpu_clock_speed` / `cpuClockSpeed`

- Type: `uint64` (singular)

Clock speed of the hardware CPU in MHz.

### `cpu_max_clock_speed` / `cpuMaxClockSpeed`

- Type: `uint64` (singular)

Maximum possible clock speed of the hardware CPU in MHz.

### `cpu_number_cores` / `cpuNumberCores`

- Type: `uint64` (singular)

Number of CPU cores.

### `ram`

- Type: `uint64` (singular)

Amount of the hardware ramdom access memory (RAM) in Mb.
