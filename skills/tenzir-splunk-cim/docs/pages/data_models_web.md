---
title: Web
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/web
last_modified: 2026-04-01T20:48:25.305Z
version: 8.5
---

# Web

The fields in the Web data model describe web server and/or proxy server data in a security or operational context.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with the Web event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| Web | web |

| \|____ Proxy | proxy |

| \|____ Storage | storage |

## Fields for Web event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |

-
- | Web | ` action ` | string | The action taken by the server or proxy. | recommended required for pytest-splunk-addon |
| Web | ` app ` | string | The application detected or hosted by the server/site such as WordPress, Splunk, or Facebook. |  |

-
- | Web | ` bytes ` | number | The total number of bytes transferred ( ` bytes_in ` + ` bytes_out ` ). | recommended required for pytest-splunk-addon |

-
- | Web | ` bytes_in ` | number | The number of inbound bytes transferred. | recommended required for pytest-splunk-addon |

-
- | Web | ` bytes_out ` | number | The number of outbound bytes transferred. | recommended required for pytest-splunk-addon |

| Web | ` cached ` | boolean | Indicates whether the event data is cached or not. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |
| Web | ` category ` | string | The category of traffic, such as may be provided by a proxy server. | required for pytest-splunk-addon |
| Web | ` cim_entity_zone ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Web | ` cookie ` | string | The cookie file recorded in the event. |  |

-
- | Web | ` dest ` | string | The destination of the network traffic (the remote host). You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended required for pytest-splunk-addon |
| Web | ` dest_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| Web | ` dest_category ` | string |  |
| Web | ` dest_ip ` | string | The IP address of the destination. |
| Web | ` dest_priority ` | string |  |  |
| Web | ` dest_port ` | number | The destination port of the web traffic. | required for pytest-splunk-addon |
| Web | ` duration ` | number | The time taken by the proxy event, in milliseconds. |  |
| Web | ` http_content_type ` | string | The content-type of the requested HTTP resource. | recommended |

-
-

| Web | ` http_method ` | string | The HTTP method used in the request. | recommended prescribed values: ` GET ` , ` PUT ` , ` POST ` , ` DELETE ` , ` HEAD ` , ` OPTIONS ` , ` CONNECT ` , ` TRACE ` |
| Web | ` http_referrer ` | string | The HTTP referrer used in the request. The W3C specification and many implementations misspell this as ` http_referer ` . Use a ` FIELDALIAS ` to handle both key names. | recommended |
| Web | ` http_referrer_domain ` | string | The domain name contained within the HTTP referrer used in the request. | recommended |

-
- | Web | ` http_user_agent ` | string | The user agent used in the request. | recommended required for pytest-splunk-addon |
| Web | ` http_user_agent_length ` | number | The length of the user agent used in the request. | required for pytest-splunk-addon |
| Web | ` response_time ` | number | The amount of time it took to receive a response, if applicable, in milliseconds. |  |
| Web | ` site ` | string | The virtual site which services the request, if applicable. |  |

-
- | Web | ` src ` | string | The source of the network traffic (the client requesting the connection). | recommended required for pytest-splunk-addon |
| Web | ` src_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| Web | ` src_category ` | string |
| Web | src_ip | string | The IP address of the source. |
| Web | ` src_priority ` | string |  |  |

-
-
-

| Web | ` status ` | string | The HTTP response code indicating the status of the proxy request. | recommended required for pytest-splunk-addon prescribed values: ` 100 ` , ` 101 ` , ` 102 ` , ` 200 ` , ` 201 ` , ` 202 ` , ` 203 ` , ` 204 ` , ` 205 ` , ` 206 ` , ` 207 ` , ` 208 ` , ` 226 ` , ` 300 ` , ` 301 ` , ` 302 ` , ` 303 ` , ` 304 ` , ` 305 ` , ` 306 ` , ` 307 ` , ` 308 ` , ` 400 ` , ` 401 ` , ` 402 ` , ` 403 ` , ` 404 ` , ` 405 ` , ` 406 ` , ` 407 ` , ` 408 ` , ` 409 ` , ` 410 ` , ` 411 ` , ` 412 ` , ` 413 ` , ` 414 ` , ` 415 ` , ` 416 ` , ` 417 ` , ` 422 ` , ` 423 ` , ` 424 ` , ` 426 ` , ` 428 ` , ` 429 ` , ` 431 ` , ` 500 ` , ` 501 ` , ` 502 ` , ` 503 ` , ` 504 ` , ` 505 ` , ` 506 ` , ` 507 ` , ` 508 ` , ` 510 ` , ` 511 ` |
| Web | ` storage_name ` | string | The name of the bucket or storage account. Used for Cloud storage tracking. |  |
| Web | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |

```text

