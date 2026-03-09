# Operators


Tenzir comes with a wide range of built-in pipeline operators.

## Analyze

### [rare](operators/rare.md)

Shows the least common values.

```tql
rare auth.token
```

### [reverse](operators/reverse.md)

Reverses the event order.

```tql
reverse
```

### [sort](operators/sort.md)

Sorts events by the given expressions.

```tql
sort name, -abs(transaction)
```

### [summarize](operators/summarize.md)

Groups events and applies aggregate functions to each group.

```tql
summarize name, sum(amount)
```

### [top](operators/top.md)

Shows the most common values.

```tql
top user
```

## Charts

### [chart\_area](operators/chart_area.md)

Plots events on an area chart.

```tql
chart_area …
```

### [chart\_bar](operators/chart_bar.md)

Plots events on an bar chart.

```tql
chart_bar …
```

### [chart\_line](operators/chart_line.md)

Plots events on an line chart.

```tql
chart_line …
```

### [chart\_pie](operators/chart_pie.md)

Plots events on an pie chart.

```tql
chart_pie …
```

## Connecting Pipelines

### [publish](operators/publish.md)

Publishes events to a channel with a topic.

```tql
publish "topic"
```

### [subscribe](operators/subscribe.md)

Subscribes to events from a channel with a topic.

```tql
subscribe "topic"
```

## Contexts

### [context::create\_bloom\_filter](operators/context/create_bloom_filter.md)

Creates a Bloom filter context.

```tql
context::create_bloom_filter "ctx", capacity=1Mi, fp_probability=0.01
```

### [context::create\_geoip](operators/context/create_geoip.md)

Creates a GeoIP context.

```tql
context::create_geoip "ctx", db_path="GeoLite2-City.mmdb"
```

### [context::create\_lookup\_table](operators/context/create_lookup_table.md)

Creates a lookup table context.

```tql
context::create_lookup_table "ctx"
```

### [context::enrich](operators/context/enrich.md)

Enriches events with data from a context.

```tql
context::enrich "ctx", key=x
```

### [context::erase](operators/context/erase.md)

Removes entries from a context.

```tql
context::erase "ctx", key=x
```

### [context::inspect](operators/context/inspect.md)

Resets a context.

```tql
context::inspect "ctx"
```

### [context::list](operators/context/list.md)

Lists all contexts

```tql
context::list
```

### [context::load](operators/context/load.md)

Loads context state.

```tql
context::load "ctx"
```

### [context::remove](operators/context/remove.md)

Deletes a context.

```tql
context::remove "ctx"
```

### [context::reset](operators/context/reset.md)

Resets a context.

```tql
context::reset "ctx"
```

### [context::save](operators/context/save.md)

Saves context state.

```tql
context::save "ctx"
```

### [context::update](operators/context/update.md)

Updates a context with new data.

```tql
context::update "ctx", key=x, value=y
```

## Detection

### [sigma](operators/sigma.md)

Filter the input with Sigma rules and output matching events.

```tql
sigma "/tmp/rules/"
```

### [yara](operators/yara.md)

Executes YARA rules on byte streams.

```tql
yara "/path/to/rules", blockwise=true
```

## Encode & Decode

### [compress](operators/compress.md)

Compresses a stream of bytes.

```tql
compress "zstd"
```

### [compress\_brotli](operators/compress_brotli.md)

Compresses a stream of bytes using Brotli compression.

```tql
compress_brotli, level=10
```

### [compress\_bz2](operators/compress_bz2.md)

Compresses a stream of bytes using bz2 compression.

```tql
compress_bz2, level=9
```

### [compress\_gzip](operators/compress_gzip.md)

Compresses a stream of bytes using gzip compression.

```tql
compress_gzip, level=8
```

### [compress\_lz4](operators/compress_lz4.md)

Compresses a stream of bytes using lz4 compression.

```tql
compress_lz4, level=7
```

### [compress\_zstd](operators/compress_zstd.md)

Compresses a stream of bytes using zstd compression.

```tql
compress_zstd, level=6
```

