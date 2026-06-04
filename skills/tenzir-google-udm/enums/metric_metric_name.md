# Metric.MetricName

The name of the precomputed analytic.

## Values

- `METRIC_NAME_UNSPECIFIED` (0): Default
- `NETWORK_BYTES_INBOUND` (1): Total received network bytes.
- `NETWORK_BYTES_OUTBOUND` (2): Total network sent bytes.
- `NETWORK_BYTES_TOTAL` (3): Total network sent bytes and received bytes.
- `AUTH_ATTEMPTS_SUCCESS` (4): Successful authentication attempts.
- `AUTH_ATTEMPTS_FAIL` (5): Failed authentication attempts.
- `AUTH_ATTEMPTS_TOTAL` (6): Total authentication attempts.
- `DNS_BYTES_OUTBOUND` (7): Total number of sent bytes for DNS events.
- `NETWORK_FLOWS_INBOUND` (8): Total number of events having non-null received bytes.
- `NETWORK_FLOWS_OUTBOUND` (9): Total number of events having non-null sent bytes.
- `NETWORK_FLOWS_TOTAL` (10): Total events having non-null sent or received bytes.
- `DNS_QUERIES_SUCCESS` (11): DNS query success count - Number of events with response_code = 0.
- `DNS_QUERIES_FAIL` (12): Number of events with responseCode != 0.
- `DNS_QUERIES_TOTAL` (13): Total number of DNS queries made.
- `FILE_EXECUTIONS_SUCCESS` (14): Number of successfule file executions.
- `FILE_EXECUTIONS_FAIL` (15): Number of failed file executions.
- `FILE_EXECUTIONS_TOTAL` (16): Total number file executions.
- `HTTP_QUERIES_SUCCESS` (17): Number of successful HTTP queries.
- `HTTP_QUERIES_FAIL` (18): Number of failed HTTP queries.
- `HTTP_QUERIES_TOTAL` (19): Total number of HTTP queries.
- `WORKSPACE_EMAILS_SENT_TOTAL` (20): Total number of emails sent in Google Workspace.
- `WORKSPACE_TOTAL_DOWNLOAD_ACTIONS` (21): Total number of download actions in Google Workspace.
- `WORKSPACE_TOTAL_CHANGE_ACTIONS` (22): Total number of change actions in Google Workspace.
- `WORKSPACE_AUTH_ATTEMPTS_TOTAL` (23): Total number of authentication attempts in Google Workspace.
- `WORKSPACE_NETWORK_BYTES_OUTBOUND` (24): Number of outbound network bytes (total sent) in Google Workspace.
- `WORKSPACE_NETWORK_BYTES_TOTAL` (25): Total number of network bytes (both sent and received) in Google Workspace.
- `ALERT_EVENT_NAME_COUNT` (26): Track number of alerts fired by EDR/SENTINEL/MICROSOFT_GRAPH.
- `RESOURCE_CREATION_TOTAL` (27): Analytic tracking successful resource creations.
- `RESOURCE_CREATION_SUCCESS` (28): Analytic tracking successful resource creations.
- `RESOURCE_READ_SUCCESS` (29): Analytic tracking successful resource reads.
- `RESOURCE_READ_FAIL` (30): Analytic tracking failed resource reads.
- `RESOURCE_DELETION_SUCCESS` (31): Analytic tracking successful resource deletions.
- `RESOURCE_CREATION_FAIL` (32): Analytic tracking failed resource creations.
- `RESOURCE_DELETION_FAIL` (33): Analytic tracking failed resource deletions.
- `RESOURCE_DELETION_TOTAL` (34): Analytic tracking total resource deletions.
- `RESOURCE_READ_TOTAL` (35): Analytic tracking total resource reads.
- `RESOURCE_WRITTEN_FAIL` (36): Analytic tracking failed resource writes.
- `RESOURCE_WRITTEN_SUCCESS` (37): Analytic tracking successful resource writes.
- `RESOURCE_WRITTEN_TOTAL` (38): Analytic tracking total resource writes.
- `UDM_DATA_PRESENCE_SUMMARY` (39): UDM data summary tracking unique values of dimensions.