```

```text

```

| Web | ` uri_path ` | string | The path of the resource served by the webserver or proxy. | other: CODE Copy /CertEnroll/Blue%20Coat%20Systems %20Internal.crl ` /CertEnroll/Blue%20Coat%20Systems %20Internal.crl ` CODE Copy /CertEnroll/PWSVL-NETSVC-01.internal.cacheflow.com_Blue%20Coat%20Systems %20Internal.crt/MFAwTqADAgEAMEcwRTBDMAkGBSsOAw IaBQAEFOoaVMtyzC9gObESY9g1eXf1VM8VBBTl1mBq2WFf 4cYqBI6c08kr4S302gIKUCIZdgAAAAAnQA%3D%3D /bag /en-US/account/login /en-US/account/login /en-US/app/simple_xml_examples/custom_viz_ forcedirected /en-US/config /en-US/splunkd/__raw/services/apps/local/simple _xml_examples /en-US/splunkd/__raw/services/configs/conf-web/settings /en-US/splunkd/__raw/services/data/user-prefs/general /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/saved/searches/_new /en-US/splunkd/__raw/services/server/info/server-info /en-US/splunkd/__raw/servicesNS/-/-/search/jobs ` /CertEnroll/PWSVL-NETSVC-01.internal.cacheflow.com_Blue%20Coat%20Systems %20Internal.crt/MFAwTqADAgEAMEcwRTBDMAkGBSsOAw IaBQAEFOoaVMtyzC9gObESY9g1eXf1VM8VBBTl1mBq2WFf 4cYqBI6c08kr4S302gIKUCIZdgAAAAAnQA%3D%3D /bag /en-US/account/login /en-US/account/login /en-US/app/simple_xml_examples/custom_viz_ forcedirected /en-US/config /en-US/splunkd/__raw/services/apps/local/simple _xml_examples /en-US/splunkd/__raw/services/configs/conf-web/settings /en-US/splunkd/__raw/services/data/user-prefs/general /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/messages /en-US/splunkd/__raw/services/saved/searches/_new /en-US/splunkd/__raw/services/server/info/server-info /en-US/splunkd/__raw/servicesNS/-/-/search/jobs ` |

```text

```

```text

