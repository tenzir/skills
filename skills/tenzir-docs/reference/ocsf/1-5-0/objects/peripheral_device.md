# Peripheral Device

> The peripheral device object describes the identity, vendor and model of a peripheral device.


The peripheral device object describes the identity, vendor and model of a peripheral device.

* **Extends**: `_entity`

## Attributes

**`class`**

* **Type**: `string_t`
* **Requirement**: required

The class of the peripheral device.

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

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the peripheral device.

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The peripheral device vendor.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`peripheral_device_query`](../classes/peripheral_device_query.md)