### [decompress](operators/decompress.md)

Decompresses a stream of bytes.

```tql
decompress "gzip"
```

### [decompress\_brotli](operators/decompress_brotli.md)

Decompresses a stream of bytes in the Brotli format.

```tql
decompress_brotli
```

### [decompress\_bz2](operators/decompress_bz2.md)

Decompresses a stream of bytes in the Bzip2 format.

```tql
decompress_bz2
```

### [decompress\_gzip](operators/decompress_gzip.md)

Decompresses a stream of bytes in the Gzip format.

```tql
decompress_gzip
```

### [decompress\_lz4](operators/decompress_lz4.md)

Decompresses a stream of bytes in the Lz4 format.

```tql
decompress_lz4
```

### [decompress\_zstd](operators/decompress_zstd.md)

Decompresses a stream of bytes in the Zstd format.

```tql
decompress_zstd
```

## Escape Hatches

### [python](operators/python.md)

Executes Python code against each event of the input.

```tql
python "self.x = self.y"
```

### [shell](operators/shell.md)

Executes a system command and hooks its stdin and stdout into the pipeline.

```tql
shell "echo hello"
```

## Filter

### [assert](operators/assert.md)

Drops events and emits a warning if the invariant is violated.

```tql
assert name.starts_with("John")
```

### [assert\_throughput](operators/assert_throughput.md)

Emits a warning if the pipeline does not have the expected throughput

```tql
assert_throughput 1000, within=1s
```

### [deduplicate](operators/deduplicate.md)

Removes duplicate events based on a common key.

```tql
deduplicate src_ip
```

### [head](operators/head.md)

Limits the input to the first `n` events.

```tql
head 20
```

### [sample](operators/sample.md)

Dynamically samples events from a event stream.

```tql
sample 30s, max_samples=2k
```

### [slice](operators/slice.md)

Keeps a range of events within the interval `[begin, end)` stepping by `stride`.

```tql
slice begin=10, end=30
```

### [tail](operators/tail.md)

Limits the input to the last `n` events.

```tql
tail 20
```

### [taste](operators/taste.md)

Limits the input to `n` events per unique schema.

```tql
taste 1
```

### [where](operators/where.md)

Keeps only events for which the given predicate is true.

```tql
where name.starts_with("John")
```

## Flow Control

### [cron](operators/cron.md)

Runs a pipeline periodically according to a cron expression.

```tql
cron "* */10 * * * MON-FRI" { from "https://example.org" }
```

### [delay](operators/delay.md)

Delays events relative to a given start time, with an optional speedup.

```tql
delay ts, speed=2.5
```

### [discard](operators/discard.md)

Discards all incoming events.

```tql
discard
```

### [every](operators/every.md)

Runs a pipeline periodically at a fixed interval.

```tql
every 10s { summarize sum(amount) }
```

### [fork](operators/fork.md)

Executes a subpipeline with a copy of the input.

```tql
fork { to "copy.json" }
```

### [load\_balance](operators/load_balance.md)

Routes the data to one of multiple subpipelines.

```tql
load_balance $over { publish $over }
```

### [parallel](operators/parallel.md)

Runs a subpipeline across multiple parallel workers.

```tql
parallel 4 { parsed = data.parse_json() }
```

### [pass](operators/pass.md)

Does nothing with the input.

```tql
pass
```

### [repeat](operators/repeat.md)

Repeats the input a number of times.

```tql
repeat 100
```

### [throttle](operators/throttle.md)

Limits the bandwidth of a pipeline.

```tql
throttle 100M, within=1min
```

## Host Inspection

### [files](operators/files.md)

Shows file information for a given directory.

```tql
files "/var/log/", recurse=true
```

### [nics](operators/nics.md)

Shows a snapshot of available network interfaces.

```tql
nics
```

### [processes](operators/processes.md)

Shows a snapshot of running processes.

```tql
processes
```

### [sockets](operators/sockets.md)

Shows a snapshot of open sockets.

```tql
sockets
```

## Internals

### [api](operators/api.md)