```

| Web | ` uri_query ` | string | The path of the resource requested by the client. | other: CODE Copy ?return_to=%2Fen-US%2Fapp%2Fsimple_xml_examples%2Fcustom_viz_ forcedirected%3Fearliest%3D0%26latest%3D ` ?return_to=%2Fen-US%2Fapp%2Fsimple_xml_examples%2Fcustom_viz_ forcedirected%3Fearliest%3D0%26latest%3D ` CODE Copy ?earliest=0&latest= ?autoload=1 ?output_mode=json&_=1424960631223 ?output_mode=json&_=1424960631232 ?output_mode=json&_=1424960631225 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&_=1424960631236 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424933765618 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424933765619 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424960631233 ?output_mode=json&_=1424960631228 ?output_mode=json&_=1424960631224 ?id=admin__admin_c2ltcGxlX3htbF9leGFtcGxlcw__ search1_1424960633.67&count=1& output_mode=json&_=1424960631243 ` ?earliest=0&latest= ?autoload=1 ?output_mode=json&_=1424960631223 ?output_mode=json&_=1424960631232 ?output_mode=json&_=1424960631225 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&_=1424960631236 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424933765618 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424933765619 ?output_mode=json&sort_key=timeCreated_ epochSecs&sort_dir=desc&count= 1000&_=1424960631233 ?output_mode=json&_=1424960631228 ?output_mode=json&_=1424960631224 ?id=admin__admin_c2ltcGxlX3htbF9leGFtcGxlcw__ search1_1424960633.67&count=1& output_mode=json&_=1424960631243 ` |

-
-
-

| Web | ` url ` | string | The URL of the requested HTTP resource. | recommended required for pytest-splunk-addon other: ` http://0.channel36.facebook.com/x/1746719903/ false/p_1243021868=11 http://0.channel36.facebook.com/x/3833188787/ false/p_1243021868=11 http://0.channel37.facebook.com/x/3598566724/ false/p_576766886=1 http://01275269302.channel11.facebook.com/x/ 832619022/false/p_792194432=2 http://03978257738.channel38.facebook.com/x/ 3905575759/false/p_1576492095=0 http://1.gravatar.com/avatar/72f230f80 db7d667952d596cafbaf928?s=16&d=identicon&r=PG http://10.0.26.105:8080/secars/secars.dll?h=3397A86 EC64FCE11F15337B7BE75CF1EF7443FFA8 E58454580830E8D41D695469C01E8D128BF891F4D 0438A70BE3E0A0D7BABD610DE3A588DF1804F823 CD509F0A2177AD97F7B9F3D09BEDA005C241B873 349D525C0264A9F1655FD408F70DD465574D5E8E BE0DC29030A6365C1F025CB2954E2C38E0404CE4 D24970B2613EB394E2611FD7EC8EB2AD84318421CD 40DF01E6DF002AFF775653030012EF432D59072C0 5F1A939A6C1467CC3A129801587BE559CB16653513 3EAA6C78D3C4BDEC6D795C2934A176DACBB3839 8ED490322037DDB59101EE725138FF8534D89657F4 43F084ACE66DF159581AEF495F317536C34477D005 49B514A81CC689BFB7ACA7C10399C2C7BD76319876 C9890FB4172BBC7CBDF50F7CE0B164BE7F8D8228E9 555E39EE9D0F50B6CE3F610533544A959087F03FCD 16D8FDF0F9C5EB692E3C7EE61B75272961CC29A05D 5F3A1629BBF7C70044BBC65D30812B8EB3E0C7510C DA0F636808B32925481602F702714C60ADC7040F58 CACA4BDD61D776C796D5344495B93AC08F16FC851E 3FB157CEBB563CC1 http://10.10.8.60/ http://10.120.109.82/en-US/static/@255606:0/app/simple_ xml_examples/components/forcedirected/ forcedirected.js?_=1424960631242 http://10.120.251.250/en-US/account/login ` |
| Web | ` url_domain ` | string | The domain name contained within the URL of the requested HTTP resource. | recommended |
| Web | ` url_length ` | number | The length of the URL. |  |
| Web | ` user ` | string | The user that requested the HTTP resource. | recommended |
| Web | ` user_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| Web | ` user_category ` | string |
| Web | ` user_priority ` | string |
| Web | ` vendor_product ` | string | The vendor and product of the proxy server, such as ` Squid Proxy Server ` . This field can be automatically populated by ` vendor ` and ` product ` fields in your data. | recommended |

| Storage | ` error_code ` | string | The error code that occurred while accessing the storage account. | other: ` NoSuchBucket ` |

| Storage | ` operation ` | string | The operation performed on the storage account. | other: ` REST.PUT.OBJECT ` |
| Storage | storage_dataset | string | New child dataset of Web for cloud storage events |  |

| Storage | ` storage_name ` | string | The name of the bucket or storage account. | other: ` es-csm-files ` |
