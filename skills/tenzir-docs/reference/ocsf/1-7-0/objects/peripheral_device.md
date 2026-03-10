# Peripheral Device

> The peripheral device object describes the properties of external, connectable, and detachable hardware.


The peripheral device object describes the properties of external, connectable, and detachable hardware.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The name of the peripheral device.

**`model`**

* **Type**: `string_t`
* **Requirement**: recommended

The peripheral device model.

**`serial_number`**

* **Type**: `string_t`
* **Requirement**: recommended

The peripheral device serial number.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The peripheral device type is unknown.
  * `1` - `External Storage`: The peripheral device is an external storage device.
  * `2` - `Keyboard`: The peripheral device is a keyboard.
  * `3` - `Mouse`: The peripheral device is a mouse.
  * `4` - `Printer`: The peripheral device is a printer.
  * `5` - `Monitor`: The peripheral device is a monitor.
  * `6` - `Microphone`: The peripheral device is a microphone.
  * `7` - `Webcam`: The peripheral device is a webcam.
  * `99` - `Other`: The peripheral device type is not mapped. See the `type` attribute which contains an event source specific value.

The normalized peripheral device type ID.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the peripheral device.

**`vendor_id_list`**

* **Type**: `string_t`
* **Requirement**: recommended

The list of vendor IDs for the peripheral device.

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The primary vendor name for the peripheral device.

**`class`**

* **Type**: `string_t`
* **Requirement**: optional

The class of the peripheral device.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The Peripheral Device type, normalized to the caption of the `type_id` value. In the case of ‘Other’, it is defined by the source.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`peripheral_activity`](../classes/peripheral_activity.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)