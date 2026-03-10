# How do I create a typical OCSF event?

> OCSF FAQ: How do I create a typical OCSF event?


Depending on the type of event, a data producer or data mapper should first determine what event class best suits your event. Start with the OCSF category to narrow down the choices. For example, an endpoint security product would likely choose an event class from the System Activity category, for example, File System Activity for an AV product. Every event class has an `activity_id` enumeration which narrows down the intended activity of the event. Sometimes these are simple CRUD activities, but often they are more specific to the class, such as `Logon` for the `Authentication` class in the `Identity and Access Management` category.

Since endpoint security products typically send alert events when malware is detected, the producer or mapper would apply the Security Control profile, which adds important attributes to the File System Activity event class, e.g. a Malware object, a MITRE ATT\&CK object, the disposition etc. These profiles have their own attributes that must be populated.

If your endpoint security product also has network security capabilities, you would choose an event class from the Network Activity category, for example the general Network Activity event class. Given that the endpoint product will have information about the host system, you would apply the Host profile, as well as the Security Control profile. The Host profile includes attributes about the device and the actor (e.g. process or user) on the host.

Every OCSF event must have all of its event class Required attributes populated, and should have its Recommended attributes populated, if possible. This includes any of the embedded objects, such as the Malware, Process and Device objects above.

All OCSF events have a set of required classification attributes from the Base Event class: the `class_uid` the `category_uid` the `activity_id` and the derived `type_uid`. Their associated `*_name` attributes are optional.

In addition to the classification attributes, a number of other Base Event class attributes are required and must be populated: the `time` `metadata` and `severity` attributes. The `metadata` attribute is an object that itself requires the `product` and associated `version` of the reporting event, as well as the version of the OCSF schema adhered to with the event.

Note that the product should be the originating event producer (i.e. not the mapping system, nor any intermediary event processing systems) in order to best represent the origin of the event. The `time` should be the time that the event actually occurred assuming that information is known, or the earliest possible time available to the event producer or mapper.

Although the `observables` array attribute is optional, populating it can make things easier for event consumers and analysts. Each Observable object surfaces an important attribute of the event in a common location in a simple tuple: name, value, type. For example, if the event class has a `device` `user` and `process` populated, an array of three Observable objects will refer to them in a common location to all OCSF events.