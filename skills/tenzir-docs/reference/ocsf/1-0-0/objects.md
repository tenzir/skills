# Objects

> Complete listing of OCSF 1.0.0 objects by category.


Complete listing of objects by category.

## Identity & Access (10 objects)

* [Account](objects/account.md): The Account object contains details about the account that initiated or performed a specific activity within a system or application.
* [Actor](objects/actor.md): The Actor object contains details about the user, role, or process that initiated or performed a specific activity.
* [Authorization Result](objects/authorization.md): The Authorization Result object provides details about the authorization outcome and associated policies related to activity.
* [Email Authentication](objects/email_auth.md): The Email Authentication object describes the Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting and Conformance (DMARC) attributes of an email.
* [Group](objects/group.md): The Group object represents a collection or association of entities, such as users, policies, or devices.
* [Identity Provider](objects/idp.md): The Identity Provider object contains detailed information about a provider responsible for creating, maintaining, and managing identity information while offering authentication services to applications.
* [Organization](objects/organization.md): The Organization object describes characteristics of an organization or company and its division if any.
* [Policy](objects/policy.md): The Policy object describes the policies that are applicable.
* [Session](objects/session.md): The Session object describes details about an authenticated session. e.g.
* [User](objects/user.md): The User object describes the characteristics of a user/person or a security principal.

## Process & System (12 objects)

