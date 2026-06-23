# Splunk


[Splunk](https://splunk.com) is a SIEM solution for storing and processing logs. Tenzir can send data to Splunk via HEC.

## Examples

### Send data to an existing HEC endpoint

To send data from a pipeline to a Splunk [HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) endpoint, use the [`to_splunk`](http://docs.tenzir.com/reference/operators/to_splunk.md) operator.

For example, deploy the following pipeline to forward [Suricata](suricata.md) alerts to Splunk:

```tql
subscribe "suricata"
where @name == "suricata.alert"
to_splunk "https://1.2.3.4:8088", hec_token="TOKEN", tls_no_verify=true
```

Replace `1.2.3.4` with the IP address of your Splunk host and `TOKEN` with your HEC token.

For more details, see the documentation for the [`to_splunk`](http://docs.tenzir.com/reference/operators/to_splunk.md) operator.

### Spawn a HEC endpoint as pipeline source

To send data to a Tenzir pipeline instead of Splunk, you can open a Splunk [HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) endpoint using the [`from_fluent_bit`](http://docs.tenzir.com/reference/operators/from_fluent_bit.md) source operator.

For example, to onboard all data into a Tenzir node instead of Splunk, point your data source to the IP address of the Tenzir node at port 9880 by deploying this pipeline:

```tql
from_fluent_bit "splunk", options={
  splunk_token: "TOKEN",
}
publish "splunk"
```

Replace `TOKEN` with the Splunk token configured at your data source.

To listen on a different IP address, e.g., 1.2.3.4 add `listen: 1.2.3.4` to the `options` argument.

For more details, read the official [Fluent Bit documentation of the Splunk input](https://docs.fluentbit.io/manual/pipeline/inputs/splunk).