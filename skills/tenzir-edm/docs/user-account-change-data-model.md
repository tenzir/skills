<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/165823/user-account-change-data-model -->

# User Account Change Data Model

This data model describes activities around user accounts and groups

- Accounts created/deleted/modified
- Groups created/deleted/modified

Examples of Account Created Events:

- Win-Security-4720 – user account created
- Win-Security-4741 – computer account created
- Generic_Unix_User_Add
- FortiGate-event-add-user
- GitLab-User-created

Examples of Account Deleted Events:

- Win-Security-4726 – user account deleted
- Win-Security-4743 – user account deleted
- Generic_Unix_User_Del
- FortiGate-event-admin-delete

Examples of Account Modified Events:

- Win-Security-4725 – user account disabled
- Win-Security-4722 - user account enabled
- Win-Security-4724 – password reset
- Win-Security-4723 – password changed
- Win-Security-4738 – user account changed
- Win-Security-4742 – computer account changed
- Win-Security-4781 – account name changed
- Win-Security-4767 – account unlocked
- Generic_Unix_User_Change_Name
- Generic_Unix_Password_Change
- Generic_Unix_Failed_Password_Change
- Generic_Unix_User_Change_Home
- Generic_Unix_User_Password_Change
- Generic_Unix_User_Change_GID
- Generic_Unix_User_Change_Shell
- FortiGate-event-password-change
- FortiGate-event-admin-settings-edit

Examples of Group Created Events:

- Win-Security-4727 – Windows security enabled global group created
- Win-Security-4731 – Windows security enabled local group created
- Win-Security-4744 – Windows security enabled universal global group created
- Generic_Unix_Group_Add
- FortiGate-event-user-group-change

Examples of Group Deleted Events:

- Win-Security-4730 – Windows security enabled global group deleted
- Win-Security-4734 – Windows security enabled local group deleted
- Win-Security-4758 – Windows security enabled universal global group deleted
- Generic_Unix_Group_Del

Examples of Group Modified Events:

- Win-Security-4728 – Windows security enabled global group member added
- Win-Security-4732– Windows security enabled local group member added
- Win-Security-4756 – Windows security enabled universal global group member added
- Win-Security-4729 – Windows security enabled global group member removed
- Win-Security-4733– Windows security enabled local group member removed
- Win-Security-4757 – Windows security enabled universal global group member removed

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| user | string | User | User whose took action |
| domain | string | Domain | Domain of User |
| targetUser | string | Target User | Affected User whose account was created/deleted/modified |
| targetDomain | string | Target User Domain | Domain of targetUser |
| targetUserGrp | string | Target User Group | Group that was created/deleted |

| Event | user | targetUser | targetUserGrp | Interpretation |
| --- | --- | --- | --- | --- |
| Account Created/Deleted/Modified | x | x |  | $user created / deleted/ modified $targetUser |
| Group Created/Deleted | x |  | x | $user created / deleted/ modified $userGrp |
| Group Modified | x | x | x | $user added $targetUser to $targetUserGrp |
