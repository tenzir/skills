# Operator Index

## Analyze

- [rare](operators/rare.md): Shows the least common values.
- [reverse](operators/reverse.md): Reverses the event order.
- [sort](operators/sort.md): Sorts events by the given expressions.
- [summarize](operators/summarize.md): Groups events and applies aggregate functions to each group.
- [top](operators/top.md): Shows the most common values.

## Charts

- [chart_area](operators/chart_area.md): Plots events on an area chart.
- [chart_bar](operators/chart_bar.md): Plots events on an bar chart.
- [chart_line](operators/chart_line.md): Plots events on an line chart.
- [chart_pie](operators/chart_pie.md): Plots events on an pie chart.

## Connecting Pipelines

- [publish](operators/publish.md): Publishes events to a channel with a topic.
- [subscribe](operators/subscribe.md): Subscribes to events from a channel with a topic.

## Contexts

- [context::create_bloom_filter](operators/context/create_bloom_filter.md): Creates a Bloom filter context.
- [context::create_geoip](operators/context/create_geoip.md): Creates a GeoIP context.
- [context::create_lookup_table](operators/context/create_lookup_table.md): Creates a lookup table context.
- [context::enrich](operators/context/enrich.md): Enriches events with data from a context.
- [context::erase](operators/context/erase.md): Removes entries from a context.
- [context::inspect](operators/context/inspect.md): Resets a context.
- [context::list](operators/context/list.md): Lists all contexts
- [context::load](operators/context/load.md): Loads context state.
- [context::lookup](operators/context/lookup.md): Performs live filtering of the import feed using a context and translates context updates into historical queries.
- [context::remove](operators/context/remove.md): Deletes a context.
- [context::reset](operators/context/reset.md): Resets a context.
- [context::save](operators/context/save.md): Saves context state.
- [context::update](operators/context/update.md): Updates a context with new data.

## Detection

- [sigma](operators/sigma.md): Filter the input with Sigma rules and output matching events.
- [yara](operators/yara.md): Executes YARA rules on byte streams.

## Encode & Decode

- [compress](operators/compress.md): Compresses a stream of bytes.
- [compress_brotli](operators/compress_brotli.md): Compresses a stream of bytes using Brotli compression.
- [compress_bz2](operators/compress_bz2.md): Compresses a stream of bytes using bz2 compression.
- [compress_gzip](operators/compress_gzip.md): Compresses a stream of bytes using gzip compression.
- [compress_lz4](operators/compress_lz4.md): Compresses a stream of bytes using lz4 compression.
- [compress_zstd](operators/compress_zstd.md): Compresses a stream of bytes using zstd compression.
- [decompress](operators/decompress.md): Decompresses a stream of bytes.
- [decompress_brotli](operators/decompress_brotli.md): Decompresses a stream of bytes in the Brotli format.
- [decompress_bz2](operators/decompress_bz2.md): Decompresses a stream of bytes in the Bzip2 format.
- [decompress_gzip](operators/decompress_gzip.md): Decompresses a stream of bytes in the Gzip format.
- [decompress_lz4](operators/decompress_lz4.md): Decompresses a stream of bytes in the Lz4 format.
- [decompress_zstd](operators/decompress_zstd.md): Decompresses a stream of bytes in the Zstd format.

## Escape Hatches

- [python](operators/python.md): Executes Python code against each event of the input.
- [shell](operators/shell.md): Executes a system command and hooks its stdin and stdout into the pipeline.

## Filter

- [assert](operators/assert.md): Drops events and emits a warning if the invariant is violated.
- [assert_throughput](operators/assert_throughput.md): Emits a warning if the pipeline does not have the expected throughput
- [deduplicate](operators/deduplicate.md): Removes duplicate events based on a common key.
- [head](operators/head.md): Limits the input to the first `n` events.
- [sample](operators/sample.md): Dynamically samples events from a event stream.
- [slice](operators/slice.md): Keeps a range of events within the interval `[begin, end)` stepping by `stride`.
- [tail](operators/tail.md): Limits the input to the last `n` events.
- [taste](operators/taste.md): Limits the input to `n` events per unique schema.
- [where](operators/where.md): Keeps only events for which the given predicate is true.

## Flow Control

- [cron](operators/cron.md): Runs a pipeline periodically according to a cron expression.
- [delay](operators/delay.md): Delays events relative to a given start time, with an optional speedup.
- [discard](operators/discard.md): Discards all incoming events.
- [every](operators/every.md): Runs a pipeline periodically at a fixed interval.
- [fork](operators/fork.md): Executes a subpipeline with a copy of the input.
- [load_balance](operators/load_balance.md): Routes the data to one of multiple subpipelines.
- [parallel](operators/parallel.md): Runs a subpipeline across multiple parallel workers.
- [pass](operators/pass.md): Does nothing with the input.
- [repeat](operators/repeat.md): Repeats the input a number of times.
- [throttle](operators/throttle.md): Limits the throughput of events in a pipeline.

