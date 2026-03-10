# When should I use HTTP Activity vs. Web Resource Access Activity?

> OCSF FAQ: When should I use HTTP Activity vs. Web Resource Access Activity?


HTTP Activity is information focused on the network protocol, and not the gating of the resource. While access to a resource is often requested via a web service or REST APIs, the HTTP Activity is the protocol activity for that access, not the activity of the gating service to the resource, which might be via the HTTP server nevertheless. And of course access activity in general is not uniquely via HTTP: Kerberos and LDAP servers grant and deny access to resources over their respective protocols.