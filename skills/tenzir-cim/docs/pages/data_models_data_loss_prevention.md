---
title: Data Loss Prevention
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/data-loss-prevention
last_modified: 2026-04-01T20:48:24.768Z
version: 8.5
---

# Data Loss Prevention

The fields in the Data Loss Prevention (DLP) data model describe events gathered from DLP tools used to identify, monitor and protect data.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with DLP event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| DLP_Incidents | dlp |
| incident |

## Fields for DLP event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |

-
- | DLP_Incidents | ` action ` | string | The action taken by the DLP device. | recommended required for pytest-splunk-addon |
| DLP_Incidents | ` app ` | string | The application involved in the event. | required for pytest-splunk-addon |

-
- | DLP_Incidents | ` category ` | string | The category of the DLP event. | recommenderd required for pytest-splunk-addon |

-
- | DLP_Incidents | ` dest ` | string | The target of the DLP event. | recommended required for pytest-splunk-addon |

| DLP_Incidents | ` dest_bunit ` | string | The business unit of the DLP target. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` dest_category ` | string | The category of the DLP target. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` dest_priority ` | string | The priority of the DLP target. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DLP_Incidents | ` dest_zone ` | string | The zone of the DLP target. |  |

-
- | DLP_Incidents | ` dlp_type ` | string | The type of DLP system that generated the event. | recommended required for pytest-splunk-addon |

-
- | DLP_Incidents | ` dvc ` | string | The device that reported the DLP event. | recommended required for pytest-splunk-addon |

| DLP_Incidents | ` dvc_bunit ` | string | The business unit of the DLP target. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` dvc_category ` | string | The category of the DLP device. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` dvc_priority ` | string | The priority of the DLP device. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DLP_Incidents | ` dvc_zone ` | string | The zone of the DLP device. |  |

-
- | DLP_Incidents | ` object ` | string | The name of the affected object. | recommended required for pytest-splunk-addon |

-
- | DLP_Incidents | ` object_category ` | string | The category of the affected object. | recommended required for pytest-splunk-addon |

-
- | DLP_Incidents | ` object_path ` | string | The path of the affected object. | recommended required for pytest-splunk-addon |

-
- | DLP_Incidents | ` severity ` | string | The severity of the DLP event. | recommended required for pytest-splunk-addon |
| DLP_Incidents | ` severity_id ` | number | The numeric or vendor specific severity indicator corresponding to the event severity. |  |

-
- | DLP_Incidents | ` signature ` | string | The name of the DLP event. | recommended required for pytest-splunk-addon |
| DLP_Incidents | ` signature_id ` | string | The unique identifier or event code of the event signature. |  |
| DLP_Incidents | ` src ` | string | The source of the DLP event. | recommended |

| DLP_Incidents | ` src_bunit ` | string | The business unit of the DLP source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` src_category ` | string | The category of the DLP source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` src_priority ` | string | The priority of the DLP source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

-
- | DLP_Incidents | ` src_user ` | string | The source user of the DLP event. | recommended required for pytest-splunk-addon |

| DLP_Incidents | ` src_user_bunit ` | string | The business unit of the DLP source user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` src_user_category ` | string | The category of the DLP source user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` src_user_priority ` | string | The priority of the DLP source user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DLP_Incidents | ` src_zone ` | string | The zone of the DLP source. |  |
| DLP_Incidents | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |
| DLP_Incidents | ` user ` | string | The target user of the DLP event. | recommended |

| DLP_Incidents | ` user_bunit ` | string | The business unit of the DLP user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` user_category ` | string | The category of the DLP user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| DLP_Incidents | ` user_priority ` | string | The priority of the DLP user. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| DLP_Incidents | ` vendor_product ` | string | The vendor and product name of the DLP system. | recommended |
