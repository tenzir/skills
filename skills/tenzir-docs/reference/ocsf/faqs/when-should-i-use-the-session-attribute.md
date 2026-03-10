# When should I use the session attribute?

> OCSF FAQ: When should I use the session attribute?


The `session` attribute is usually paired with the `user` attribute. A Session object has information pertaining to a particular user session through which the activity was initiated. User is an entity object that isn’t always associated with a session, and isn’t always an actor, hence Session isn’t part of the User object, but is included with the Actor object for actor semantics.

Related to this, the `process` attribute of type Process has a User object which represents the user’s account that the process runs under or is impersonating. Hence, the Process object also has a `session` attribute paired with its `user` attribute.

Often, User and Session objects will be paired in many event classes.