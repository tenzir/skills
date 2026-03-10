# MITRE Mitigation

> The MITRE Mitigation object describes the ATT&CK® or ATLAS™ Mitigation ID and/or name that is associated to an attack.


The MITRE Mitigation object describes the ATT\&CK® or ATLAS™ Mitigation ID and/or name that is associated to an attack.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The Mitigation name that is associated with the attack technique. For example: `Password Policies`, or `Code Signing`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The Mitigation ID that is associated with the attack technique. For example: `M1027`, or `AML.M0013`.

**`countermeasures`**

* **Type**: [`d3fend`](d3fend.md)
* **Requirement**: optional

The D3FEND countermeasures that are associated with the attack technique. For example: ATT\&CK Technique `T1003` is addressed by Mitigation `M1027`, and D3FEND Technique `D3-OTP`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the Mitigation. For example: `https://attack.mitre.org/versions/v14/mitigations/M1027`.

## Constraints

At least one of: `name`, `uid`