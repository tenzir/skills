# When should I use the unmapped attribute?

> OCSF FAQ: When should I use the unmapped attribute?


The `unmapped` attribute is a catchall for event producers and mappers when there is data that doesn’t populate the more specific attributes of the class. For example, product specific data that is extracted into fields and values from a log that aren’t mapped.

Where `unmapped` is best used, is for a mapper who is mapping events from multiple vendors where each vendor may have unique fields not common to other vendors for the same type of data source.

However, using `unmapped` is not recommended for event producers. A native event producer should extend the schema to properly capture the data that can’t be mapped. For product specific data, an extension is preferred, using either a vendor developed profile, or in some cases a new event class if the core event class doesn’t adequately represent the event due to data that can’t be naturally mapped, or activities not captured by the core class.