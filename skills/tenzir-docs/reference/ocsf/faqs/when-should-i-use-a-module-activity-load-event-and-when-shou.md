# When should I use a `Module Activity: Load` event and when should I use a `Process Activity: Inject` event

> OCSF FAQ: When should I use a `Module Activity: Load` event and when should I use a `Process Activity: Inject` event


Confusion exists here because both `Module Activity: Load` and `Process Activity: Inject` with `injection_type_id = 2 (Load Library)` can be used to represent an endpoint process loading a module. `Process Activity: Inject` with `injection_type_id = 2 (Load Library)` represents when an actor process acts on a target process to cause that target process to load a module. `Module Activity: Load` covers the more general case of an endpoint process loading a module which is something that endpoint processes routinely do. Given that `Process Activity: Inject` with `injection_type_id = 2 (Load Library)` is more specific, it should be used if applicable.