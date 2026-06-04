# UsernameType

- **Source**: [`ASIM/schemas/common/ASimEnumerations.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/common/ASimEnumerations.yaml)
- **Values**: `4`
- **Referenced by fields**: [`ActorUsernameType`](../fields/actor_username_type.md), [`SrcUsernameType`](../fields/src_username_type.md), [`TargetUsernameType`](../fields/target_username_type.md)

## Values

| Value | Description | Examples | Link |
| --- | --- | --- | --- |
| `UPN` | User principal name | `jdow@contoso.com` |  |
| `Windows` | A username that includes domain information in Windows format | `contoso\jdow` |  |
| `DN` | LDAP Distinguished Name | `CN=Jeff Smith,OU=Sales,DC=Fabrikam,DC=COM` |  |
| `Simple` | A simple username without scope information. | `jdow` |  |
