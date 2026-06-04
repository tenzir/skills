# UserType

- **Source**: [`ASIM/schemas/common/ASimEnumerations.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/common/ASimEnumerations.yaml)
- **Values**: `8`
- **Referenced by fields**: [`ActorUserType`](../fields/actor_user_type.md), [`SrcUserType`](../fields/src_user_type.md), [`TargetUserType`](../fields/target_user_type.md)

## Values

| Value | Description | Examples | Link |
| --- | --- | --- | --- |
| `Regular` | An account associated with a regular user. |  |  |
| `Machine` | A special account associated with a system. |  |  |
| `Admin` | An account used for system administration. While the best practice is to use a dedicated account, in some cases a regular user account is granted additional permissions to enable administration. |  |  |
| `Guest` | An external account which is not defined in the primary directory the system, application or service belongs to. |  |  |
| `System` | A special account user exclusively by the operating system. |  |  |
| `Service` | an account that is used by automated processes, such as tasks or services. | `Active Directory service account`, `Azure Active Directory Service Principal`, `AWS Role` |  |
| `Application` | A service account that is associated with a specific services. | `Azure Active Directory Managed Identity`, `AWS AWSservice` |  |
| `Other` | An user account not related to any of the types above. |  |  |
