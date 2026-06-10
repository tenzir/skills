<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/586301/service-install-start-stop-data-model -->

# Service Install / Start / Stop Data Model

This includes services installed in Windows and Linux Systems.

Events from Windows System Logs:

- Win-System-Service-Control-Manager-7045 – new service installed
- Win-System-Service-Control-Manager-7036-Start – service started
- Win-System-Service-Control-Manager-7036-Stop – service stopped
- Win-System-Service-Control-Manager-7040 – service start type changed
- Win-System-Service-Control-Manager-7034 – service terminated unexpectedly

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP of the host |
| hostName | string | Host Name | Hostname of the device |
| serviceName | string | Service Name | Name of the service |
| serviceFileName | string | Service File Name | Name of the service file name |
| serviceType | string | Service Type | Values such as KernelDriver, FileSystemDriver |
| serviceStartType | string | Service Start Type | Auto or Manual |
| serviceAccount | string | Service Account | The account that owns this service |