Use Tenzir's REST API directly from a pipeline.

```tql
api "/pipeline/list"
```

### [batch](operators/batch.md)

The `batch` operator controls the batch size of events.

```tql
batch timeout=1s
```

### [buffer](operators/buffer.md)

An in-memory buffer to improve handling of data spikes in upstream operators.

```tql
buffer 10M, policy="drop"
```

### [cache](operators/cache.md)

An in-memory cache shared between pipelines.

```tql
cache "w01wyhTZm3", ttl=10min
```

### [local](operators/local.md)

Forces a pipeline to run locally.

```tql
local { sort foo }
```

### [measure](operators/measure.md)

Replaces the input with metrics describing the input.

```tql
measure
```

### [remote](operators/remote.md)

Forces a pipeline to run remotely at a node.

```tql
remote { version }
```

### [serve](operators/serve.md)

Make events available under the `/serve` REST API endpoint

```tql
serve "abcde12345"
```

### [strict](operators/strict.md)

Treats all warnings as errors.

```tql
strict { assert false }
```

### [unordered](operators/unordered.md)

Removes ordering assumptions from a pipeline.

```tql
unordered { read_ndjson }
```

## Modify

### [dns\_lookup](operators/dns_lookup.md)

Performs DNS lookups to resolve IP addresses to hostnames or hostnames to IP addresses.

```tql
dns_lookup ip_address, result=dns_info
```

### [drop](operators/drop.md)

Removes fields from the event.

```tql
drop name, metadata.id
```

### [drop\_null\_fields](operators/drop_null_fields.md)

Removes fields containing null values from the event.

```tql
drop_null_fields name, metadata.id
```

### [enumerate](operators/enumerate.md)

Add a field with the number of preceding events.

```tql
enumerate num
```

### [http](operators/http.md)

Sends HTTP/1.1 requests and forwards the response.

```tql
http "example.com"
```

### [move](operators/move.md)

Moves values from one field to another, removing the original field.

```tql
move id=parsed_id, ctx.message=incoming.status
```

### [replace](operators/replace.md)

Replaces all occurrences of a value with another value.

```tql
replace what=42, with=null
```

### [select](operators/select.md)

Selects some values and discards the rest.

```tql
select name, id=metadata.id
```

### [set](operators/set.md)

Assigns a value to a field, creating it if necessary.

```tql
name = "Tenzir"
```

### [timeshift](operators/timeshift.md)

Adjusts timestamps relative to a given start time, with an optional speedup.

```tql
timeshift ts, start=2020-01-01
```

### [unroll](operators/unroll.md)

Returns a new event for each member of a list or a record in an event, duplicating the surrounding event.

```tql
unroll names
```

## OCSF

### [ocsf::apply](operators/ocsf/apply.md)

Casts incoming events to their OCSF type.

```tql
ocsf::apply
```

### [ocsf::cast](operators/ocsf/cast.md)

Casts incoming events to their OCSF type.

```tql
ocsf::cast
```

### [ocsf::derive](operators/ocsf/derive.md)

Automatically assigns enum strings from their integer counterparts and vice versa.

```tql
ocsf::derive
```

### [ocsf::trim](operators/ocsf/trim.md)

Drops fields from OCSF events to reduce their size.

```tql
ocsf::trim
```

## Packages

### [package::add](operators/package/add.md)

Installs a package.

```tql
package::add "suricata-ocsf"
```

### [package::list](operators/package/list.md)

Shows installed packages.

```tql
package::list
```

### [package::remove](operators/package/remove.md)

Uninstalls a package.

```tql
package::remove "suricata-ocsf"
```

## Parsing

### [read\_all](operators/read_all.md)

Parses an incoming bytes stream into a single event.

```tql
read_all binary=true
```

### [read\_bitz](operators/read_bitz.md)

Parses bytes as *BITZ* format.

```tql
read_bitz
```

### [read\_cef](operators/read_cef.md)

Parses an incoming Common Event Format (CEF) stream into events.

```tql
read_cef
```

### [read\_csv](operators/read_csv.md)

