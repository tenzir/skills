---
title: Certificates
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/certificates
last_modified: 2026-04-01T20:48:25.949Z
version: 8.5
---

# Certificates

The fields and tags in the Certificates data model describe key and certificate management events from a variety of secure servers and IAM systems.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Certificates event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Certificates | certificate |

| \|____ SSL | ssl OR tls |

## Fields for Certificates event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| All_Certificates | ` dest ` | string | The target in the certificate management event. |  |

| All_Certificates | ` dest_bunit ` | string | The business unit of the target. This field is automatically provided by Asset and Identity correlation features of applications like Splunk Enterprise Security. |  |

| All_Certificates | ` dest_category ` | string | The category of the target. This field is automatically provided by Asset and Identity correlation features of applications like the Splunk Enterprise Security. | other: ` email_server ` , ` SOX-compliant ` |
| All_Certificates | ` dest_port ` | number | The port number of the target. |  |
| All_Certificates | ` dest_priority ` | string | The priority of the target. Field is automatically provided by the Asset and Identity correlation features of applications such as Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Certificates | ` duration ` | number | The amount of time for the completion of the certificate management event, in seconds. |  |
| All_Certificates | ` response_time ` | number | The amount of time it took to receive a response in the certificate management event, if applicable. |  |

| All_Certificates | ` src ` | string | The source involved in the certificate management event. You can alias this from more specific fields, such as ` src_host ` , ` src_ip ` , or ` src_nt_host ` . Note: Do not confuse ` src ` with the event ` source ` or ` sourcetype ` fields. |  |

| All_Certificates | ` src_bunit ` | string | The business unit of the certificate management source. This field is automatically provided by Asset and Identity correlation features of applications like Splunk Enterprise Security. |  |

| All_Certificates | ` src_category ` | string | The category of the certificate management source. This field is automatically provided by Asset and Identity correlation features of applications like the Splunk Enterprise Security. | other: ` email_server ` , ` SOX-compliant ` |
| All_Certificates | ` src_port ` | number | The port number of the source. |  |
| All_Certificates | ` src_priority ` | string | The priority of the certificate management source. |  |
| All_Certificates | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Add-on builders do not need to populate it. |  |
| All_Certificates | ` transport ` | string | The transport protocol of the Network Traffic involved with this certificate. |  |
| SSL | ` ssl_end_time ` | time | The expiry time of the certificate. Needs to be converted to UNIX time for calculations in dashboards. | recommended |
| SSL | ` ssl_engine ` | string | The name of the signature engine that created the certificate. |  |
| SSL | ` ssl_hash ` | string | The hash of the certificate. | recommended |

| SSL | ` ssl_is_valid ` | boolean | Indicator of whether the ssl certificate is valid or not. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |

-
- | SSL | ` ssl_issuer ` | string | The certificate issuer's RFC2253 Distinguished Name. | recommended required for pytest-splunk-addon |

-
- | SSL | ` ssl_issuer_common_name ` | string | The certificate issuer's common name. | recommended required for pytest-splunk-addon |
| SSL | ` ssl_issuer_email ` | string | The certificate issuer's email address. |  |
| SSL | ` ssl_issuer_email_domain ` | string | The domain name contained within the certificate issuer's email address. | recommended |
| SSL | ` ssl_issuer_locality ` | string | The certificate issuer's locality. |  |
| SSL | ` ssl_issuer_organization ` | string | The certificate issuer's organization. |  |
| SSL | ` ssl_issuer_state ` | string | The certificate issuer's state of residence. |  |
| SSL | ` ssl_issuer_street ` | string | The certificate issuer's street address. |  |
| SSL | ` ssl_issuer_unit ` | string | The certificate issuer's organizational unit. |  |
| SSL | ` ssl_name ` | string | The name of the ssl certificate. |  |
| SSL | ` ssl_policies ` | string | The Object Identification Numbers's of the certificate's policies in a comma separated string. |  |
| SSL | ` ssl_publickey ` | string | The certificate's public key. |  |
| SSL | ` ssl_publickey_algorithm ` | string | The algorithm used to create the public key. |  |