* [Container](objects/container.md): The Container object describes an instance of a specific container.
* [Device](objects/device.md): The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network.
* [Device Hardware Info](objects/device_hw_info.md): The Device Hardware Information object contains details and specifications of the physical components that make up a device.
* [Display](objects/display.md): The Display object contains information about the physical or virtual display connected to a computer system.
* [Image](objects/image.md): The Image object provides a description of a specific Virtual Machine (VM) or Container image.
* [Kernel Resource](objects/kernel.md): The Kernel Resource object provides information about a specific kernel resource, including its name and type.
* [Kernel Extension](objects/kernel_driver.md): The Kernel Extension object describes a kernel driver that has been loaded or unloaded into the operating system (OS) kernel.
* [Keyboard Information](objects/keyboard_info.md): The Keyboard Information object contains details and attributes related to a computer or device keyboard.
* [Module](objects/module.md): The Module object describes the load attributes of a module.
* [Operating System (OS)](objects/os.md): The Operating System (OS) object describes characteristics of an OS, such as Linux or Windows.
* [Process](objects/process.md): The Process object describes a running instance of a launched program.
* [Service](objects/service.md): The Service object describes characteristics of a service, \` e.g.

## Network (14 objects)

* [DNS Answer](objects/dns_answer.md): The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation.
* [DNS Query](objects/dns_query.md): The DNS query object represents a specific request made to the Domain Name System (DNS) to retrieve information about a domain or perform a DNS operation.
* [Endpoint](objects/endpoint.md): The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network.
* [HTTP Cookie](objects/http_cookie.md): The HTTP Cookie object, also known as a web cookie or browser cookie, contains details and values pertaining to a small piece of data that a server sends to a user’s web browser.
* [HTTP Header](objects/http_header.md): TThe HTTP Header object represents the headers sent in an HTTP request or response.
* [HTTP Request](objects/http_request.md): The HTTP Request object represents the attributes of a request made to a web server.
* [HTTP Response](objects/http_response.md): The HTTP Response object contains detailed information about the response sent from a web server to the requester.
* [Network Connection Information](objects/network_connection_info.md): The Network Connection Information object describes characteristics of a network connection.
* [Network Endpoint](objects/network_endpoint.md): The Network Endpoint object describes characteristics of a network endpoint.
* [Network Interface](objects/network_interface.md): The Network Interface object describes the type and associated attributes of a network interface.
* [Network Proxy Endpoint](objects/network_proxy.md): The Network Proxy Endpoint describes characteristics of a network proxy.
* [Network Traffic](objects/network_traffic.md): The Network Traffic object describes characteristics of network traffic.
* [Transport Layer Security (TLS)](objects/tls.md): The Transport Layer Security (TLS) object describes the negotiated TLS protocol used for secure communications over an establish network connection.
* [TLS Extension](objects/tls_extension.md): The TLS Extension object describes additional attributes that extend the base Transport Layer Security (TLS) object.

## File & Data (5 objects)

* [Digital Signature](objects/digital_signature.md): The Digital Signature object contains information about the cryptographic mechanism used to verify the authenticity, integrity, and origin of the file or application.
* [File](objects/file.md): The File object represents the metadata associated with a file stored in a computer system.
* [Fingerprint](objects/fingerprint.md): The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content.
* [HASSH](objects/hassh.md): The HASSH (Honeypot Attention-Grabbing SSH) object contains SSH network fingerprinting values for specific client/server implementations.
* [Software Package](objects/package.md): The Software Package object describes details about a software package.

## Security & Compliance (12 objects)

* [Analytic](objects/analytic.md): The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the finding or conclusion.
* [Attack](objects/attack.md): The Attack object describes the technique and associated tactics related to an attack.
* [CIS Benchmark Result](objects/cis_benchmark_result.md): The CIS Benchmark Result object contains information as defined by the Center for Internet Security ([CIS](https://www.cisecurity.org/cis-benchmarks/)) benchmark result.
* [CIS Control](objects/cis_control.md): The CIS Control contains information as defined by the Center for Internet Security Critical Security Control [(CIS CSC)](https://www.cisecurity.org/controls).
* [Compliance](objects/compliance.md): The Compliance object contains information about compliance requirements related of a finding generated by security tool.
* [CVE](objects/cve.md): The Common Vulnerabilities and Exposures (CVE) object represents publicly disclosed cybersecurity vulnerabilities defined in CVE Program catalog ([CVE](https://cve.mitre.org/)).
* [CVSS Score](objects/cvss.md): The Common Vulnerability Scoring System ([CVSS](https://www.first.org/cvss/)) object provides a way to capture the principal characteristics of a vulnerability and produce a numerical score reflecting its severity.
* [Finding](objects/finding.md): The Finding object contains details related to a security finding generated by a security tool or system.
* [Kill Chain](objects/kill_chain.md): The Kill Chain object represents a single phase of a cyber attack, including the initial reconnaissance and planning stages up to the final objective of the attacker.
* [Malware](objects/malware.md): The Malware object describes the classification of known malicious software, which is intentionally designed to cause damage to a computer, server, client, or computer network.
* [Rule](objects/rule.md): The Rule object describes characteristics of a rule associated with a policy or an event.
* [Vulnerability Details](objects/vulnerability.md): The Vulnerability Details object describes characteristics of an observed vulnerability.

## Cloud & Infrastructure (9 objects)

* [API](objects/api.md): The API, or Application Programming Interface, object represents information pertaining to an API request and response.
* [Cloud](objects/cloud.md): The Cloud object contains information about a cloud account such as AWS Account ID, regions, etc.
* [Job](objects/job.md): The Job object provides information about a scheduled job or task, including its name, command line, and state.
* [Managed Entity](objects/managed_entity.md): The Managed Entity object describes the type and version of an entity, such as a policy or configuration.
* [Product](objects/product.md): The Product object describes characteristics of a software product.
* [Request Elements](objects/request.md): The Request Elements object describes characteristics of an API request.
* [Resource Details](objects/resource_details.md): The Resource Details object describes details about resources that were affected by the activity/event.
* [Response Elements](objects/response.md): The Response Elements object describes characteristics of an API response.
* [Web Resource](objects/web_resource.md): The Web Resource object describes characteristics of a web resource that was affected by the activity/event.

## Observability (3 objects)

* [Enrichment](objects/enrichment.md): The Enrichment object provides inline enrichment data for specific attributes of interest within an event.
* [Metric](objects/metric.md): The Metric object defines a simple name/value pair entity for a metric.
* [Observable](objects/observable.md): The observable object is a pivot element that contains related information found in many places in the event.

## Other (16 objects)

* [Digital Certificate](objects/certificate.md): The Digital Certificate, also known as a Public Key Certificate, object contains information about the ownership and usage of a public key.
* [DCE/RPC](objects/dce_rpc.md): The DCE/RPC, or Distributed Computing Environment/Remote Procedure Call, object describes the remote procedure call system for distributed computing environments.
* [Email](objects/email.md): The Email object describes the email metadata such as sender, recipients, and direction.
* [Schema Extension](objects/extension.md): The OCSF Schema Extension object provides detailed information about the schema extension used to construct the event.
* [Feature](objects/feature.md): The Feature object provides information about the software product feature that generated a specific event.
* [Geo Location](objects/location.md): The Geo Location object describes a geographical location, usually associated with an IP address.
* [Metadata](objects/metadata.md): The Metadata object describes the metadata associated with the event.
* [Object](objects/object.md): An unordered collection of attributes.
* [Related Event](objects/related_event.md): The Related Event object describes an event related to a finding or detection as identified by the security product.
* [Remediation](objects/remediation.md): The Remediation object describes details about recommended remediation strategies.
* [Reputation](objects/reputation.md): The Reputation object describes the reputation/risk score of an entity (e.g. device, user, domain).
* [RPC Interface](objects/rpc_interface.md): The RPC Interface represents the remote procedure call interface used in the DCE/RPC session.
* [Subject Alternative Name](objects/san.md): The Subject Alternative name (SAN) object describes a SAN secured by a digital certificate
* [Tactic](objects/tactic.md): The Tactic object describes the tactic IDs and/or name that are associated with the attack technique, as defined by ATT\&CK MatrixTM.
* [Technique](objects/technique.md): The Technique object describes the technique related to an attack, as defined by ATT\&CK MatrixTM.
* [Uniform Resource Locator](objects/url.md): The Uniform Resource Locator(URL) object describes the characteristics of a URL.