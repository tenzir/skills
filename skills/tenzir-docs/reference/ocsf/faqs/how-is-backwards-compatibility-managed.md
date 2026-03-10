# How is backwards compatibility managed?

> OCSF FAQ: How is backwards compatibility managed?


OCSF follows the [semver](https://semver.org/) versioning scheme.

From the semver documentation:

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> MAJOR version when you make incompatible API changes MINOR version when you add functionality in a backward compatible manner PATCH version when you make backward compatible bug fixes

In terms practical to OCSF users, this means:

* PATCH version increments may change documentation values like `description`.
* MINOR version increments may add new schemata like attributes or events.
* MAJOR version increments may add and remove anything.

So any version in the 1.x line should be backwards-compatible with previous 1.x versions.