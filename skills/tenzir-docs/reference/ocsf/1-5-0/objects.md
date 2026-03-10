# Objects

> Complete listing of OCSF 1.5.0 objects by category.


Complete listing of objects by category.

## Identity & Access (17 objects)

* [Account](objects/account.md): The Account object contains details about the account that initiated or performed a specific activity within a system or application.
* [Actor](objects/actor.md): The Actor object contains details about the user, role, application, service, or process that initiated or performed a specific activity.
* [Authentication Factor](objects/auth_factor.md): An Authentication Factor object describes a category of methods used for identity verification in an authentication attempt.
* [Authentication Token](objects/authentication_token.md): The Authentication Token object contains the attributes pertaining to an authentication token, ticket, or assertion e.g.
* [Authorization Result](objects/authorization.md): The Authorization Result object provides details about the authorization outcome and associated policies related to activity.
* [Email Authentication](objects/email_auth.md): The Email Authentication object describes the Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting and Conformance (DMARC) attributes of an email.
* [Group](objects/group.md): The Group object represents a collection or association of entities, such as users, policies, or devices.
* [Identity Provider](objects/idp.md): The Identity Provider object contains detailed information about a provider responsible for creating, maintaining, and managing identity information while offering authentication services to applications.
* [LDAP Person](objects/ldap_person.md): The additional LDAP attributes that describe a person.
* [Organization](objects/organization.md): The Organization object describes characteristics of an organization or company and its division if any.
* [Policy](objects/policy.md): The Policy object describes the policies that are applicable.
* [Session](objects/session.md): The Session object describes details about an authenticated session. e.g.
* [SSO](objects/sso.md): The Single Sign-On (SSO) object provides a structure for normalizing SSO attributes, configuration, and/or settings from Identity Providers.
* [Threat Actor](objects/threat_actor.md): Threat actor is responsible for the observed malicious activity.
* [Ticket](objects/ticket.md): The Ticket object represents ticket in the customer’s IT Service Management (ITSM) systems like ServiceNow, Jira, etc.
* [Trait](objects/trait.md): Describes a characteristic or feature of an entity that was observed.
* [User](objects/user.md): The User object describes the characteristics of a user/person or a security principal.

## Process & System (19 objects)