Read CSV (Comma-Separated Values) from a byte stream.

```tql
read_csv null_value="-"
```

### [read\_delimited](operators/read_delimited.md)

Parses an incoming bytes stream into events using a string as delimiter.

```tql
read_delimited "|"
```

### [read\_delimited\_regex](operators/read_delimited_regex.md)

Parses an incoming bytes stream into events using a regular expression as delimiter.

```tql
read_delimited_regex r"\s+"
```

### [read\_feather](operators/read_feather.md)

Parses an incoming Feather byte stream into events.

```tql
read_feather
```

### [read\_gelf](operators/read_gelf.md)

Parses an incoming GELF stream into events.

```tql
read_gelf
```

### [read\_grok](operators/read_grok.md)

Parses lines of input with a grok pattern.

```tql
read_grok "%{IP:client} %{WORD:action}"
```

### [read\_json](operators/read_json.md)

Parses an incoming JSON stream into events.

```tql
read_json arrays_of_objects=true
```

### [read\_kv](operators/read_kv.md)

Read Key-Value pairs from a byte stream.

```tql
read_kv r"(\s+)[A-Z_]+:", r":\s*"
```

### [read\_leef](operators/read_leef.md)

Parses an incoming LEEF stream into events.

```tql
read_leef
```

### [read\_lines](operators/read_lines.md)

Parses an incoming bytes stream into events.

```tql
read_lines
```

### [read\_ndjson](operators/read_ndjson.md)

Parses an incoming NDJSON (newline-delimited JSON) stream into events.

```tql
read_ndjson
```

### [read\_parquet](operators/read_parquet.md)

Reads events from a Parquet byte stream.

```tql
read_parquet
```

### [read\_pcap](operators/read_pcap.md)

Reads raw network packets in PCAP file format.

```tql
read_pcap
```

### [read\_ssv](operators/read_ssv.md)

Read SSV (Space-Separated Values) from a byte stream.

```tql
read_ssv header="name count"
```

### [read\_suricata](operators/read_suricata.md)

Parses an incoming Suricata EVE JSON stream into events.

```tql
read_suricata
```

### [read\_syslog](operators/read_syslog.md)

Parses an incoming Syslog stream into events.

```tql
read_syslog
```

### [read\_tsv](operators/read_tsv.md)

Read TSV (Tab-Separated Values) from a byte stream.

```tql
read_tsv auto_expand=true
```

### [read\_xsv](operators/read_xsv.md)

Read XSV from a byte stream.

```tql
read_xsv ";", ":", "N/A"
```

### [read\_yaml](operators/read_yaml.md)

Parses an incoming YAML stream into events.

```tql
read_yaml
```

### [read\_zeek\_json](operators/read_zeek_json.md)

Parse an incoming Zeek JSON stream into events.

```tql
read_zeek_json
```

### [read\_zeek\_tsv](operators/read_zeek_tsv.md)

Parses an incoming `Zeek TSV` stream into events.

```tql
read_zeek_tsv
```

## Pipelines

### [pipeline::activity](operators/pipeline/activity.md)

Summarizes the activity of pipelines.

```tql
pipeline::activity range=1d, interval=1h
```

### [pipeline::detach](operators/pipeline/detach.md)

Starts a pipeline in the node.

```tql
pipeline::detach { … }
```

### [pipeline::list](operators/pipeline/list.md)

Shows managed pipelines.

```tql
pipeline::list
```

### [pipeline::run](operators/pipeline/run.md)

Starts a pipeline in the node and waits for it to complete.

```tql
pipeline::run { … }
```

## Printing

### [write\_bitz](operators/write_bitz.md)

Writes events in *BITZ* format.

```tql
write_bitz
```

### [write\_csv](operators/write_csv.md)

Transforms event stream to CSV (Comma-Separated Values) byte stream.

```tql
write_csv
```

### [write\_feather](operators/write_feather.md)

Transforms the input event stream to Feather byte stream.

```tql
write_feather
```

### [write\_json](operators/write_json.md)

