# When should I use `status` and when should I use `state` when adding to the schema?

> OCSF FAQ: When should I use `status` and when should I use `state` when adding to the schema?


The convention we try to stick to when authoring OCSF classes and objects is to use `status_id` and its sibling `status` for the result of an activity, usually as a class attribute, and use `state_id` and its sibling `state` for the state of an object. The latter might sound obvious but it may not be obvious to not use `status` for objects. The reasoning is that an object exist independent of time or an activity or action, and therefore it has a state. It could have just as easily had a status, over an indeterminate period of time, but we have tried to distinguish between the two situations by reserving `status` for the point in time result of an activity or action.