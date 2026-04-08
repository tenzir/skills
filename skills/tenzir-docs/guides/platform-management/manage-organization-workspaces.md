# Manage organization workspaces


This guide shows you how to create, view, and delete workspaces that belong to an organization. You’ll learn the difference between personal and organization workspaces and how access control works for shared workspaces.

## Personal vs. organization workspaces

Workspaces can be owned by either a user or an organization:

* **Personal workspaces** are owned by a single user and accessible only to that user.
* **Organization workspaces** are owned by the organization and accessible to all organization members.

The workspace switcher in the web app groups workspaces by their owning organization, making it easy to navigate between them.

## Create a workspace

Only organization admins can create new workspaces under an organization.

### Web app

On the organization page, find the **Workspaces** section and click **New Workspace**. Enter a name and confirm.

### CLI

```sh
tenzir-platform org create-workspace --name="Production"
```

If you omit `--name`, the platform generates a name based on the current timestamp.

## View organization workspaces

### Web app

The **Workspaces** section on the organization page lists all workspaces owned by the organization. Click a workspace to navigate to it.

### CLI

Use `tenzir-platform org info` to see the number of workspaces in your organization. Individual workspace management is available through the web app.

## Delete a workspace

Destructive action

Deleting a workspace permanently removes all its nodes, secrets, and dashboards. This action cannot be undone.

Only organization admins can delete organization-owned workspaces.

### Web app

On the organization page, click the delete button next to the workspace you want to remove. Confirm the deletion in the dialog.

Note

Workspaces created through static configuration files cannot be deleted through the web app or CLI. They must be removed from the configuration file instead. See [Configure workspaces](configure-workspaces.md) for details.

## Access control

All members of an organization automatically have access to the organization’s workspaces. You can further restrict access using auth rules that require a specific organization role. For example, you can create a workspace that only organization admins can access.

For advanced access control configuration, see [Configure workspaces](configure-workspaces.md).

## See Also

* [Manage organizations](manage-organizations.md)
* [Manage organization members](manage-organization-members.md)
* [Configure workspaces](configure-workspaces.md)
* [Platform](../../explanations/platform.md)