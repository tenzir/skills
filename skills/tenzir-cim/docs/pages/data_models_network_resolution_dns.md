---
title: Network Resolution (DNS)
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/network-resolution-dns
last_modified: 2026-04-01T20:48:25.388Z
version: 8.5
---

# Network Resolution (DNS)

The fields and tags in the Network Resolution (DNS) data model describe DNS traffic, both server:server and client:server.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with the DNS event dataset

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see the topic How to use these reference tables in this manual.

| Dataset name | Tag name |
| --- | --- |
| DNS | network |
| resolution |
| dns |

## Fields for the Network Resolution event dataset

The following table lists the extracted and calculated fields for the event dataset in the model. The table does not include any inherited fields. For more information, see the topic How to use these reference tables in this manual.

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| DNS | ` additional_answer_count ` | number | Number of entries in the "additional" section of the DNS message. | required for pytest-splunk-addon |

-
- | DNS | ` answer ` | string | Resolved address for the query. | recommended required for pytest-splunk-addon |
| DNS | ` answer_count ` | number | Number of entries in the answer section of the DNS message. | required for pytest-splunk-addon |
| DNS | ` authority_answer_count ` | number | Number of entries in the 'authority' section of the DNS message. | required for pytest-splunk-addon |

-
- | DNS | ` dest ` | string | The destination of the network resolution event. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended required for pytest-splunk-addon |

| DNS | ` dest_bunit ` | string | The business unit of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DNS | ` dest_category ` | string | The category of the network resolution target, such as ` email_server ` or ` SOX-compliant ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DNS | ` dest_port ` | number | The destination port number. | recommended |

| DNS | ` dest_priority ` | string | The priority of the destination, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DNS | ` duration ` | number | The time taken by the network resolution event, in seconds. |  |

-
-
-

| DNS | ` message_type ` | string | Type of DNS message. | recommended required for pytest-splunk-addon prescribed values: ` Query ` , ` Response ` |
| DNS | ` name ` | string | The name of the DNS event. |  |

-
- | DNS | ` query ` | string | The domain which needs to be resolved. Applies to messages of type "Query". | recommended required for pytest-splunk-addon |
| DNS | ` query_count ` | number | Number of entries that appear in the "Questions" section of the DNS query. | required for pytest-splunk-addon |

-

| DNS | ` query_type ` | string | The field may contain DNS OpCodes or Resource Record Type codes. For details, see the Domain Name System Parameters on the Internet Assigned Numbers Authority (IANA) web site. If a value is not set, the ` DNS.record_type ` fieldis referenced. | required for pytest-splunk-addon Example values: ` Query, IQuery, Status, Notify, Update, A, MX, NS, PTR ` |

-

| DNS | ` record_type ` | string | The DNS resource record type. For details, see the List of DNS record types on the IANA web site. | required for pytest-splunk-addon Example values: ` A, DNAME, MX, NS, PTR ` |

-
-
-

-

| DNS | ` reply_code ` | string | The return code for the response. For details, see the Domain Name System Parameters on the Internet Assigned Numbers Authority (IANA) web site. | recommended required for pytest-splunk-addon prescribed values: ` No Error ` , ` Format Error ` , ` Server Failure ` , ` Non-Existent Domain ` other: ` NoError, FormErr, ServFail, NXDomain, NotImp, Refused, YXDomain, YXRRSet, NotAuth, NotZone, BADVERS, BADSIG, BADKEY, BADTIME, BADMODE, BADNAME, BADALG ` |

-
-
-

| DNS | ` reply_code_id ` | number | The numerical id of a return code. For details, see the Domain Name System Parameters on the Internet Assigned Numbers Authority (IANA) web site. | recommended required for pytest-splunk-addon prescribed values: ` 0 ` , ` NoError ` , ` 1 ` , ` FormErr ` , ` 2 ` , ` ServFail ` , ` 3 ` , ` NXDomain ` , |
| DNS | ` response_time ` | number | The amount of time it took to receive a response in the network resolution event, in seconds if consistent across all data sources, if applicable. | required for pytest-splunk-addon |

-
- | DNS | ` src ` | string | The source of the network resolution event. You can alias this from more specific fields, such as ` src_host ` , ` src_ip ` , or ` src_name ` . | recommended required for pytest-splunk-addon |

| DNS | ` src_bunit ` | string | The business unit of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DNS | ` src_category ` | string | The category of the source, such as ` email_server ` or ` SOX-compliant ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DNS | ` src_port ` | number | The port number of the source. | recommended |

| DNS | ` src_priority ` | string | The priority of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DNS | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |
| DNS | ` transaction_id ` | number | The unique numerical transaction id of the network resolution event. | required for pytest-splunk-addon |
| DNS | ` transport ` | string | The transport protocol used by the network resolution event. | required for pytest-splunk-addon |
| DNS | ` ttl ` | number | The time-to-live of the network resolution event. | recommended |
| DNS | ` vendor_product ` | string | The vendor product name of the DNS server. The Splunk platform can derive this field from the fields ` vendor ` and ` product ` in the raw data, if they exist. | recommended |
