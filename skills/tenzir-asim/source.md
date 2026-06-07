# Source

This skill is generated from Microsoft Defender Docs Markdown. The generated YAML files are the primary agent-facing reference; use this page only when provenance or raw source lookup is needed.

- **Requested docs ref**: `public`
- **Resolved Defender Docs commit**: `15d29199b26d9f13e1580144d447c8482ad485c8`
- **Schema catalog source path**: [`sentinel/normalization-about-schemas.md`](docs/sentinel/normalization-about-schemas.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-about-schemas.md))
- **Event schemas**: `12`
- **Entity schemas**: `1`
- **Generated schemas**: `13`
- **Generated distinct fields**: `539`
- **Generated schema field records**: `1426`
- **Alias field records**: `73`

Raw Microsoft Defender Docs Markdown is copied under `docs/sentinel/` for audit and parser debugging.

## Schema source paths

- [AssetEntity](schemas/asset_entity.yaml): [`sentinel/normalization-schema-asset.md`](docs/sentinel/normalization-schema-asset.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-asset.md))
- [AgentEvent](schemas/agent_event.yaml): [`sentinel/normalization-schema-agent.md`](docs/sentinel/normalization-schema-agent.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-agent.md))
- [AlertEvent](schemas/alert_event.yaml): [`sentinel/normalization-schema-alert.md`](docs/sentinel/normalization-schema-alert.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-alert.md))
- [AuditEvent](schemas/audit_event.yaml): [`sentinel/normalization-schema-audit.md`](docs/sentinel/normalization-schema-audit.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-audit.md))
- [Authentication](schemas/authentication.yaml): [`sentinel/normalization-schema-authentication.md`](docs/sentinel/normalization-schema-authentication.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-authentication.md))
- [DhcpEvent](schemas/dhcp_event.yaml): [`sentinel/normalization-schema-dhcp.md`](docs/sentinel/normalization-schema-dhcp.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-dhcp.md))
- [Dns](schemas/dns.yaml): [`sentinel/normalization-schema-dns.md`](docs/sentinel/normalization-schema-dns.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-dns.md))
- [FileEvent](schemas/file_event.yaml): [`sentinel/normalization-schema-file-event.md`](docs/sentinel/normalization-schema-file-event.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-file-event.md))
- [NetworkSession](schemas/network_session.yaml): [`sentinel/normalization-schema-network.md`](docs/sentinel/normalization-schema-network.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-network.md))
- [ProcessEvent](schemas/process_event.yaml): [`sentinel/normalization-schema-process-event.md`](docs/sentinel/normalization-schema-process-event.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-process-event.md))
- [RegistryEvent](schemas/registry_event.yaml): [`sentinel/normalization-schema-registry-event.md`](docs/sentinel/normalization-schema-registry-event.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-registry-event.md))
- [UserManagement](schemas/user_management.yaml): [`sentinel/normalization-schema-user-management.md`](docs/sentinel/normalization-schema-user-management.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-user-management.md))
- [WebSession](schemas/web_session.yaml): [`sentinel/normalization-schema-web.md`](docs/sentinel/normalization-schema-web.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-schema-web.md))

## Supporting source paths

- [`sentinel/normalization-about-schemas.md`](docs/sentinel/normalization-about-schemas.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-about-schemas.md))
- [`sentinel/normalization-common-fields.md`](docs/sentinel/normalization-common-fields.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-common-fields.md))
- [`sentinel/normalization-content.md`](docs/sentinel/normalization-content.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-content.md))
- [`sentinel/normalization-entity-application.md`](docs/sentinel/normalization-entity-application.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-entity-application.md))
- [`sentinel/normalization-entity-device.md`](docs/sentinel/normalization-entity-device.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-entity-device.md))
- [`sentinel/normalization-entity-user.md`](docs/sentinel/normalization-entity-user.md) ([upstream](https://github.com/MicrosoftDocs/defender-docs/blob/15d29199b26d9f13e1580144d447c8482ad485c8/sentinel/normalization-entity-user.md))
