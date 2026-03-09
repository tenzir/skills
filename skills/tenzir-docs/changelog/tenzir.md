# Tenzir Node

> The security data pipeline engine that collects security telemetry, normalizes events to OCSF, and offers an open data lake for storage.


The security data pipeline engine that collects security telemetry, normalizes events to OCSF, and offers an open data lake for storage.

[ GitHub ](https://github.com/tenzir/tenzir/releases)

[Download releases and artifacts](https://github.com/tenzir/tenzir/releases)

[ RSS Feed ](/changelog/tenzir.xml)

[Subscribe to release updates](/changelog/tenzir.xml)

## Releases

* [v5.28.0 Mar 6, 2026](tenzir/v5-28-0.md)

  [This release adds support for parsing Check Point syslog structured-data dialects that deviate from RFC 5424, improving out-of-the-box interoperability with Check Point exports. It also makes DNS hostname resolution in the load\_tcp operator opt-in and fixes several parser bugs related to schema c...](tenzir/v5-28-0.md)
* [v5.27.3 Mar 3, 2026](tenzir/v5-27-3.md)

  [This release fixes a crash that could occur when reading JSON data. It also improves CEF parsing to handle non-conforming unescaped equals characters.](tenzir/v5-27-3.md)
* [v5.27.2 Feb 27, 2026](tenzir/v5-27-2.md)

  [This release adds the hmac function for computing Hash-based Message Authentication Codes over strings and blobs. It also fixes an assertion failure in array slicing that was introduced in v5.27.0.](tenzir/v5-27-2.md)
* [v5.27.1 Feb 25, 2026](tenzir/v5-27-1.md)

  [This release fixes an issue where the platform plugin did not correctly use the configured certfile, keyfile, and cafile options for client certificate authentication.](tenzir/v5-27-1.md)
* [v5.27.0 Feb 24, 2026](tenzir/v5-27-0.md)

  [This release enhances the sort function with custom comparators and descending order support, and extends the slice function to work with lists.](tenzir/v5-27-0.md)
* [v5.26.0 Feb 13, 2026](tenzir/v5-26-0.md)

  [This release introduces the from\_mysql operator for reading data directly from MySQL databases, with support for live streaming, custom SQL queries, and TLS connections. It also adds link-based HTTP pagination and optional field parameters for user-defined operators.](tenzir/v5-26-0.md)
* [v5.25.2 Feb 9, 2026](tenzir/v5-25-2.md)

  [This release fixes the sigma operator to correctly load all rule files from a directory.](tenzir/v5-25-2.md)
* [v5.25.1 Jan 30, 2026](tenzir/v5-25-1.md)

  [This release includes several bug fixes for the JSON parser, `where`, `replace`, and `if` operators, along with Kafka decompression support and a new `raw_message` option for the `read_syslog` operator.](tenzir/v5-25-1.md)
* [v5.25.0 Jan 27, 2026](tenzir/v5-25-0.md)

  [This release adds periodic emission to the summarize operator, enabling real-time streaming analytics with configurable intervals and accumulation modes. It also introduces AWS IAM authentication across SQS, S3, and Kafka operators, and fixes memory instability in from\_http when used with slow do...](tenzir/v5-25-0.md)
* [v5.24.0 Jan 16, 2026](tenzir/v5-24-0.md)

  [This release adds XML parsing functions (`parse_xml` and `parse_winlog`) for analyzing XML-formatted logs including Windows Event Logs. It also introduces the `parallel` operator for parallel pipeline execution, fixes a socket leak in `from_http` that could cause resource exhaustion, and includes...](tenzir/v5-24-0.md)
* [v5.23.1 Jan 2, 2026](tenzir/v5-23-1.md)

  [This release fixes internal errors in expression evaluation for heterogeneous data, resolves a crash in the operator when using , and ensures the connector shuts down gracefully.](tenzir/v5-23-1.md)
* [v5.23.0 Dec 23, 2025](tenzir/v5-23-0.md)

  [This release introduces centralized node-level TLS configuration, allowing you to configure TLS settings once in tenzir.yaml instead of passing options to each operator individually. It also adds support for event-timestamp-based compaction rules and a count field in the deduplicate operator.](tenzir/v5-23-0.md)
* [v5.22.2 Dec 21, 2025](tenzir/v5-22-2.md)

  [This release fixes a performance regression when parsing lists with mixed-type elements, where batch processing was inadvertently broken. It also resolves an assertion failure that could crash Tenzir when encountering events with duplicate keys.](tenzir/v5-22-2.md)
* [v5.22.1 Dec 18, 2025](tenzir/v5-22-1.md)

  [This release fixes a bug where the `publish` operator could drop events.](tenzir/v5-22-1.md)
* [v5.22.0 Dec 16, 2025](tenzir/v5-22-0.md)

  [This release introduces support for arguments in user-defined operators, letting operators declare positional and named parameters with optional default values and use them just like built-in operators. It also enhances parser behavior for duplicate keys and includes several important stability, ...](tenzir/v5-22-0.md)
* [v5.21.2 Nov 28, 2025](tenzir/v5-21-2.md)

  [This is a bugfix release that fixes timestamp handling in the python operator and the backpressure handling in publish and subscribe.](tenzir/v5-21-2.md)
* [v5.21.1 Nov 24, 2025](tenzir/v5-21-1.md)

  [This release features new and improved hash functions as well as a couple of bugfixes.](tenzir/v5-21-1.md)
* [v5.21.0 Nov 19, 2025](tenzir/v5-21-0.md)

  [This release improves the stability of pipelines by applying backpressure more effectively, ensuring upstream components slow down before overwhelming subscribers. It also enhances daily operations by improving parquet reliability, adding Base58 support, and extending the built-in OCSF operators ...](tenzir/v5-21-0.md)
* [v5.20.2 Nov 25, 2025](tenzir/v5-20-2.md)

  [This release backports the changes made in v5.21.1 to v5.20.1.](tenzir/v5-20-2.md)
* [v5.20.1 Nov 13, 2025](tenzir/v5-20-1.md)

  [This patch release comes with a few new experimental memory metrics. Furthermore, it resolves an issue where the memory usage would grow without bounds on some systems.](tenzir/v5-20-1.md)
* [v5.20.0 Nov 3, 2025](tenzir/v5-20-0.md)

  [We continue our quest for better memory usage by switching out the memory allocator to the battle-tested `mimalloc`, as well as adding metrics collecting for memory usage.](tenzir/v5-20-0.md)
* [v5.19.0 Oct 27, 2025](tenzir/v5-19-0.md)

  [This release introduces the `ocsf::cast` operator to streamline schema transformations for OCSF events and adds support for one-level recursion in OCSF objects, enabling recursive relations such as `process.parent_process` and `analytic.related_analytics`.](tenzir/v5-19-0.md)
* [v5.18.0 Oct 20, 2025](tenzir/v5-18-0.md)

  [This release focuses on improving performance and memory usage. Pipelines are now faster, especially when using if conditions or parsing highly heterogeneous events. Memory usage has also been substantially reduced.](tenzir/v5-18-0.md)
* [v5.17.0 Oct 13, 2025](tenzir/v5-17-0.md)

  [This release introduces user-defined operators in packages, allowing you to extend Tenzir with custom operators defined in TQL files. It also adds list manipulation functions, a recursive search function, and improved memory management.](tenzir/v5-17-0.md)
* [v5.16.0 Sep 26, 2025](tenzir/v5-16-0.md)

  [This release brings forth stability improvements under high load that could cause platform unresponsiveness, fixes API request isolation problems, better kafka diagnostics and more.](tenzir/v5-16-0.md)
* [v5.15.0 Sep 19, 2025](tenzir/v5-15-0.md)

  [This release enhances TQL's data transformation capabilities with lambda expressions that can capture surrounding fields in `map` and `where` functions, plus grouped enumeration for separate event counting. We've also improved operator composability with enhanced `to_splunk` parameters, added oct...](tenzir/v5-15-0.md)
* [v5.14.0 Sep 11, 2025](tenzir/v5-14-0.md)

  [This release introduces an integration fo SentinelOne Singularity™ Data Lake and a new message based `to_kafka` operator that features a one to one event to message relation.](tenzir/v5-14-0.md)
* [v5.13.2 Sep 1, 2025](tenzir/v5-13-2.md)

  [This release adds a new S3 operator and fixes a bug within the `fork` operator.](tenzir/v5-13-2.md)
* [v5.13.1 Aug 28, 2025](tenzir/v5-13-1.md)

  [This release adds a new Azure Blob Storage operator with account key authentication and improves Google Security Operations retry handling. It also contains various small fixes and improvements.](tenzir/v5-13-1.md)
* [v5.13.0 Aug 20, 2025](tenzir/v5-13-0.md)

  [This release enhances UDP ingestion with the new `from_udp` operator that produces structured events with sender metadata. We also improved the execution model for `every` and `cron` subpipelines, added DNS lookup capabilities, and made the Syslog parser more flexible.](tenzir/v5-13-0.md)
* [v5.12.1 Aug 6, 2025](tenzir/v5-12-1.md)

  [We fixed two bugs in the `to_google_secops` and `to_amazon_security_lake` operators.](tenzir/v5-12-1.md)
* [v5.12.0 Aug 4, 2025](tenzir/v5-12-0.md)

  [This release adds support for OCSF 1.6.0 and introduces the `replace` operator.](tenzir/v5-12-0.md)
* [v5.11.1 Aug 1, 2025](tenzir/v5-11-1.md)

  [This release introduces payload compression for Azure Log Analytics to reduce bandwidth usage, as well as an important fix for a `from_http` bug that was introduced with the previous release.](tenzir/v5-11-1.md)
* [v5.11.0 Aug 1, 2025](tenzir/v5-11-0.md)

  [This release delivers significant performance improvements for situations with many concurrent pipelines, making Tenzir more robust under high-load scenarios. New features include AWS role assumption support, enhanced string trimming functionality, and improved HTTP error handling capabilities. A...](tenzir/v5-11-0.md)
* [v5.10.0 Jul 22, 2025](tenzir/v5-10-0.md)

  [This release introduces two new powerful OCSF operators that automate enum derivation and provide intelligent field trimming. The update also includes string padding functions, better HTTP requests, IP categorization and much more!](tenzir/v5-10-0.md)
* [v5.9.0 Jul 6, 2025](tenzir/v5-9-0.md)

  [This release brings a family of UUID functions to TQL, making it easier to generate random numbers for a variety of use cases.](tenzir/v5-9-0.md)
* [v5.8.0 Jul 3, 2025](tenzir/v5-8-0.md)

  [This release introduces format and compression inference from URLs for HTTP data sources, streamlining data loading workflows. It also includes bug fixes for secret resolution and HTTP server mode.](tenzir/v5-8-0.md)
* [v5.7.0 Jul 1, 2025](tenzir/v5-7-0.md)

  [Tenzir Node v5.7.0 introduces a new secret type that keeps its sensitive content hidden while enabling flexible secret retrieval. This release also adds support for OCSF extensions and brings several improvements to the operator.](tenzir/v5-7-0.md)
* [v5.6.1 Jun 24, 2025](tenzir/v5-6-1.md)

  [This release restores an aggregation function that was accidentally made unavailable in Tenzir Node v5.6.0.](tenzir/v5-6-1.md)
* [v5.6.0 Jun 24, 2025](tenzir/v5-6-0.md)

  [The operator now supports event-dependent topics, making routing between pipelines more flexible. Additionally, new and operators make taking apart custom logs easier than before.](tenzir/v5-6-0.md)
* [v5.5.0 Jun 18, 2025](tenzir/v5-5-0.md)

  [Built-in support for normalizing OCSF events to their upstream schema makes normalizations easier than ever with Tenzir Node v5.5.](tenzir/v5-5-0.md)
* [v5.4.1 Jun 13, 2025](tenzir/v5-4-1.md)

  [This release fixes a bug within the JSON printer that could lead to invalid JSON being produced, and also led to response timeouts when using the Tenzir Platform.](tenzir/v5-4-1.md)
* [v5.4.0 Jun 12, 2025](tenzir/v5-4-0.md)

  [With the introduction of format strings to TQL, this release makes string construction from multiple parts easier than ever before.](tenzir/v5-4-0.md)
* [v5.3.4 Jun 10, 2025](tenzir/v5-3-4.md)

  [This release fixes a bug that caused package installation outside of the Tenzir Library to fail, which caused Demo Nodes in the Tenzir Platform to not have any packages installed.](tenzir/v5-3-4.md)
* [v5.3.3 Jun 6, 2025](tenzir/v5-3-3.md)

  [The from\_http and http operators now support response sizes upto 2GiB](tenzir/v5-3-3.md)
* [v5.3.2 Jun 3, 2025](tenzir/v5-3-2.md)

  [Tenzir Node v5.3.1 updated the pyproject version but did not actually commit it, causing the Python operator to fail to start. This release fixes the issue.](tenzir/v5-3-2.md)
* [v5.3.0 Jun 3, 2025](tenzir/v5-3-0.md)

  [This release brings forth improvements to HTTP support in Tenzir, supporting requests as transformations and paginating APIs.](tenzir/v5-3-0.md)
* [v5.2.0 May 23, 2025](tenzir/v5-2-0.md)
* [v5.1.8 May 20, 2025](tenzir/v5-1-8.md)
* [v5.1.7 May 19, 2025](tenzir/v5-1-7.md)
* [v5.1.6 May 15, 2025](tenzir/v5-1-6.md)
* [v5.1.5 May 12, 2025](tenzir/v5-1-5.md)
* [v5.1.4 May 8, 2025](tenzir/v5-1-4.md)
* [v5.1.3 May 5, 2025](tenzir/v5-1-3.md)
* [v5.1.2 Apr 30, 2025](tenzir/v5-1-2.md)
* [v5.1.1 Apr 28, 2025](tenzir/v5-1-1.md)
* [v5.1.0 Apr 25, 2025](tenzir/v5-1-0.md)
* [v5.0.1 Apr 22, 2025](tenzir/v5-0-1.md)
* [v5.0.0 Apr 17, 2025](tenzir/v5-0-0.md)
* [v4.32.1 Apr 8, 2025](tenzir/v4-32-1.md)
* [v4.32.0 Apr 4, 2025](tenzir/v4-32-0.md)
* [v4.31.2 Apr 1, 2025](tenzir/v4-31-2.md)
* [v4.31.0 Mar 31, 2025](tenzir/v4-31-0.md)
* [v4.30.3 Mar 25, 2025](tenzir/v4-30-3.md)
* [v4.30.2 Mar 22, 2025](tenzir/v4-30-2.md)
* [v4.30.1 Mar 20, 2025](tenzir/v4-30-1.md)
* [v4.30.0 Mar 18, 2025](tenzir/v4-30-0.md)
* [v4.29.2 Mar 11, 2025](tenzir/v4-29-2.md)
* [v4.29.1 Mar 3, 2025](tenzir/v4-29-1.md)
* [v4.29.0 Feb 25, 2025](tenzir/v4-29-0.md)
* [v4.28.2 Feb 13, 2025](tenzir/v4-28-2.md)
* [v4.28.0 Feb 10, 2025](tenzir/v4-28-0.md)
* [v4.27.0 Jan 30, 2025](tenzir/v4-27-0.md)
* [v4.26.0 Jan 22, 2025](tenzir/v4-26-0.md)
* [v4.25.0 Jan 9, 2025](tenzir/v4-25-0.md)
* [v4.24.1 Dec 12, 2024](tenzir/v4-24-1.md)
* [v4.24.0 Dec 3, 2024](tenzir/v4-24-0.md)
* [v4.23.1 Nov 21, 2024](tenzir/v4-23-1.md)
* [v4.23.0 Nov 7, 2024](tenzir/v4-23-0.md)
* [v4.22.2 Oct 28, 2024](tenzir/v4-22-2.md)
* [v4.22.1 Oct 23, 2024](tenzir/v4-22-1.md)
* [v4.22.0 Oct 18, 2024](tenzir/v4-22-0.md)
* [v4.21.1 Oct 11, 2024](tenzir/v4-21-1.md)
* [v4.21.0 Oct 4, 2024](tenzir/v4-21-0.md)
* [v4.20.3 Sep 9, 2024](tenzir/v4-20-3.md)
* [v4.20.2 Sep 6, 2024](tenzir/v4-20-2.md)
* [v4.20.1 Sep 2, 2024](tenzir/v4-20-1.md)
* [v4.20.0 Aug 30, 2024](tenzir/v4-20-0.md)
* [v4.19.6 Aug 15, 2024](tenzir/v4-19-6.md)
* [v4.19.5 Aug 13, 2024](tenzir/v4-19-5.md)
* [v4.19.4 Aug 8, 2024](tenzir/v4-19-4.md)
* [v4.19.3 Aug 6, 2024](tenzir/v4-19-3.md)
* [v4.19.2 Aug 6, 2024](tenzir/v4-19-2.md)
* [v4.19.1 Aug 2, 2024](tenzir/v4-19-1.md)
* [v4.19.0 Jul 26, 2024](tenzir/v4-19-0.md)
* [v4.18.5 Jul 19, 2024](tenzir/v4-18-5.md)
* [v4.18.4 Jul 17, 2024](tenzir/v4-18-4.md)
* [v4.18.3 Jul 16, 2024](tenzir/v4-18-3.md)
* [v4.18.2 Jul 15, 2024](tenzir/v4-18-2.md)
* [v4.18.1 Jul 12, 2024](tenzir/v4-18-1.md)
* [v4.18.0 Jul 11, 2024](tenzir/v4-18-0.md)
* [v4.17.4 Jun 27, 2024](tenzir/v4-17-4.md)
* [v4.17.3 Jun 25, 2024](tenzir/v4-17-3.md)
* [v4.17.2 Jun 24, 2024](tenzir/v4-17-2.md)
* [v4.17.1 Jun 21, 2024](tenzir/v4-17-1.md)
* [v4.17.0 Jun 21, 2024](tenzir/v4-17-0.md)
* [v4.16.0 Jun 5, 2024](tenzir/v4-16-0.md)
* [v4.15.2 May 31, 2024](tenzir/v4-15-2.md)
* [v4.15.1 May 31, 2024](tenzir/v4-15-1.md)
* [v4.15.0 May 31, 2024](tenzir/v4-15-0.md)
* [v4.14.0 May 17, 2024](tenzir/v4-14-0.md)
* [v4.13.1 May 14, 2024](tenzir/v4-13-1.md)
* [v4.13.0 May 10, 2024](tenzir/v4-13-0.md)
* [v4.12.2 Apr 30, 2024](tenzir/v4-12-2.md)
* [v4.12.1 Apr 26, 2024](tenzir/v4-12-1.md)
* [v4.12.0 Apr 24, 2024](tenzir/v4-12-0.md)
* [v4.11.2 Mar 26, 2024](tenzir/v4-11-2.md)
* [v4.11.0 Mar 22, 2024](tenzir/v4-11-0.md)
* [v4.10.4 Mar 13, 2024](tenzir/v4-10-4.md)
* [v4.10.3 Mar 12, 2024](tenzir/v4-10-3.md)
* [v4.10.1 Mar 11, 2024](tenzir/v4-10-1.md)
* [v4.10.0 Mar 11, 2024](tenzir/v4-10-0.md)
* [v4.9.0 Feb 21, 2024](tenzir/v4-9-0.md)
* [v4.8.2 Jan 24, 2024](tenzir/v4-8-2.md)
* [v4.8.1 Jan 23, 2024](tenzir/v4-8-1.md)
* [v4.8.0 Jan 22, 2024](tenzir/v4-8-0.md)
* [v4.7.1 Dec 20, 2023](tenzir/v4-7-1.md)
* [v4.7.0 Dec 19, 2023](tenzir/v4-7-0.md)
* [v4.6.4 Dec 7, 2023](tenzir/v4-6-4.md)
* [v4.6.3 Dec 4, 2023](tenzir/v4-6-3.md)
* [v4.6.0 Dec 1, 2023](tenzir/v4-6-0.md)
* [v4.5.0 Nov 16, 2023](tenzir/v4-5-0.md)
* [v4.4.0 Nov 6, 2023](tenzir/v4-4-0.md)
* [v4.3.0 Oct 10, 2023](tenzir/v4-3-0.md)
* [v4.2.0 Sep 19, 2023](tenzir/v4-2-0.md)
* [v4.1.0 Aug 31, 2023](tenzir/v4-1-0.md)
* [v4.0.1 Aug 9, 2023](tenzir/v4-0-1.md)
* [v4.0.0 Aug 7, 2023](tenzir/v4-0-0.md)
* [v3.1.0 May 12, 2023](tenzir/v3-1-0.md)
* [v3.0.4 Apr 18, 2023](tenzir/v3-0-4.md)
* [v3.0.3 Mar 31, 2023](tenzir/v3-0-3.md)
* [v3.0.2 Mar 21, 2023](tenzir/v3-0-2.md)
* [v3.0.1 Mar 16, 2023](tenzir/v3-0-1.md)
* [v3.0.0 Mar 14, 2023](tenzir/v3-0-0.md)
* [v2.4.2 Mar 31, 2023](tenzir/v2-4-2.md)
* [v2.4.1 Dec 19, 2022](tenzir/v2-4-1.md)
* [v2.4.0 Dec 9, 2022](tenzir/v2-4-0.md)
* [v2.3.1 Oct 14, 2022](tenzir/v2-3-1.md)
* [v2.3.0 Sep 1, 2022](tenzir/v2-3-0.md)
* [v2.2.0 Aug 5, 2022](tenzir/v2-2-0.md)
* [v2.1.0 Jul 7, 2022](tenzir/v2-1-0.md)
* [v2.0.0 May 16, 2022](tenzir/v2-0-0.md)
* [v1.1.2 Mar 29, 2022](tenzir/v1-1-2.md)
* [v1.1.1 Mar 25, 2022](tenzir/v1-1-1.md)
* [v1.1.0 Mar 3, 2022](tenzir/v1-1-0.md)
* [v1.0.0 Jan 27, 2022](tenzir/v1-0-0.md)