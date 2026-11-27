---
title: "Create role"
description: "Creates a custom organization role with its raw policy"
canonical: https://tenzir.com/docs/reference/api/organizations/create-role
source: https://tenzir.com/docs/reference/api/organizations/create-role.md
section: "Docs"
---

# Create role

> Creates a custom organization role with its raw policy

`POST /api/organizations/{org}/roles`

Creates a custom organization role with its raw policy

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `label` (`string`, required) Length: `>= 1`.

* `color` (`enum`, required): The display color of an organization role. Allowed values: `neutral`, `blue`, `green`, `lightblue`, `purple`, `pink`, `orange`, `yellow`, `red`.

* `description` (`string`, optional)

* `policy` (`array<[Constraints, array<string>]>`, required)

  Array items:

  * `[0]` (`Constraints`, required)

    * `target` (`Authorization Selector`, required)

      Any of:

      * **System Selector** (`System Selector`)
        * `_tag` (`"System"`, required)

      * **User Selector** (`User Selector`)

        * `_tag` (`"User"`, required)
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **Organization Selector** (`Organization Selector`)

        * `_tag` (`"Organization"`, required)
        * `orgId` (`string`, optional): A UUID

      * **Invitation Selector** (`Invitation Selector`)

        * `_tag` (`"Invitation"`, required)
        * `orgId` (`string`, optional): A UUID
        * `invitationId` (`string`, optional): The identifier of an organization invitation

      * **OrganizationMember Selector** (`OrganizationMember Selector`)

        * `_tag` (`"OrganizationMember"`, required)
        * `orgId` (`string`, optional): A UUID
        * `memberId` (`string`, optional): A stable membership identifier
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **OrganizationRole Selector** (`OrganizationRole Selector`)

        * `_tag` (`"OrganizationRole"`, required)

        * `orgId` (`string`, optional): A UUID

        * `roleId` (`enum / string`, optional): The identifier of a built-in or custom organization role

          Any of:

          * **Built-in Organization Role ID** (`enum`)
          * **Custom Role ID** (`string`)

      * **Workspace Selector** (`Workspace Selector`)

        * `_tag` (`"Workspace"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID

      * **WorkspaceBranch Selector** (`WorkspaceBranch Selector`)

        * `_tag` (`"WorkspaceBranch"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `branch` (`string`, optional)
        * `protected` (`boolean`, optional)

      * **Deployment Selector** (`Deployment Selector`)

        * `_tag` (`"Deployment"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID

      * **DeploymentUser Selector** (`DeploymentUser Selector`)

        * `_tag` (`"DeploymentUser"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **ApiKey Selector** (`ApiKey Selector`)

        * `_tag` (`"ApiKey"`, required)

        * `apiKeyId` (`string`, optional): A UUID

        * `owner` (`User Selector / Organization Selector`, optional)

          Any of:

          * **User Selector** (`User Selector`)

            * `_tag` (`"User"`, required)
            * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

          * **Organization Selector** (`Organization Selector`)

            * `_tag` (`"Organization"`, required)
            * `orgId` (`string`, optional): A UUID

      * **AssistantConversation Selector** (`AssistantConversation Selector`)

        * `_tag` (`"AssistantConversation"`, required)
        * `conversationId` (`string<uuid>`, optional): A UUID that the client chooses when it creates the conversation. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
        * `ownerId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **AdhocPipeline Selector** (`AdhocPipeline Selector`)

        * `_tag` (`"AdhocPipeline"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `pipelineId` (`string`, optional): The id the platform gave an ad-hoc pipeline when it started it
        * `ownerId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **OrgSecret Selector** (`OrgSecret Selector`)

        * `_tag` (`"OrgSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.
        * `restricted` (`boolean`, optional)

      * **WorkspaceSecret Selector** (`WorkspaceSecret Selector`)

        * `_tag` (`"WorkspaceSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.
        * `restricted` (`boolean`, optional)

      * **DeploymentSecret Selector** (`DeploymentSecret Selector`)

        * `_tag` (`"DeploymentSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.

      * **SecretValue Selector** (`SecretValue Selector`)

        * `_tag` (`"SecretValue"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID

      * **IngestEndpoint Selector** (`IngestEndpoint Selector`)

        * `_tag` (`"IngestEndpoint"`, required)
        * `orgId` (`string`, optional): A UUID
        * `endpointId` (`string`, optional): A UUID
        * `name` (`string`, optional): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

      * **IngestEndpointAttachment Selector** (`IngestEndpointAttachment Selector`)

        * `_tag` (`"IngestEndpointAttachment"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `endpointId` (`string`, optional): A UUID
        * `name` (`string`, optional): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

    * `relationships` (`array<enum>`, required)

  * `[1]` (`array<string>`, required)

## Responses

### `201`: A custom organization role with display metadata and its raw policy

Media type: `application/json`

* `_tag` (`"Custom"`, required)

* `id` (`string`, required): A UUID that identifies a custom organization role

* `label` (`string`, required) Length: `>= 1`.

* `color` (`enum`, required): The display color of an organization role. Allowed values: `neutral`, `blue`, `green`, `lightblue`, `purple`, `pink`, `orange`, `yellow`, `red`.

* `description` (`string`, required)

* `policy` (`array<[Constraints, array<string>]>`, required)

  Array items:

  * `[0]` (`Constraints`, required)

    * `target` (`Authorization Selector`, required)

      Any of:

      * **System Selector** (`System Selector`)
        * `_tag` (`"System"`, required)

      * **User Selector** (`User Selector`)

        * `_tag` (`"User"`, required)
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **Organization Selector** (`Organization Selector`)

        * `_tag` (`"Organization"`, required)
        * `orgId` (`string`, optional): A UUID

      * **Invitation Selector** (`Invitation Selector`)

        * `_tag` (`"Invitation"`, required)
        * `orgId` (`string`, optional): A UUID
        * `invitationId` (`string`, optional): The identifier of an organization invitation

      * **OrganizationMember Selector** (`OrganizationMember Selector`)

        * `_tag` (`"OrganizationMember"`, required)
        * `orgId` (`string`, optional): A UUID
        * `memberId` (`string`, optional): A stable membership identifier
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **OrganizationRole Selector** (`OrganizationRole Selector`)

        * `_tag` (`"OrganizationRole"`, required)

        * `orgId` (`string`, optional): A UUID

        * `roleId` (`enum / string`, optional): The identifier of a built-in or custom organization role

          Any of:

          * **Built-in Organization Role ID** (`enum`)
          * **Custom Role ID** (`string`)

      * **Workspace Selector** (`Workspace Selector`)

        * `_tag` (`"Workspace"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID

      * **WorkspaceBranch Selector** (`WorkspaceBranch Selector`)

        * `_tag` (`"WorkspaceBranch"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `branch` (`string`, optional)
        * `protected` (`boolean`, optional)

      * **Deployment Selector** (`Deployment Selector`)

        * `_tag` (`"Deployment"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID

      * **DeploymentUser Selector** (`DeploymentUser Selector`)

        * `_tag` (`"DeploymentUser"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **ApiKey Selector** (`ApiKey Selector`)

        * `_tag` (`"ApiKey"`, required)

        * `apiKeyId` (`string`, optional): A UUID

        * `owner` (`User Selector / Organization Selector`, optional)

          Any of:

          * **User Selector** (`User Selector`)

            * `_tag` (`"User"`, required)
            * `userId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

          * **Organization Selector** (`Organization Selector`)

            * `_tag` (`"Organization"`, required)
            * `orgId` (`string`, optional): A UUID

      * **AssistantConversation Selector** (`AssistantConversation Selector`)

        * `_tag` (`"AssistantConversation"`, required)
        * `conversationId` (`string<uuid>`, optional): A UUID that the client chooses when it creates the conversation. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
        * `ownerId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **AdhocPipeline Selector** (`AdhocPipeline Selector`)

        * `_tag` (`"AdhocPipeline"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `pipelineId` (`string`, optional): The id the platform gave an ad-hoc pipeline when it started it
        * `ownerId` (`string<uuid>`, optional): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * **OrgSecret Selector** (`OrgSecret Selector`)

        * `_tag` (`"OrgSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.
        * `restricted` (`boolean`, optional)

      * **WorkspaceSecret Selector** (`WorkspaceSecret Selector`)

        * `_tag` (`"WorkspaceSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.
        * `restricted` (`boolean`, optional)

      * **DeploymentSecret Selector** (`DeploymentSecret Selector`)

        * `_tag` (`"DeploymentSecret"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `secretId` (`string`, optional): A UUID
        * `name` (`unknown`, optional): A path-safe identifier. Length: `<= 255`.

      * **SecretValue Selector** (`SecretValue Selector`)

        * `_tag` (`"SecretValue"`, required)
        * `orgId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID

      * **IngestEndpoint Selector** (`IngestEndpoint Selector`)

        * `_tag` (`"IngestEndpoint"`, required)
        * `orgId` (`string`, optional): A UUID
        * `endpointId` (`string`, optional): A UUID
        * `name` (`string`, optional): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

      * **IngestEndpointAttachment Selector** (`IngestEndpointAttachment Selector`)

        * `_tag` (`"IngestEndpointAttachment"`, required)
        * `orgId` (`string`, optional): A UUID
        * `workspaceId` (`string`, optional): A UUID
        * `deploymentId` (`string`, optional): A UUID
        * `endpointId` (`string`, optional): A UUID
        * `name` (`string`, optional): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

    * `relationships` (`array<enum>`, required)

  * `[1]` (`array<string>`, required)

### `400`: CredentialConflict | Validation

Media type: `application/json`

Any of:

* **CredentialConflict** (`CredentialConflict`)

  * `_tag` (`"CredentialConflict"`, required)
  * `message` (`string`, required)

* **Validation** (`Validation`)

  * `_tag` (`"Validation"`, required)
  * `message` (`string`, required)

### `401`: Unauthenticated

Media type: `application/json`

* `_tag` (`"Unauthenticated"`, required)
* `message` (`string`, required)

### `403`: Unauthorized

Media type: `application/json`

* `_tag` (`"Unauthorized"`, required)
* `message` (`string`, required)

### `404`: NotFound

Media type: `application/json`

* `_tag` (`"NotFound"`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
