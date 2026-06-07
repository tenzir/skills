---
title: Use the common action model to build custom alert actions
url: https://help.splunk.com/en/data-management/common-information-model/8.5/using-the-common-information-model/use-the-common-action-model-to-build-custom-alert-actions
last_modified: 2026-04-01T20:48:22.733Z
version: 8.5
---

# Use the common action model to build custom alert actions

The common action model is a common information model for alert actions. It is not a data model. Rather, it is a set of tools and best practices for creating alert actions that are consistent, robust, and easy to introspect. Splunk developed the common action model to support the adaptive response framework in Splunk Enterprise Security, but it is not exclusive to that use case.

The common action model consists of three components:

- a `cim_actions.py `library, which assists developers with building alert actions in a way that conforms to the common action model.
- a JSON spec in `alert_actions.conf.spec `, which classifies actions and specifies other metadata expected by the adaptive response framework.
- an extension to the Splunk Audit Logs data model that describes the introspection event data produced by alert actions that conform to the common action model.

Developers can use these components to design new alert actions or adaptive response actions or refactor existing custom actions to comply with the model. You can incorporate the common action model into your manual development process, or you can use the Splunk Add-on Builder, which incorporates the common action model in its custom alert action creation wizard. The Splunk Enterprise Security developer documentation contains a detailed walkthrough of both of these methods of creating an adaptive response action, which is an alert action with special functionality in Splunk Enterprise Security. See Create an adaptive response action on the Splunk developer portal.

## Using the ` cim_actions.py ` library

The `cim_actions.py `library is located at `$SPLUNK_HOME/etc/apps/Splunk_SA_CIM/lib/cim_actions.py `. If you are creating your action manually, import this library so that you can use the methods provided in it. If you are using Add-on Builder to create your action, the code snippet provided on the code editor imports the library for you and provides sample code for the methods available.

## Incorporating the JSON spec

The JSON spec is located at `$SPLUNK_HOME/etc/apps/Splunk_SA_CIM/README/alert_actions.conf.spec `. It defines the `param._cam `attribute and provides its documentation. The same folder also contains `alert_actions.conf.example `, which contains two examples of how to follow the specification in your `alert_actions.conf `file.

| Parameter | Description | Examples |
| --- | --- | --- |
| category | The category or categories the action belongs to. See ` cam_categories.csv ` for recommended values. | Information Conveyance, Information Gathering, Information Tracking, Permissions Control, Device Control |
| task | The function or functions performed by the action. See ` cam_tasks.csv ` for recommended values. | block, allow, create, update, delete, scan |
| subject | The object or objects that the action's task or tasks can be performed on. See ` cam_subjects.csv ` for recommended values. | endpoint.file, network.proxy, process.sandbox |

```text

```

| technology | The technology vendor(s), product(s), and version(s) that the action supports. | { "vendor": "Splunk", "product": "Enterprise", "version": ["6.4.3", "6.5.0"] } |
| supports_adhoc | Specifies if the action supports ad-hoc invocation from the Actions menu on the Incident Review dashboard in Splunk Enterprise Security. This parameter is only relevant within Splunk Enterprise Security, and defaults to false. See Adaptive Response framework in Splunk ES on the Splunk developer portal. | true |

```text

```

| drilldown_uri | An optional customized drilldown for the link that appears in the detailed view of a notable event on the Incident Review dashboard in Splunk Enterprise Security. This parameter is only relevant within Splunk Enterprise Security. If you do not want to specify a custom drilldown link, remove this parameter. Do not leave this parameter blank. If the parameter is not included, the default drilldown URL leads to a search for the result events created by this response action. If you want to specify a target in an app outside Enterprise Security, use the format ` ../<app_context>/<viewname>?<additional drilldown parameters> ` . If you are redirecting to a custom view within Enterprise Security, use the format ` /<viewname>?<additional drilldown parameters> ` . | "../my_app/my_view? form.orig_sid=$sid$&form.orig_rid=$rid$" |

| field_name_params | The param or params which represent the name of a result field. This parameter is only relevant within Splunk Enterprise Security. Incident Review uses the specified field name parameters to render a dropdown with field names present in the notable event. | ["param.my_param"] |

| required_params | Parameter(s) required for successful action execution. This parameter is only relevant within Splunk Enterprise Security. Incident Review uses the specified field name parameters to render a ` * ` on the user interface to indicate that the parameter is required. | ["param.my_param"] |

## Modeling introspection data

The Splunk Audit Logs data model includes the `Modular_Actions `dataset. The `message() `method in the `cim_actions.py `library automatically creates and tags introspection events for this data model. See Splunk Audit Logs for details of the fields.

If you have Splunk Enterprise Security installed, select the Adaptive Response Action Center to view introspection data for all actions compliant with the common action model.