## Host Inspection

- [files](operators/files.md): Shows file information for a given directory.
- [nics](operators/nics.md): Shows a snapshot of available network interfaces.
- [processes](operators/processes.md): Shows a snapshot of running processes.
- [sockets](operators/sockets.md): Shows a snapshot of open sockets.

## Internals

- [api](operators/api.md): Use Tenzir’s REST API directly from a pipeline.
- [batch](operators/batch.md): The `batch` operator controls the batch size of events.
- [buffer](operators/buffer.md): An in-memory buffer to improve handling of data spikes in upstream operators.
- [cache](operators/cache.md): An in-memory cache shared between pipelines.
- [local](operators/local.md): Forces a pipeline to run locally.
- [measure](operators/measure.md): Replaces the input with metrics describing the input.
- [remote](operators/remote.md): Forces a pipeline to run remotely at a node.
- [serve](operators/serve.md): Make events available under the `/serve` REST API endpoint
- [strict](operators/strict.md): Treats all warnings as errors.
- [unordered](operators/unordered.md): Removes ordering assumptions from a pipeline.

## Modify

- [dns_lookup](operators/dns_lookup.md): Performs DNS lookups to resolve IP addresses to hostnames or hostnames to IP addresses.
- [drop](operators/drop.md): Removes fields from the event.
- [drop_null_fields](operators/drop_null_fields.md): Removes fields containing null values from the event.
- [enumerate](operators/enumerate.md): Add a field with the number of preceding events.
- [http](operators/http.md): Sends HTTP/1.1 requests and forwards the response.
- [move](operators/move.md): Moves values from one field to another, removing the original field.
- [replace](operators/replace.md): Replaces all occurrences of a value with another value.
- [select](operators/select.md): Selects some values and discards the rest.
- [set](operators/set.md): Assigns a value to a field, creating it if necessary.
- [timeshift](operators/timeshift.md): Adjusts timestamps relative to a given start time, with an optional speedup.
- [unroll](operators/unroll.md): Returns a new event for each member of a list or a record in an event, duplicating the surrounding event.

## OCSF

- [ocsf::apply](operators/ocsf/apply.md): Casts incoming events to their OCSF type.
- [ocsf::cast](operators/ocsf/cast.md): Casts incoming events to their OCSF type.
- [ocsf::derive](operators/ocsf/derive.md): Automatically assigns enum strings from their integer counterparts and vice versa.
- [ocsf::trim](operators/ocsf/trim.md): Drops fields from OCSF events to reduce their size.

## Packages

- [package::add](operators/package/add.md): Installs a package.
- [package::list](operators/package/list.md): Shows installed packages.
- [package::remove](operators/package/remove.md): Uninstalls a package.

## Parsing

