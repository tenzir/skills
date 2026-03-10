# Sentinel & Log Analytics


Send security logs and events from Tenzir to Microsoft’s cloud, where you can analyze them with [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview) (SIEM), create alerts with [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview), or query them with [KQL](https://learn.microsoft.com/en-us/kusto/query/).

All logs in Azure land in a [Log Analytics Workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview). Microsoft Sentinel and Azure Monitor read from this workspace; they don’t store data themselves.

To get data into a workspace, Azure uses two components:

1. A [Data Collection Endpoint (DCE)](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-endpoint-overview) receives your data via HTTPS. This is the URL Tenzir sends events to.
2. A [Data Collection Rule (DCR)](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview) transforms incoming data and routes it to a specific table in your workspace.

This separation lets you send all data to one DCE while routing different streams to different tables, or even different cost tiers, by configuring multiple DCRs.

## Storage Tiers

Tables in a Log Analytics Workspace can use different pricing plans:

| Plan                                                                                                               | Use Case                                         | Trade-offs                             |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | -------------------------------------- |
| [Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs#log-analytics-workspace) | Real-time alerting, dashboards, frequent queries | Higher cost per GB ingested            |
| [Auxiliary](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/create-custom-table#table-plan)             | Compliance, forensics, occasional hunting        | \~90% cheaper, but no scheduled alerts |

The [Sentinel Data Lake](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-data-lake) uses Auxiliary tables to store high-volume logs (like NetFlow or firewall allows) cost-effectively for up to 12 years.

## Prerequisites

Before using this integration, set up the following in the Azure Portal:

1. **Log Analytics Workspace**: [Create a workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace) if you don’t have one.
2. **Entra ID Application**: [Register an app](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) to get your `tenant_id`, `client_id`, and `client_secret` for authentication.
3. **Data Collection Endpoint**: [Create a DCE](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-endpoint-overview#create-a-data-collection-endpoint) in your region to get the ingestion URL.
4. **Custom Table**: [Create a table](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/create-custom-table) in your workspace to receive the data (e.g., `MyLogs_CL`).
5. **Data Collection Rule**: [Create a DCR](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-create-edit) that routes data from your DCE to your table.
6. **Permissions**: Grant your Entra app the **Monitoring Metrics Publisher** role on the DCR.

End-to-End Tutorial

Microsoft’s [Logs Ingestion API tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal) walks through all these steps with screenshots.

## Examples

### Send Suricata Alerts as OCSF to Sentinel

Use [`to_azure_log_analytics`](../../reference/operators/to_azure_log_analytics.md) to forward Suricata alerts as OCSF Detection Findings for correlation in Sentinel:

```tql
from_file "/var/log/suricata/eve.json", follow=true
where event_type == "alert"
suricata::ocsf::map
to_azure_log_analytics \
  tenant_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  dce="https://my-dce.westeurope-1.ingest.monitor.azure.com",
  dcr="dcr-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  stream="OCSF_DetectionFinding_CL"
```

### Use the Sentinel Data Lake for High-Volume Logs

For high-volume logs like NetFlow, DNS queries, or firewall allows that you need for compliance or hunting but not real-time alerting, use the cost-optimized Auxiliary tier:

1. [Create a custom table](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/create-custom-table) (e.g., `NetFlow_CL`).
2. In the Azure Portal, change the table’s plan from **Analytics** to **Auxiliary**.
3. [Create a DCR](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-create-edit) that routes to this table.
4. Ship data with the same operator:

```tql
from_file "netflow.parquet"
to_azure_log_analytics \
  tenant_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  dce="https://my-dce.westeurope-1.ingest.monitor.azure.com",
  dcr="dcr-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  stream="NetFlow_CL"
```

Auxiliary tables store data in Parquet format with retention up to 12 years, making them ideal for historical forensics and ad-hoc KQL queries.