# Metric.MetricName

The name of the precomputed analytic.

## Values

0. `METRIC_NAME_UNSPECIFIED`: Default
1. `NETWORK_BYTES_INBOUND`: Total received network bytes.
2. `NETWORK_BYTES_OUTBOUND`: Total network sent bytes.
3. `NETWORK_BYTES_TOTAL`: Total network sent bytes and received bytes.
4. `AUTH_ATTEMPTS_SUCCESS`: Successful authentication attempts.
5. `AUTH_ATTEMPTS_FAIL`: Failed authentication attempts.
6. `AUTH_ATTEMPTS_TOTAL`: Total authentication attempts.
7. `DNS_BYTES_OUTBOUND`: Total number of sent bytes for DNS events.
8. `NETWORK_FLOWS_INBOUND`: Total number of events having non-null received bytes.
9. `NETWORK_FLOWS_OUTBOUND`: Total number of events having non-null sent bytes.
10. `NETWORK_FLOWS_TOTAL`: Total events having non-null sent or received bytes.
11. `DNS_QUERIES_SUCCESS`: DNS query success count - Number of events with response_code = 0.
12. `DNS_QUERIES_FAIL`: Number of events with response_code != 0.
13. `DNS_QUERIES_TOTAL`: Total number of DNS queries made.
14. `FILE_EXECUTIONS_SUCCESS`: Number of successfule file executions.
15. `FILE_EXECUTIONS_FAIL`: Number of failed file executions.
16. `FILE_EXECUTIONS_TOTAL`: Total number file executions.
17. `HTTP_QUERIES_SUCCESS`: Number of successful HTTP queries.
18. `HTTP_QUERIES_FAIL`: Number of failed HTTP queries.
19. `HTTP_QUERIES_TOTAL`: Total number of HTTP queries.
20. `WORKSPACE_EMAILS_SENT_TOTAL`: Total number of emails sent in Google Workspace.
21. `WORKSPACE_TOTAL_DOWNLOAD_ACTIONS`: Total number of download actions in Google Workspace.
22. `WORKSPACE_TOTAL_CHANGE_ACTIONS`: Total number of change actions in Google Workspace.
23. `WORKSPACE_AUTH_ATTEMPTS_TOTAL`: Total number of authentication attempts in Google Workspace.
24. `WORKSPACE_NETWORK_BYTES_OUTBOUND`: Number of outbound network bytes (total sent) in Google Workspace.
25. `WORKSPACE_NETWORK_BYTES_TOTAL`: Total number of network bytes (both sent and received) in Google Workspace.
26. `ALERT_EVENT_NAME_COUNT`: Track number of alerts fired by EDR/SENTINEL/MICROSOFT_GRAPH.
27. `RESOURCE_CREATION_TOTAL`: Analytic tracking successful resource creations.
28. `RESOURCE_CREATION_SUCCESS`: Analytic tracking successful resource creations.
29. `RESOURCE_READ_SUCCESS`: Analytic tracking successful resource reads.
30. `RESOURCE_READ_FAIL`: Analytic tracking failed resource reads.
31. `RESOURCE_DELETION_SUCCESS`: Analytic tracking successful resource deletions.
32. `RESOURCE_CREATION_FAIL`: Analytic tracking failed resource creations.
33. `RESOURCE_DELETION_FAIL`: Analytic tracking failed resource deletions.
34. `RESOURCE_DELETION_TOTAL`: Analytic tracking total resource deletions.
35. `RESOURCE_READ_TOTAL`: Analytic tracking total resource reads.
36. `RESOURCE_WRITTEN_FAIL`: Analytic tracking failed resource writes.
37. `RESOURCE_WRITTEN_SUCCESS`: Analytic tracking successful resource writes.
38. `RESOURCE_WRITTEN_TOTAL`: Analytic tracking total resource writes.
39. `UDM_DATA_PRESENCE_SUMMARY`: UDM data summary tracking unique values of dimensions.
