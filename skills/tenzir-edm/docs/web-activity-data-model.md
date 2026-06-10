<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/525169/web-activity-data-model -->

# Web Activity Data Model

This data model can be used to describe web traffic – both from the point of view of a Web Server or a network gateway or a firewall.

Examples from Apache:

- Apache-Web-Request-Success
- Apache-Web-Bad-Request
- Apache-Web-Client-Access-Denied

Examples from nginx:

- Nginx-Web-Request-Success
- Nginx-Web-Forbidden-Access-Denied
- Nginx-Web-Client-Access-Denied
- Nginx-Web-Bad-Request

Examples from IIS Web Server:

- IIS-Web-Request-Success
- IIS-Web-Bad-Request
- IIS-Web-Client-Access-Denied
- IIS-Web-Client-Error
- IIS-Web-Forbidden-Access-Denied
- IIS-Web-Length-Reqd-Access-Denied
- IIS-Web-Request-Redirect

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of a device as identified in the event. |
| srcGeoCountry | string | Source Country | The Country in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoState | string | Source State | The State in the country in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoCity | string | Source City | The City in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoLatitude | string | Source Latitude | The latitude on which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoLongitude | string | Source Longitude | The longitude on which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destIpAddr | IP | Destination IP | Destination IP of a device as identified in the event. |
| destName | string | Destination Host Name | Destination device's hostname as identified in the log, can also be enriched using reverse lookup of the destination IP address. |
| sentBytes64 | uint64 | Sent Bytes64 | Number of bytes sent by a host. This has 64bit resolution. |
| recvBytes64 | uint64 | Received Bytes64 | Number of bytes received by the web server. This has 64bit resolution. |
| totBytes64 | uint64 | Total Bytes64 | Total number of sent and received bytes in the connection. This has 64bit resolution. |
| durationMSec | uint32 | Duration | Duration of a connection (in msec) |
| httpCookie | string | Http Cookie | Http Cookie |
| httpVersion | string | HTTP Proto Version | HTTP Proto Version |
| httpUserAgent | string | HTTP User Agent | HTTP User Agent |
| httpReferrer | string | HTTP Referrer | HTTP Referrer |
| httpMethod | string | HTTP Method | HTTP Method |
| httpStatusCode | string | HTTP Status | HTTP Status |
| httpSubStatusCode | string | HTTP Sub-status | HTTP Sub-status |
| httpWin32Status | string | HTTP Win32 Status | HTTP Win32 Status |
| httpContentLen | uint16 | HTTP Content Length | HTTP Content Length |
| httpContentType | string | HTTP Content Type | HTTP Content Type |
| user | string | User | User making the request |
| uriStem | string | URI Stem | URI Stem |
| uriQuery | string | URI Query | URI Query |
| downloadURL | string | Download URL |  |
| infoURL | string | Informational URL |  |