- [read_all](operators/read_all.md): Parses an incoming bytes stream into a single event.
- [read_bitz](operators/read_bitz.md): Parses bytes as *BITZ* format.
- [read_cef](operators/read_cef.md): Parses an incoming Common Event Format (CEF) stream into events.
- [read_csv](operators/read_csv.md): Read CSV (Comma-Separated Values) from a byte stream.
- [read_delimited](operators/read_delimited.md): Parses an incoming bytes stream into events using a string as delimiter.
- [read_delimited_regex](operators/read_delimited_regex.md): Parses an incoming bytes stream into events using a regular expression as delimiter.
- [read_feather](operators/read_feather.md): Parses an incoming Feather byte stream into events.
- [read_gelf](operators/read_gelf.md): Parses an incoming GELF stream into events.
- [read_grok](operators/read_grok.md): Parses lines of input with a grok pattern.
- [read_json](operators/read_json.md): Tip
- [read_kv](operators/read_kv.md): Read Key-Value pairs from a byte stream.
- [read_leef](operators/read_leef.md): Parses an incoming [LEEF](https://www.ibm.com/docs/en/dsm?topic=overview-leef-event-components) stream into events.
- [read_lines](operators/read_lines.md): Parses an incoming bytes stream into events.
- [read_ndjson](operators/read_ndjson.md): Parses an incoming NDJSON (newline-delimited JSON) stream into events.
- [read_parquet](operators/read_parquet.md): Reads events from a Parquet byte stream.
- [read_pcap](operators/read_pcap.md): Reads raw network packets in PCAP file format.
- [read_ssv](operators/read_ssv.md): Read SSV (Space-Separated Values) from a byte stream.
- [read_suricata](operators/read_suricata.md): Parse an incoming [Suricata EVE JSON](https://suricata.readthedocs.io/en/latest/output/eve/eve-json-output.html) stream into events.
- [read_syslog](operators/read_syslog.md): Parses an incoming Syslog stream into events.
- [read_tsv](operators/read_tsv.md): Read TSV (Tab-Separated Values) from a byte stream.
- [read_xsv](operators/read_xsv.md): Read XSV from a byte stream.
- [read_yaml](operators/read_yaml.md): Parses an incoming YAML stream into events.
- [read_zeek_json](operators/read_zeek_json.md): Parse an incoming Zeek JSON stream into events.
- [read_zeek_tsv](operators/read_zeek_tsv.md): Parses an incoming `Zeek TSV` stream into events.

## Pipelines

- [pipeline::activity](operators/pipeline/activity.md): Summarizes the activity of pipelines.
- [pipeline::detach](operators/pipeline/detach.md): Starts a pipeline in the node.
- [pipeline::list](operators/pipeline/list.md): Shows managed pipelines.
- [pipeline::run](operators/pipeline/run.md): Starts a pipeline in the node and waits for it to complete.

## Printing

- [write_bitz](operators/write_bitz.md): Writes events in *BITZ* format.
- [write_csv](operators/write_csv.md): Transforms event stream to CSV (Comma-Separated Values) byte stream.
- [write_feather](operators/write_feather.md): Transforms the input event stream to Feather byte stream.
- [write_json](operators/write_json.md): Transforms the input event stream to a JSON byte stream.
- [write_kv](operators/write_kv.md): Writes events in a Key-Value format.
- [write_lines](operators/write_lines.md): Writes events as key-value pairsthe *values* of an event.
- [write_ndjson](operators/write_ndjson.md): Transforms the input event stream to a Newline-Delimited JSON byte stream.
- [write_parquet](operators/write_parquet.md): Transforms event stream to a Parquet byte stream.
- [write_pcap](operators/write_pcap.md): Transforms event stream to PCAP byte stream.
- [write_ssv](operators/write_ssv.md): Transforms event stream to SSV (Space-Separated Values) byte stream.
- [write_syslog](operators/write_syslog.md): Writes events as syslog.
- [write_tql](operators/write_tql.md): Transforms the input event stream to a TQL notation byte stream.
- [write_tsv](operators/write_tsv.md): Transforms event stream to TSV (Tab-Separated Values) byte stream.
- [write_xsv](operators/write_xsv.md): Transforms event stream to XSV byte stream.
- [write_yaml](operators/write_yaml.md): Transforms the input event stream to YAML byte stream.
- [write_zeek_tsv](operators/write_zeek_tsv.md): Transforms event stream into Zeek Tab-Separated Value byte stream.

## Inputs

- [load_amqp](operators/load_amqp.md): Loads a byte stream via AMQP messages.
- [load_azure_blob_storage](operators/load_azure_blob_storage.md): Loads bytes from Azure Blob Storage.
- [load_file](operators/load_file.md): Loads the contents of the file at `path` as a byte stream.
- [load_ftp](operators/load_ftp.md): Loads a byte stream via FTP.
- [load_gcs](operators/load_gcs.md): Loads bytes from a Google Cloud Storage object.
- [load_google_cloud_pubsub](operators/load_google_cloud_pubsub.md): Subscribes to a Google Cloud Pub/Sub subscription and obtains bytes.
- [load_http](operators/load_http.md): Loads a byte stream via HTTP.
- [load_kafka](operators/load_kafka.md): Loads a byte stream from an Apache Kafka topic.
- [load_nic](operators/load_nic.md): Loads bytes from a network interface card (NIC).
- [load_s3](operators/load_s3.md): Loads from an Amazon S3 object.
- [load_sqs](operators/load_sqs.md): Loads bytes from [Amazon SQS](https://docs.aws.amazon.com/sqs/) queues.
- [load_stdin](operators/load_stdin.md): Accepts bytes from standard input.
- [load_tcp](operators/load_tcp.md): Loads bytes from a TCP or TLS connection.
- [load_udp](operators/load_udp.md): Loads bytes from a UDP socket.
- [load_zmq](operators/load_zmq.md): Receives ZeroMQ messages.
- [from](operators/from.md): Obtains events from an URI, inferring the source, compression and format.
- [from_azure_blob_storage](operators/from_azure_blob_storage.md): Reads one or multiple files from Azure Blob Storage.
- [from_file](operators/from_file.md): Reads one or multiple files from a filesystem.
- [from_fluent_bit](operators/from_fluent_bit.md): Receives events via Fluent Bit.
- [from_gcs](operators/from_gcs.md): Reads one or multiple files from Google Cloud Storage.
- [from_google_cloud_pubsub](operators/from_google_cloud_pubsub.md): Subscribes to a Google Cloud Pub/Sub subscription and yields events.
- [from_http](operators/from_http.md): Sends and receives HTTP/1.1 requests.
- [from_kafka](operators/from_kafka.md): Receives events from an Apache Kafka topic.
- [from_opensearch](operators/from_opensearch.md): Receives events via Opensearch Bulk API.
- [from_s3](operators/from_s3.md): Reads one or multiple files from Amazon S3.
- [from_sentinelone_data_lake](operators/from_sentinelone_data_lake.md): Retrieves PowerQuery results from SentinelOne Singularity Data Lake.
- [from_udp](operators/from_udp.md): Receives UDP datagrams and outputs structured events.
- [from_velociraptor](operators/from_velociraptor.md): Submits VQL to a Velociraptor server and returns the response as events.

## Node

- [diagnostics](operators/diagnostics.md): Retrieves diagnostic events from a Tenzir node.
- [metrics](operators/metrics.md): Retrieves metrics events from a Tenzir node.
- [openapi](operators/openapi.md): Shows the node’s OpenAPI specification.
- [plugins](operators/plugins.md): Shows all available plugins and built-ins.
- [version](operators/version.md): Shows the current version.
- [export](operators/export.md): Retrieves events from a Tenzir node.
- [fields](operators/fields.md): Retrieves all fields stored at a node.
- [import](operators/import.md): Imports events into a Tenzir node.
- [partitions](operators/partitions.md): Retrieves metadata about events stored at a node.
- [schemas](operators/schemas.md): Retrieves all schemas for events stored at a node.

## Outputs

- [save_amqp](operators/save_amqp.md): Saves a byte stream via AMQP messages.
- [save_azure_blob_storage](operators/save_azure_blob_storage.md): Saves bytes to Azure Blob Storage.
- [save_email](operators/save_email.md): Saves bytes through an SMTP server.
- [save_file](operators/save_file.md): Writes a byte stream to a file.
- [save_ftp](operators/save_ftp.md): Saves a byte stream via FTP.
- [save_gcs](operators/save_gcs.md): Saves bytes to a Google Cloud Storage object.
- [save_google_cloud_pubsub](operators/save_google_cloud_pubsub.md): Publishes to a Google Cloud Pub/Sub topic.
- [save_http](operators/save_http.md): Sends a byte stream via HTTP.
- [save_kafka](operators/save_kafka.md): Saves a byte stream to a Apache Kafka topic.
- [save_s3](operators/save_s3.md): Saves bytes to an Amazon S3 object.
- [save_sqs](operators/save_sqs.md): Saves bytes to [Amazon SQS](https://docs.aws.amazon.com/sqs/) queues.
- [save_stdout](operators/save_stdout.md): Writes a byte stream to standard output.
- [save_tcp](operators/save_tcp.md): Saves bytes to a TCP or TLS connection.
- [save_udp](operators/save_udp.md): Saves bytes to a UDP socket.
- [save_zmq](operators/save_zmq.md): Sends bytes as ZeroMQ messages.
- [to](operators/to.md): Saves to an URI, inferring the destination, compression and format.
- [to_amazon_security_lake](operators/to_amazon_security_lake.md): Sends OCSF events to Amazon Security Lake.
- [to_azure_log_analytics](operators/to_azure_log_analytics.md): Sends events to the Microsoft Azure Logs Ingestion API.
- [to_clickhouse](operators/to_clickhouse.md): Sends events to a ClickHouse table.
- [to_fluent_bit](operators/to_fluent_bit.md): Sends events via Fluent Bit.
- [to_google_cloud_logging](operators/to_google_cloud_logging.md): Sends events to Google Cloud Logging.
- [to_google_cloud_pubsub](operators/to_google_cloud_pubsub.md): Publishes events to a Google Cloud Pub/Sub topic.
- [to_google_secops](operators/to_google_secops.md): Sends unstructured events to a Google SecOps Chronicle instance.
- [to_hive](operators/to_hive.md): Writes events to a URI using hive partitioning.
- [to_kafka](operators/to_kafka.md): Sends messages to an Apache Kafka topic.
- [to_opensearch](operators/to_opensearch.md): Sends events to an OpenSearch-compatible Bulk API.
- [to_sentinelone_data_lake](operators/to_sentinelone_data_lake.md): Sends security events to SentinelOne Singularity Data Lake via REST API.
- [to_snowflake](operators/to_snowflake.md): Sends events to a Snowflake database.
- [to_splunk](operators/to_splunk.md): Sends events to a Splunk [HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/9.3.1/Data/UsetheHTTPEventCollector).
