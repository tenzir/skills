# unmapped is of Object type. What does that mean and is it different from JSON or a String type?

> OCSF FAQ: unmapped is of Object type. What does that mean and is it different from JSON or a String type?


Object is the empty complex data type from which all OCSF objects extend with JSON formatted attributes, requirements, and descriptions. Think of `unmapped` as if it were an OCSF object that you created on the fly. In the Java programming language, it would be like an inner class that doesn’t need to be declared externally or globally. That is to say, it is used within the instance of an OCSF class only, and not part of the schema.

JSON is more free form data, hence the `data` attribute is of type JSON. It can be anything encapsulated within JSON and does not need to look like an OCSF object. It should not be used for unmapped extracted fields, but rather other data that may be captured with the event. It is used, for example, within the Enrichment object (the `enrichments` array attribute of the Base Event) to augment one or more of the mapped or unmapped attributes.

A String type is reserved for unformatted text, such as the `raw_data` attribute of the Base Event class. Binary data is Base64 encoded in an attribute of `bytestring_t` type, currently not used in the core schema but may be used in extensions or within the `unmapped` object.