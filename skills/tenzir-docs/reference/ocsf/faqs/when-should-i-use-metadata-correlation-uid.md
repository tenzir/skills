# When should I use metadata.correlation_uid?

> OCSF FAQ: When should I use metadata.correlation_uid?


When an event producer or mapper emits multiple events that have some grouping characteristic, or similarity of any form, it should populate the `metadata.correlation_uid` attribute with a constant identifier. This allows consumers and analysts of the set of events to more easily aggregate and correlate the events.

A simple example would be a vulnerability scanner that emits events at the start of a scan of a system, at the end of the scan, and separate events for each vulnerability discovered. If these are separate events, they would all have their `metadata.correlation_uid` set to the same value.

It is possible for an intermediary system to determine the grouping characteristic as well, populating the attribute after collection of the events, although when OCSF events are immutable a copy of the original events would be made with added correlation information. See the next question.