Transforms the input event stream to a JSON byte stream.

```tql
write_json
```

### [write\_kv](operators/write_kv.md)

Writes events in a Key-Value format.

```tql
write_kv
```

### [write\_lines](operators/write_lines.md)

Writes events as key-value pairsthe *values* of an event.

```tql
write_lines
```

### [write\_ndjson](operators/write_ndjson.md)

Transforms the input event stream to a Newline-Delimited JSON byte stream.

```tql
write_ndjson
```

### [write\_parquet](operators/write_parquet.md)

Transforms event stream to a Parquet byte stream.

```tql
write_parquet
```

### [write\_pcap](operators/write_pcap.md)

Transforms event stream to PCAP byte stream.

```tql
write_pcap
```

### [write\_ssv](operators/write_ssv.md)

Transforms event stream to SSV (Space-Separated Values) byte stream.

```tql
write_ssv
```

### [write\_syslog](operators/write_syslog.md)

Writes events as syslog.

```tql
write_syslog
```

### [write\_tql](operators/write_tql.md)

Transforms the input event stream to a TQL notation byte stream.

```tql
write_tql
```

### [write\_tsv](operators/write_tsv.md)

Transforms event stream to TSV (Tab-Separated Values) byte stream.

```tql
write_tsv
```

### [write\_xsv](operators/write_xsv.md)

Transforms event stream to XSV byte stream.

```tql
write_xsv
```

### [write\_yaml](operators/write_yaml.md)

Transforms the input event stream to YAML byte stream.

```tql
write_yaml
```

### [write\_zeek\_tsv](operators/write_zeek_tsv.md)

Transforms event stream into Zeek Tab-Separated Value byte stream.

```tql
write_zeek_tsv
```

## Inputs

### Bytes

### [load\_amqp](operators/load_amqp.md)

Loads a byte stream via AMQP messages.

```tql
load_amqp
```

### [load\_azure\_blob\_storage](operators/load_azure_blob_storage.md)

Loads bytes from Azure Blob Storage.

```tql
load_azure_blob_storage "abfs://container/file"
```

### [load\_file](operators/load_file.md)

Loads the contents of the file at `path` as a byte stream.

```tql
load_file "/tmp/data.json"
```

### [load\_ftp](operators/load_ftp.md)

Loads a byte stream via FTP.

```tql
load_ftp "ftp.example.org"
```

### [load\_gcs](operators/load_gcs.md)

Loads bytes from a Google Cloud Storage object.

```tql
load_gcs "gs://bucket/object.json"
```

### [load\_google\_cloud\_pubsub](operators/load_google_cloud_pubsub.md)

Subscribes to a Google Cloud Pub/Sub subscription and obtains bytes.

```tql
load_google_cloud_pubsub project_id="my-project"
```

### [load\_http](operators/load_http.md)

Loads a byte stream via HTTP.

```tql
load_http "example.org", params={n: 5}
```

### [load\_kafka](operators/load_kafka.md)

Loads a byte stream from an Apache Kafka topic.

```tql
load_kafka topic="example"
```

### [load\_nic](operators/load_nic.md)

Loads bytes from a network interface card (NIC).

```tql
load_nic "eth0"
```

### [load\_s3](operators/load_s3.md)

Loads from an Amazon S3 object.

```tql
load_s3 "s3://my-bucket/obj.csv"
```

### [load\_sqs](operators/load_sqs.md)

Loads bytes from Amazon SQS queues.

```tql
load_sqs "sqs://tenzir"
```

### [load\_stdin](operators/load_stdin.md)

Accepts bytes from standard input.

```tql
load_stdin
```

### [load\_tcp](operators/load_tcp.md)

Loads bytes from a TCP or TLS connection.

```tql
load_tcp "0.0.0.0:8090" { read_json }
```

### [load\_udp](operators/load_udp.md)

Loads bytes from a UDP socket.

```tql
load_udp "0.0.0.0:8090"
```

### [load\_zmq](operators/load_zmq.md)

Receives ZeroMQ messages.

```tql
load_zmq
```

### Events

