---
title: Authentication Field Mapping
url: https://help.splunk.com/en/data-management/common-information-model/8.5/field-mappings/authentication-field-mapping
last_modified: 2026-04-01T20:48:26.315Z
version: 8.5
---

# Authentication Field Mapping

The following shows an example of how authentication events map differently from various cloud providers to CIM data model field names.

See the Authentication data model for full field descriptions.

## Login success example

The login success event from Google Cloud Platform (GCP), Microsoft Office 356 (MS o365), and Amazon Web Services (AWS) is a good way to see a common event and how each cloud provider maps to CIM data model field names.

### GCP success

A sample GCP successful user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { "actor":{ "email":"name@gmail.com", /** ----- user_id "profileId":"104465715494659475645" }, "etag":"\"JDMC8884sebSczDxOtZ17CIssbQ/Pau_EbIGF8FWZWC7W8Ti1uoCfjc\"", "events":[ { "name":"login_success", /** ----- action "parameters":[ { "name":"login_type", "value":"google_password" }, { "multiValue":[ "password" /** ----- authentication_method ], "name":"login_challenge_method" }, { "boolValue":false, "name":"is_suspicious" } ], "type":"login" /** ----- signature } ], "id":{ "applicationName":"login", "customerId":"C035c27ok", /** ----- vendor_account "time":"2020-02-24T23:31:48.090Z", "uniqueQualifier":"529462392776" }, "ipAddress":"4.14.104.185", /** ----- src, src_ip "kind":"admin#reports#activity" /** ----- user_agent }

```text
`{
   "actor":{
      "email":"name@gmail.com",                /** -----  user_id
      "profileId":"104465715494659475645"
   },
   "etag":"\"JDMC8884sebSczDxOtZ17CIssbQ/Pau_EbIGF8FWZWC7W8Ti1uoCfjc\"",
   "events":[
      {
         "name":"login_success",               /** -----  action
         "parameters":[
            {
               "name":"login_type",
               "value":"google_password"
            },
            {
               "multiValue":[
                  "password"                   /** -----  authentication_method
               ],
               "name":"login_challenge_method"
            },
            {
               "boolValue":false,
               "name":"is_suspicious"
            }
         ],
         "type":"login"                       /** -----  signature
      }
   ],
   "id":{
      "applicationName":"login",
      "customerId":"C035c27ok",               /** -----  vendor_account
      "time":"2020-02-24T23:31:48.090Z",
      "uniqueQualifier":"529462392776"
   },
   "ipAddress":"4.14.104.185",                /** -----  src, src_ip
   "kind":"admin#reports#activity"            /** -----  user_agent
}`
```

### MS o365 success

A sample MS o365 successful user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { [-] Actor: [ [-] { [-] ID: df22f023-9e0f-4d78-bdd5-d496688af11e /** ----- user_id Type: 0 } { [-] ID: admin@a830edad9050849NDA3079.onmicrosoft.com /** ----- user_id Type: 5 } { [-] ID: 10037FFE8EC1E08E /** ----- user_id Type: 3 } ] ActorContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c /** ----- vendor_account ActorIpAddress: 4.14.104.185 /** ----- src, src_ip ApplicationId: c44b4083-3bb0-49c1-b47d-974e53cbdf3c AzureActiveDirectoryEventType: 1 ClientIP: 4.14.104.185 CreationTime: 2020-02-27T00:49:21 ExtendedProperties: [ [-] { [-] Name: UserAgent Value: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 /** ----- user_agent } { [-] Name: FlowTokenScenario Value: Login } { [-] Name: UserAuthenticationMethod Value: 1 /** ----- authentication_method } { [-] Name: RequestType Value: Login:login } { [-] Name: ResultStatusDetail Value: Success } ] Id: 6c7bb43a-4fc5-403e-9e20-a1e6d4fdc7b3 InterSystemsId: a2c96557-09ee-4be2-9d8a-a13c7326ff0e IntraSystemId: 4bc7a6ba-fabb-4bcc-9663-2a1be0a11a00 ModifiedProperties: [ [-] ] ObjectId: 797f4846-ba00-4fd7-ba43-dac1f8f63013 Operation: UserLoggedIn /** ----- signature OrganizationId: 2ed28a74-1f6f-4829-8530-fe359c77d35c RecordType: 15 ResultStatus: Succeeded /** ----- action SupportTicketId: Target: [ [-] { [-] ID: 797f4846-ba00-4fd7-ba43-dac1f8f63013 Type: 0 } ] TargetContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c UserId: admin@a830edad9050849NDA3079.onmicrosoft.com UserKey: 10037FFE8EC1E08E@a830edad9050849NDA3079.onmicrosoft.com UserType: 0 Version: 1 Workload: AzureActiveDirectory }

```text
`{ [-]
   Actor: [ [-]
     { [-]
       ID: df22f023-9e0f-4d78-bdd5-d496688af11e         /** -----  user_id
       Type: 0
     }
     { [-]
       ID: admin@a830edad9050849NDA3079.onmicrosoft.com /** -----  user_id
       Type: 5
     }
     { [-]
       ID: 10037FFE8EC1E08E                             /** -----  user_id
       Type: 3
     }
   ]
   ActorContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c  /** -----  vendor_account
   ActorIpAddress: 4.14.104.185                          /** -----  src, src_ip
   ApplicationId: c44b4083-3bb0-49c1-b47d-974e53cbdf3c
   AzureActiveDirectoryEventType: 1
   ClientIP: 4.14.104.185
   CreationTime: 2020-02-27T00:49:21
   ExtendedProperties: [ [-]
     { [-]
       Name: UserAgent
       Value: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36                           /** -----  user_agent
     }
     { [-]
       Name: FlowTokenScenario
       Value: Login
     }
     { [-]
       Name: UserAuthenticationMethod
       Value: 1                                /** -----  authentication_method
     }
     { [-]
       Name: RequestType
       Value: Login:login
     }
     { [-]
       Name: ResultStatusDetail
       Value: Success
     }
   ]
   Id: 6c7bb43a-4fc5-403e-9e20-a1e6d4fdc7b3
   InterSystemsId: a2c96557-09ee-4be2-9d8a-a13c7326ff0e
   IntraSystemId: 4bc7a6ba-fabb-4bcc-9663-2a1be0a11a00
   ModifiedProperties: [ [-]
   ]
   ObjectId: 797f4846-ba00-4fd7-ba43-dac1f8f63013
   Operation: UserLoggedIn                       /** -----  signature
   OrganizationId: 2ed28a74-1f6f-4829-8530-fe359c77d35c
   RecordType: 15
   ResultStatus: Succeeded                       /** -----  action
   SupportTicketId:
   Target: [ [-]
     { [-]
       ID: 797f4846-ba00-4fd7-ba43-dac1f8f63013
       Type: 0
     }
   ]
   TargetContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c
   UserId: admin@a830edad9050849NDA3079.onmicrosoft.com
   UserKey: 10037FFE8EC1E08E@a830edad9050849NDA3079.onmicrosoft.com
   UserType: 0
   Version: 1
   Workload: AzureActiveDirectory
}`
```

### AWS success

A sample AWS successful user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { additionalEventData: { LoginTo: https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true MFAUsed: No /** ----- authentication_method MobileVersion: No } awsRegion: us-east-1 eventID: 040eb5f3-1132-4325-b06b-022e580c44fe eventName: ConsoleLogin /** ----- signature eventSource: signin.amazonaws.com eventTime: 2020-02-21T23:06:26Z eventType: AwsConsoleSignIn eventVersion: 1.05 recipientAccountId: 772089552793 requestParameters: null responseElements: { ConsoleLogin: Success /** ----- action } sourceIPAddress: 4.14.104.185 /** ----- src userAgent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 /** ----- user_agent userIdentity: { accountId: 772089552793 /** ----- vendor_account arn: arn:aws:iam::772089552793:user/example_user principalId: AIDA3HRA7T6MUVQJRHPKV type: IAMUser userName: example_user /** ----- user_id, user, src_user } }

```text
`{
   additionalEventData: {
     LoginTo: https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true
     MFAUsed: No                             /** -----  authentication_method
     MobileVersion: No
   }
   awsRegion: us-east-1
   eventID: 040eb5f3-1132-4325-b06b-022e580c44fe
   eventName: ConsoleLogin                   /** -----  signature
   eventSource: signin.amazonaws.com
   eventTime: 2020-02-21T23:06:26Z
   eventType: AwsConsoleSignIn
   eventVersion: 1.05
   recipientAccountId: 772089552793
   requestParameters: null
   responseElements: {
     ConsoleLogin: Success                     /** -----  action
   }
   sourceIPAddress: 4.14.104.185               /** -----  src
   userAgent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36                         /** -----  user_agent
   userIdentity: {
     accountId: 772089552793                   /** -----  vendor_account
     arn: arn:aws:iam::772089552793:user/example_user
     principalId: AIDA3HRA7T6MUVQJRHPKV
     type: IAMUser
     userName: example_user                    /** -----  user_id, user, src_user
   }
}`
```

### Login success field mapping

Using the login success from GCP as a base sample, and comparing it to a similar event from MS o365 and AWS is a good way to see the similarities and differences per common CIM field names.

| User id example data | Provider field name | CIM field name |
| --- | --- | --- |
| Action example data | Provider field name | CIM field name |
| Signature example data | Provider field name | CIM field name |
| Authentication method example data | Provider field name | CIM field name |
| Vendor account example data | Provider field name | CIM field name |
| Source example data | Provider field name | CIM field name |
| User agent data | Provider field name | CIM field name |

| GCP ` name@gmail.com ` | actor.email | user_id |

-
-
- | MS o365 ` df22f023-9e0f-4d78-bdd5-d496688af11e ` ` admin@a830edad9050849NDA3079.onmicrosoft.com ` ` 10037FFE8EC1E08E ` | Id | user_id |

-
-
- | AWS ` example_user ` | userIdentity.userName | user_id user src_user |

| GCP ` login_success ` | events.name | action |

| MS o365 ` Succeeded ` | ResultStatus | action |

| AWS ` Success ` | responseElements.ConsoleLogin | action |

| GCP ` login ` | events.type | signature |

| MS o365 ` UserLoggedIn ` | Operation | signature |

| AWS ` ConsoleLogin ` | eventName | signature |

-
- | GCP ` password ` | multiValue events.parameters.name.login_challenge_method | authentication_method |

| MS o365 ` 1 ` | UserAuthenticationMethod | authentication_method |

| AWS ` No ` | MFAUsed | authentication_method |

| GCP ` C035c27ok ` | id.customerId | vendor_account |

| MS o365 ` 2ed28a74-1f6f-4829-8530-fe359c77d35c ` | OrganizationId | vendor_account |

| AWS ` 772089552793 ` | userIdentity.accountId | vendor_account |

-
- | GCP ` 4.14.104.185 ` | ipAddress | src src_ip |

-
- | MS o365 ` 4.14.104.185 ` | ClientIP | src src_ip |

| AWS ` 4.14.104.185 ` | sourceIPAddress | src |

| GCP ` admin#reports#activity ` | kind | user_agent |

| MS o365 ` Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 ` | UserAgent | user_agent |

| AWS ` Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 ` | userAgent | user_agent |

## Login failure example

The login failure event from Google Cloud Platform (GCP), Microsoft Office 356 (MS o365), and Amazon Web Services (AWS) is a good way to see a common event and how each cloud provider maps to CIM data model field names.

### GCP failure

A sample GCP failed user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { "protoPayload": { "@type": "type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo": { "principalEmail": "example_user@gmail.com" /** ----- user_id }, "requestMetadata": { "callerIp": "2601:646:8400:b0:a991:7135:7879:6cea" /** ----- src, src_ip }, "serviceName": "login.googleapis.com", /** ----- app, dest "methodName": "google.login.LoginService.loginFailure", /** ----- signature "resourceName": "organizations/809036120291", "metadata": { "activityId": { "timeUsec": "1588189783734201", "uniqQualifier": "1023108278221" }, "event": [ { "eventType": "login", "eventName": "login_failure", "parameter": [ { "name": "login_type", "value": "unknown", "label": "LABEL_OPTIONAL", "type": "TYPE_STRING" }, { "name": "login_challenge_method", /** ----- authentication_method "multiStrValue": [ /** ----- reason "password", "password" ], "label": "LABEL_REPEATED", "type": "TYPE_STRING" }, { "name": "dusi", "value": "IMyb8fehs77-gQE", "label": "LABEL_OPTIONAL", "type": "TYPE_STRING" } ] } ], "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto" } }, "insertId": "mh9fqkc4a2", "resource": { "type": "audited_resource", "labels": { "method": "google.login.LoginService.loginFailure", "service": "login.googleapis.com" } }, "timestamp": "2020-04-29T19:49:43.734201Z", "severity": "NOTICE", /** ----- action "logName": "organizations/809036120291/logs/cloudaudit.googleapis.com%2Fdata_access", "receiveTimestamp": "2020-04-29T20:43:00.836830467Z" }

```text
`{
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "authenticationInfo": {
      "principalEmail": "example_user@gmail.com"             /** -----  user_id
    },
    "requestMetadata": {
      "callerIp": "2601:646:8400:b0:a991:7135:7879:6cea"     /** -----  src, src_ip
    },
    "serviceName": "login.googleapis.com",                   /** -----  app, dest
    "methodName": "google.login.LoginService.loginFailure",  /** -----  signature
    "resourceName": "organizations/809036120291",
    "metadata": {
      "activityId": {
        "timeUsec": "1588189783734201",
        "uniqQualifier": "1023108278221"
      },
      "event": [
        {
          "eventType": "login",
          "eventName": "login_failure",
          "parameter": [
            {
              "name": "login_type",
              "value": "unknown",
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "login_challenge_method",               /** -----  authentication_method
              "multiStrValue": [                              /** -----  reason
                "password",
                "password"
              ],
              "label": "LABEL_REPEATED",
              "type": "TYPE_STRING"
            },
            {
              "name": "dusi",
              "value": "IMyb8fehs77-gQE",
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        }
      ],
      "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
    }
  },
  "insertId": "mh9fqkc4a2",
  "resource": {
    "type": "audited_resource",
    "labels": {
      "method": "google.login.LoginService.loginFailure",
      "service": "login.googleapis.com"
    }
  },
  "timestamp": "2020-04-29T19:49:43.734201Z",
  "severity": "NOTICE",                                       /** -----  action
  "logName": "organizations/809036120291/logs/cloudaudit.googleapis.com%2Fdata_access",
  "receiveTimestamp": "2020-04-29T20:43:00.836830467Z"
}`
```

### MS o365 failure

A sample MS o365 failed user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { [-] Actor: [ [-] { [-] ID: 1d48684f-70ea-41e7-8459-9a7a24a8690a Type: 0 } { [-] ID: jc3@a830edad9050849NDA3079.onmicrosoft.com /** ----- user_id Type: 5 } { [-] ID: 10030000AEF912F2 Type: 3 } ] ActorContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c ActorIpAddress: 13.67.186.66 ApplicationId: 00000002-0000-0ff1-ce00-000000000000 AzureActiveDirectoryEventType: 1 ClientIP: 13.67.186.66 /** ----- src_ip, src CreationTime: 2020-02-27T07:46:00 ExtendedProperties: [ [-] { [-] Name: UserAgent /** ----- user_agent Value: python-requests/2.12.4 } { [-] Name: RequestType Value: OrgIdWsTrust2:process } { [-] Name: ResultStatusDetail Value: UserError } ] Id: 8498834c-4ca4-4300-9351-099f917bd2e7 InterSystemsId: 3f3bd815-8d38-48c8-aa71-445216d908de IntraSystemId: c3b22bc6-14c4-4b41-9aee-f4fb7f1e1000 LogonError: InvalidUserNameOrPassword /** ----- reason ModifiedProperties: [ [-] ] ObjectId: Unknown Operation: UserLoginFailed /** ----- signature OrganizationId: 2ed28a74-1f6f-4829-8530-fe359c77d35c /** ----- vendor_account RecordType: 15 ResultStatus: Failed /** ----- action SupportTicketId: Target: [ [-] { [-] ID: Unknown Type: 0 } ] TargetContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c UserId: jc3@a830edad9050849NDA3079.onmicrosoft.com /** ----- user, user_id UserKey: 10030000AEF912F2@a830edad9050849NDA3079.onmicrosoft.com UserType: 0 /** ----- user_type Version: 1 Workload: AzureActiveDirectory /** ----- app }

```text
`{ [-]
   Actor: [ [-]
     { [-]
       ID: 1d48684f-70ea-41e7-8459-9a7a24a8690a
       Type: 0
     }
     { [-]
       ID: jc3@a830edad9050849NDA3079.onmicrosoft.com               /** -----  user_id
       Type: 5
     }
     { [-]
       ID: 10030000AEF912F2
       Type: 3
     }
   ]
   ActorContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c
   ActorIpAddress: 13.67.186.66
   ApplicationId: 00000002-0000-0ff1-ce00-000000000000
   AzureActiveDirectoryEventType: 1
   ClientIP: 13.67.186.66                                            /** -----  src_ip,  src
   CreationTime: 2020-02-27T07:46:00
   ExtendedProperties: [ [-]
     { [-]
       Name: UserAgent                                               /** -----  user_agent
       Value: python-requests/2.12.4
     }
     { [-]
       Name: RequestType
       Value: OrgIdWsTrust2:process
     }
     { [-]
       Name: ResultStatusDetail
       Value: UserError
     }
   ]
   Id: 8498834c-4ca4-4300-9351-099f917bd2e7
   InterSystemsId: 3f3bd815-8d38-48c8-aa71-445216d908de
   IntraSystemId: c3b22bc6-14c4-4b41-9aee-f4fb7f1e1000
   LogonError: InvalidUserNameOrPassword                              /** -----  reason
   ModifiedProperties: [ [-]
   ]
   ObjectId: Unknown
   Operation: UserLoginFailed                                         /** -----  signature
   OrganizationId: 2ed28a74-1f6f-4829-8530-fe359c77d35c               /** -----  vendor_account
   RecordType: 15
   ResultStatus: Failed                                               /** -----  action
   SupportTicketId:
   Target: [ [-]
     { [-]
       ID: Unknown
       Type: 0
     }
   ]
   TargetContextId: 2ed28a74-1f6f-4829-8530-fe359c77d35c
   UserId: jc3@a830edad9050849NDA3079.onmicrosoft.com                  /** -----  user, user_id
   UserKey: 10030000AEF912F2@a830edad9050849NDA3079.onmicrosoft.com
   UserType: 0                                                         /** -----  user_type
   Version: 1
   Workload: AzureActiveDirectory                                      /** -----  app
}`
```

### AWS failure

A sample AWS failed user login follows:

Click expand or collapse to show or hide the example.

JSON Copy { additionalEventData: { LoginTo: https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true MFAUsed: No /** ----- authentication_method MobileVersion: No } awsRegion: us-east-1 errorMessage: Failed authentication /** ----- reason eventID: 9c6005a8-def1-4075-a1b8-daba01c8150b eventName: ConsoleLogin /** ----- signature eventSource: signin.amazonaws.com /** ----- app, dest eventTime: 2020-02-21T23:06:11Z eventType: AwsConsoleSignIn eventVersion: 1.05 recipientAccountId: 772089552793 requestParameters: null responseElements: { ConsoleLogin: Failure /** ----- action } sourceIPAddress: 4.14.104.185 /** ----- src userAgent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 /** ----- user_agent userIdentity: { accessKeyId: accountId: 772089552793 /** ----- vendor_account principalId: AIDA3HRA7T6MUVQJRHPKV type: IAMUser /** ----- user_type userName: example_user /** ----- user_id } }

```text
`{
   additionalEventData: {
     LoginTo: https://console.aws.amazon.com/console/home?state=hashArgs%23&isauthcode=true
     MFAUsed: No                                               /** -----  authentication_method
     MobileVersion: No
   }
   awsRegion: us-east-1
   errorMessage: Failed authentication                         /** -----  reason
   eventID: 9c6005a8-def1-4075-a1b8-daba01c8150b
   eventName: ConsoleLogin                                     /** -----  signature
   eventSource: signin.amazonaws.com                           /** -----  app, dest
   eventTime: 2020-02-21T23:06:11Z
   eventType: AwsConsoleSignIn
   eventVersion: 1.05
   recipientAccountId: 772089552793
   requestParameters: null
   responseElements: {
     ConsoleLogin: Failure                                     /** -----  action
   }
   sourceIPAddress: 4.14.104.185                              /** -----  src
   userAgent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36
    (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36     /** -----  user_agent
   userIdentity: {
     accessKeyId:
     accountId: 772089552793                                   /** -----  vendor_account
     principalId: AIDA3HRA7T6MUVQJRHPKV
     type: IAMUser                                             /** -----  user_type
     userName: example_user                                    /** -----  user_id
   }
}`
```

### Login failure field mapping

Using the login failure from GCP as a base sample, and comparing it to a similar event from MS o365 and AWS is a good way to see the similarities and differences per common CIM field names.

| User id example data | Provider field name | CIM field name |
| --- | --- | --- |
| User type example data | Provider field name | CIM field name |
| App example data | Provider field name | CIM field name |
| Action example data | Provider field name | CIM field name |
| Signature example data | Provider field name | CIM field name |
| Authentication method example data | Provider field name | CIM field name |
| Vendor account example data | Provider field name | CIM field name |
| Source example data | Provider field name | CIM field name |
| Reason example data | Provider field name | CIM field name |
| User agent data | Provider field name | CIM field name |

| GCP ` example_user@gmail.com ` | protoPayload.authenticationInfo.principalEmail | user_id |

| MS o365 ` jc3@a830edad9050849NDA3079.onmicrosoft.com ` | UserId | user_id |

| AWS ` example_user ` | userIdentity.userName | user_id |

| MS o365 ` 0 ` | UserType | user_type |

| AWS ` IAMUser ` | userIdentity.type | user_type |

| GCP ` login.googleapis.com ` | protoPayload.serviceName | app |

| MS o365 ` AzureActiveDirectory ` | Workload | app |

| AWS ` signin.amazonaws.com ` | eventSource | app |

| GCP ` NOTICE ` | severity | action |

| MS o365 ` Failed ` | ResultStatus | action |

| AWS ` Failure ` | responseElements.ConsoleLogin | action |

| GCP ` google.login.LoginService.loginFailure ` | protoPayload.methodName | signature |

| MS o365 ` UserLoginFailed ` | Operation | signature |

| AWS ` ConsoleLogin ` | eventName | signature |

| GCP ` login_challenge_method ` | events.parameters.name.login_challenge_method | authentication_method |

| AWS ` No ` | additionalEventData.MFAUsed | authentication_method |

| MS o365 ` 2ed28a74-1f6f-4829-8530-fe359c77d35c ` | OrganizationId | vendor_account |

| AWS ` 772089552793 ` | userIdentity.accountId | vendor_account |

-
- | GCP ` 2601:646:8400:b0:a991:7135:7879:6cea ` | requestMetadata.callerIp | src src_ip |

-
- | MS o365 ` 13.67.186.66 ` | ClientIP | src src_ip |

| AWS ` 4.14.104.185 ` | sourceIPAddress | src |

| GCP ` password ` | event.parameter.multiStrValue | reason |

| MS o365 ` InvalidUserNameOrPassword ` | LogonError | reason |

| AWS ` Failed authentication ` | errorMessage | reason |

| MS o365 ` python-requests/2.12.4 ` | UserAgent | user_agent |

| AWS ` Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 ` | userAgent | user_agent |

## Privilege escalation example

The privilege escalation event from AWS is a good way to see a common event and how a cloud provider maps to CIM data model field names.

Privilege escalations include scenarios such as when a user, app, or agent logs in with one set of privileges, and then assumes a new set of privileges (such as `sudo su - `or short-lived credentials for service accounts).

### AWS privilege escalation

A sample AssumeRoleWithSAML follows:

JSON Copy { "eventVersion": "1.05", "userIdentity": { "type": "SAMLUser", "principalId": "g4RD/xcF3dcnEghdegAhfaPo+ow=:example_user@aws.com", "userName": "example_user@aws.com", /** ----- src_user "identityProvider": "g4RD/xcF3dcnEghdegAhfaPo+ow=" }, "eventTime": "2020-03-02T20:25:30Z", "eventSource": "sts.amazonaws.com", /** ----- app, dest "eventName": "AssumeRoleWithSAML", /** ----- signature "awsRegion": "us-east-1", "sourceIPAddress": "12.26.0.2", "userAgent": "aws-sdk-go/2.0.0-preview.2 (go1.9.6; darwin; amd64)", "requestParameters": { "sAMLAssertionID": "id29525874074479896480891647", "roleSessionName": "example_user@aws.com", "durationSeconds": 43200, "roleArn": "arn:aws:iam::671568874969:role/splunkcloud_account_metadata_read", "principalArn": "arn:aws:iam::671568874969:saml-provider/SplunkcloudOkta" }, "responseElements": { "subjectType": "unspecified", "issuer": "http://www.okta.com/exksfwc0mwQGJQoJ62p6", "credentials": { "accessKeyId": "ASIAZYXE7ZXMXCVFRGMO", "expiration": "Mar 3, 2020 8:25:30 AM", "sessionToken": "FwoGZXIvYXdzEG4aDKrC390jc4wlJW7kpyLnAWpYPA0uT1YdeIogg1iol1J0mdHQkIy1QmETyBa8o8KWXP7ptMeilV1UiPmtPQppTu0iXsMOpUM25WOaPioornDWpHwY3ieOhJl1gVODA9cjlLu3pH8j9q4nFXxelkhieBdguExhUslmDSmGLoI94IPOn27bISDZW8vRJwnj9/7WupIM6g4zOOipstGNbWfgTE4/6fkc4HRxdrfS5c1c7ijFxfSaCoT134vhEA1xxhrKLn896ydbFuiIcxsYggDBe886NHKY+DNq1aYPKEiTrJKfWDLLs97sq0ZTi79fOW7arjtNccyKqyi61/XyBTIrZFsRcfIx6xpsS7cOszFx9wNIBJY8X4BjYCXx7QiCZW3pcKAIYbOcBLavSg==" }, "nameQualifier": "g4RD/xcF3dcnEghdegAhfaPo+ow=", "assumedRoleUser": { "assumedRoleId": "AROAIDCBHGVCTRIEIG2X2:example_user@aws.com", "arn": "arn:aws:sts::671568874969:assumed-role/splunkcloud_account_metadata_read/example_user@aws.com" /** ----- user }, "subject": "example_user@aws.com", "audience": "https://signin.aws.amazon.com/saml" }, "requestID": "7c7ac23a-fc2d-4c76-976e-8e2b40073d7d", "eventID": "84dd288a-bdc0-4708-ad61-cde4f45dcc64", "resources": [ { "ARN": "arn:aws:iam::671568874969:role/splunkcloud_account_metadata_read", "accountId": "671568874969", "type": "AWS::IAM::Role" }, { "ARN": "arn:aws:iam::671568874969:saml-provider/SplunkcloudOkta", "accountId": "671568874969", "type": "AWS::IAM::SAMLProvider" } ], "eventType": "AwsApiCall", "recipientAccountId": "671568874969" }

```text
`{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "SAMLUser",
        "principalId": "g4RD/xcF3dcnEghdegAhfaPo+ow=:example_user@aws.com",
        "userName": "example_user@aws.com",                 /** -----  src_user
        "identityProvider": "g4RD/xcF3dcnEghdegAhfaPo+ow="
    },
    "eventTime": "2020-03-02T20:25:30Z",
    "eventSource": "sts.amazonaws.com",                     /** -----  app, dest
    "eventName": "AssumeRoleWithSAML",                      /** -----  signature
    "awsRegion": "us-east-1",
    "sourceIPAddress": "12.26.0.2",
    "userAgent": "aws-sdk-go/2.0.0-preview.2 (go1.9.6; darwin; amd64)",
    "requestParameters": {
        "sAMLAssertionID": "id29525874074479896480891647",
        "roleSessionName": "example_user@aws.com",
        "durationSeconds": 43200,
        "roleArn": "arn:aws:iam::671568874969:role/splunkcloud_account_metadata_read",
        "principalArn": "arn:aws:iam::671568874969:saml-provider/SplunkcloudOkta"
    },
    "responseElements": {
        "subjectType": "unspecified",
        "issuer": "http://www.okta.com/exksfwc0mwQGJQoJ62p6",
        "credentials": {
            "accessKeyId": "ASIAZYXE7ZXMXCVFRGMO",
            "expiration": "Mar 3, 2020 8:25:30 AM",
            "sessionToken": "FwoGZXIvYXdzEG4aDKrC390jc4wlJW7kpyLnAWpYPA0uT1YdeIogg1iol1J0mdHQkIy1QmETyBa8o8KWXP7ptMeilV1UiPmtPQppTu0iXsMOpUM25WOaPioornDWpHwY3ieOhJl1gVODA9cjlLu3pH8j9q4nFXxelkhieBdguExhUslmDSmGLoI94IPOn27bISDZW8vRJwnj9/7WupIM6g4zOOipstGNbWfgTE4/6fkc4HRxdrfS5c1c7ijFxfSaCoT134vhEA1xxhrKLn896ydbFuiIcxsYggDBe886NHKY+DNq1aYPKEiTrJKfWDLLs97sq0ZTi79fOW7arjtNccyKqyi61/XyBTIrZFsRcfIx6xpsS7cOszFx9wNIBJY8X4BjYCXx7QiCZW3pcKAIYbOcBLavSg=="
        },
        "nameQualifier": "g4RD/xcF3dcnEghdegAhfaPo+ow=",
        "assumedRoleUser": {
            "assumedRoleId": "AROAIDCBHGVCTRIEIG2X2:example_user@aws.com",
            "arn": "arn:aws:sts::671568874969:assumed-role/splunkcloud_account_metadata_read/example_user@aws.com"  /** -----  user
        },
        "subject": "example_user@aws.com",
        "audience": "https://signin.aws.amazon.com/saml"
    },
    "requestID": "7c7ac23a-fc2d-4c76-976e-8e2b40073d7d",
    "eventID": "84dd288a-bdc0-4708-ad61-cde4f45dcc64",
    "resources": [
        {
            "ARN": "arn:aws:iam::671568874969:role/splunkcloud_account_metadata_read",
            "accountId": "671568874969",
            "type": "AWS::IAM::Role"
        },
        {
            "ARN": "arn:aws:iam::671568874969:saml-provider/SplunkcloudOkta",
            "accountId": "671568874969",
            "type": "AWS::IAM::SAMLProvider"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "671568874969"
}`
```

### GCP short-lived credentials

A sample GCP short-lived credentials follows:

JSON Copy { "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access", "protoPayload": { "@type": "type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo": { "principalEmail": "example_user@gmail.com" /** ----- src_user }, "methodName": "GenerateAccessToken", /** ----- signature "request": { "@type": "type.googleapis.com/google.iam.credentials.v1.GenerateAccessTokenRequest", "name": "projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com" }, "serviceName": "iamcredentials.googleapis.com" /** ----- app, dest }, "resource": { "labels": { "email_id": "my-service-account@my-project.iam.gserviceaccount.com", /** ----- user "project_id": "my-project", /** ----- vendor_account "unique_id": "123456789012345678901" }, "type": "service_account" } }

```text
`{
  "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access",
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "authenticationInfo": {
      "principalEmail": "example_user@gmail.com"                            /** -----  src_user
    },
    "methodName": "GenerateAccessToken",                                    /** -----  signature
    "request": {
      "@type": "type.googleapis.com/google.iam.credentials.v1.GenerateAccessTokenRequest",
      "name": "projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com"
    },
    "serviceName": "iamcredentials.googleapis.com"                          /** -----  app, dest
  },
  "resource": {
    "labels": {
      "email_id": "my-service-account@my-project.iam.gserviceaccount.com",  /** -----  user
      "project_id": "my-project",                                           /** -----  vendor_account
      "unique_id": "123456789012345678901"
    },
    "type": "service_account"
  }
}`
```

### Privilege escalation field mapping

Using the privilege escalation from AWS as a base sample is a good way to see the similarities and differences per common CIM field names.

| Vendor account example data | Provider field name | CIM field name |
| --- | --- | --- |
| Source user example data | Provider field name | CIM field name |
| App, dest example data | Provider field name | CIM field name |
| Signature example data | Provider field name | CIM field name |
| User example data | Provider field name | CIM field name |

| AWS ` 671568874969 ` | userIdentity.accountId | vendor_account |

| GCP ` my-project ` | resource.labels.project_id | vendor_account |

| AWS ` example_user@aws.com ` | userIdentity.userName | src_user |

| GCP ` example_user@gmail.com ` | protoPayload.authenticationInfo.principalEmail | src_user |

| AWS ` sts.amazonaws.com ` | eventSource | app, dest |

| GCP ` iamcredentials.googleapis.com ` | protoPayload.serviceName | app, dest |

| AWS ` AssumeRoleWithSAML ` | eventName | signature |

| GCP ` GenerateAccessToken ` | protoPayload.methodName | signature |

| AWS ` arn:aws:sts::671568874969:assumed-role/splunkcloud_account_metadata_read/example_user@aws.com ` | assumedRoleUser.arn | user |

| GCP ` my-service-account@my-project.iam.gserviceaccount.com ` | resource.labels.email_id | user |
