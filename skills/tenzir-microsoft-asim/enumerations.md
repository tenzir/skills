# Enumerations

ASIM defines 13 enumerations with 63 values.

## AppType

- `Process`
- `Service`
- `Resource`
- `URL`
- `SaaS application`
- `Operating System`
- `Container`
- `CSP`: A cloud service provider control plane.
- `Other`

## AttackTactic

- `https://attack.mitre.org/docs/enterprise-attack-v13.0/enterprise-attack-v13.0-tactics.xlsx`

## AttackTechnique

- `https://attack.mitre.org/docs/enterprise-attack-v13.0/enterprise-attack-v13.0-techniques.xlsx`

## DeviceType

- `Computer`
- `Mobile Device`
- `IOT Device`
- `Other`

## DomainType

- `Windows`
- `FQDN`

## DvcIdType

- `MDEid`: A system ID assigned by Microsoft Defender for Endpoint.
- `AzureResourceId`: An Azure resource ID.
- `MD4IoTid`: The Microsoft Defender for IoT resource ID.
- `VMConnectionId`: The Azure Monitor VM Insights solution resource ID.
- `AwsVpcId`: An AWS VPC ID.
- `Other`: An ID type not listed above.

## EventProduct

- `Sysmon for Linux`
- `Sysmon`
- `M365 Defender for Endpoint`
- `Azure File Storage`
- `SharePoint`
- `OneDrive`
- `Exchange 365`
- `Windows`

## EventVendor

- `Microsoft`

## FilePathType

- `Windows Local`
- `Windows Share`
- `Unix`
- `URL`

## Schemas

- `Dns`
- `NetworkSession`
- `WebSession`
- `FileEvent`
- `ProcessEvent`
- `RegistryEvent`
- `Authentication`
- `AuditEvent`

## UserIdType

- `SID`: Windows user SID
- `UID`: Unix user ID
- `AADID`: Azure AD User ID
- `OktaId`: Okta user ID
- `AWSId`: AWS user ID
- `PUID`: Microsoft 365 User ID
- `Other`: User ID in a scope other than the listed above.

## UsernameType

- `UPN`: User principal name Examples: `jdow@contoso.com`.
- `Windows`: A username that includes domain information in Windows format Examples: `contoso\jdow`.
- `DN`: LDAP Distinguished Name Examples: `CN=Jeff Smith,OU=Sales,DC=Fabrikam,DC=COM`.
- `Simple`: A simple username without scope information. Examples: `jdow`.

## UserType

- `Regular`: An account associated with a regular user.
- `Machine`: A special account associated with a system.
- `Admin`: An account used for system administration. While the best practice is to use a dedicated account, in some cases a regular user account is granted additional permissions to enable administration.
- `Guest`: An external account which is not defined in the primary directory the system, application or service belongs to.
- `System`: A special account user exclusively by the operating system.
- `Service`: an account that is used by automated processes, such as tasks or services. Examples: `Active Directory service account`, `Azure Active Directory Service Principal`, `AWS Role`.
- `Application`: A service account that is associated with a specific services. Examples: `Azure Active Directory Managed Identity`, `AWS AWSservice`.
- `Other`: An user account not related to any of the types above.
