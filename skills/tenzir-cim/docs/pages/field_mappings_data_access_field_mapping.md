---
title: Data Access Field Mapping
url: https://help.splunk.com/en/data-management/common-information-model/8.5/field-mappings/data-access-field-mapping
last_modified: 2026-04-01T20:48:26.590Z
version: 8.5
---

# Data Access Field Mapping

The following shows an example of how data access events map differently from various cloud providers to CIM data model field names.

See the Data Access data model for full field descriptions.

## File upload success example

The file upload success event from Google Drive and Box is a good way to see a common event and how each cloud provider maps to CIM data model field names.

### Google Drive upload success

A sample Google Drive user successfully uploading a file follows:

Click expand or collapse to show or hide the example.

```text
{
  "kind": "admin#reports#activity",
  "id": {
    "time": "2021-01-27T20:55:22.553Z",
    "uniqueQualifier": "-5126288301746458201",
    "applicationName": "drive",               /** -----  app, dest_name, vendor_product, dvc
    "customerId": "C01yel9ht"                           /** -----  tenant_id
  },
  "etag": "\"fhmPGI5aiiS0KGD55zBI3n4f0Di-XQVRRMmqt75xUJc/Qtt_cFE351_xxWrZD43B_hFtj7I\"",
  "actor": {
    "email": "name@example.com",                        /** -----  email, user
    "profileId": "110778908138668363959"                /** -----  user_id
  },
  "ipAddress": "96.231.134.130",                        /** -----  src
  "events": [
    {
      "type": "access",
      "name": "upload",                                 /** -----  action
      "parameters": [
        {
          "name": "primary_event",
          "boolValue": true
        },
        {
          "name": "billable",
          "boolValue": true
        },
        {
          "name": "doc_id",                              /** -----  object_id
          "value": "1s2ww0PVPGuuKXAzdjg6jGgmZtcxGchH7"
        },
        {
          "name": "doc_type",                            /** -----  object_type
          "value": "unknown"
        },
        {
          "name": "doc_title",                            /** -----  object
          "value": "quickstart.py"
        },
        {
          "name": "visibility",
          "value": "private"
        },
        {
          "name": "originating_app_id",
          "value": "691301496089"
        },
        {
          "name": "actor_is_collaborator_account",        /** -----  user_role
          "boolValue": false
        },
        {
          "name": "owner",                                /** -----  owner
          "value": "name@example.com"
        },
        {
          "name": "owner_is_shared_drive",
          "boolValue": false
        },
        {
          "name": "owner_is_team_drive",
          "boolValue": false
        }
      ]
    }
      ]
    }
  ]
}
```

### Box upload success

A sample Box user successfully uploading a file follows:

Click expand or collapse to show or hide the example.

```text
source_item_type="file",                                              /** -----  object_type
source_item_id="782729174962",                                        /** -----  object_id
source_item_name="Consolidated Quarter-VII-IV Schedule -
     Participants.xlsx",                                              /** -----  object
source_parent_type="folder",
source_parent_name="Test",
source_parent_id="132755355986",
source_owned_by_type="user",
source_owned_by_id="15230886095",                                     /** -----  owner_id
source_owned_by_name="Example Name",                                  /** -----  owner
source_owned_by_login="name@example.com",                             /** -----  owner_email
created_by_type="user",
created_by_id="15230886095",                                          /** -----  user_id
created_by_name="Example Name",                                       /** -----  user
created_by_login="name@example.com",                                  /** -----  email
action_by="",
created_at="2021-03-03T10:10:40-08:00",
event_id="30fe6b3e-41ea-40a5-894d-38c575c0be5f",
event_type="UPLOAD",                                                  /** -----  action
ip_address="103.226.185.0",                                           /** -----  src
type="event",
session_id="",
additional_details_size="22564",                                      /** -----  object_size
additional_details_ekm_id="b03b4375-03c9-4c03-9559-9cedddab801d",
additional_details_version_id="836198952562",
additional_details_service_id="231318",
additional_details_service_name="Multiput Uploads",
account_id=15230886095                                                /** -----  user_id
```

### Upload field mapping

Using the file upload success from Google Drive as a base sample, and comparing it to a similar event from Box is a good way to see the similarities and differences per common CIM field names.

| Source example data | Provider field name | CIM field name |
| --- | --- | --- |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Device example data | Provider field name | CIM field name |
| Google Drive ` name@example.com ` | actor.email | - email - user |
| Box ` name@example.com ` | created_by_login | email |
| Google Drive ` name@example.com ` | actor.email | - email - user |
| Box ` Example Name ` | created_by_name | user |
| Google Drive ` 110778908138668363959 ` | actor. profileId | user_id |
| Box ` 15230886095 ` | - created_by_id - account_id | user_id |
| Google Drive ` 96.231.134.130 ` | ipAddress | src |
| Box ` 103.226.185.0 ` | ip_address | src |
| Google Drive ` upload ` | name | action |
| Box ` UPLOAD ` | event_type | action |
| Google Drive ` 1s2ww0PVPGuuKXAzdjg6jGgmZtcxGchH7 ` | "name": "doc_id" | object_id |
| Box ` 782729174962 ` | source_item_id | object_id |
| Google Drive ` unknown ` | "name": "doc_type" | object_type |
| Box ` file ` | source_item_type | object_type |
| Google Drive ` quickstart.py ` | "name": "doc_title" | object |
| Box ` Consolidated Quarter-VII-IV Schedule - Participants.xlsx ` | source_item_name | object |
| Google Drive ` name@example.com ` | "name": "owner" | owner |
| Box ` Example Name ` | source_owned_by_name | owner |
