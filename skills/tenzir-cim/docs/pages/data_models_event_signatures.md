---
title: Event Signatures
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/event-signatures
last_modified: 2026-04-01T20:48:26.046Z
version: 8.5
---

# Event Signatures

Event Signatures is a standard location to store Windows EventID. This data model is searchable as DataModel.DataSet. It is not accelerated by default, but the appropriate acceleration settings have been defined.

The Event Signatures data model is vendor specific to Microsoft Windows and applies only to the Windows event ID and its description field. For example: `signature_id=4689 ``signature=A process has exited. `

Any use case, which uses the windows event ID, can use this data model.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

| Dataset name | Tag name |
| --- | --- |
| Event_Signatures |  |
| \|____ Signatures | track_event_signatures |

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

## Event Signatures

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Signatures | ` dest ` | string | System affected by the signature. |  |
| Signatures | ` dest_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Signatures | ` dest_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Signatures | ` dest_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Signatures | ` signature ` | string | The human readable event name. |  |
| Signatures | ` signature_id ` | string | The event name identifier (as supplied by the vendor). |  |
| Signatures | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |

## Calculations

| Calculation ID | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| ` Signatures_vendor_product ` | ` vendor_product ` | string | The vendor and product name of the technology that reported the event, such as Carbon Black Cb Response. This field can be automatically populated by vendor and product fields in your data. Expression: ` case(isnotnull(vendor_product),vendor_product, ` ` isnotnull(vendor) AND vendor!=\"unknown\" AND isnotnull(product) AND product!=\"unknown\",vendor.\" \".product,isnotnull(vendor) AND vendor!=\"unknown\" AND (isnull(product) OR product=\"unknown\"),vendor.\" unknown\",(isnull(vendor) OR vendor=\"unknown\") AND isnotnull(product) AND product!=\"unknown\",\"unknown \".product,isnotnull(sourcetype),sourcetype, 1=1,\"unknown\")" ` | recommended |

## Search Example

An example follows for the summary count of signatures by destination ID:

`| tstats count from datamodel=Event_Signatures.Signatures by Signatures.signature_id,Signatures.dest `