### [from](operators/from.md)

Obtains events from an URI, inferring the source, compression and format.

```tql
from "data.json"
```

### [from\_azure\_blob\_storage](operators/from_azure_blob_storage.md)

Reads one or multiple files from Azure Blob Storage.

```tql
from_azure_blob_storage "abfs://container/data/**.json"
```

### [from\_file](operators/from_file.md)

Reads one or multiple files from a filesystem.

```tql
from_file "s3://data/**.json"
```

### [from\_fluent\_bit](operators/from_fluent_bit.md)

Receives events via Fluent Bit.

```tql
from_fluent_bit "opentelemetry"
```

### [from\_gcs](operators/from_gcs.md)

Reads one or multiple files from Google Cloud Storage.

```tql
from_gcs "gs://my-bucket/data/**.json"
```

### [from\_google\_cloud\_pubsub](operators/from_google_cloud_pubsub.md)

Subscribes to a Google Cloud Pub/Sub subscription and yields events.

```tql
from_google_cloud_pubsub project_id="my-project", subscription_id="my-sub"
```

### [from\_http](operators/from_http.md)

Sends and receives HTTP/1.1 requests.

```tql
from_http "0.0.0.0:8080"
```

### [from\_kafka](operators/from_kafka.md)

Receives events from an Apache Kafka topic.

```tql
from_kafka "logs"
```

### [from\_opensearch](operators/from_opensearch.md)

Receives events via Opensearch Bulk API.

```tql
from_opensearch
```

### [from\_s3](operators/from_s3.md)

Reads one or multiple files from Amazon S3.

```tql
from_s3 "s3://my-bucket/data/**.json"
```

### [from\_sentinelone\_data\_lake](operators/from_sentinelone_data_lake.md)

Retrieves PowerQuery results from SentinelOne Singularity Data Lake.

```tql
from_sentinelone_data_lake "https://…", …
```

### [from\_udp](operators/from_udp.md)

Receives UDP datagrams and outputs structured events.

```tql
from_udp "0.0.0.0:8090"
```

### [from\_velociraptor](operators/from_velociraptor.md)

Submits VQL to a Velociraptor server and returns the response as events.

```tql
from_velociraptor subscribe="Windows"
```

## Node

### Inspection

### [diagnostics](operators/diagnostics.md)

Retrieves diagnostic events from a Tenzir node.

```tql
diagnostics
```

### [metrics](operators/metrics.md)

Retrieves metrics events from a Tenzir node.

```tql
metrics "cpu"
```

### [openapi](operators/openapi.md)

Shows the node's OpenAPI specification.

```tql
openapi
```

### [plugins](operators/plugins.md)

Shows all available plugins and built-ins.

```tql
plugins
```

### [version](operators/version.md)

Shows the current version.

```tql
version
```

### Storage Engine

### [export](operators/export.md)

Retrieves events from a Tenzir node.

```tql
export
```

### [fields](operators/fields.md)

Retrieves all fields stored at a node.

```tql
fields
```

### [import](operators/import.md)

Imports events into a Tenzir node.

```tql
import
```

### [partitions](operators/partitions.md)

Retrieves metadata about events stored at a node.

```tql
partitions src_ip == 1.2.3.4
```

### [schemas](operators/schemas.md)

Retrieves all schemas for events stored at a node.

```tql
schemas
```

## Outputs

### Bytes

### [save\_amqp](operators/save_amqp.md)

Saves a byte stream via AMQP messages.

```tql
save_amqp
```

### [save\_azure\_blob\_storage](operators/save_azure_blob_storage.md)

Saves bytes to Azure Blob Storage.

```tql
save_azure_blob_storage "abfs://container/file"
```

### [save\_email](operators/save_email.md)

Saves bytes through an SMTP server.

```tql
save_email "user@example.org"
```

### [save\_file](operators/save_file.md)

Writes a byte stream to a file.

```tql
save_file "/tmp/out.json"
```

### [save\_ftp](operators/save_ftp.md)

Saves a byte stream via FTP.

