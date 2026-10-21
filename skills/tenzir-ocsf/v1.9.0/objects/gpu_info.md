# GPU Information (gpu_info)

The GPU information object contains attributes describing graphical processing hardware.

- **Extends**: [Object (object)](object.md)

## Attributes

### `bus_type`

- **Type**: `string_t`
- **Requirement**: optional

The attachment bus or interface standard, normalized to the caption of the bus_type_id value. In the case of 'Other', it is defined by the event source.

### `bus_type_id`

- **Type**: `integer_t`
- **Requirement**: optional
- **Sibling**: `bus_type`

#### Enum values

- `0`: `Unknown` - The bus type is unknown or not reported.
- `1`: `Onboard` - The device is attached directly on the motherboard or SoC (often referred to as 'integrated' or 'onboard').
- `2`: `PCIe x16` - Peripheral Component Interconnect Express slot with 16 lanes, typically used for high‑bandwidth add‑in devices.
- `3`: `PCIe x8` - Peripheral Component Interconnect Express slot with 8 lanes; common for high‑performance NICs, storage controllers, and accelerators.
- `4`: `MXM Type A` - Mobile PCI Express Module (MXM) Type A form factor (compact laptop/embedded GPU module).
- `5`: `MXM Type B` - Mobile PCI Express Module (MXM) Type B form factor (larger laptop/embedded GPU module).
- `6`: `M.2` - M.2 (NGFF) internal module form factor/connector exposing PCIe (and/or SATA/USB) for SSDs and add‑in modules.
- `7`: `CXL` - Compute Express Link (CXL), an open cache‑coherent interconnect for processors, memory expansion, and accelerators built on the PCIe physical layer.
- `99`: `Other` - A bus or interface standard not covered by the defined values; the exact value is reported by the event source.

The normalized identifier of the attachment bus or interface standard.

### `cores`

- **Type**: `integer_t`
- **Requirement**: optional

The number of processing cores or compute units for the component.

### `model`

- **Type**: `string_t`
- **Requirement**: recommended

The model name of the GPU. For example: `GeForce RTX A6000`, `Radeon PRO W7900`, or `Intel Data Center GPU Max 1550`.

### `vendor_name`

- **Type**: `string_t`
- **Requirement**: recommended

The name of the vendor of the GPU. For example: `NVIDIA`, `AMD`, or `Intel`.

### `vram_mode`

- **Type**: `string_t`
- **Requirement**: recommended

The video memory attachment mode, indicating how the VRAM hardware is integrated with the system (e.g., shared or dedicated), normalized to the caption of the vram_mode_id value. For 'Other', the exact attachment mode is defined by the event source.

### `vram_mode_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Sibling**: `vram_mode`

#### Enum values

- `0`: `Unknown` - The VRAM mode is unknown or not reported.
- `1`: `Shared` - Video memory is allocated from system memory.
- `2`: `Dedicated` - Video memory is physically separate from system memory.
- `99`: `Other` - A VRAM mode not covered by the defined values; the exact value is reported by the event source.

The normalized identifier of the video memory attachment mode.

### `vram_size`

- **Type**: `integer_t`
- **Requirement**: recommended

The total amount of installed video RAM.
