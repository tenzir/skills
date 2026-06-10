# Custom event keys

Vendors and partners can define their own custom event keys and include them in the payload of the LEEF format.

Use custom key value-pair attributes in an event payload when there is no default key to represent information about an event for your appliance. Create custom event attributes only when there is no acceptable mapping to a predefined event attribute. For example, if your appliance monitors access, you can require the file name that is accessed by a user where no file name attribute exists in LEEF by default.

> **Note:** Event attribute keys and values can appear one time only in each payload. Using a key-value pair twice in the same payload can cause IBM® Security QRadar® to ignore the value of the duplicate key.

Custom event keys are *non-normalized*, which means that any specialized key value pairs you include in your LEEF event are not displayed by default on the Log Activity tab of QRadar. To view custom attributes and *non-normalized* events on the Log Activity tab of QRadar, you must create a custom event property. *Non-normalized* event data is still part of your LEEF event, is searchable in QRadar, and is viewable in the event payload. For more information about creating a custom event property, see the *IBM QRadar Administration Guide*.
