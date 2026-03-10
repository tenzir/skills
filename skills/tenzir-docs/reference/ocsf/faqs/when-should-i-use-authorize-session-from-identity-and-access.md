# When should I use Authorize Session from Identity and Access Management vs. Web Resource Access Activity from the Application category?

> OCSF FAQ: When should I use Authorize Session from Identity and Access Management vs. Web Resource Access Activity from the Application category?


These two event classes are complementary. Changes to a security principal’s permissions, privileges, roles are authorization activities, while the access of web resources by a security principal is logged as Web Access Activity. IAM category authorization or change events are independent of a particular resource access, while enforcement of authorization restrictions is made at access time and is logged as such. For example, when a new Logon session is created, authorization checks are made and if logged, belong in the Authorize Session class. However, when the user or process that has those permissions accesses a web resource, and it is granted or denied, the Web Access Activity class is used.