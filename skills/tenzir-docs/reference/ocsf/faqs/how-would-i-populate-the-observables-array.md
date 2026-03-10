# How would I populate the `observables` array?

> OCSF FAQ: How would I populate the `observables` array?


There are three important attributes of the `Observable` object, and the Base Event class allows for an array of these objects with the `observables` attribute: `name`, `type_id` and `value`. The first two are required attributes, while `value` is optional. Why it is optional will become clear soon. There can be multiple observables within an event, even of the same type. This is why `observables` is an array.

The required `name` attribute of the `Observable` object should be the fully qualified attribute name within the event. E.g. `fingerprint.value` or `actor.process.file` or `actor.process.file.name`. In other words, `observable.name` is the locator of that observable within the instance of the event. Note that the observable attribute can be a scalar, like `device.ip`, or it can be an object, like `actor.process.file`.

When the `type_id` of the observable indicates that the observable’s `name` attribute is of object type, e.g. Fingerprint, the observable’s `value` attribute is not populated. When the `type_id` indicates the observable’s `name` is a scalar, e.g. File Hash or File Name, then the observable’s `value` should be populated with the value of that attribute, that is, a copy of the value from the event.