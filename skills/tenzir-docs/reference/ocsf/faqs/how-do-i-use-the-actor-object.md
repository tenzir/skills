# How do I use the Actor object?

> OCSF FAQ: How do I use the Actor object?


The Actor object is intended for use in event classes when knowledge of one entity that is initiating or causing some action on another entity.\
For example, a process deleting a file is the actor in a Filesystem Activity event.

From a structural standpoint, the `actor` attribute avoids name collisions with the other end of the activity in cases where a process acts on another process, as those attribute names would be in contention at the same level within the class.

Currently the Actor object has a `process` and `user` attribute, where one or the other is in the role of the actor in the activity. It also has Optional attributes for Session, `authorizations`, `idp`, and `invoked_by`.

The `idp` is populated in IAM category event classes, when the actor’s identity provider is known and logged with Authentication and related events.

The `authorizations` attribute is an array of information pertaining to what permissions and privileges the actor has at the time of the event, if known.

The `invoked_by` attribute is populated with the name of the service or application through which the actor’s activity was initiated.