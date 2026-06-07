# Splunk CIM Docs

These Markdown files provide additional Splunk CIM prose context for workflows, examples, interpretation guidance, setup, and release notes.

Use `../data/` as the authoritative reference for generated CIM facts: models, datasets, fields, tags, constraints, calculated fields, and lookups. Use this docs tree only to decide how to think about or apply those facts.

- **Docs root**: https://help.splunk.com/en/data-management/common-information-model/8.5/introduction/install-the-splunk-common-information-model-add-on
- **Docs version**: `8.5`
- **Manual PDF**: https://help.splunk.com/en/data-management/common-information-model/8.5/cim_user.pdf

## Start By Task

| Task | Read first | Boundary |
| --- | --- | --- |
| Understand CIM at a high level | [Overview of the Splunk Common Information Model](pages/introduction_overview_of_the_splunk_common_information_model.md) | Use docs for concepts and scope; use `../data/catalog.yaml` for the generated model inventory. |
| Normalize a new source | [Use the CIM to normalize data at search time](pages/using_the_common_information_model_use_the_cim_to_normalize_data_at_search_time.md) | Use docs for the workflow; use `../data/catalog.yaml` and `../data/models/*.yaml` for exact mapping facts. |
| Interpret reference tables | [How to use the CIM data model reference tables](pages/data_models_how_to_use_the_cim_data_model_reference_tables.md) | Use docs for how to read Splunk prose tables; use `../data/` files for authoritative fields and constraints. |
| Validate CIM compliance | [Use the CIM to validate your data](pages/using_the_common_information_model_use_the_cim_to_validate_your_data.md) | Use docs for the validation workflow; use `../data/models/splunk_cim_validation.yaml` for generated reference data. |
| Review provider field mapping examples | [Field mapping examples](#field-mapping-examples) | Use examples for reasoning patterns only; use `../data/fields.yaml` for exact CIM field usage. |
| Build reports, dashboards, or accelerated searches | [Workflows](#workflows) | Use docs for Splunk workflow guidance; use generated YAML for the model and dataset details. |
| Check release, setup, or support guidance | [Introduction and setup](#introduction-and-setup) | Use docs for Splunk operational guidance; use `../source.md` for generator provenance. |

## Imported Pages

Each page entry has a curated trigger summary to help decide whether to open the linked article. These summaries are navigation context only and intentionally do not restate generated CIM data.

### Start

#### [8.5](pages/index.md)

Open this when an agent needs the root landing metadata for the bundled CIM docs version. It only provides version and URL context, not substantive CIM guidance.


### Introduction and setup

#### [Overview of the Splunk Common Information Model](pages/introduction_overview_of_the_splunk_common_information_model.md)

Open this for high-level questions about what Splunk CIM is, why it exists, and how the manual is organized. It gives conceptual context for search-time normalization, CIM tooling, and where reference material lives; use `../data/` for exact model, field, and tag facts.

#### [Install the Splunk Common Information Model Add-on](pages/introduction_install_the_splunk_common_information_model_add_on.md)

Open this for installation-oriented tasks around the CIM add-on, especially where to install it and what index-related checks matter before setup. It provides deployment-scope guidance and points onward to setup and performance configuration.

#### [Release notes for the Splunk Common Information Model Add-on](pages/introduction_release_notes_for_the_splunk_common_information_model_add_on.md)

Open this when an agent needs release-specific context, compatibility notes, upgrade cautions, fixed issues, limitations, or deprecation history for the bundled CIM version. It is useful for explaining version behavior, not for deriving exact CIM model contents.

#### [Set up the Splunk Common Information Model Add-on](pages/introduction_set_up_the_splunk_common_information_model_add_on.md)

Open this for tasks about configuring CIM after installation: setup page access, index constraints, tag allowlists, data model acceleration, acceleration status, and field-filter impacts. It provides operational Splunk setup context and performance tradeoffs; use `../data/` for exact model, tag, and field reference facts.

#### [Support and resource links for the Splunk Common Information Model Add-on](pages/introduction_support_and_resource_links_for_the_splunk_common_information_model_add_on.md)

Open this when an agent needs support, download, Q&A, or broader Splunk documentation links for the CIM add-on. It is a resource-routing page rather than a technical normalization reference.

#### [Troubleshooting adaptive response actions](pages/introduction_troubleshooting_adaptive_response_actions.md)

Open this for troubleshooting adaptive response relay or action errors, especially Splunk Cloud Platform search head cluster deployments or environments without Splunk Enterprise Security. It provides cause-and-solution context for CAM/ARR setup and required related apps.


### Workflows

#### [Approaches to using the CIM](pages/using_the_common_information_model_approaches_to_using_the_cim.md)

Open this when an agent needs to choose the right CIM workflow for a broad task like normalization, validation, reporting, or custom alert actions. It provides routing context rather than implementation detail.

#### [Accelerate CIM data models](pages/using_the_common_information_model_accelerate_cim_data_models.md)

Open this when the task is about enabling, disabling, tuning, or auditing CIM data model acceleration. It gives operational workflow context for CIM Setup, summary ranges, acceleration enforcement, and the Data Model Audit dashboard.

#### [Match TA event types with CIM data models to accelerate searches](pages/using_the_common_information_model_match_ta_event_types_with_cim_data_models_to_accelerate_searches.md)

Open this when explaining how Technology Add-ons, event types, tags, data models, and accelerated searches fit together in Splunk Enterprise Security. It provides conceptual workflow context; use `../data/` for exact CIM model, tag, field, or dataset facts.

#### [Use the CIM Filters to exclude data](pages/using_the_common_information_model_use_the_cim_filters_to_exclude_data.md)

Open this when the task is to reduce CIM-backed search noise or false positives by excluding known categories of data. It explains the CIM filter macro workflow and where those macros fit into searches, especially with Enterprise Security asset and identity categories.

#### [Use the CIM to create reports and dashboards](pages/using_the_common_information_model_use_the_cim_to_create_reports_and_dashboards.md)

Open this when a user wants to build reports, dashboard panels, or Pivot visualizations from data already normalized to CIM. It provides reporting workflow context, including Pivot/Datasets entry points and the relationship between normalized data, dashboards, and acceleration monitoring.

#### [Use the CIM to normalize data at search time](pages/using_the_common_information_model_use_the_cim_to_normalize_data_at_search_time.md)

Open this when the task is to normalize a new Splunk data source to CIM at search time. It provides the end-to-end workflow for choosing relevant models, tagging events, mapping fields, validating output, optionally extending models, and packaging the result; use `../data/` for exact model, field, and tag facts.

#### [Use the CIM to validate your data](pages/using_the_common_information_model_use_the_cim_to_validate_your_data.md)

Open this when checking whether indexed data is actually mapping to CIM as expected. It gives validation workflow context using `datamodelsimple`, Pivot, validation datasets, missing extraction checks, and untagged event checks; use `../data/` for exact CIM structures.

#### [Use the common action model to build custom alert actions](pages/using_the_common_information_model_use_the_common_action_model_to_build_custom_alert_actions.md)

Open this when building or refactoring Splunk custom alert actions or adaptive response actions to follow the common action model. It provides developer workflow context for the helper library, alert action metadata spec, and introspection data emitted by compliant actions.


### Data model prose

#### [How to use the CIM data model reference tables](pages/data_models_how_to_use_the_cim_data_model_reference_tables.md)

Open this when an agent needs to understand how Splunk's CIM reference prose should be interpreted, especially tags as constraints, inherited fields, expected values, and the limits of rendered tables. Use it for narrative guidance on reading the docs; defer exact field, tag, hierarchy, and constraint facts to `../data/models/*.yaml` or `../data/fields.yaml`.

#### [Alerts](pages/data_models_alerts.md)

Open this when deciding whether an event belongs in the Alerts model, especially for vendor-agnostic security alerts produced by alerting systems rather than Splunk alerts, notable events, raw packet counts, or non-security IT alerts. It provides scope boundaries and examples of what should not be modeled as Alerts; use `../data/` for exact schema facts.

#### [Application State (deprecated)](pages/data_models_application_state_deprecated.md)

Open this for legacy references to Application State or when migrating older process, service, or listening-port inventory mappings. The narrative context is mainly historical: this model is deprecated and replaced by Endpoint, so current work should prefer the Endpoint model.

#### [Authentication](pages/data_models_authentication.md)

Open this for questions about modeling login activity from any source, including authentication outcomes, involved applications, source and destination systems, and privilege-escalation context. It explains the semantic roles of users and systems in authentication events; defer exact fields, prescribed values, and dataset constraints to `../data/`.

#### [Certificates](pages/data_models_certificates.md)

Open this for key and certificate management events from secure servers or IAM systems, especially SSL/TLS certificate observations. It provides narrative context for issuer/subject identity, validity timing, and a worked certificate-event example; exact field requirements and dataset facts belong in `../data/`.

#### [Change](pages/data_models_change.md)

Open this for administrative or policy changes to infrastructure devices, servers, cloud environments, accounts, network controls, or EDR systems. Its most useful prose explains the boundary between Change and Endpoint, especially administrative changes versus endpoint-client activity; exact facts should come from `../data/`.

#### [Change Analysis (deprecated)](pages/data_models_change_analysis_deprecated.md)

Open this only when handling old Change Analysis references or migration from pre-4.12 CIM content. It frames the deprecated CRUD-change model and its historical scope; use the current Change page for active guidance and YAML files for exact facts.

#### [CIM fields per associated data model](pages/data_models_cim_fields_per_associated_data_model.md)

Open this when an agent needs a prose index for field overlap across CIM models or wants context for joining or searching across datasets that share field names. Treat it as a cross-reference aid, not the source of truth; use `../data/fields.yaml` and model YAML files for exact associations.

#### [Data Access](pages/data_models_data_access.md)

Open this for user-driven access to shared, collaborative data such as documents, repositories, comments, tasks, invites, and similar user-managed objects. The key narrative value is boundary guidance against Change and Web: regular-user content collaboration maps here, while admin configuration and web-server client delivery generally do not.

#### [Data Loss Prevention](pages/data_models_data_loss_prevention.md)

Open this for events generated by DLP tools that identify, monitor, or protect sensitive data. It frames DLP as incident-oriented tool output involving affected objects, users, sources, destinations, and severity context; defer exact field and tag requirements to `../data/`.

#### [Databases](pages/data_models_databases.md)

Open this for events about structured or semi-structured data storage systems, including database activity, health, sessions, locks, queries, capacity, and performance context. The page provides narrative scope for database observability; use YAML sources for exact dataset and field details.

#### [Email](pages/data_models_email.md)

Open this for email traffic normalization, whether server-to-server or client-to-server. It gives narrative context for message delivery, content, filtering, senders, recipients, attachments, and mail infrastructure roles; exact protocol values, fields, and dataset facts belong in `../data/`.

#### [Endpoint](pages/data_models_endpoint.md)

Open this for endpoint-client monitoring such as process launches, service launches, listening ports, filesystem activity, and registry activity on user machines, laptops, virtual desktops, or BYOD endpoints. Its key narrative guidance is the distinction from Change: endpoint activity belongs here, while administrative or policy changes belong under Change.

#### [Event Signatures](pages/data_models_event_signatures.md)

Open this when a task asks where Windows Event IDs and their human-readable descriptions belong in CIM. It explains that this model is specifically for Microsoft Windows event signature context, not a general event taxonomy.

#### [Interprocess Messaging](pages/data_models_interprocess_messaging.md)

Open this for questions about modeling RPC, WMI, REST/SOAP calls, queues, or message-oriented middleware transactions. It gives narrative scope for request/response messaging, timing, payloads, and endpoints; use YAML for exact field requirements.

#### [Intrusion Detection](pages/data_models_intrusion_detection.md)

Open this when deciding how to model IDS/IPS attack detections or signature-based traffic blocks. It explains the boundary between simple network allow/deny traffic and intrusion detection based on deeper traffic patterns or signatures.

#### [Inventory](pages/data_models_inventory.md)

Open this for asset inventory, compute inventory, infrastructure topology, OS, local accounts, virtual systems, snapshots, and hardware/resource descriptions. It provides the model's broad inventory intent and notes the legacy Compute Inventory naming context.

#### [Java Virtual Machines (JVM)](pages/data_models_java_virtual_machines_jvm.md)

Open this for JVM monitoring questions covering Java runtime, threading, class loading, compilation, OS, and memory observations. It frames the model as generic Java server platform telemetry; exact metric names belong in YAML.

#### [Malware](pages/data_models_malware.md)

Open this for antivirus, anti-malware, endpoint protection, infection detections, and malware product operations. It explains the distinction between malware attack alerting and operational health/status monitoring for protection systems.

#### [Network Resolution (DNS)](pages/data_models_network_resolution_dns.md)

Open this for DNS resolution telemetry, including client/server and server/server DNS activity. It provides the narrative scope for DNS queries, responses, timing, and resolution outcomes; defer exact record and response details to YAML.

#### [Network Sessions](pages/data_models_network_sessions.md)

Open this for DHCP and VPN session modeling, especially lease starts/ends, VPN start/teardown attempts, and session user/client context. It explains that the model is about network session lifecycle rather than raw packet or flow traffic.

#### [Network Traffic](pages/data_models_network_traffic.md)

Open this for firewall, flow, proxy-adjacent, NAT, packet/byte, port, transport, and connection allow/deny modeling. It provides the key distinction from Intrusion Detection: rule-based connection handling versus signature/pattern-based attack detection.

#### [Performance](pages/data_models_performance.md)

Open this for performance telemetry across systems, facilities, CPU, memory, storage, network throughput, uptime, and time synchronization. It gives scope for operational health and resource tracking; use YAML for exact metric fields.

#### [Splunk Audit Logs](pages/data_models_splunk_audit_logs.md)

Open this for Splunk-internal audit, search activity, scheduler activity, data model acceleration, view activity, web service errors, and modular alert actions. It provides narrative context for Splunk platform observability and custom alert action results.

#### [Ticket Management](pages/data_models_ticket_management.md)

Open this for service desk, ITIL-style requests, incidents, problems, changes, GRC tickets, or bug/ticket workflow normalization. It explains the lifecycle and ownership context for service requests without replacing exact model facts in YAML.

#### [Updates](pages/data_models_updates.md)

Open this for patch management, update status, patch errors, and central or endpoint update tooling events. It frames update telemetry around affected systems, patch requirements, installation outcomes, and update product context.

#### [Vulnerabilities](pages/data_models_vulnerabilities.md)

Open this for vulnerability scanner findings, CVE-style references, severity, affected hosts, and scanner/reporting system context. It explains vulnerability detection scope and cross-reference intent; use YAML for exact identifiers and fields.

#### [Web](pages/data_models_web.md)

Open this for web server, proxy, HTTP request/response, URL, user agent, response code, and cloud storage access events in security or operational contexts. It provides the narrative boundary for web/proxy telemetry, while exact HTTP and storage fields belong in YAML.


### Field mapping examples

#### [Authentication Field Mapping](pages/field_mappings_authentication_field_mapping.md)

Open this when the task involves reasoning about CIM-style normalization for cloud authentication events, especially login success, login failure, or privilege escalation. It compares GCP, Microsoft 365, AWS, and short-lived credential flows; use it for mapping intuition only and defer exact fields to `../data/`.

#### [Change Field Mapping](pages/field_mappings_change_field_mapping.md)

Open this when the task is about cloud administrative change events, such as user updates or compute reboot actions. It gives AWS and Azure examples and useful reasoning about identifying the changed object from provider payloads, while exact CIM field expectations should still come from `../data/`.

#### [Data Access Field Mapping](pages/field_mappings_data_access_field_mapping.md)

Open this when the task involves data-access normalization for file activity, especially upload events in SaaS storage logs. It compares Google Drive and Box examples to show how actor, object, owner, and source context can appear differently across providers.

#### [Network Traffic Field Mapping](pages/field_mappings_network_traffic_field_mapping.md)

Open this when the task involves cloud flow-log normalization or comparing network traffic records from different providers. It uses GCP and AWS source-flow examples to illustrate provider-specific context such as endpoints, direction/reporting perspective, counters, and timing without serving as the authoritative field source.


### Worked examples

#### [Use the CIM to normalize OSSEC data](pages/examples_use_the_cim_to_normalize_ossec_data.md)

Open this when the task needs a full worked example of turning a proprietary IDS/syslog source into a Splunk add-on aligned with CIM expectations. It walks through sourcetyping, tags, regex extractions, aliases, lookups, validation, and optional packaging for OSSEC data.

#### [Use the CIM to normalize CPU performance metrics](pages/examples_use_the_cim_to_normalize_cpu_performance_metrics.md)

Open this when the task is about a procedural CIM-normalization workflow for performance metrics, especially CPU metrics for ITSI-style use cases. It provides both Splunk Web and config-file approaches for tags, event types, field aliases, extraction, and validation.


### Additional normalizations

#### [ITSI Normalization](pages/additional_normalizations_itsi_normalization.md)

Open this when an agent needs ITSI Universal Alerting normalization context or wants to understand what kind of alert fields the ITSI-oriented normalization discusses. It contains a field-oriented table, but use `../data/` for exact structured facts when needed.