-
- | SSL | ` ssl_serial ` | string | The certificate's serial number. | recommended required for pytest-splunk-addon |
| SSL | ` ssl_session_id ` | string | The session identifier for this certificate. |  |
| SSL | ` ssl_signature_algorithm ` | string | The algorithm used by the Certificate Authority to sign the certificate. |  |
| SSL | ` ssl_start_time ` | time | This is the start date and time for this certificate's validity. Needs to be converted to UNIX time for calculations in dashboards. | recommended |

-
- | SSL | ` ssl_subject ` | string | The certificate owner's RFC2253 Distinguished Name. | recommended required for pytest-splunk-addon |

-
- | SSL | ` ssl_subject_common_name ` | string | This certificate owner's common name. | recommended required for pytest-splunk-addon |
| SSL | ` ssl_subject_email ` | string | The certificate owner's e-mail address. |  |
| SSL | ` ssl_subject_email_domain ` | string | The domain name contained within the certificate subject's email address. | recommended |
| SSL | ` ssl_subject_locality ` | string | The certificate owner's locality. |  |
| SSL | ` ssl_subject_organization ` | string | The certificate owner's organization. | required for pytest-splunk-addon |
| SSL | ` ssl_subject_state ` | string | The certificate owner's state of residence. |  |
| SSL | ` ssl_subject_street ` | string | The certificate owner's street address. |  |
| SSL | ` ssl_subject_unit ` | string | The certificate owner's organizational unit. |  |
| SSL | ` ssl_validity_window ` | number | The length of time (in seconds) for which this certificate is valid. | required for pytest-splunk-addon |
| SSL | ` ssl_version ` | string | The ssl version of this certificate. |  |

## Examples for Certificates event datasets

The following is a sample of a certificate event from zeek/corelight:

```text
{
  "ts": 1586817752.481357,
  "id": "FBKnzp4LVE2thdglSe",
  "certificate.version": 3,
  "certificate.serial": "0B1641AEAE93F5DB71B36C977B7FCF63",
  "certificate.subject": "CN=Outlook.live.com,O=Microsoft Corporation,L=Redmond,ST=Washington,C=US",
  "certificate.issuer": "CN=DigiCert Cloud Services CA-1,O=DigiCert Inc,C=US",
  "certificate.not_valid_before": 1585008000.0,
  "certificate.not_valid_after": 1648123200.0,
  "certificate.key_alg": "rsaEncryption",
  "certificate.sig_alg": "sha256WithRSAEncryption",
  "certificate.key_type": "rsa",
  "certificate.key_length": 2048,
  "certificate.exponent": "65537",
  "san.dns": ["Outlook.live.com", "outlook-sdf.live.com", "attachment.outlook.office.net", "attachment.outlook.officeppe.net", "hotmail.com", "*.calendar.live.com", "*.hotmail.com", "*.live.com", "*.mail.live.com", "afd-a-acdc-direct.office.com", "live.com", "*.nrb.footprintdns.com", "*.fp.measure.office.com", "premium.outlook.com"],
  "basic_constraints.ca": false
}
```

The following are CIM fields extracted from this sample:

```text
"ssl_start_time" = "1585008000"
"ssl_end_time" = "1648123200"
"ssl_validity_window" = "63115200"
"ssl_issuer" = "CN=DigiCert Cloud Services CA-1,O=DigiCert Inc,C=US"
"ssl_issuer_common_name" = "DigiCert Cloud Services CA-1"
"ssl_issuer_locality" = "Redmond"
"ssl_issuer_state" = "Washington
"ssl_issuer_organization" = "DigiCert Inc"
"ssl_subject" = "CN=Outlook.live.com,O=Microsoft Corporation,L=Redmond,ST=Washington,C=US"
"ssl_subject_common_name" = "Outlook.live.com"
"ssl_subject_organization" = "Microsoft Corporation"
"ssl_subject_locality" = "Redmond"
"ssl_subject_state" = "Washington"
"ssl_subject_organization" = "Microsoft Corporation"
"ssl_is_valid" = "true"
"ssl_version" = "3"
"ssl_serial" = "0B1641AEAE93F5DB71B36C977B7FCF63"
"ssl_publickey_algorithm" = "rsaEncryption"
"ssl_signature_algorithm" = "sha256WithRSAEncryption"
```