* [Agent](objects/agent.md): An Agent (also known as a Sensor) is typically installed on an Operating System (OS) and serves as a specialized software component that can be designed to monitor, detect, collect, archive, or take action.
* [Application](objects/application.md): An Application describes the details for an inventoried application as reported by an Application Security tool or other Developer-centric tooling.
* [Container](objects/container.md): The Container object describes an instance of a specific container.
* [Device](objects/device.md): The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network.
* [Device Hardware Info](objects/device_hw_info.md): The Device Hardware Information object contains details and specifications of the physical components that make up a device.
* [Display](objects/display.md): The Display object contains information about the physical or virtual display connected to a computer system.
* [Environment Variable](objects/environment_variable.md): An environment variable.
* [Image](objects/image.md): The Image object provides a description of a specific Virtual Machine (VM) or Container image.
* [Kernel Resource](objects/kernel.md): The Kernel Resource object provides information about a specific kernel resource, including its name and type.
* [Kernel Extension](objects/kernel_driver.md): The Kernel Extension object describes a kernel driver that has been loaded or unloaded into the operating system (OS) kernel.
* [Keyboard Information](objects/keyboard_info.md): The Keyboard Information object contains details and attributes related to a computer or device keyboard.
* [Module](objects/module.md): The Module object describes the load attributes of a module.
* [Operating System (OS)](objects/os.md): The Operating System (OS) object describes characteristics of an OS, such as Linux or Windows.
* [OSINT](objects/osint.md): The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information.
* [Peripheral Device](objects/peripheral_device.md): The peripheral device object describes the identity, vendor and model of a peripheral device.
* [Process](objects/process.md): The Process object describes a running instance of a launched program.
* [Process Entity](objects/process_entity.md): The Process Entity object provides critical fields for referencing a process.
* [Service](objects/service.md): The Service object describes characteristics of a service, \` e.g.
* [Startup Item](objects/startup_item.md): The startup item object describes an application component that has associated startup criteria and configurations.

## Network (18 objects)

* [Autonomous System](objects/autonomous_system.md): An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the internet.
* [DNS Answer](objects/dns_answer.md): The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation.
* [DNS Query](objects/dns_query.md): The DNS query object represents a specific request made to the Domain Name System (DNS) to retrieve information about a domain or perform a DNS operation.
* [Endpoint](objects/endpoint.md): The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network.
* [Endpoint Connection](objects/endpoint_connection.md): The Endpoint Connection object contains information detailing a connection attempt to an endpoint.
* [Firewall Rule](objects/firewall_rule.md): The Firewall Rule object represents a specific rule within a firewall policy or event.
* [HTTP Cookie](objects/http_cookie.md): The HTTP Cookie object, also known as a web cookie or browser cookie, contains details and values pertaining to a small piece of data that a server sends to a user’s web browser.
* [HTTP Header](objects/http_header.md): The HTTP Header object represents the headers sent in an HTTP request or response.
* [HTTP Request](objects/http_request.md): The HTTP Request object represents the attributes of a request made to a web server.
* [HTTP Response](objects/http_response.md): The HTTP Response object contains detailed information about the response sent from a web server to the requester.
* [Load Balancer](objects/load_balancer.md): The load balancer object describes the load balancer entity and contains additional information regarding the distribution of traffic across a network.
* [Network Connection Information](objects/network_connection_info.md): The Network Connection Information object describes characteristics of an OSI Transport Layer communication, including TCP and UDP.
* [Network Endpoint](objects/network_endpoint.md): The Network Endpoint object describes characteristics of a network endpoint.
* [Network Interface](objects/network_interface.md): The Network Interface object describes the type and associated attributes of a physical or virtual network interface.
* [Network Proxy Endpoint](objects/network_proxy.md): The network proxy endpoint object describes a proxy server, which acts as an intermediary between a client requesting a resource and the server providing that resource.
* [Network Traffic](objects/network_traffic.md): The Network Traffic object describes characteristics of network traffic.
* [Transport Layer Security (TLS)](objects/tls.md): The Transport Layer Security (TLS) object describes the negotiated TLS protocol used for secure communications over an establish network connection.
* [TLS Extension](objects/tls_extension.md): The TLS Extension object describes additional attributes that extend the base Transport Layer Security (TLS) object.

## File & Data (15 objects)

* [Affected Software Package](objects/affected_package.md): The Affected Package object describes details about a software package identified as affected by a vulnerability/vulnerabilities.
* [Data Classification](objects/data_classification.md): The Data Classification object includes information about data classification levels and data category types.
* [Data Security](objects/data_security.md): The Data Security object describes the characteristics, techniques and content of a Data Loss Prevention (DLP), Data Loss Detection (DLD), Data Classification, or similar tools’ finding, alert, or detection mechanism(s).
* [Database](objects/database.md): The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.
* [Databucket](objects/databucket.md): The databucket object is a basic container that holds data, typically organized through the use of data partitions.
* [Digital Signature](objects/digital_signature.md): The Digital Signature object contains information about the cryptographic mechanism used to verify the authenticity, integrity, and origin of the file or application.
* [Encryption Details](objects/encryption_details.md): Details about the encrytpion methodology utilized.
* [File](objects/file.md): The File object represents the metadata associated with a file stored in a computer system.
* [Fingerprint](objects/fingerprint.md): The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content.
* [HASSH](objects/hassh.md): The HASSH object contains SSH network fingerprinting values for specific client/server implementations.
* [JA4+ Fingerprint](objects/ja4_fingerprint.md): The JA4+ fingerprint object provides detailed fingerprint information about various aspects of network traffic which is both machine and human readable.
* [Software Package](objects/package.md): The Software Package object describes details about a software package.
* [Software Bill of Materials](objects/sbom.md): The Software Bill of Materials object describes characteristics of a generated SBOM.
* [Script](objects/script.md): The Script object describes a script or command that can be executed by a shell, script engine, or interpreter.
* [Software Component](objects/software_component.md): The Software Component object describes characteristics of a software component within a software package.

## Security & Compliance (27 objects)

* [Analytic](objects/analytic.md): The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.
* [Anomaly](objects/anomaly.md): Describes an anomaly or deviation detected in a system.
* [Anomaly Analysis](objects/anomaly_analysis.md): Describes the analysis of activity patterns and anomalies of target entities to identify potential security threats, performance issues, or other deviations from established baselines.
* [Assessment](objects/assessment.md): The Assessment object describes a point-in-time assessment, check, or evaluation of a specific configuration or signal against an asset, entity, person, or otherwise.
* [MITRE ATT\&CK® & ATLAS™](objects/attack.md): The MITRE ATT\&CK® & ATLAS™ object describes the tactic, technique, sub-technique & mitigation associated to an attack.
* [Baseline](objects/baseline.md): Describes the baseline or expected behavior of a system, service, or component based on historical observations and measurements.
* [Campaign](objects/campaign.md): Campaign represent organized efforts by threat actors to achieve malicious objectives over a period, often characterized by shared tactics, techniques, and procedures (TTPs).
* [Check](objects/check.md): The check object defines a specific, testable compliance verification point that evaluates a target device against a standard, framework, or custom requirement.
* [CIS Benchmark](objects/cis_benchmark.md): The CIS Benchmark object describes best practices for securely configuring IT systems, software, networks, and cloud infrastructure as defined by the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/).
* [CIS Benchmark Result](objects/cis_benchmark_result.md): The CIS Benchmark Result object contains information as defined by the Center for Internet Security ([CIS](https://www.cisecurity.org/cis-benchmarks/)) benchmark result.
* [CIS Control](objects/cis_control.md): The CIS Control (aka Critical Security Control) object describes a prioritized set of actions to protect your organization and data from cyber-attack vectors.
* [CIS CSC](objects/cis_csc.md): The CIS Critical Security Control (CSC) contains information as defined by the Center for Internet Security Critical Security Control [(CIS CSC)](https://www.cisecurity.org/controls).
* [Compliance](objects/compliance.md): The Compliance object contains information about Industry and Regulatory Framework standards, controls and requirements or details about custom assessments utilized in a compliance evaluation.
* [CVE](objects/cve.md): The Common Vulnerabilities and Exposures (CVE) object represents publicly disclosed cybersecurity vulnerabilities defined in CVE Program catalog ([CVE](https://cve.mitre.org/)).
* [CVSS Score](objects/cvss.md): The Common Vulnerability Scoring System ([CVSS](https://www.first.org/cvss/)) object provides a way to capture the principal characteristics of a vulnerability and produce a numerical score reflecting its severity.
* [CWE](objects/cwe.md): The CWE object represents a weakness in a software system that can be exploited by a threat actor to perform an attack.
* [MITRE D3FEND™ Tactic](objects/d3f_tactic.md): The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack.
* [MITRE D3FEND™ Technique](objects/d3f_technique.md): The MITRE D3FEND™ Technique object describes the leaf defensive technique ID and/or name associated to a countermeasure.
* [MITRE D3FEND™](objects/d3fend.md): The MITRE D3FEND™ object describes the tactic & technique associated with a countermeasure.
* [Finding](objects/finding.md): The Finding object describes metadata related to a security finding generated by a security tool or system.
* [Finding Information](objects/finding_info.md): The Finding Information object describes metadata related to a security finding generated by a security tool or system.
* [Kill Chain Phase](objects/kill_chain_phase.md): The Kill Chain Phase object represents a single phase of a cyber attack, including the initial reconnaissance and planning stages up to the final objective of the attacker.
* [Malware](objects/malware.md): The Malware object describes the classification of known malicious software, which is intentionally designed to cause damage to a computer, server, client, or computer network.
* [Malware Scan Info](objects/malware_scan_info.md): The malware scan information object describes characteristics, metadata of a malware scanning job.
* [MITRE Mitigation](objects/mitigation.md): The MITRE Mitigation object describes the ATT\&CK® or ATLAS™ Mitigation ID and/or name that is associated to an attack.
* [Rule](objects/rule.md): The Rule object describes characteristics of a rule associated with a policy or an event.
* [Vulnerability Details](objects/vulnerability.md): The vulnerability is an unintended characteristic of a computing component or system configuration that multiplies the risk of an adverse event or a loss occurring either due to accidental exposure, deliberate attack, or conflict with new system components.

## Cloud & Infrastructure (9 objects)

* [API](objects/api.md): The API, or Application Programming Interface, object represents information pertaining to an API request and response.
* [Cloud](objects/cloud.md): The Cloud object contains information about a cloud or Software-as-a-Service account or similar construct, such as AWS Account ID, regions, organizations, folders, compartments, tenants, etc.
* [Job](objects/job.md): The Job object provides information about a scheduled job or task, including its name, command line, and state.
* [Managed Entity](objects/managed_entity.md): The Managed Entity object describes the type and version of an entity, such as a user, device, or policy.
* [Product](objects/product.md): The Product object describes characteristics of a software product.
* [Request Elements](objects/request.md): The Request Elements object describes characteristics of an API request.
* [Resource Details](objects/resource_details.md): The Resource Details object describes details about resources that were affected by the activity/event.
* [Response Elements](objects/response.md): The Response Elements object describes characteristics of an API response.
* [Web Resource](objects/web_resource.md): The Web Resource object describes characteristics of a web resource that was affected by the activity/event.

## Observability (14 objects)

* [Enrichment](objects/enrichment.md): The Enrichment object provides inline enrichment data for specific attributes of interest within an event.
* [Evidence Artifacts](objects/evidences.md): A collection of evidence artifacts associated to the activity/activities that triggered a security detection.
* [Graph](objects/graph.md): A graph data structure representation with nodes and edges.
* [Logger](objects/logger.md): The Logger object represents the device and product where events are stored with times for receipt and transmission.
* [Metric](objects/metric.md): The Metric object defines a simple name/value pair entity for a metric.
* [Node](objects/node.md): Represents a node or a vertex in a graph structure.
* [Observable](objects/observable.md): The observable object is a pivot element that contains related information found in many places in the event.
* [Observation](objects/observation.md): A record of an observed value or event that captures the timing and frequency of its occurrence.
* [Occurrence Details](objects/occurrence_details.md): Details about where in the target entity, specified information was discovered.
* [Query Evidence](objects/query_evidence.md): The specific resulting evidence information that was queried or discovered.
* [Span](objects/span.md): Represents a single unit of work or operation within a distributed trace.
* [Time Span](objects/timespan.md): The Time Span object represents different time period durations.
* [Trace](objects/trace.md): The trace object contains information about a distributed trace, which is crucial for observability.
* [Transformation Info](objects/transformation_info.md): The transformation\_info object represents the mapping or transformation used.

## Other (38 objects)

* [Advisory](objects/advisory.md): The Advisory object represents publicly disclosed cybersecurity vulnerabilities defined in a Security advisory. e.g. `Microsoft KB Article`, \`Apple Security Ad
* [Affected Code](objects/affected_code.md): The Affected Code object describes details about a code block identified as vulnerable.
* [Aircraft](objects/aircraft.md): The Aircraft object represents any aircraft or otherwise airborne asset such as an unmanned system, airplane, balloon, spacecraft, or otherwise.
* [Analysis Target](objects/analysis_target.md): The analysis target defines the scope of monitored activities, specifying what entity, system or process is analyzed for activity patterns.
* [Digital Certificate](objects/certificate.md): The Digital Certificate, also known as a Public Key Certificate, object contains information about the ownership and usage of a public key.
* [Classifier Details](objects/classifier_details.md): The Classifier Details object describes details about the classifier used for data classification.
* [DCE/RPC](objects/dce_rpc.md): The DCE/RPC, or Distributed Computing Environment/Remote Procedure Call, object describes the remote procedure call system for distributed computing environments.
* [Discovery Details](objects/discovery_details.md): The Discovery Details object describes results of a discovery task/job.
* [Domain Contact](objects/domain_contact.md): The contact information related to a domain registration, e.g., registrant, administrator, abuse, billing, or technical contact.
* [Edge](objects/edge.md): Represents a connection or relationship between two nodes in a graph.
* [Email](objects/email.md): The Email object describes the email metadata such as sender, recipients, and direction, and can include embedded URLs and files.
* [EPSS](objects/epss.md): The Exploit Prediction Scoring System (EPSS) object describes the estimated probability a vulnerability will be exploited.
* [Schema Extension](objects/extension.md): The OCSF Schema Extension object provides detailed information about the schema extension used to construct the event.
* [Feature](objects/feature.md): The Feature object provides information about the software product feature that generated a specific event.
* [KB Article](objects/kb_article.md): The KB Article object contains metadata that describes the patch or update.
* [Key:Value object](objects/key_value_object.md): A generic object allowing to define a `{key:value}` pair.
* [Geo Location](objects/location.md): The Geo Location object describes a geographical location, usually associated with an IP address.
* [Long String](objects/long_string.md): This object is a used to capture strings which may be truncated by a security product due to their length.
* [Metadata](objects/metadata.md): The Metadata object describes the metadata associated with the event.
* [Object](objects/object.md): An unordered collection of attributes.
* [Query Information](objects/query_info.md): The query info object holds information related to data access within a datastore.
* [Related Event/Finding](objects/related_event.md): The Related Event object describes an event or another finding related to a finding.
* [Remediation](objects/remediation.md): The Remediation object describes the recommended remediation steps to address identified issue(s).
* [Reputation](objects/reputation.md): The Reputation object describes the reputation/risk score of an entity (e.g. device, user, domain).
* [RPC Interface](objects/rpc_interface.md): The RPC Interface represents the remote procedure call interface used in the DCE/RPC session.
* [Subject Alternative Name](objects/san.md): The Subject Alternative name (SAN) object describes a SAN secured by a digital certificate
* [Scan](objects/scan.md): The Scan object describes characteristics of a proactive scan.
* [SCIM](objects/scim.md): The System for Cross-domain Identity Management (SCIM) Configuration object provides a structured set of attributes related to SCIM protocols used for identity provisioning and management across cloud-based platforms.
* [Security State](objects/security_state.md): The Security State object describes the security related state of a managed entity.
* [MITRE Sub-technique](objects/sub_technique.md): The MITRE Sub-technique object describes the ATT\&CK® or ATLAS™ Sub-technique ID and/or name associated to an attack.
* [Table](objects/table.md): The table object represents a table within a structured relational database or datastore, which contains columns and rows of data that are able to be create, updated, deleted and queried.
* [MITRE Tactic](objects/tactic.md): The MITRE Tactic object describes the ATT\&CK® or ATLAS™ Tactic ID and/or name that is associated to an attack.
* [MITRE Technique](objects/technique.md): The MITRE Technique object describes the ATT\&CK® or ATLAS™ Technique ID and/or name associated to an attack.
* [Unmanned Aerial System](objects/unmanned_aerial_system.md): The Unmanned Aerial System object describes the characteristics, Position Location Information (PLI), and other metadata of Unmanned Aerial Systems (UAS) and other unmanned and drone systems used in Remote ID.
* [Unmanned System Operating Area](objects/unmanned_system_operating_area.md): The Unmanned System Operating Area object describes details about a precise area of operations for a UAS flight or mission.
* [Uniform Resource Locator](objects/url.md): The Uniform Resource Locator (URL) object describes the characteristics of a URL.
* [Vendor Attributes](objects/vendor_attributes.md): The Vendor Attributes object can be used to represent values of attributes populated by the Vendor/Finding Provider.
* [WHOIS](objects/whois.md): The resources of a WHOIS record for a given domain.