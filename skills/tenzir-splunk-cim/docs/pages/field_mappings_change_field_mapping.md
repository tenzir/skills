---
title: Change Field Mapping
url: https://help.splunk.com/en/data-management/common-information-model/8.5/field-mappings/change-field-mapping
last_modified: 2026-04-01T20:48:26.409Z
version: 8.5
---

# Change Field Mapping

The following shows an example of how change events map differently from various cloud providers to CIM data model field names.

See the Change data model for full field descriptions.

## Update user example

The update user event from Amazon Web Services (AWS) and Azure is a good way to see a common event and how each cloud provider maps to CIM data model field names. An example case is where an admin creates or updates an IAMUser. The admin is the source user and source type.

### AWS update user

A sample AWS update user action follows:

Click expand or collapse to show or hide the example.

JSON Copy { "eventVersion": "1.05", "userIdentity": { "type": "IAMUser", /** ----- user_type, src_user_type "principalId": "AIDA3HRA7T6MUVQJRHPKV", /** ----- user, user_id "arn": "arn:aws:iam::772089552793:user/example_name", "accountId": "772089552793", /** ----- vendor_account "accessKeyId": "AKIA3HRA7T6MVC4EBVOG", "userName": "example_name" /** ----- user_name }, "eventTime": "2020-06-25T16:56:12Z", "eventSource": "iam.amazonaws.com", /** ----- app, dest "eventName": "UpdateUser", /** ----- action, command "awsRegion": "us-east-1", "sourceIPAddress": "72.83.94.230", /** ----- src, src_ip "userAgent": "aws-cli/2.0.0 Python/3.7.4 Darwin/19.5.0 botocore/2.0.0dev4", /** ----- user_agent "requestParameters": { /** ----- object, object_attrs, object_category, object_id, object_path "userName": "user_change_dm", "newUserName": "user_change" }, "responseElements": null, "requestID": "7e371c54-8df7-4f1f-b3b8-03d1298a52fd", "eventID": "74f66cee-7fe3-48f1-97ee-9c59efc40a5f", "eventType": "AwsApiCall", "recipientAccountId": "772089552793" }

```text
`{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",                      /** -----  user_type, src_user_type
    "principalId": "AIDA3HRA7T6MUVQJRHPKV", /** -----  user, user_id
    "arn": "arn:aws:iam::772089552793:user/example_name",
    "accountId": "772089552793",            /** -----  vendor_account
    "accessKeyId": "AKIA3HRA7T6MVC4EBVOG",
    "userName": "example_name"              /** -----  user_name
  },
  "eventTime": "2020-06-25T16:56:12Z",
  "eventSource": "iam.amazonaws.com",       /** -----  app, dest
  "eventName": "UpdateUser",                /** -----  action, command
  "awsRegion": "us-east-1",
  "sourceIPAddress": "72.83.94.230",        /** -----  src, src_ip
  "userAgent": "aws-cli/2.0.0 Python/3.7.4 Darwin/19.5.0 botocore/2.0.0dev4", /** -----  user_agent
  "requestParameters": {                    /** -----  object, object_attrs, object_category, object_id, object_path
    "userName": "user_change_dm",
    "newUserName": "user_change"
  },
  "responseElements": null,
  "requestID": "7e371c54-8df7-4f1f-b3b8-03d1298a52fd",
  "eventID": "74f66cee-7fe3-48f1-97ee-9c59efc40a5f",
  "eventType": "AwsApiCall",
  "recipientAccountId": "772089552793"
}`
```

### Azure update user

A sample Azure update user action follows:

Click expand or collapse to show or hide the example.

JSON Copy { "id": "Directory_5c4d6b97-3e18-4565-ad44-3c20ee2c70ab_1CKOF_99617149", "category": "UserManagement", /** ----- object_category "correlationId": "5c4d6b97-3e18-4565-ad44-3c20ee2c70ab", "result": "success", /** ----- status "resultReason": "", /** ----- result "activityDisplayName": "Disable Strong Authentication", /** ----- command "activityDateTime": "2020-06-11T23:07:51.971036Z", "loggedByService": "Core Directory", /** ----- dvc "operationType": "Update", /** ----- action "initiatedBy": { "app": null, "user": { "id": "df22f023-9e0f-4d78-bdd5-d496688af11e", "displayName": null, "userPrincipalName": "admin@a830edad9050849NDA3079.onmicrosoft.com", /** ----- src_user "ipAddress": null, "userType": null } }, "targetResources": [ { "id": "93a565f6-d0fc-4ac3-9d2a-8c1de9aeed3c", /** ----- object_id "displayName": null, "type": "User", /** ----- change_type, object_category "userPrincipalName": "es_csm_change_model@a830edad9050849nda3079.onmicrosoft.com", /** ----- user, user_id "groupType": null, "modifiedProperties": [ { "displayName": "StrongAuthenticationRequirement", "oldValue": "[{\"RelyingParty\":\"*\",\"State\":1,\"RememberDevicesNotIssuedBefore\":\"2020-06-11T23:07:35+00:00\"}]", "newValue": "[]" }, { "displayName": "Included Updated Properties", "oldValue": null, "newValue": "\"StrongAuthenticationRequirement\"" /** ----- object_attrs } ] } ], "additionalDetails": [] }

```text
`{
  "id": "Directory_5c4d6b97-3e18-4565-ad44-3c20ee2c70ab_1CKOF_99617149",
  "category": "UserManagement",                 /** -----  object_category
  "correlationId": "5c4d6b97-3e18-4565-ad44-3c20ee2c70ab",
  "result": "success",                          /** -----  status
  "resultReason": "",                           /** -----  result
  "activityDisplayName": "Disable Strong Authentication", /** -----  command
  "activityDateTime": "2020-06-11T23:07:51.971036Z",
  "loggedByService": "Core Directory",          /** -----  dvc
  "operationType": "Update",                    /** -----  action
  "initiatedBy": {
    "app": null,
    "user": {
      "id": "df22f023-9e0f-4d78-bdd5-d496688af11e",
      "displayName": null,
      "userPrincipalName": "admin@a830edad9050849NDA3079.onmicrosoft.com",  /** -----  src_user
      "ipAddress": null,
      "userType": null
    }
  },
  "targetResources": [
    {
      "id": "93a565f6-d0fc-4ac3-9d2a-8c1de9aeed3c", /** -----  object_id
      "displayName": null,
      "type": "User",                               /** -----  change_type, object_category
      "userPrincipalName": "es_csm_change_model@a830edad9050849nda3079.onmicrosoft.com",  /** -----  user, user_id
      "groupType": null,
      "modifiedProperties": [
        {
          "displayName": "StrongAuthenticationRequirement",
          "oldValue": "[{\"RelyingParty\":\"*\",\"State\":1,\"RememberDevicesNotIssuedBefore\":\"2020-06-11T23:07:35+00:00\"}]",
          "newValue": "[]"
        },
        {
          "displayName": "Included Updated Properties",
          "oldValue": null,
          "newValue": "\"StrongAuthenticationRequirement\"" /** -----  object_attrs
        }
      ]
    }
  ],
  "additionalDetails": []
}`
```

### User update field mapping

Using the user update from AWS as a base sample, and comparing it to a similar event from Azure is a good way to see the similarities and differences per common CIM field names.

| User example data | Provider field name | CIM field name |
| --- | --- | --- |
| Destination example data | Provider field name | CIM field name |
| Action example data | Provider field name | CIM field name |
| Object example data | Provider field name | CIM field name |

-
- | AWS ` AIDA3HRA7T6MUVQJRHPKV ` | userIdentity.principalId | user user_id |

-
- | Azure ` es_csm_change_model@a830edad9050849nda3079.onmicrosoft.com ` | targetResources.userPrincipalName | user user_id |

-
- | AWS ` iam.amazonaws.com ` | eventSource | app dest |

- | Azure ` Core Directory ` | loggedByService | dvc |

-
- | AWS ` UpdateUser ` | eventName | action command |

| Azure ` Update ` | operationType | action |

```text

```

-
-
-
-
- | AWS JSON Copy "requestParameters": { "userName": "user_change_dm", "newUserName": "user_change" }, ` "requestParameters": { "userName": "user_change_dm", "newUserName": "user_change" }, ` | requestParameters | object object_attrs object_category object_id object_path |

| Azure ` UserManagement ` | category | object_category |

| Azure ` 93a565f6-d0fc-4ac3-9d2a-8c1de9aeed3c ` | targetResources.id | object_id |

| Azure ` "StrongAuthenticationRequirement\" ` | targetResources.modifiedProperties | object_attrs |

## Reboot example

The login success event from Amazon Web Services (AWS) and Azure is a good way to see a common event and how each cloud provider maps to CIM data model field names.

### AWS EC2 instance reboot

A sample AWS EC2 instance reboot action follows:

Click expand or collapse to show or hide the example.

JSON Copy { "eventVersion": "1.05", "userIdentity": { "type": "IAMUser", /** ----- user_type, src_user_type "principalId": "AIDA3HRA7T6MRJYJZSGXO", /** ----- user, user_id "arn": "arn:aws:iam::772089552793:user/example_name", "accountId": "772089552793", /** ----- vendor_account "accessKeyId": "ASIA3HRA7T6MR2NXOREA", "userName": "example_name", /** ----- user_name "sessionContext": { "sessionIssuer": {}, "webIdFederationData": {}, "attributes": { "mfaAuthenticated": "false", "creationDate": "2020-06-08T21:51:29Z" } } }, "eventTime": "2020-06-09T01:05:55Z", "eventSource": "ec2.amazonaws.com", /** ----- app, dest "eventName": "RebootInstances", /** ----- action, command "awsRegion": "us-east-2", /** ----- vendor_region "sourceIPAddress": "73.162.147.20", /** ----- src, src_ip "userAgent": "console.ec2.amazonaws.com", /** ----- user_agent "requestParameters": { /** ----- object, object_attrs, object_category, object_id, object_path "instancesSet": { "items": [ { "instanceId": "i-09b1f332093983cc1" } ] } }, "responseElements": { "requestId": "b09c7d96-645e-45db-aa6f-e09c32ad076e", "_return": true }, "requestID": "b09c7d96-645e-45db-aa6f-e09c32ad076e", "eventID": "43a8628d-5fc7-42f7-8666-b71664cefbac", "eventType": "AwsApiCall", "recipientAccountId": "772089552793" }

```text
`{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",                         /** -----  user_type, src_user_type
    "principalId": "AIDA3HRA7T6MRJYJZSGXO",    /** -----  user, user_id
    "arn": "arn:aws:iam::772089552793:user/example_name",
    "accountId": "772089552793",               /** -----  vendor_account
    "accessKeyId": "ASIA3HRA7T6MR2NXOREA",
    "userName": "example_name",                /** -----  user_name
    "sessionContext": {
      "sessionIssuer": {},
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-06-08T21:51:29Z"
      }
    }
  },
  "eventTime": "2020-06-09T01:05:55Z",
  "eventSource": "ec2.amazonaws.com",            /** -----  app, dest
  "eventName": "RebootInstances",                /** -----  action, command
  "awsRegion": "us-east-2",                      /** -----  vendor_region
  "sourceIPAddress": "73.162.147.20",            /** -----  src, src_ip
  "userAgent": "console.ec2.amazonaws.com",      /** -----  user_agent
  "requestParameters": {                         /** -----  object, object_attrs, object_category, object_id, object_path
    "instancesSet": {
      "items": [
        {
          "instanceId": "i-09b1f332093983cc1"
        }
      ]
    }
  },
  "responseElements": {
    "requestId": "b09c7d96-645e-45db-aa6f-e09c32ad076e",
    "_return": true
  },
  "requestID": "b09c7d96-645e-45db-aa6f-e09c32ad076e",
  "eventID": "43a8628d-5fc7-42f7-8666-b71664cefbac",
  "eventType": "AwsApiCall",
  "recipientAccountId": "772089552793"
}`
```

### Azure virtual machine reboot

A sample Azure virtual machine reboot action follows:

Click expand or collapse to show or hide the example.

JSON Copy { "time": "2020-06-18T22:31:41.7234475Z", "resourceId": "/SUBSCRIPTIONS/AE4AB7C9-DCDF-4427-9729-48E8C7551BE9/RESOURCEGROUPS/ES_CSM_CHANGE_MODEL/PROVIDERS/MICROSOFT.COMPUTE/VIRTUALMACHINES/ES-CSM-CHNAGE-VM-1", /** ----- object_id, object, app, object_category, dest "operationName": "MICROSOFT.COMPUTE/VIRTUALMACHINES/RESTART/ACTION", /** ----- app "category": "Administrative", "resultType": "Success", "resultSignature": "Succeeded.", /** ----- status "durationMs": 0, "callerIpAddress": "174.62.106.48", "correlationId": "3cdcca7c-a98c-46b6-b3f9-9ce2d27c5fe4", "identity": { "authorization": { "scope": "/subscriptions/ae4ab7c9-dcdf-4427-9729-48e8c7551be9/resourceGroups/es_csm_change_model/providers/Microsoft.Compute/virtualMachines/es-csm-chnage-vm-1", "action": "Microsoft.Compute/virtualMachines/restart/action", /** ----- action, command "evidence": { "role": "Contributor", "roleAssignmentScope": "/subscriptions/ae4ab7c9-dcdf-4427-9729-48e8c7551be9", "roleAssignmentId": "8eb22423e5cc461592fda56f5b5dc2aa", "roleDefinitionId": "b24988ac618042a0ab8820f7382dd24c", "principalId": "149ec7a11f3a4878a1d558f4a1e67655", "principalType": "User" } }, "claims": { "aud": "https://management.core.windows.net/", "iss": "https://sts.windows.net/2ed28a74-1f6f-4829-8530-fe359c77d35c/", "iat": "1592517408", "nbf": "1592517408", "exp": "1592521308", "http://schemas.microsoft.com/claims/authnclassreference": "1", "aio": "ATQAy/8PAAAAtikpFkPjCTjg0x5DI7ch1Ki6e2TVeKzmZrn2OnJ5GchOOfM/PN7RfBss5uGIecXp", "http://schemas.microsoft.com/claims/authnmethodsreferences": "pwd", "appid": "c44b4083-3bb0-49c1-b47d-974e53cbdf3c", "appidacr": "2", "ipaddr": "174.62.106.48", /** ----- src, src_ip "name": "Example_Name", "http://schemas.microsoft.com/identity/claims/objectidentifier": "149ec7a1-1f3a-4878-a1d5-58f4a1e67655", "puid": "10032000C9954D8E", "http://schemas.microsoft.com/identity/claims/scope": "user_impersonation", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": "nZAgSAB9HehKWTDa3J1iIqTLWNzipERZJYScR7qzot4", "http://schemas.microsoft.com/identity/claims/tenantid": "2ed28a74-1f6f-4829-8530-fe359c77d35c", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": "admin@a830edad9050849nda3079.onmicrosoft.com", /** ----- user_id "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "admin@a830edad9050849nda3079.onmicrosoft.com", "uti": "Ka0FzSYrf02er9SWaHN9AA", "ver": "1.0" } }, "level": "Information", "properties": { "category": "Administrative" } }

```text
`{
  "time": "2020-06-18T22:31:41.7234475Z",
  "resourceId": "/SUBSCRIPTIONS/AE4AB7C9-DCDF-4427-9729-48E8C7551BE9/RESOURCEGROUPS/ES_CSM_CHANGE_MODEL/PROVIDERS/MICROSOFT.COMPUTE/VIRTUALMACHINES/ES-CSM-CHNAGE-VM-1",                                    /** -----  object_id, object, app, object_category, dest
  "operationName": "MICROSOFT.COMPUTE/VIRTUALMACHINES/RESTART/ACTION",    /** -----  app
  "category": "Administrative",
  "resultType": "Success",
  "resultSignature": "Succeeded.",                                        /** -----  status
  "durationMs": 0,
  "callerIpAddress": "174.62.106.48",
  "correlationId": "3cdcca7c-a98c-46b6-b3f9-9ce2d27c5fe4",
  "identity": {
    "authorization": {
      "scope": "/subscriptions/ae4ab7c9-dcdf-4427-9729-48e8c7551be9/resourceGroups/es_csm_change_model/providers/Microsoft.Compute/virtualMachines/es-csm-chnage-vm-1",
      "action": "Microsoft.Compute/virtualMachines/restart/action",       /** -----  action, command
      "evidence": {
        "role": "Contributor",
        "roleAssignmentScope": "/subscriptions/ae4ab7c9-dcdf-4427-9729-48e8c7551be9",
        "roleAssignmentId": "8eb22423e5cc461592fda56f5b5dc2aa",
        "roleDefinitionId": "b24988ac618042a0ab8820f7382dd24c",
        "principalId": "149ec7a11f3a4878a1d558f4a1e67655",
        "principalType": "User"
      }
    },
    "claims": {
      "aud": "https://management.core.windows.net/",
      "iss": "https://sts.windows.net/2ed28a74-1f6f-4829-8530-fe359c77d35c/",
      "iat": "1592517408",
      "nbf": "1592517408",
      "exp": "1592521308",
      "http://schemas.microsoft.com/claims/authnclassreference": "1",
      "aio": "ATQAy/8PAAAAtikpFkPjCTjg0x5DI7ch1Ki6e2TVeKzmZrn2OnJ5GchOOfM/PN7RfBss5uGIecXp",
      "http://schemas.microsoft.com/claims/authnmethodsreferences": "pwd",
      "appid": "c44b4083-3bb0-49c1-b47d-974e53cbdf3c",
      "appidacr": "2",
      "ipaddr": "174.62.106.48",                                          /** -----  src, src_ip
      "name": "Example_Name",
      "http://schemas.microsoft.com/identity/claims/objectidentifier": "149ec7a1-1f3a-4878-a1d5-58f4a1e67655",
      "puid": "10032000C9954D8E",
      "http://schemas.microsoft.com/identity/claims/scope": "user_impersonation",
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": "nZAgSAB9HehKWTDa3J1iIqTLWNzipERZJYScR7qzot4",
      "http://schemas.microsoft.com/identity/claims/tenantid": "2ed28a74-1f6f-4829-8530-fe359c77d35c",
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": "admin@a830edad9050849nda3079.onmicrosoft.com", /** -----  user_id
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "admin@a830edad9050849nda3079.onmicrosoft.com",
      "uti": "Ka0FzSYrf02er9SWaHN9AA",
      "ver": "1.0"
    }
  },
  "level": "Information",
  "properties": {
    "category": "Administrative"
  }
}`
```

### Reboot field mapping

Using the reboot from AWS as a base sample, and comparing it to a similar event from Azure is a good way to see the similarities and differences per common CIM field names.

| User example data | Provider field name | CIM field name |
| --- | --- | --- |
| User type example data | Provider field name | CIM field name |
| Destination example data | Provider field name | CIM field name |
| Action example data | Provider field name | CIM field name |
| Source example data | Provider field name | CIM field name |
| Object example data | Provider field name | CIM field name |

| AWS ` AIDA3HRA7T6MRJYJZSGXO ` | userIdentity.principalId | user, user_id |

-
- | Azure ` admin@a830edad9050849nda3079.onmicrosoft.com ` | identity.claims. http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name | user src_user |

-
- | AWS ` IAMUser ` | userIdentity.type | user_type src_user_type |

| Azure ` n/a ` | n/a | na/ |

-
- | AWS ` ec2.amazonaws.com ` | eventSource | app dest |

- | Azure ` Microsoft.Compute ` | operationName | app |

| Azure ` ae4ab7c9-dcdf-4427-9729-48e8c7551be9 ` | Subscription ID extracted from resourceID | dest |

-
- | AWS ` RebootInstances ` | eventName | action command |

-
- | Azure ` MICROSOFT.COMPUTE/VIRTUALMACHINES/RESTART/ACTION ` | operationName | action command |

-
- | AWS ` 73.162.147.20 ` | sourceIPAddress | src src_ip |

-
- | Azure ` 174.62.106.48 ` | claims.ipaddr | src src_ip |

```text

```

-
-
-
-
- | AWS JSON Copy "requestParameters": { "force": false, "instancesSet": { "items": [{ "instanceId": "i-c103dcc9" }] } }, ` "requestParameters": { "force": false, "instancesSet": { "items": [{ "instanceId": "i-c103dcc9" }] } }, ` | requestParameters | object object_attrs object_category object_id object_path |

-
-

-

| Azure ` /SUBSCRIPTIONS/AE4AB7C9-DCDF-4427-9729-48E8C7551BE9/RESOURCEGROUPS/ES_CSM_CHANGE_MODEL/PROVIDERS/MICROSOFT.COMPUTE/VIRTUALMACHINES/ES-CSM-CHNAGE-VM-1 ` | resourceId | object_id object: .../ES_CSM_CHANGE_MODEL-VM-1 object_category: .../VIRTUALMACHINES/... |

You must assign `requestParameters `to different `object_* `fields in CIM. The CIM field `object_* `is the object of change, which implies that it is the specific resource object that is reported as changed by the event.

In the AWS examples provided for the `UpdateUser `event, the object of the change is the user, who is listed in `requestParameters `. Therefore, the CIM field `object `maps to `requestParameters.newUserName `. The value for `newUserName `is `user_change `. Additionally, the values for both `object_category `and `object_attr `is the user because there are no known user attributes in the sample. The `object_id `is `user_change `because there no other user ID exists in the example other than the `userName `. The field `object_path `is not mapped because no path exists in the sample.

In the AWS examples provided for the `RebootInstances `event, the object of the change is the instance. Therefore, the CIM field `object `maps to `requestParameters.instancesSet.items.instanceId `. The value for `instanceId `is `i-09b1f332093983cc1 `. Additionally, the values for both `object_category `and `object_attr `is the instance because no known instance attributes exist in the example. The field `object_id `is `i-09b1f332093983cc1 `and the field `object_path `is not mapped because no instance path exists in the example.