```tql
save_ftp "ftp.example.org"
```

### [save\_gcs](operators/save_gcs.md)

Saves bytes to a Google Cloud Storage object.

```tql
save_gcs "gs://bucket/object.json"
```

### [save\_google\_cloud\_pubsub](operators/save_google_cloud_pubsub.md)

Publishes to a Google Cloud Pub/Sub topic.

```tql
save_google_cloud_pubsub project_id="my-project"
```

### [save\_http](operators/save_http.md)

Sends a byte stream via HTTP.

```tql
save_http "example.org/api"
```

### [save\_kafka](operators/save_kafka.md)

Saves a byte stream to a Apache Kafka topic.

```tql
save_kafka topic="example"
```

### [save\_s3](operators/save_s3.md)

Saves bytes to an Amazon S3 object.

```tql
save_s3 "s3://my-bucket/obj.csv"
```

### [save\_sqs](operators/save_sqs.md)

Saves bytes to Amazon SQS queues.

```tql
save_sqs "sqs://tenzir"
```

### [save\_stdout](operators/save_stdout.md)

Writes a byte stream to standard output.

```tql
save_stdout
```

### [save\_tcp](operators/save_tcp.md)

Saves bytes to a TCP or TLS connection.

```tql
save_tcp "0.0.0.0:8090", tls=true
```

### [save\_udp](operators/save_udp.md)

Saves bytes to a UDP socket.

```tql
save_udp "0.0.0.0:8090"
```

### [save\_zmq](operators/save_zmq.md)

Sends bytes as ZeroMQ messages.

```tql
save_zmq
```

### Events

### [to](operators/to.md)

Saves to an URI, inferring the destination, compression and format.

```tql
to "output.json"
```

### [to\_amazon\_security\_lake](operators/to_amazon_security_lake.md)

Sends OCSF events to Amazon Security Lake.

```tql
to_amazon_security_lake "s3://…"
```

### [to\_azure\_log\_analytics](operators/to_azure_log_analytics.md)

Sends events to the Microsoft Azure Logs Ingestion API.

```tql
to_azure_log_analytics tenant_id="...", workspace_id="..."
```

### [to\_clickhouse](operators/to_clickhouse.md)

Sends events to a ClickHouse table.

```tql
to_clickhouse table="my_table"
```

### [to\_fluent\_bit](operators/to_fluent_bit.md)

Sends events via Fluent Bit.

```tql
to_fluent_bit "elasticsearch" …
```

### [to\_google\_cloud\_logging](operators/to_google_cloud_logging.md)

Sends events to Google Cloud Logging.

```tql
to_google_cloud_logging …
```

### [to\_google\_cloud\_pubsub](operators/to_google_cloud_pubsub.md)

Publishes events to a Google Cloud Pub/Sub topic.

```tql
to_google_cloud_pubsub project_id="my-project", topic_id="alerts", message=text
```

### [to\_google\_secops](operators/to_google_secops.md)

Sends unstructured events to a Google SecOps Chronicle instance.

```tql
to_google_secops …
```

### [to\_hive](operators/to_hive.md)

Writes events to a URI using hive partitioning.

```tql
to_hive "s3://…", partition_by=[x]
```

### [to\_kafka](operators/to_kafka.md)

Sends messages to an Apache Kafka topic.

```tql
to_kafka "topic", message=this.print_json()
```

### [to\_opensearch](operators/to_opensearch.md)

Sends events to an OpenSearch-compatible Bulk API.

```tql
to_opensearch "localhost:9200", …
```

### [to\_sentinelone\_data\_lake](operators/to_sentinelone_data_lake.md)

Sends security events to SentinelOne Singularity Data Lake via REST API.

```tql
to_sentinelone_data_lake "https://…", …
```

### [to\_snowflake](operators/to_snowflake.md)

Sends events to a Snowflake database.

```tql
to_snowflake account_identifier="…
```

### [to\_splunk](operators/to_splunk.md)

Sends events to a Splunk HTTP Event Collector (HEC).

```tql
to_splunk "localhost:8088", …
```