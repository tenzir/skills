# SecOps


[Google Security Operations (SecOps)](https://cloud.google.com/security/products/security-operations) is Google’s security operations platform. Tenzir can send events to Google SecOps using the [unstructured logs ingestion API](https://cloud.google.com/chronicle/docs/reference/ingestion-api#unstructuredlogentries).

## UDM mapping

Google SecOps stores normalized security data in the Unified Data Model (UDM). Use [Map to UDM](../../guides/normalization/map-to-udm.md) to shape parsed events into API-facing UDM records.

For agent-assisted work, follow [Use agent skills](../../guides/ai-workbench/use-agent-skills.md#use-the-google-udm-skill) to use the `tenzir-google-udm` skill. The skill helps map logs into UDM API ingestion payloads with names such as `metadata.eventType`, and write YARA-L or rule field paths with names such as `metadata.event_type`.

Tenzir’s [`to_google_secops`](/reference/operators/to_google_secops.md) operator currently sends unstructured logs. Structured UDM ingestion support is coming soon.

## Examples

### Send an event to Google SecOps

```tql
from {log: "31-Mar-2025 01:35:02.187 client 0.0.0.0#4238: query: tenzir.com IN A + (255.255.255.255)"}
to_google_secops \
  customer_id="00000000-0000-0000-00000000000000000",
  private_key=secret("my_secops_key"),
  client_email="somebody@example.com",
  log_text=log,
  log_type="BIND_DNS",
  region="europe"
```